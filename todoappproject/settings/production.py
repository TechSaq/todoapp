from .base import *
import django_heroku
import dj_database_url


# DEBUG = config('DEBUG', cast=bool)
DEBUG = True


db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
print(DATABASES['default'])


ALLOWED_HOSTS = ['zeesertodoapp.herokuapp.com']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())
