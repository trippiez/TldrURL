from flask import Flask
from flask_migrate import Migrate
# from flask_redoc import Redoc
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from settings import Config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app, metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate(app, db, render_as_batch=True)
# redoc = Redoc(app)


from . import api_views, error_handlers, models, views
