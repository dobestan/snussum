from django.views.generic.base import TemplateView


class Profile(TemplateView):
    template_name = "users/profile.html"
