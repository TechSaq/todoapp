from .base import *


DEBUG = config('DEBUG')


ALLOWED_HOSTS = []

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())
