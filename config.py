import os

class Config:
    key = os.urandom(16)
    SECRET_KEY = os.environ.get('SECRET_KEY', key)
    TIMEOUT = 10