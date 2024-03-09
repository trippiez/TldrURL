from flask import render_template

from . import app, db
from .forms import URLMapForm
from .models import URLMap


# @shortener.route('/<short_url>')
# def redirect_to_url():
#     pass
#     # return render_template('index.html')


@app.route('/')
def index():
    form = URLMapForm()
    return render_template('index.html', form=form)


@app.route('/add_link', methods=['POST'])
def add_link():
    form = URLMapForm()
    if form.validate_on_submit():
        urlmap = URLMap(
            original=form.original.data,
            short=form.short.data)
        db.session.add(urlmap)
        db.session.commit()
    return render_template('index.html', form=form, new_url=urlmap.short)


# @shortener.errorhandler(404)
# def page_not_found(error):
#     return render_template('404.html'), 404
#     return '<h1>Not Found</h1>'