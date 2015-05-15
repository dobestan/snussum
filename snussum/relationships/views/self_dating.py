from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from relationships.forms.self_dating import SelfDatingForm, SelfDatingApplyForm

from django.utils.decorators import method_decorator
from users.decorators import university_verified_required, profile_verifed_required
from django.contrib.auth.decorators import login_required

from relationships.models.self_dating import SelfDating, SelfDatingApply


class SelfDatingBase(View):
    model = SelfDating
    slug_field = "hash_id"
    context_object_name = "self_dating"

    @method_decorator(university_verified_required)
    @method_decorator(profile_verifed_required)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SelfDatingBase, self).dispatch(*args, **kwargs)


class SelfDatingCreate(SelfDatingBase, CreateView):
    template_name = "datings/self_dating/new.html"
    form_class = SelfDatingForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return super(SelfDatingCreate, self).form_valid(form)


class SelfDatingDetail(SelfDatingBase, DetailView):
    template_name = "datings/self_dating/detail.html"

    def get_context_data(self, **kwargs):
        context = super(SelfDatingDetail, self).get_context_data(**kwargs)
        context['form'] = SelfDatingApplyForm()
        context['recent_self_datings'] = SelfDating.objects.exclude(
            pk=context['self_dating'].pk).order_by('-ends_at')[:3]
        return context


class SelfDatingApply(SelfDatingBase, CreateView):
    model = SelfDatingApply
    fields = ['content']

    def form_valid(self, form):
        self_dating = SelfDating.objects.get(hash_id=self.kwargs['slug'])

        self_dating_apply_object = form.save(commit=False)
        self_dating_apply_object.user = self.request.user
        self_dating_apply_object.self_dating = self_dating
        self_dating_apply_object.save()

        return super(SelfDatingApply, self).form_valid(form)
