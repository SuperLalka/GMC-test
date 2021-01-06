from .settings import *

DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080',
)
CORS_ORIGIN_REGEX_WHITELIST = (
    'http://localhost:8080',
)

MEDIA_URL = '/dmedia/'
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

STATIC_URL = 'library/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
