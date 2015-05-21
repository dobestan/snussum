import os
from ._application import BASE_DIR


STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'components'),
)

AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]

AWS_S3_CUSTOM_DOMAIN = 'cdn.snussum.com'
AWS_S3_URL_PROTOCOL = 'https'

# STATIC_URL = 'https://cdn.snussum.com/'

# django-pipeline
# https://django-pipeline.readthedocs.org/en/latest/installation.html

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

STATIC_ROOT = os.path.join(BASE_DIR, 'STATIC_ROOT')

PIPELINE_JS = {
    'main': {
        'source_filenames': (
            # Jquery
            'js/jquery.min.js',
            'js/jquery-cookie.js',

            # Bootstrap
            'js/bootstrap.min.js',
            'js/moment.min.js',
            'js/bootstrap-notify.min.js',
            'js/bootstrap-switch.min.js',
            'js/bootstrap-tagsinput.min.js',
            'js/bootstrap-datetimepicker.min.js',

            # 3rd Party
            'js/highcharts.min.js',

            # Application
            'js/application.js',
            'js/datings/*.js',
        ),
        'output_filename': (
            'js/snussum.min.js'
        )
    }
}

PIPELINE_CSS = {
    'main': {
        'source_filenames': (
            'css/bootstrap.min.css',
            'css/font-awesome.min.css',
            'css/animate.min.css',
            'css/bootstrap-tagsinput.css',
            'css/bootstrap-switch.min.css',
            'css/bootstrap-datetimepicker.min.css',
            'css/application.css',
        ),
        'output_filename': (
            'css/snussum.min.css'
        )
    }
}
