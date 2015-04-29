from snussum.settings import *


INSTALLED_APPS += (
    # Django Libraries
    'django_extensions',
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

INTERNAL_IPS = (
    '0.0.0.0',
    '127.0.0.1',
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
