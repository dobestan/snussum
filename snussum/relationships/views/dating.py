from django.views.generic.detail import DetailView

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from users.decorators import university_verified_required, profile_verifed_required

from relationships.models.dating import Dating


class DatingBase(DetailView):
    model = Dating
    slug_field = "hash_id"
    context_object_name = "dating"

    @method_decorator(login_required)
    @method_decorator(university_verified_required)
    @method_decorator(profile_verifed_required)
    def dispatch(self, *args, **kwargs):
        return super(DatingBase, self).dispatch(*args, **kwargs)


class DatingDetail(DatingBase):
    template_name = "datings/detail.html"


class TodayDetail(DatingDetail):

    def get_object(self):
        return self.request.user.userprofile.dating_matched_today()
