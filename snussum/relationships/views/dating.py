from django.views.generic import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from users.decorators import university_verified_required, profile_verifed_required

from relationships.models.dating import Dating
from relationships.models.rating import Rating

from datetime import datetime


class DatingBase(View):
    model = Dating
    slug_field = "hash_id"
    context_object_name = "dating"

    @method_decorator(login_required)
    @method_decorator(university_verified_required)
    @method_decorator(profile_verifed_required)
    def dispatch(self, *args, **kwargs):
        return super(DatingBase, self).dispatch(*args, **kwargs)


class DatingDetail(DatingBase, DetailView):
    template_name = "datings/detail.html"

    def get_context_data(self, **kwargs):
        context = super(DatingDetail, self).get_context_data(**kwargs)

        if self.request.user.userprofile.is_boy:
            partner = self.object.girl
        else:
            partner = self.object.boy

        # Ratings
        context['RATING_SCORE_CHOICES'] = Rating.SCORE_CHOICES
        context['recent_ratings'] = Rating.objects.filter(reviewee=partner).exclude(dating=self.object)
        context['my_rating'] = Rating.objects.filter(dating=self.object, reviewer=self.request.user).first()

        return context



class TodayDetail(DatingBase, DetailView):

    def get_object(self):
        return self.request.user.userprofile.dating_matched_today()


class DatingAccept(DatingBase, UpdateView):
    model = Dating
    fields = []

    def form_valid(self, form):
        content = self.request.POST.get("content", None)

        if self.request.user.userprofile.is_boy:
            self.object.is_boy_accepted = True
            self.object.boy_accepted_at = datetime.now()
            self.object.boy_accepted_message = content
        else:
            self.object.is_girl_accepted = True
            self.object.girl_accepted_at = datetime.now()
            self.object.girl_accepted_message = content
        self.object.save()

        return super(DatingAccept, self).form_valid(form)


class DatingRefuse(DatingBase, UpdateView):
    model = Dating
    fields = []

    def form_valid(self, form):
        if self.request.user.userprofile.is_boy:
            self.object.is_boy_accepted = False
            self.object.boy_accepted_at = datetime.now()
        else:
            self.object.is_girl_accepted = False
            self.object.girl_accepted_at = datetime.now()
        self.object.save()

        return super(DatingRefuse, self).form_valid(form)


class DatingRatingCreate(DatingBase, CreateView):
    model = Rating
    fields = ['score', 'content', ]

    def form_valid(self, form):
        dating = Dating.objects.get(hash_id=self.kwargs['slug'])

        if self.request.user.userprofile.is_boy:
            partner = dating.girl
        else:
            partner = dating.boy

        self.object = form.save(commit=False)
        self.object.dating = dating
        self.object.reviewer = self.request.user
        self.object.reviewee = partner
        self.object.save()

        return super(DatingRatingCreate, self).form_valid(form)
