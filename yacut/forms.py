from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import (URL, DataRequired, Length, Optional, Regexp,
                                ValidationError)

from .constants import (INVALID_CHARACTERS, INVALID_URL_MESSAGE,
                        LONG_LINK_LABEL, MAX_ORIGINAL_LENGTH, MAX_SHORT_LENGTH,
                        REQUIRED_FIELD_MESSAGE, SHORT_LENGTH,
                        SHORT_LINK_EXISTS, SHORT_LINK_OPTION_LABEL,
                        SHORT_REGEX, SUBMIT_LABEL, URL_LENGTH_MESSAGE)
from .models import URLMap


class URLMapForm(FlaskForm):
    original_link = URLField(LONG_LINK_LABEL, validators=[
        DataRequired(message=REQUIRED_FIELD_MESSAGE),
        URL(message=INVALID_URL_MESSAGE),
        Length(min=SHORT_LENGTH, max=MAX_ORIGINAL_LENGTH, message=URL_LENGTH_MESSAGE)]
    )
    custom_id = URLField(SHORT_LINK_OPTION_LABEL, validators=[
        Optional(strip_whitespace=False),
        Length(SHORT_LENGTH, MAX_SHORT_LENGTH),
        Regexp(SHORT_REGEX, message=INVALID_CHARACTERS)]
    )
    submit = SubmitField(SUBMIT_LABEL)

    def validate_custom_id(self, field):
        if field.data and URLMap.get_urlmap_by_short(field.data):
            raise ValidationError(SHORT_LINK_EXISTS)