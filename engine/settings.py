# -*- coding: utf-8 -*-

DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = (
    ('#Name#', '#Email#'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/path/to/main.db'
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

TIME_ZONE = 'Europe/Kiev'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
MEDIA_ROOT = ''
MEDIA_URL = ''
FORCE_SCRIPT_NAME = ""
ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = '#deleted#'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'sslauth.middleware.SSLAuthMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'sslauth.backends.SSLAuthBackend',
)

ROOT_URLCONF = 'engine.urls'

TEMPLATE_DIRS = (
    '/path/to/engine/templates'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'tagging',
    'wiki',
    'sslauth',
    'google_analytics',
    'splash',
)

FORCE_LOWERCASE_TAGS = False

GOOGLE_ANALYTICS_MODEL = True

GMAP_KEY='#deleted#'

SSLAUTH_SUBJECT_MATCH_KEYS = (
    'subject_c',
    'subject_o',
    'subject_ou',
    'subject_cn',
)

SSLAUTH_CREATE_USERNAME_CALLBACK = lambda ssl_info: \
                                   ''.join(filter(lambda s: s.isalnum(), list(ssl_info.subject_cn)))
