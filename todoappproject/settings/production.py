from .base import *
import django_heroku


DEBUG = config('DEBUG', cast=bool)


ALLOWED_HOSTS = ['zeesertodoapp.herokuapp.com']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())
