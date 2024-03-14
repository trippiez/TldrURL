from http import HTTPStatus

from flask import jsonify, request

from yacut import app, db

from .constants import (MISSING_BODY_ERROR, MISSING_URL_FIELD_ERROR,
                        NOT_FOUND_ERROR, URL_WITH_ID_NOT_FOUND_ERROR)
from .error_handlers import InvalidAPIUsage, ValidationError
from .models import URLMap
from .utils import URLMapUtils


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_link(short_id):
    original = URLMapUtils.get_urlmap_by_short(short=short_id)

    if original is None:
        raise InvalidAPIUsage(NOT_FOUND_ERROR, HTTPStatus.NOT_FOUND)

    return jsonify(original.original_to_dict()), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def create_url():
    data = request.get_json()

    if data is None:
        raise InvalidAPIUsage(MISSING_BODY_ERROR)

    if 'url' not in data:
        raise InvalidAPIUsage(MISSING_URL_FIELD_ERROR)

    try:
        return (
            jsonify(URLMapUtils.create(
                data['url'],
                data.get('custom_id'),
                to_validate=True
            ).to_dict()
            ),
            HTTPStatus.CREATED
        )
    except ValidationError as error:
        raise InvalidAPIUsage(str(error))


@app.route('/api/id/delete/<int:id>/', methods=['DELETE'])
def delete_link(id):
    url = URLMap.query.get(id)

    if url is None:
        raise InvalidAPIUsage(URL_WITH_ID_NOT_FOUND_ERROR, HTTPStatus.NOT_FOUND)

    db.session.delete(url)
    db.session.commit()
    return '', HTTPStatus.NO_CONTENT
