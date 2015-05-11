from django.views.generic.edit import CreateView
from relationships.forms.self_dating import SelfDatingForm


class SelfDatingFormView(CreateView):
    template_name = "datings/self_dating/new.html"
    form_class = SelfDatingForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return super(SelfDatingFormView, self).form_valid(form)
