from django.views.generic.detail import DetailView

from django.utils.decorators import method_decorator
from users.decorators import university_verified_required, profile_verifed_required

from relationships.models.dating import Dating
from relationships.models.self_dating import SelfDating



class DatingDetail(DetailView):
    model = Dating
    slug_field = "hash_id"
    template_name = "datings/detail.html"
    context_object_name = "dating"

    @method_decorator(university_verified_required)
    @method_decorator(profile_verifed_required)
    def dispatch(self, *args, **kwargs):
        return super(DatingDetail, self).dispatch(*args, **kwargs)


class TodayDetail(DatingDetail):

    def get_object(self):
        return self.request.user.userprofile.dating_matched_today()


class SelfDatingDetail(DetailView):
    model = SelfDating
    slug_field = "hash_id"
    template_name = "datings/self_dating/detail.html"
    context_object_name = "self_dating"

    @method_decorator(university_verified_required)
    @method_decorator(profile_verifed_required)
    def dispatch(self, *args, **kwargs):
        return super(SelfDatingDetail, self).dispatch(*args, **kwargs)
