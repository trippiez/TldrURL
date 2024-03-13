import os
# from pathlib import Path

# FWQ_DIR = Path(__file__).resolve().parent
# openapi_file = os.path.join(FWQ_DIR, 'openapi.yml')


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default='sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', default='TQDM')