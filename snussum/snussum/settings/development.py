from snussum.settings import *


INSTALLED_APPS += (
# Django Libraries
    'django_extensions',
    'django_nose',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
