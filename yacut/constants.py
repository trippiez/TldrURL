import re
from string import ascii_letters, digits

# general constants
MAX_ORIGINAL_LENGTH = 256
MAX_SHORT_LENGTH = 16
SHORT_LENGTH = 6


# models.py
SHORT_LENGTH_EXCEEDED = 'Длина короткой ссылки превышает 16 символов'
INVALID_CHARACTERS = 'Указано недопустимое имя для короткой ссылки'
SHORT_LINK_EXISTS = 'Предложенный вариант короткой ссылки уже существует.'
ORIGINAL_LENGTH_EXCEEDED = 'Длина исходной ссылки превышает 256 символов'
UNIQUE_SHORT_GENERATE_FAILED = 'Не удалось создать уникальную короткую ссылку'
SHORT_ID_ATTEMPTS = 3
VALID_SYMBOLS = ascii_letters + digits
SHORT_REGEX = (rf'^[{re.escape(ascii_letters + digits)}]+$')


# routes.py & api_routes.py
NOT_FOUND_ERROR = "Указанный id не найден"
MISSING_BODY_ERROR = 'Отсутствует тело запроса'
MISSING_URL_FIELD_ERROR = '"url" является обязательным полем!'
URL_WITH_ID_NOT_FOUND_ERROR = "URL с указанным id не найден."


# forms.py
LONG_LINK_LABEL = 'Long link'
SHORT_LINK_OPTION_LABEL = 'Your short link option.'
SUBMIT_LABEL = 'Create'
REQUIRED_FIELD_MESSAGE = 'Required field'
INVALID_URL_MESSAGE = 'Invalid URL'
URL_LENGTH_MESSAGE = 'Url link is already short.'