import re
from string import ascii_letters, digits

from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import (URL, DataRequired, Length, Optional, Regexp,
                                ValidationError)

from .models import URLMap


class URLMapForm(FlaskForm):
    original_link = URLField('Long link', validators=[
        DataRequired(message='Required field'),
        URL(message='Invalid URL'),
        Length(min=6, max=256, message='Url link is already short.')]
    )
    custom_id = URLField('Your short link option.', validators=[
        Optional(strip_whitespace=False),
        Length(1, 16),
        Regexp((rf'^[{re.escape(ascii_letters + digits)}]+$'), message='Проверьте формат короткой ссылки')]
    )
    submit = SubmitField('Create')

    def validate_custom_id(self, field):
        if field.data and URLMap.get_urlmap_by_short(field.data):
            raise ValidationError('Предложенный вариант короткой ссылки уже существует.')