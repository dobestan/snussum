from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from users.decorators import university_verified_required


class Profile(TemplateView):
    template_name = "users/profile.html"

    @method_decorator(university_verified_required)
    def dispatch(self, *args, **kwargs):
        return super(Profile, self).dispatch(*args, **kwargs)
