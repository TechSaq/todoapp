from .base import *


DEBUG = config('DEBUG', cast=boolean)


ALLOWED_HOSTS = ['zeesertodoapp.herokuapp.com']

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())
