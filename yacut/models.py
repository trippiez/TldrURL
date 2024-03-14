from datetime import datetime

from flask import url_for

from yacut import db

from .constants import MAX_ORIGINAL_LENGTH, MAX_SHORT_LENGTH


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_ORIGINAL_LENGTH), nullable=False)
    short = db.Column(db.String(MAX_SHORT_LENGTH), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def original_to_dict(self):
        lt_output = {
            'url': self.original
        }
        return lt_output

    def to_dict(self):
        lt_output = {
            'url': self.original,
            'short_link': self.get_short_link()
        }
        return lt_output

    def get_short_link(self):
        return url_for('redirect_to_url', short=self.short, _external=True)