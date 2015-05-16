from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils.decorators import method_decorator

from users.decorators import university_verified_required, university_not_verified_required

from django.contrib.auth.models import User
from users.models.user_profile import UserProfile
from users.models.university import University

from django.contrib import messages

from users.forms.profile import UserProfileVerificationForm


class VerifyUniversity(TemplateView):
    template_name = "users/verify/univ.html"

    def get_context_data(self, **kwargs):
        context = super(VerifyUniversity, self).get_context_data(**kwargs)
        context["universities"] = University.objects.all()
        return context


class VerifyUniversitySNU(TemplateView):
    template_name = "users/verify/snu.html"

    @method_decorator(university_not_verified_required)
    def dispatch(self, *args, **kwargs):
        return super(VerifyUniversitySNU, self).dispatch(*args, **kwargs)


class VerifyProfile(UpdateView):
    model = UserProfile
    template_name = "users/verify/profile.html"
    fields = ['nickname', 'is_boy', 'profile_introduce', 'age', 'height', ]

    def get_object(self):
        return self.request.user.userprofile

    @method_decorator(university_verified_required)
    def dispatch(self, *args, **kwargs):
        return super(VerifyProfile, self).dispatch(*args, **kwargs)


def university_verification(request, university_verification_token):
    if request.user.is_authenticated() and request.user.userprofile.is_university_verified:
        return redirect("home")

    user = get_object_or_404(
        User,
        userprofile__university_verification_token=university_verification_token
    )

    user.userprofile.is_university_verified = True
    user.userprofile.save()

    return redirect("home")


def phonenumber_verification(request, phonenumber_verification_token):
    user = get_object_or_404(User, userprofile__phonenumber_verification_token=phonenumber_verification_token)
    user.userprofile.is_phonenumber_verified = True
    user.userprofile.save()

    messages.add_message(request, messages.INFO,
                         '연락처가 인증되었습니다. 감사합니다.',
                         extra_tags="success")
    return redirect("home")
