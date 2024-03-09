from flask import Flask
# from flask_redoc import Redoc
from flask_sqlalchemy import SQLAlchemy

from settings import Config

# from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
# redoc = Redoc(app)
# migrate = Migrate(app, db, render_as_batch=True)


from . import api_views, error_handlers, models, views
