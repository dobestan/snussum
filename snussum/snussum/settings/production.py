from snussum.settings import *


# Deployment checklist
# https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/
DEBUG=False
ALLOWED_HOSTS = [".snussum.com",]

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
