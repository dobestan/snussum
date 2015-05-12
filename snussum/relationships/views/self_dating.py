from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from relationships.forms.self_dating import SelfDatingForm, SelfDatingApplyForm

from django.utils.decorators import method_decorator
from users.decorators import university_verified_required, profile_verifed_required

from relationships.models.self_dating import SelfDating


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


class SelfDatingDetail(DetailView):
    model = SelfDating
    slug_field = "hash_id"
    template_name = "datings/self_dating/detail.html"
    context_object_name = "self_dating"

    @method_decorator(university_verified_required)
    @method_decorator(profile_verifed_required)
    def dispatch(self, *args, **kwargs):
        return super(SelfDatingDetail, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SelfDatingDetail, self).get_context_data(**kwargs)
        context['form'] = SelfDatingApplyForm()
        context['recent_self_datings'] = SelfDating.objects.exclude(pk=context['self_dating'].pk).order_by('-ends_at')[:3]
        return context
