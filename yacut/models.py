import string
from datetime import datetime
from random import choices

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def get_unique_short_id():
        characters = string.digits + string.ascii_letters
        short = ''.join(choices(characters, k=16))
        return short