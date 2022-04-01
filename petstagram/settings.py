import os
from pathlib import Path
from petstagram.utils import is_production, is_test


BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = os.getenv("DEBUG", "True") == "True"
APP_ENVIRONMENT = os.getenv("APP_ENVIRONMENT", "Development")
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-t^jhlxn515i5sbhy3(e6l6c&$ex6(ct7j)5e@(nh=^1(db(&g7",
)
ALLOWED_HOSTS = os.getenv("DB_HOST", "127.0.0.1").split(" ")
print(ALLOWED_HOSTS)
# Application definition

DJANGO_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
)

THIRD_PARTY_APPS = ()

PROJECT_APPS = (
    "petstagram.main",
    "petstagram.accounts",
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "petstagram.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "petstagram.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.getenv("DB_HOST", "127.0.0.1"),
        "PORT": os.getenv("DB_PORT", "5432"),
        "NAME": os.getenv("DB_NAME", "petstragram_db"),
        "USER": os.getenv("DB_USER", "postgres"),
        "PASSWORD": os.getenv("DB_PASSWORD", "Newlife7"),
    }
}

AUTH_PASSWORD_VALIDATORS = []
if is_production():
    AUTH_PASSWORD_VALIDATORS.extend(
        [
            {
                "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
            },
            {
                "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
            },
            {
                "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
            },
            {
                "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
            },
        ]
    )


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (BASE_DIR / "static",)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


MEDIA_ROOT = BASE_DIR / "media/"
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGGING_LEVEL = "DEBUG"

if is_production():
    LOGGING_LEVEL = "INFO"
elif is_test():
    LOGGING_LEVEL = "CRITICAL"

LOGGING = {
    "version": 1,
    "handlers": {
        "console": {
            # DEBUG, WARNING, INFO, ERROR, CRITICAL,
            "level": LOGGING_LEVEL,
            "filters": [],
            "class": "logging.StreamHandler",
        }
    },
    "loggers": {
        "django.db.backends": {
            "level": LOGGING_LEVEL,
            "handlers": ["console"],
        }
    },
}

AUTH_USER_MODEL = "accounts.PetstagramUser"
