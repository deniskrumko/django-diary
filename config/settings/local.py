from .common import *  # noqa

import dj_database_url


SECRET_KEY = 'example'

DEBUG = True

DATABASES = {
    'default': dj_database_url.config(
        default='postgres://postgres:@localhost:5432/djangodiary'
    )
}

AUTH_PASSWORD_VALIDATORS = []

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# Shell plus pre imports
SHELL_PLUS_PRE_IMPORTS = [('{}.factories'.format(app), '*')
                          for app in INSTALLED_APPS]  # noqa
