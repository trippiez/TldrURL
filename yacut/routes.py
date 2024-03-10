from flask import flash, redirect, render_template, request, url_for

from . import app, db
from .forms import URLMapForm
from .models import URLMap


@app.route('/<short>')
def redirect_to_url(short):
    link = URLMap.query.filter_by(short=short).first()
    return redirect(link.original)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLMapForm()

    if request.method == 'POST':
        short = form.short.data

        if short and URLMap.query.filter_by(short=short).first() is not None:
            flash('The proposed short link option already exists.')
            return redirect(url_for('index'))

        if not short:
            short = URLMap.get_unique_short_id()

        if form.validate_on_submit():
            link = URLMap(
                original=form.original.data,
                short=short
            )
            db.session.add(link)
            db.session.commit()
        return render_template('index.html', form=form, short=short)
    return render_template('index.html', form=form)


@app.route('/delete/<int:id>')
def delete_link(id):
    link = URLMap.query.get(id)
    db.session.delete(link)
    db.session.commit()
    return "<h1>success deleted</h1>"

    # formdata = session.get('formdata', None)
    # if formdata:
    #     form = MyForm(MultiDict(formdata))
    #     form.validate()
    #     session.pop('formdata')