from snussum.settings import *


INSTALLED_APPS += (
    # Django Libraries
    'raven.contrib.django.raven_compat',
)

# Deployment checklist
# https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

DEBUG = False
ALLOWED_HOSTS = [".snussum.com", ]


# Static/Media File Management

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'snussum.storage.S3PipelineManifestStorage'


# Django Secure - ONLY Production
# https://github.com/carljm/django-secure/
# http://django-secure.readthedocs.org/en/latest/index.html

# all non-SSL requests should be permanently redirected to SSL.
SECURE_SSL_REDIRECT = True

# prevent framing of your pages and protect them from clickjacking.
SECURE_FRAME_DENY = True

# prevent the browser from guessing asset content types.
SECURE_CONTENT_TYPE_NOSNIFF = True

# http://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security
SECURE_HSTS_SECONDS = 30
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# enable the browser's XSS filtering protections.
SECURE_BROWSER_XSS_FILTER = True

# https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-SESSION_COOKIE_HTTPONLY
# https://docs.djangoproject.com/en/1.8/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True


# Set your DSN value
RAVEN_CONFIG = {
    'dsn': 'https://4445971377fd46fa8c60b8da0367cde9:a53eddf3cc974e0fa4db16823d565c5c@app.getsentry.com/43279',
}
