import os

from .base import *

INSTALLED_APPS = ["daphne"] + INSTALLED_APPS

CANONICAL_ROOT_DOMAIN = "localhost:8000"

DEBUG = True

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", ["localhost", "127.0.0.1"])

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "memcached:11211",
    }
}
