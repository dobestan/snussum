from django.views.generic.detail import DetailView

from relationships.models.dating import Dating


class DatingDetail(DetailView):
    model = Dating
    slug_field = "hash_id"
    template_name = "datings/detail.html"
    context_object_name = "dating"


class TodayDetail(DatingDetail):

    def get_object(self):
        return self.request.user.userprofile.dating_matched_today()