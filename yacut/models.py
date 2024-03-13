import random
import re
from datetime import datetime

from flask import url_for

from . import db
from .constants import (INVALID_CHARACTERS, MAX_ORIGINAL_LENGTH,
                        MAX_SHORT_LENGTH, ORIGINAL_LENGTH_EXCEEDED,
                        SHORT_ID_ATTEMPTS, SHORT_LENGTH, SHORT_LINK_EXISTS,
                        SHORT_REGEX, UNIQUE_SHORT_GENERATE_FAILED,
                        VALID_SYMBOLS)
from .error_handlers import ShortError, ValidationError


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_ORIGINAL_LENGTH), nullable=False)
    short = db.Column(db.String(MAX_SHORT_LENGTH), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def original_to_dict(self):
        return dict(url=self.original)

    def to_dict(self):
        return dict(url=self.original, short_link=self.get_short_link())

    def get_short_link(self):
        return url_for('redirect_to_url', short=self.short, _external=True)

    @staticmethod
    def get_unique_short_id(symbols=VALID_SYMBOLS, length=SHORT_LENGTH):
        for _ in range(SHORT_ID_ATTEMPTS):
            short_link = ''.join(random.choices(symbols, k=length))
            if not URLMap.get_urlmap_by_short(short=short_link):
                return short_link
        raise ShortError(UNIQUE_SHORT_GENERATE_FAILED)

    @staticmethod
    def get_original_or_404(short):
        return URLMap.query.filter_by(short=short).first_or_404().original

    @staticmethod
    def get_urlmap_by_short(short):
        return URLMap.query.filter_by(short=short).first()

    @staticmethod
    def create(original, short=None, to_validate=False):
        if to_validate:
            original_len = len(original)
            if original_len > MAX_ORIGINAL_LENGTH:
                raise ValidationError(ORIGINAL_LENGTH_EXCEEDED)
            if short:
                short_len = len(short)
                if short_len > MAX_SHORT_LENGTH:
                    raise ValidationError(INVALID_CHARACTERS)
                if not re.match(SHORT_REGEX, short):
                    raise ValidationError(INVALID_CHARACTERS)
                if URLMap.get_urlmap_by_short(short):
                    raise ValidationError(SHORT_LINK_EXISTS)
        if not short:
            short = URLMap.get_unique_short_id()
        urlmap = URLMap(original=original, short=short)
        db.session.add(urlmap)
        db.session.commit()
        return urlmap
