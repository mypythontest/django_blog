from .base import *

DEBUG = True

SECRET_KEY = 'dev'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dev',
        'USER': 'test',
        'PASSWORD': 'test',
    }
}

