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

# django-pipeline
# https://django-pipeline.readthedocs.org/en/latest/installation.html

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)

STATIC_ROOT = os.path.join(BASE_DIR, 'STATIC_ROOT')

PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.closure.ClosureCompressor'
PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yui.YUICompressor'

PIPELINE_CLOSURE_BINARY = '/usr/local/bin/closure-compiler'
# PIPELINE_YUI_BINARY = '/usr/local/bin/yuicompressor'

PIPELINE_JS = {
    'vendor': {
        'source_filenames': (
            # Jquery
            'js/jquery.min.js',
            'js/jquery-cookie.js',

            # Bootstrap
            'js/bootstrap.min.js',
            'js/bootstrap-notify.min.js',
            'js/bootstrap-tagsinput.min.js',

            # 'js/bootstrap-switch.min.js',
            # 'js/bootstrap-datetimepicker.min.js',
            # 'js/moment.min.js',

            # 3rd Party
            'js/highcharts.min.js',
        ),
        'output_filename': 'js/vendor.min.js',
    },
    'main': {
        'source_filenames': (
            # Application
            'js/application.js',
            'js/datings/*.js',
            'js/users/*.js',
        ),
        'output_filename': 'js/snussum.min.js'
    }
}

PIPELINE_CSS = {
    'vendor': {
        'source_filenames': (
            'css/bootstrap.min.css',
            'css/animate.min.css',
            'css/font-awesome.min.css',
            'css/bootstrap-tagsinput.css',
            # 'css/bootstrap-switch.min.css',
            # 'css/bootstrap-datetimepicker.min.css',
        ),
        'output_filename': 'css/vendor.min.css'
    },
    'main': {
        'source_filenames': (
            'css/application.css',
        ),
        'output_filename': 'css/snussum.min.css'
    }
}
