from flask import jsonify, request

from . import app, db
from .constants import (MISSING_BODY_ERROR, MISSING_URL_FIELD_ERROR,
                        NOT_FOUND_ERROR, URL_WITH_ID_NOT_FOUND_ERROR)
from .error_handlers import InvalidAPIUsage, ValidationError
from .models import URLMap


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_link(short_id):
    original = URLMap.get_urlmap_by_short(short=short_id)

    if original is None:
        raise InvalidAPIUsage(NOT_FOUND_ERROR, 404)

    return jsonify(original.original_to_dict()), 200


@app.route('/api/id/', methods=['POST'])
def create_url():
    data = request.get_json()

    if data is None:
        raise InvalidAPIUsage(MISSING_BODY_ERROR)

    if 'url' not in data:
        raise InvalidAPIUsage(MISSING_URL_FIELD_ERROR)

    try:
        return (
            jsonify(URLMap.create(
                data['url'],
                data.get('custom_id'),
                to_validate=True
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
        raise InvalidAPIUsage(URL_WITH_ID_NOT_FOUND_ERROR, 404)

    db.session.delete(url)
    db.session.commit()
    return '', 204
