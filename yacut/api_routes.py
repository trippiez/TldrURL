from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage, ValidationError
from .models import URLMap


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_link(short_id):
    original = URLMap.get_urlmap_by_short(short=short_id)

    if original is None:
        raise InvalidAPIUsage("Указанный id не найден", 404)
        # raise InvalidAPIUsage("URL with the specified 'short' was not found.", 404)

    return jsonify(original.original_to_dict()), 200


@app.route('/api/id/', methods=['POST'])
def create_url():
    data = request.get_json()

    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
        # raise InvalidAPIUsage('A JSON body is required to create a short link.')

    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
        # raise InvalidAPIUsage('The request is missing required fields.')
    try:
        return (
            jsonify(
                URLMap.create(
                    data['url'], data.get('custom_id'), to_validate=True
                ).to_dict()
            ),
            201
        )
    except ValidationError as error:
        raise InvalidAPIUsage(str(error))


@app.route('/api/id/delete/<int:id>/', methods=['DELETE'])
def delete_link(id):
    url = URLMap.query.get(id)

    if url is None:
        raise InvalidAPIUsage("URL with the specified id was not found.", 404)

    db.session.delete(url)
    db.session.commit()
    return '', 204
