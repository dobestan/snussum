from django.conf.urls import patterns, url

from api.views.update_profile import UpdateProfileUniversity, UpdateProfileNickname, UpdateProfileIntroduce
from api.views.messages import APIMessageSMS, APIMessageEmail
from api.views.datings import DatingComment
from api.views.verify import VerifySNUSnulifeLogin


urlpatterns = patterns(
    '',

    url(r'^login/$', 'rest_framework_jwt.views.verify_jwt_token'),
    url(r'^users/university/$', UpdateProfileUniversity.as_view(), name='update-university'),
    url(r'^users/nickname/$', UpdateProfileNickname.as_view(), name='update-nickname'),
    url(r'^users/introduce/$', UpdateProfileIntroduce.as_view(), name='update-introduce'),

    url(r'^ssum/(?P<hash_id>\w+)/comment/$', DatingComment.as_view(), name='dating-comment'),

    url(r'sms/$', APIMessageSMS.as_view(), name='sms'),
    url(r'email/$', APIMessageEmail.as_view(), name='email'),

    # SNU Verifications
    url(r'users/snulife/login/$', VerifySNUSnulifeLogin.as_view(), name='snulife-login'),
)
