import os
import environ
import urllib.parse


env = environ.Env()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')
EXTERNAL_API_TOKEN = env('EXTERNAL_API_TOKEN')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django.contrib.sites',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    'corsheaders',
]

LOCAL_APPS = [
    'cashback_api.resellers',
    'cashback_api.sales',
    'cashback_api.users',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

X_FRAME_OPTIONS = 'DENY'

USE_X_FORWARDED_HOST = not DEBUG

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': env.db_url(
        'DATABASE_DEFAULT_URL',
        default='sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))
    ),
}

##############
# MIDDLEWARE #
##############
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

############
# SESSIONS #
############
# Cache to store session data if using the cache session backend.
SESSION_CACHE_ALIAS = 'sessions'
# The module to store session data
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# A string like "example.com", or None for standard domain cookie.
SESSION_COOKIE_DOMAIN = env.str('SESSION_COOKIE_DOMAIN', default=None)
# Whether the session cookie should be secure (https:// only).
SESSION_COOKIE_SECURE = not DEBUG

#########
# CACHE #
#########
# The cache backends to use.
CACHES = {
    'default': env.cache(
        'CACHES_DEFAULT_URL', default='locmemcache://unique-snowflake'),
    'sessions': env.cache(
        'CACHES_SESSIONS_URL', default='locmemcache://unique-snowflake'),
}

########
# CSRF #
########
CSRF_COOKIE_DOMAIN = env.str('CSRF_COOKIE_DOMAIN', default=None)
CSRF_COOKIE_SECURE = not DEBUG
CSRF_TRUSTED_ORIGINS = env.list('CSRF_TRUSTED_ORIGINS', default=[])


#######################
# django-cors-headers #
#######################

CORS_ORIGIN_ALLOW_ALL = True


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = urllib.parse.urljoin(
    env.str('STATIC_HOST', default=''), '/static/')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = env.str(
    'STATICFILES_STORAGE',
    default='django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
)


MEDIA_URL = urllib.parse.urljoin(env.str('MEDIA_URL', default=''), '/media/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


AUTH_USER_MODEL = 'users.CustomUser'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        } 
    },
    'USE_SESSION_AUTH': False,
    'JSON_EDITOR': True,
}

