from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional


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
    submit = SubmitField('Создать')