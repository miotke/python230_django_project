""" Holds production settings """

import os
import dj_database_url
from .settings import *


DATABASES = {
    'default': dj_database_url.config(default='sqlite:///' + os.path.join(BASE_DIR, 'db_sqlite3'))
}

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS'), 'localhost']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
SECRET_KEY = os.environ.get('SECRET_KEY')
