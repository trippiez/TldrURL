from flask import jsonify, request
from . import app, db
from .models import URLMap
from .error_handlers import InvalidAPIUsage


@app.route('/api/id/', methods=['POST'])
def create_url():
    if not request.is_json:
        raise InvalidAPIUsage('Request data must be in JSON format.')

    data = request.get_json()

    if 'url' not in data:
        raise InvalidAPIUsage('The request is missing required fields.')

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