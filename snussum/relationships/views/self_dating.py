from django.shortcuts import get_object_or_404

from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from relationships.forms.self_dating import SelfDatingForm, SelfDatingApplyForm

from django.utils.decorators import method_decorator
from users.decorators import university_verified_required, profile_verifed_required, phonenumber_verifed_required
from django.contrib.auth.decorators import login_required

from relationships.models.self_dating import SelfDating, SelfDatingApply

from datetime import datetime

from django.db.models import Q

from notifications import notify

from users.tasks.self_dating import send_self_dating_applied_sms, send_self_dating_accepted_sms


class SelfDatingBase(View):
    model = SelfDating
    slug_field = "hash_id"
    context_object_name = "self_dating"

    @method_decorator(login_required)
    @method_decorator(university_verified_required)
    @method_decorator(profile_verifed_required)
    @method_decorator(phonenumber_verifed_required)
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


class SelfDatingApplyCreate(SelfDatingBase, CreateView):
    model = SelfDatingApply
    fields = ['content']

    def form_valid(self, form):
        self_dating = SelfDating.objects.get(hash_id=self.kwargs['slug'])

        self_dating_apply_object = form.save(commit=False)
        self_dating_apply_object.user = self.request.user
        self_dating_apply_object.self_dating = self_dating
        self_dating_apply_object.save()

        send_self_dating_applied_sms(
            self_dating_apply_object.self_dating.user,
            self_dating_apply_object.user,
            self_dating_apply_object)

        return super(SelfDatingApplyCreate, self).form_valid(form)


class SelfDatingApplyAccept(SelfDatingBase, UpdateView):
    model = SelfDatingApply
    fields = ["accepted_message", ]

    def get_object(self):
        return get_object_or_404(self.model, hash_id=self.kwargs['self_dating_apply_hash_id'])

    def form_valid(self, form):
        self.object.is_accepted = True
        self.object.accepted_at = datetime.now()

        # 셀프소개팅 지원자에게 알림 전달
        notify.send(self.object.self_dating.user, recipient=self.object.user,
                    action_object=self.object, verb="accepted",
                    description=self.object.accepted_message)

        send_self_dating_accepted_sms(self.object.self_dating.user, self.object.user, self.object.self_dating)
        send_self_dating_accepted_sms(self.object.user, self.object.self_dating.user, self.object.self_dating)

        return super(SelfDatingApplyAccept, self).form_valid(form)


class SelfDatingApplyRefuse(SelfDatingBase, UpdateView):
    model = SelfDatingApply
    fields = ["accepted_message", ]

    def get_object(self):
        return get_object_or_404(self.model, hash_id=self.kwargs['self_dating_apply_hash_id'])

    def form_valid(self, form):
        self.object.is_accepted = False
        self.object.accepted_at = datetime.now()

        # 셀프소개팅 지원자에게 알림 전달
        notify.send(self.object.self_dating.user, recipient=self.object.user,
                    action_object=self.object, verb="refused",
                    description=self.object.accepted_message)

        return super(SelfDatingApplyRefuse, self).form_valid(form)


class SelfDatingList(ListView):
    template_name = "datings/self_dating/list.html"
    context_object_name = 'self_datings'
    paginate_by = 10

    def get_queryset(self):
        search_query = self.request.GET.get('search') or str()
        return SelfDating.objects.filter(
            Q(title__contains=search_query) |
            Q(content__contains=search_query)
        )

    def get_context_data(self, **kwargs):
        context = super(SelfDatingList, self).get_context_data(**kwargs)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SelfDatingList, self).dispatch(*args, **kwargs)
