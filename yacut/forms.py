from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional


class URLMapForm(FlaskForm):
    original = URLField(validators=[
        Length(1, 256),
        DataRequired(message='Required field'),
        URL(message='Invalid URL')]
    )
    short = StringField(validators=[
        Optional(),
        Length(1, 16)]
    )
    submit = SubmitField('Create')