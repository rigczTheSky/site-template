# News Portal Django Project

A simple Django-based news portal featuring categorized posts, TinyMCE rich text editor, and image upload support.

## Features

- Display posts categorized as World, Domestic, and About
- TinyMCE editor for rich content creation and formatting
- Image upload functionality within posts
- Responsive layout with sidebar navigation
- Separate settings for development and production environments
- Environment variable support for sensitive data

## Technologies

- Python 3.12
- Django 5.2.1
- TinyMCE
- SQLite (default development database)

## Installation

git clone https://github.com/rigczTheSky/site-template.git
cd site-template
python3 -m venv .venv
source .venv/bin/activate # Linux/macOS
source .venv\Scripts\activate.bat # Windows
pip install django django-tinymce
python manage.py makemigrations
python manage.py migrate 
python manage.py runserver

