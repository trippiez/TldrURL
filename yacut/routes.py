from flask import abort, flash, redirect, render_template, request, url_for

from . import app, db
from .forms import URLMapForm
from .models import URLMap


@app.route('/<short>')
def redirect_to_url(short):
    url = URLMap.query.filter_by(short=short).first()
    if url:
        return redirect(url.original)
    abort(404)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLMapForm()

    if request.method == 'POST':
        short = form.short.data

        if not short:
            short = URLMap.get_unique_short_id()

        if short and URLMap.query.filter_by(short=short).first() is not None:
            flash('Short link is already exists.')
            return redirect(url_for('index'))

        if form.validate_on_submit():
            url = URLMap(
                original=form.original.data,
                short=short
            )
            db.session.add(url)
            db.session.commit()
        return render_template('index.html', form=form, short=short)
    return render_template('index.html', form=form)

    # formdata = session.get('formdata', None)
    # if formdata:
    #     form = MyForm(MultiDict(formdata))
    #     form.validate()
    #     session.pop('formdata')