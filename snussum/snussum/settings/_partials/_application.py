import os
import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SNUSSUM_URL = "http://local.snussum.com:9000"

INSTALLED_APPS = (
    # http://django-grappelli.readthedocs.org/en/latest/quickstart.html#installation
    'grappelli',

    # Django Default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Django Libraries
    "djangosecure",
    'cachalot',
    'social.apps.django_app.default',
    'storages',
    'imagekit',
    'admin_honeypot',
    'notifications',
    'django_summernote',
    'pipeline',
    'robots',

    # Snussum Apps
    'users',
    'relationships',
    'api',
    'analytics',
    'snuanal',
    'snusex',
)

MIDDLEWARE_CLASSES = (
    "djangosecure.middleware.SecurityMiddleware",

    'django.middleware.gzip.GZipMiddleware',
    'pipeline.middleware.MinifyHTMLMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'snussum.urls'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'

DATABASES = {
    'default': dj_database_url.config(default=os.environ['DATABASE_URL'])
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

HASHIDS_DATING_SALT = os.environ["HASHIDS_DATING_SALT"]
HASHIDS_SELF_DATING_SALT = os.environ["HASHIDS_SELF_DATING_SALT"]
HASHIDS_SELF_DATING_APPLY_SALT = os.environ["HASHIDS_SELF_DATING_APPLY_SALT"]
HASHIDS_COMMENT_SALT = os.environ["HASHIDS_COMMENT_SALT"]
HASHIDS_USER_PROFILE_SALT = os.environ["HASHIDS_USER_PROFILE_SALT"]

WSGI_APPLICATION = 'snussum.wsgi.application'

DEBUG = True
ALLOWED_HOSTS = []
SECRET_KEY = os.environ["SECRET_KEY"]

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

API_STORE_SMS_BASE_URL = os.environ['API_STORE_SMS_BASE_URL']
API_STORE_SMS_KEY = os.environ['API_STORE_SMS_KEY']

API_STORE_SMS_SEND_NAME = "썸타는 서울대, 스누썸"
API_STORE_SMS_SUBJECT = "썸타는 서울대, 스누썸"

MAILGUN_ACCESS_KEY = os.environ["MAILGUN_ACCESS_KEY"]
MAILGUN_SERVER_NAME = os.environ["MAILGUN_SERVER_NAME"]

TIME_ZONE = "Asia/Seoul"

GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]


# django-redis
# http://niwibe.github.io/django-redis

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

ADMIN_URL = os.environ["ADMIN_URL"]

SITE_ID = 1
