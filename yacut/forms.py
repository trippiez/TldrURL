from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField
from wtforms.validators import DataRequired, Optional, URL, Length


class URLMapForm(FlaskForm):
    original = URLField(validators=[
        Length(1, 256),
        DataRequired(message='Обязательное поле'),
        URL(message='Не удалось распознать URL')]
    )
    short = StringField(validators=[
        Optional(),
        Length(1, 16)]
    )
    submit = SubmitField()