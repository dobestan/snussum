from django.views.generic.base import TemplateView

from django.utils.decorators import method_decorator
from users.decorators import university_verified_required, profile_verifed_required


class Dashboard(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['dating_matched_today'] = self.request.user.userprofile.dating_matched_today()
        context['datings_matched_recently'] = self.request.user.userprofile.datings_matched_recently_except_today()
        return context

    @method_decorator(university_verified_required)
    @method_decorator(profile_verifed_required)
    def dispatch(self, *args, **kwargs):
        return super(Dashboard, self).dispatch(*args, **kwargs)
