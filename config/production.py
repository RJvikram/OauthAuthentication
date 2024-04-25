from pathlib import Path
import dj_database_url, os
from .base import *
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL', 'postgresql://oauthUser:AuthUser!1234@localhost:5432/OauthAuthentication')
    )
}