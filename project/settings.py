"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.2.23.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url
from django.contrib.messages import constants as messages
if os.path.exists('env.py'):
    import env

development = os.environ.get('DEVELOPMENT', False)

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['final-project-ada-02b27917ae0c.herokuapp.com', '8000-adamolnar-finalproject-scsmnofs6ih.ws-eu107.gitpod.io' , 'localhost']


# Application definition

INSTALLED_APPS = [
    'jazzmin',


    # Django built-in apps
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',


    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'cloudinary_storage',
    'django.contrib.staticfiles',

    'widget_tweaks',
    
    'cloudinary',
    'django_summernote',
    'crispy_forms',
    'django_social_share',
    'coverage',

    # Custom apps
    'blog',
    'profile',
    'author',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOT_REDIRECT_URL = '/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(BASE_DIR, 'author', 'templates'),
            os.path.join(BASE_DIR, 'blog', 'templates'),
            os.path.join(BASE_DIR, 'profile', 'templates'),
        ],
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

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
   'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

# DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite3')
# DATABASES = {'default': dj_database_url.parse(DATABASE_URL)}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'author', 'static'),
    os.path.join(BASE_DIR, 'blog', 'static'),
    os.path.join(BASE_DIR, 'profile', 'static'),

]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Default Account email validation
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SESSION_REMEMBER = True

# Built-in views for the password reset process.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Custom ErrorList form for signup.html
ACCOUNT_FORMS = {
  'signup': 'profile.forms.CustomSignUpForm',
  'login': 'profile.forms.CustomLoginForm',
}