import os
import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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

    # Django Libraries
    'storages',
    'imagekit',

    # Snussum Apps
    'users',
    'relationships',
    'api',
)

MIDDLEWARE_CLASSES = (
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
            ],
        },
    },
]

HASHIDS_DATING_SALT = os.environ["HASHIDS_DATING_SALT"]
HASHIDS_USER_PROFILE_SALT = os.environ["HASHIDS_USER_PROFILE_SALT"]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'components'),
)

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