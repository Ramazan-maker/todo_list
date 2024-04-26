"""
Django settings for samplesite project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os.path
from pathlib import Path

import environ

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',

    'captcha',
    'precise_bbcode',
    'bootstrap4',
    'django_cleanup',
    'easy_thumbnails',

    'bboard.apps.BboardConfig',  # 'bboard',
    'testapp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # 'django.middleware.cache.UpdateCacheMiddleware',  # для кэша

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    # 'django.middleware.cache.FetchFromCacheMiddleware',  # для кэша

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'bboard.middlewares.my_middleware',
    # 'bboard.middlewares.MyMiddleware',
    # 'bboard.middlewares.RubricMiddleware',
]

ROOT_URLCONF = 'samplesite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            # 'file_charset': 'utf-8',
            # 'debug': False,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',  # user, perms
                'django.contrib.messages.context_processors.messages',

                # 'django.template.context_processors.csrf',
                'django.template.context_processors.static',
                # 'django.template.context_processors.media',
                'bboard.middlewares.rubrics',
            ],
            # 'libraries': {
            #     'filtertags': 'bboard.filtertags',
            # },
            # 'builtins': [
            #     'bboard.templatetags.filtertags',
            # ],
        },
    },
]

WSGI_APPLICATION = 'samplesite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    #     # 'ATOMIC_REQUEST': False,
    #     'AUTOCOMMIT': False,
    # }
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        # "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "123",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'samplesite.validators.NoForbiddenCharsValidator',
        'OPTIONS': {'forbidden_chars': (' ', ',', '.', ':', ';')},
    },
]

# AUTH_USER_MODEL = "testapp.AdvUser"


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
# STATIC_ROOT = BASE_DIR / 'static'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# FILE_UPLOAD_MAX_MEMORY_SIZE = 2621440
# FILE_UPLOAD_TEMP_DIR = None
# FILE_UPLOAD_PERMISSIONS = 0o644
# FILE_UPLOAD_DIRECTORY_PERMISSIONS = None

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ABSOLUTE_URL_OVERRIDES = {
#     # 'bboard.rubric': lambda rec: "/%s/" % rec.pk,
#     'bboard.rubric': lambda rec: f"/{rec.pk}/",
# }

LOGIN_URL = "bboard:login"
LOGIN_REDIRECT_URL = "bboard:index"
LOGOUT_REDIRECT_URL = "bboard:index"

# Настройки Капчи
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
CAPTCHA_LENGTH = 4  # 6
CAPTCHA_WORDS_DICTIONARY = '/static/captcha_words.txt'
CAPTCHA_TIMEOUT = 5  # МИНУТ


# DATA_UPLOAD_MAX_MEMORY_SIZE = 2621440  # 2.5 Mbytes
# DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000


# BBCode
BBCODE_NEWLINE = "<br>"
# BBCODE_ESCAPE_HTML = ""
BBCODE_DISABLE_BUILTIN_TAGS = False
BBCODE_ALLOW_CUSTOM_TAGS = True
BBCODE_ALLOW_SMILIES = True
BBCODE_SMILIES_UPLOAD_TO = os.path.join('precise_bbcode', 'smilies')


# BOOTSTRAP4 = {
#     'horizontal_label_class': 'col-md-3',
#     'horizontal_field_class': 'col-md-9',
#     'required_css_class': '',
#     'success_css_class': 'has-success',
#     'error_css_class': 'has-error',
# }

THUMBNAIL_ALIASES = {
    'bboard.Bb.picture': {
        'default': {
            'size': (500, 300),
            'crop': 'scale',
        },
    },
    'testapp': {
        'default': {
            'size': (400, 300),
            'crop': 'smart',
            'bw': True,
        },
    },
    '': {
        'default': {
            'size': (180, 240),
            'crop': 'scale',
        },
        'big': {
            'size': (480, 640),
            'crop': '10,10'
        },
    },
}

THUMBNAIL_DEFAULT_OPTIONS = {
    'quality': 90,
    'subsampling': 1,
}

THUMBNAIL_PRESERVE_EXTENSION = True  # ('png',)


# SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# SESSION_ENGINE = 'django.contrib.sessions.backends.file'
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
# SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

# MESSAGE_LEVEL = 20

# from django.contrib import messages
# MESSAGE_LEVEL = messages.DEBUG

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.dummy.EmailBackend"

DEFAULT_FROM_EMAIL = "webmaster@localhost"

# только для SMTP
EMAIL_HOST = "localhost"
EMAIL_PORT = 25
# EMAIL_HOST_USER = env('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
# EMAIL_TIMEOUT = 5  # сек.

EMAIL_FILE_PATH = 'tmp/messages/'

ADMINS = [
    ('admin', 'admin@supersite.kz'),
]

# MANGERS = [
#     ('manager', 'manager@supersite.kz'),
# ]

CACHES = {
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    #     'LOCATION': 'cache1',
    #     # 'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
    #     # 'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
    #     # 'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    #     # 'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
    #     'TIMEOUT': 300,  # сек
    #     'OPTIONS': {
    #         'MAX_ENTRIES': 300,
    #         'CULL_FREQUENCY': 3,
    #     }
    # },
    #
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
        'TIMEOUT': 120,
        'OPTIONS': {
            'MAX_ENTRIES': 200,
        }
    },
}

# CACHE_MIDDLEWARE_ALIAS = 'default'
# CACHE_MIDDLEWARE_SECONDS = 600  # сек
