from snussum.settings import *


# Deployment checklist
# https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
DEBUG = False
ALLOWED_HOSTS = [".snussum.com", ]

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]

AWS_S3_CUSTOM_DOMAIN = 'cdn.snussum.com'
AWS_S3_URL_PROTOCOL = 'https'

STATIC_URL = 'https://cdn.snussum.com/'

STATICFILES_DIRS = (
    os.path.join(os.path.join(BASE_DIR, 'static'), 'deploy'),
)


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
