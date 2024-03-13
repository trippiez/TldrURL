from flask import flash, redirect, render_template

from . import app
from .error_handlers import ShortError, ValidationError
from .forms import URLMapForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    try:
        return render_template(
            'index.html',
            form=form,
            short_link=URLMap.create(
                original=form.original_link.data,
                short=form.data.get('custom_id')
            ).get_short_link()
        )
    except (ValidationError, ShortError) as error:
        flash(str(error))
    return render_template('index.html', form=form)


@app.route('/<string:short>')
def redirect_to_url(short):
    return redirect(URLMap.get_original_or_404(short))