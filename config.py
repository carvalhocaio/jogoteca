import os
from decouple import config


SECRET_KEY = config('SECRET_KEY')

MYSQL_HOST = config('MYSQL_HOST')
MYSQL_USER = config('MYSQL_USER')
MYSQL_PASSWORD = config('MYSQL_PASSWORD')
MYSQL_DB = config('MYSQL_DB')
MYSQL_PORT = 3306
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
