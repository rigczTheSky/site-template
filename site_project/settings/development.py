from .base import *
import os

# Bezpieczeństwo
SECRET_KEY = 'dev-secret-key-do-nie-uzywania-w-produkcji'

DEBUG = True

ALLOWED_HOSTS = []

# Baza danych - SQLite (prosta, lokalna)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

