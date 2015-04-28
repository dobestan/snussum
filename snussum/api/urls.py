from django.conf.urls import patterns, url

from api.views.update_profile import UpdateProfileUniversity


urlpatterns = patterns(
    '',

    url(r'^login/$', 'rest_framework_jwt.views.verify_jwt_token'),
    url(r'^users/university/$', UpdateProfileUniversity.as_view(), name='update-university'),
)
