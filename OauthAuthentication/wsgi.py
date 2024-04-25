"""
WSGI config for OauthAuthentication project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OauthAuthentication.settings')
ENVIRONMENT = os.getenv('DJANGO_ENV', 'production')

# Import the appropriate settings based on the environment
if ENVIRONMENT == 'production':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.production')
if ENVIRONMENT == 'development':
    print("calling")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.development')

application = get_wsgi_application()
