from flask import Flask
from flask_migrate import Migrate
from flask_redoc import Redoc
from flask_sqlalchemy import SQLAlchemy

from settings import Config, openapi_file

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
db.create_all()
migrate = Migrate(app, db, render_as_batch=True)

redoc = Redoc(app, openapi_file)


from . import api_routes, constants, error_handlers, models, routes
