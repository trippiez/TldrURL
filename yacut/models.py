from datetime import datetime

from yacut import db
import string
from random import choices


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.get_unique_short_id()

    def get_unique_short_id(self):
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=16))

        link = self.query.filter_by(short=short_url).first()
        if link:
            return self.get_unique_short_id