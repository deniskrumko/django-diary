INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'import_export',
]

LOCAL_APPS = [
    'apps.diary',
    'apps.users',
    'apps.website',
]

INSTALLED_APPS += LOCAL_APPS
