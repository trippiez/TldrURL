import string
from datetime import datetime
from random import choices

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(6), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @staticmethod
    def get_unique_short_id():
        characters = string.digits + string.ascii_letters
        short = ''.join(choices(characters, k=6))
        return short

    def to_dict(self):
        return dict(
            id=self.id,
            short_link=self.short if self.short else self.get_unique_short_id(),
            url=self.original,
            timestamp=self.timestamp
        )

    def from_dict(self, data):
        self.original = data['url']
        if 'custom_id' in data:
            self.short = data['custom_id']