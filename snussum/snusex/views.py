from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name = "snusex/home.html"


class About(TemplateView):
    template_name = "snusex/about.html"
