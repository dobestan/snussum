from django.views.generic import View
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView

from django.utils.decorators import method_decorator
from users.decorators import university_verified_required, profile_verifed_required
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from users.models.user_profile import UserProfile
from users.forms.profile import UserProfileInformationForm


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
        return super(View, self).dispatch(*args, **kwargs)


class UpdateUserProfileInformation(UpdateUserProfileBase):
    model = UserProfile
    fields = ['nickname', 'profile_introduce', 'age', 'height']


class Notification(TemplateView):
    template_name = "users/notification.html"

    @method_decorator(university_verified_required)
    @method_decorator(profile_verifed_required)
    def dispatch(self, *args, **kwargs):
        return super(Notification, self).dispatch(*args, **kwargs)
