from django.conf.urls import patterns, url

from users.views.verify import VerifyUniversity, VerifyUniversitySNU, VerifyProfile
from users.views.profile import Profile
from users.views.password import PasswordReset


urlpatterns = patterns(
    '',

    url(r'^login/$', 'users.views.login', name='login'),
    url(r'^signup/$', 'users.views.signup', name='signup'),
    url(r'^logout/$', 'users.views.logout', name='logout'),

    url(r'^password/reset/$', PasswordReset.as_view(), name='password-reset'),

    url(r'^profile/$', Profile.as_view(), name='profile'),

    url(r'^verify/univ/$', VerifyUniversity.as_view(), name='verify-univ'),
    url(r'^verify/snu/$', VerifyUniversitySNU.as_view(), name='verify-snu'),
    url(r'^verify/profile/$', VerifyProfile.as_view(), name='verify-profile'),

    url(r'^verify/(?P<university_verification_token>\w+)/$',
        'users.views.university_verification',
        name='university-verification'
        ),
)
