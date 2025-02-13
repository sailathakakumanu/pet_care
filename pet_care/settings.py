from pathlib import Path
import pymysql

# If you're using PyMySQL instead of mysqlclient
pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'django-insecure-mhwe_n*$t%zf$sl(%tv6mk6&h1+26=pfev+a3dw*&58(zit3y%'
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
    'allauth',  # Add django-allauth for authentication
    'allauth.account',  # Add account management functionality
    'allauth.socialaccount',  # Add social account management
    'allauth.socialaccount.providers.google',  # Google sign-in provider
    'pets',
    'tailwind',
    # 'theme',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

ROOT_URLCONF = 'pet_care.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Template directory
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

WSGI_APPLICATION = 'pet_care.wsgi.application'

# Database configuration for MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'petcare',  # Your database name
        'USER': 'root',  # Your MySQL username
        'PASSWORD': 'Omkar@2007',  # Your MySQL password
        'HOST': 'localhost',  # Set to 'localhost' if MySQL is local
        'PORT': '3306',  # Default MySQL port
    }
}

# Password validation settings
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

# Localization settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files settings
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication settings
AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',  # Backend for allauth
)

# Allauth settings
SITE_ID = 1  # Required for allauth
LOGIN_REDIRECT_URL = '/'  # Redirect after login

# Google OAuth2 configuration (for Google Sign-In)
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<YOUR_GOOGLE_CLIENT_ID>'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<YOUR_GOOGLE_CLIENT_SECRET>'

# For security reasons, do not store sensitive keys in code. You can use environment variables or a .env file instead.
TAILWIND_APP_NAME = 'theme'
