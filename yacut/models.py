import random
import re
from datetime import datetime
from string import ascii_letters, digits

from flask import url_for

from yacut import db

from .error_handlers import ShortGenerateError, ValidationError


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(256), nullable=False)
    short = db.Column(db.String(16), nullable=False, unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def original_to_dict(self):
        return dict(url=self.original)

    def to_dict(self):
        return dict(url=self.original, short_link=self.get_short_link())

    def get_short_link(self):
        return url_for('redirect_to_url', short=self.short, _external=True)

    @staticmethod
    def get_unique_short_id(
        symbols=ascii_letters + digits,
        length=6
    ):
        for _ in range(3):
            short_link = ''.join(random.choices(symbols, k=length))
            if not URLMap.get_urlmap_by_short(short=short_link):
                return short_link
        raise ShortGenerateError(
            'Имя {} уже занято!'.format(short_link)
        )

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
            if original_len > 256:
                raise ValidationError('Длина оригинальной ссылки "{}" больше чем 4096'.format(original_len))
            if short:
                short_len = len(short)
                if short_len > 16:
                    raise ValidationError('Указано недопустимое имя для короткой ссылки')
                if not re.match((rf'^[{re.escape(ascii_letters + digits)}]+$'), short):
                    raise ValidationError('Указано недопустимое имя для короткой ссылки')
                if URLMap.get_urlmap_by_short(short):
                    raise ValidationError('Предложенный вариант короткой ссылки уже существует.')
        if not short:
            short = URLMap.get_unique_short_id()
        urlmap = URLMap(original=original, short=short)
        db.session.add(urlmap)
        db.session.commit()
        return urlmap