from django.views.generic.base import TemplateView

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.contrib.auth.models import User
from users.models.university import University


class Verify(TemplateView):
    template_name = "users/verify.html"

    def get_context_data(self, **kwargs):
        context = super(Verify, self).get_context_data(**kwargs)
        context["universities"] = University.objects.all()
        return context


def university_verification(request, university_verification_token):
    if request.user.is_authenticated() and request.user.userprofile.is_university_verified:
        return redirect("home")

    user = get_object_or_404(
        User,
        userprofile__university_verification_token=university_verification_token
    )

    user.userprofile.is_university_verified = True
    user.save()

    return redirect("home")
