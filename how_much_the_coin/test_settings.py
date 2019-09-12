"""SETTINGS FOR TEST ENV."""
import os
from dotenv import load_dotenv

try:
    from .settings import *
except ImportError:
    print("Can't import base settings")


load_dotenv()


SECRET_KEY = 'dfgfhyjth767np*2^9f%ze878mghj990=0ghng324+$a83@$9j%3b'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'db',
        'PORT': 5432,
        'USER': 'postgres',
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'test_rates'),
        'NAME': 'coin_rates_test',
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[{asctime}] {message}',
            'style': '{',
            'datefmt': "%d/%b/%Y %H:%M:%S",
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },

    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}