# Django settings for nord project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Oleg Smirnov', 'oleg.smirnov+nord@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '/var/www/nord/nord.db'
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
ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = 'lhh3vvulzn0k#w#^*nkunvxn5nnz^sj#s=22n%oz5qdlfwsa8@'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'nord.urls'

TEMPLATE_DIRS = (
    "/var/www/nord/templates"
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'tagging',
    'wiki',
)

WIKI_MARKUP_CHOICES = (
    ('crl', u'Creole'),
)

STATIC_MEDIA_PATH = "/var/www/media.nord/"
