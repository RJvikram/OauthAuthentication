from pathlib import Path
import dj_database_url, os
from .base import *
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL', 'postgresql://accountoauthuser:AuthUser!1234@localhost:5432/oauthauthentication')
    )
}

CORS_ALLOWED_ORIGINS = ["http://localhost:8000", "https://example.com",]