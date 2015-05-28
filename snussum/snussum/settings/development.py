from snussum.settings import *


INSTALLED_APPS += (
    # Django Libraries
    'django_extensions',
    'django_nose',
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

INTERNAL_IPS = (
    '0.0.0.0',
    '127.0.0.1',
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# django-debug-toolbar
# http://django-debug-toolbar.readthedocs.org/en/latest/configuration.html

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',

    # http://django-cachalot.readthedocs.org/en/latest/quickstart.html#usage
    'cachalot.panels.CachalotPanel',
]
