from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def create_url():
    if not request.is_json:
        raise InvalidAPIUsage('A JSON body is required to create a short link.')

    data = request.get_json()

    if 'url' not in data:
        raise InvalidAPIUsage('The request is missing required fields.')

    if 'custom_id' in data:
        if not data['custom_id'].isalnum():
            raise InvalidAPIUsage("The 'custom_id' contains invalid values. Can only contain digits and ASCII letters.")

        if data['custom_id'] and URLMap.query.filter_by(short=data['custom_id']).first() is not None:
            raise InvalidAPIUsage('Short link is already exists.')

    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify({'url': url.to_dict()}), 201


@app.route('/api/id/<string:short_id>', methods=['GET'])
def get_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()

    if url is None:
        raise InvalidAPIUsage("URL with the specified 'short' was not found.", 404)

    url_dict = url.to_dict()
    return jsonify({'url': url_dict['url']}), 200