from django.conf.urls import patterns, url

from users.views.verify import Verify


urlpatterns = patterns(
    '',

    url(r'^login/$', 'users.views.login', name='login'),
    url(r'^signup/$', 'users.views.signup', name='signup'),
    url(r'^logout/$', 'users.views.logout', name='logout'),

    url(r'^verify/$', Verify.as_view(), name='verify'),
    url(r'^verify/(?P<university_verification_token>\w+)/$',
        'users.views.university_verification',
        name='university-verification'
        ),
)
