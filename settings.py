import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
openapi_file = os.path.join(BASE_DIR, 'openapi.yml')


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')