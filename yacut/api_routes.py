from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def create_url():
    data = request.get_json()

    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
        # raise InvalidAPIUsage('A JSON body is required to create a short link.')

    url = URLMap()

    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
        # raise InvalidAPIUsage('The request is missing required fields.')

    if 'custom_id' in data:
        custom_id = data['custom_id']
        if not custom_id.isalnum() or len(custom_id) > 16:
            raise InvalidAPIUsage("Указано недопустимое имя для короткой ссылки", 400)
            # raise InvalidAPIUsage("Invalid 'custom_id'.")

        if URLMap.query.filter_by(short=custom_id).first() is not None:
            raise InvalidAPIUsage('Предложенный вариант короткой ссылки уже существует.')
            # raise InvalidAPIUsage('Short link is already exists.')

    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify({'url': url.to_dict()}), 201


@app.route('/api/id/delete/<int:id>/', methods=['DELETE'])
def delete_link(id):
    url = URLMap.query.get(id)

    if url is None:
        raise InvalidAPIUsage("URL with the specified id was not found.", 404)

    db.session.delete(url)
    db.session.commit()
    return '', 204


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()

    if url is None:
        raise InvalidAPIUsage("Указанный id не найден", 404)
        # raise InvalidAPIUsage("URL with the specified 'short' was not found.", 404)

    url_dict = url.to_dict()
    return jsonify({'url': url_dict['url']}), 200
