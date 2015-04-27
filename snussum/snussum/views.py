from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name = "home.html"


class Dashboard(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['dating_matched_today'] = self.request.user.userprofile.dating_matched_today()
        context['datings_matched_recently'] = self.request.user.userprofile.datings_matched_recently_except_today()
        return context
