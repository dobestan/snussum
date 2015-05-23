from django.views.generic.base import TemplateView

from relationships.models.self_dating import SelfDating


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['self_datings'] = SelfDating.objects.order_by('-ends_at')[:3]
        return context


class About(TemplateView):
    template_name = "about.html"
