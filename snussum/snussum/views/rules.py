from django.views.generic.base import TemplateView


class Privacy(TemplateView):
    template_name = "rules/privacy.html"


class Service(TemplateView):
    template_name = "rules/service.html"
