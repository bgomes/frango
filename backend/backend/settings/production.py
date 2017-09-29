from django.utils.log import DEFAULT_LOGGING

from .base import *

import dj_database_url
import time


DEFAULT_LOGGING['handlers']['console']['filters'] = []

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
#USE_TZ = False

ALLOWED_HOSTS = [
    '*.herokuapp.com',
    '127.0.0.1',
    'localhost',
    '*',
]

# Heroku Database
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(FRONTEND_DIR, 'dist', 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
            ],
        },
    },
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(FRONTEND_DIR, 'dist', 'static'),
]


expires = time.time() + 6 * 24 * 3600 # 6 days from now

WHITENOISE_MAX_AGE = 86400

AWS_ACCESS_KEY_ID = os.environ.get('AWSAccessKeyId', '')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWSSecretKey', '')
AWS_STORAGE_BUCKET_NAME = os.environ.get('S3_BUCKET_NAME', '')
AWS_QUERYSTRING_AUTH = False
AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME', '')
AWS_IS_GZIPPED = True
AWS_S3_OBJECT_PARAMETERS = {
    'Expires': time.strftime("%a, %d-%b-%Y %T GMT", time.gmtime(expires)),
    'CacheControl': 'max-age=86400',
}
STATIC_URL = '/static/'

STATICFILES_LOCATION = '/static/'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
MEDIA_URL = 'https://s3-'+AWS_S3_REGION_NAME+'.amazonaws.com/'+AWS_STORAGE_BUCKET_NAME+'/'
