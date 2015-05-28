import os

# Authentication
# https://github.com/omab/python-social-auth
# http://psa.matiasaguirre.net/


AUTHENTICATION_BACKENDS = (
    # Django Default
    'django.contrib.auth.backends.ModelBackend',

    # Python-Social-Auth Modules
    # 'social.backends.open_id.OpenIdAuth',
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.kakao.KakaoOAuth2',
)

# FacebookOAuth2
# http://psa.matiasaguirre.net/docs/backends/facebook.html#oauth2
# https://developers.facebook.com/

SOCIAL_AUTH_FACEBOOK_KEY = os.environ['SOCIAL_AUTH_FACEBOOK_KEY']
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ['SOCIAL_AUTH_FACEBOOK_SECRET']

SOCIAL_AUTH_FACEBOOK_SCOPE = []

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {}


# KakaoOAuth2
# http://psa.matiasaguirre.net/docs/backends/kakao.html
# https://developers.kakao.com/docs/restapi

SOCIAL_AUTH_KAKAO_KEY = os.environ['SOCIAL_AUTH_KAKAO_KEY']
SOCIAL_AUTH_KAKAO_SECRET = os.environ['SOCIAL_AUTH_KAKAO_SECRET']

SOCIAL_AUTH_KAKAO_SCOPE = []

# URL Options
# http://psa.matiasaguirre.net/docs/configuration/settings.html#urls-options

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
# SOCIAL_AUTH_LOGIN_ERROR_URL = '/login-error/'
# SOCIAL_AUTH_LOGIN_URL = '/login-url/'
# SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'
# SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/new-association-redirect-url/'
# SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/account-disconnected-redirect-url/'
# SOCIAL_AUTH_INACTIVE_USER_URL = '/inactive-user/'
