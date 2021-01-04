from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['*']

MEDIA_URL = '/dmedia/'
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")

STATIC_URL = 'library/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
