from flask import jsonify, request
from . import app, db
from .models import URLMap


@app.route('/api/id/', methods=['POST'])
def create_url():
    data = request.get_json()
    url = URLMap()
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify({'url': url.to_dict()}), 201


@app.route('/api/id/<string:short_id>', methods=['GET'])
def get_url(short_id):
    url = URLMap.query.filter_by(short=short_id).first()
    url_dict = url.to_dict()
    return jsonify({'url': url_dict['url']}), 200