from django.views.generic.edit import FormView
from relationships.forms.self_dating import SelfDatingForm


class SelfDatingFormView(FormView):
    template_name = "datings/self_dating/new.html"
    form_class = SelfDatingForm
