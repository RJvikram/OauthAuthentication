"""
Django settings for OauthAuthentication project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from django.core.management.utils import get_random_secret_key

# Determine the current environment ('development', 'production', etc.)
ENVIRONMENT = os.getenv('DJANGO_ENV', 'development')

# Import the appropriate settings based on the environment
if ENVIRONMENT == 'production':
    from config.production import *
if ENVIRONMENT == 'development':
    from config.development import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', get_random_secret_key())

# Application definition
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'accounts.apps.AccountsConfig',
]

THIRDPARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'django_admin_generator',
    'rest_framework.authtoken',
]

INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS + THIRDPARTY_APPS

DEFAULT_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

THIRDPARTY__MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]

MIDDLEWARE = DEFAULT_MIDDLEWARE + THIRDPARTY__MIDDLEWARE

# X_FRAME_OPTIONS = 'DENY'

ROOT_URLCONF = 'OauthAuthentication.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'OauthAuthentication.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static_root")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Media files (Uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.User'

# Email settings
DEFAULT_EMAIL_FROM = os.getenv('DEFAULT_EMAIL_FROM', 'Credit Engine Tool <sipltest49@gmail.com>')
DEFAULT_EMAIL_BCC = os.getenv('DEFAULT_EMAIL_BCC', 'aashish.soni@systematixindia.com')
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.googlemail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 465))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'sipltest49@gmail.com')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'False').lower() == 'true'
EMAIL_USE_SSL = os.getenv('EMAIL_USE_SSL', 'True').lower() == 'true'
SERVER_EMAIL = os.getenv('SERVER_EMAIL', 'sipltest49@gmail.com')

# Configure session-related settings
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Database-backed sessions
SESSION_COOKIE_AGE = 1800  # Session cookie age in seconds (30 minutes)
SESSION_COOKIE_NAME = 'my_session'  # Session cookie name
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Session does not expire on browser close
SESSION_COOKIE_SECURE = False  # Use secure session cookies (requires HTTPS)
SESSION_COOKIE_HTTPONLY = True  # Restrict session cookies from client-side JavaScript
SESSION_SAVE_EVERY_REQUEST = True