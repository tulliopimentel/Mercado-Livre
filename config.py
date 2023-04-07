import os

class Config:
    key = os.urandom(16)
    SECRET_KEY = os.environ.get('SECRET_KEY', key)
    TIMEOUT = 10
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3307
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Tu110201'
    MYSQL_DB = 'application'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Tu110201@localhost:3306/application'