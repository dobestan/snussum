from django.views.generic.edit import CreateView
from relationships.forms.self_dating import SelfDatingForm

from django.utils.decorators import method_decorator
from users.decorators import university_verified_required, profile_verifed_required

class SelfDatingFormView(CreateView):
    template_name = "datings/self_dating/new.html"
    form_class = SelfDatingForm

    @method_decorator(university_verified_required)
    @method_decorator(profile_verifed_required)
    def dispatch(self, *args, **kwargs):
        return super(SelfDatingFormView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return super(SelfDatingFormView, self).form_valid(form)
