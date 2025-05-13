from .base import *
import os

# Pobieramy klucz z zmiennej środowiskowej (np. z pliku .env)
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
if not SECRET_KEY:
    raise Exception("DJANGO_SECRET_KEY is not set in environment variables!")

DEBUG = False

# Dozwolone hosty - wpisz domeny swojej strony
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')

# Konfiguracja bazy danych produkcyjnej (np. PostgreSQL)
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# Statyczne pliki - w produkcji zbieramy do STATIC_ROOT
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


