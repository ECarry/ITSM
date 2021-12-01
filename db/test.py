import os

import redis
from django.conf import settings
settings.configure(DEBUG=True)

pool = redis.ConnectionPool()
