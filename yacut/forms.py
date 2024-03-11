from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional


class URLMapForm(FlaskForm):
    original = URLField('Long link', validators=[
        Length(min=6, max=256, message='Url link is already short'),
        DataRequired(message='Required field'),
        URL(message='Invalid URL')]
    )
    short = StringField('Your short link option', validators=[
        Optional(),
        Length(1, 16)]
    )
    submit = SubmitField('Create')