from django.views.generic.base import TemplateView

from django.utils.decorators import method_decorator
from users.decorators import anonymous_required


class PasswordReset(TemplateView):
    template_name = "users/password_reset.html"

    @method_decorator(anonymous_required)
    def dispatch(self, *args, **kwargs):
        return super(PasswordReset, self).dispatch(*args, **kwargs)
