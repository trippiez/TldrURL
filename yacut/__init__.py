from flask import Flask
from flask_migrate import Migrate
from flask_redoc import Redoc
from flask_sqlalchemy import SQLAlchemy

from settings import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# redoc = Redoc(app, openapi_file)


from . import api_views, error_handlers, views
