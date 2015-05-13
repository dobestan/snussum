from django.views.generic import View
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView

from django.utils.decorators import method_decorator
from users.decorators import university_verified_required, profile_verifed_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from users.models.user_profile import UserProfile
from users.forms.profile import UserProfileInformationForm

from django.core.urlresolvers import reverse
from django.contrib import messages


class Profile(TemplateView):
    template_name = "users/profile.html"

    @method_decorator(university_verified_required)
    @method_decorator(profile_verifed_required)
    def dispatch(self, *args, **kwargs):
        return super(Profile, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context['information_form'] = UserProfileInformationForm(instance=self.request.user.userprofile)
        return context


class UpdateUserProfileBase(View):

    @method_decorator(require_POST)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UpdateUserProfileBase, self).dispatch(*args, **kwargs)


class UpdateUserProfileInformation(UpdateView, UpdateUserProfileBase):
    model = UserProfile
    fields = ['nickname', 'profile_introduce', 'age', 'height']

    def get_object(self):
        return self.request.user.userprofile

    def get_success_url(self):
        return reverse("users:profile")

    def form_valid(self, form):
        messages.add_message(self.request, messages.INFO,
                             '프로필이 성공적으로 업데이트 되었습니다. 감사합니다.',
                             extra_tags="success")
        return super(UpdateUserProfileInformation, self).form_valid(form)


class Notification(TemplateView):
    template_name = "users/notification.html"

    @method_decorator(university_verified_required)
    @method_decorator(profile_verifed_required)
    def dispatch(self, *args, **kwargs):
        return super(Notification, self).dispatch(*args, **kwargs)
