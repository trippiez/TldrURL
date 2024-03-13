from flask import Flask
from flask_migrate import Migrate
from flask_redoc import Redoc
from flask_sqlalchemy import SQLAlchemy

from settings import Config, openapi_file

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'TQDM'

db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)

redoc = Redoc(app, openapi_file)


from . import api_views, error_handlers, views
