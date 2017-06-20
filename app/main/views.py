from flask import render_template, url_for, request
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from app.main.forms import ShowEntriesForm
from app.main.models import Entry
from config import MAIN_LANGUAGE
from . import main


@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
        return redirect(url_for('auth.login'))


@main.route('/dictionary', methods=['GET', 'POST'])
@login_required
def dictionary():
    form = ShowEntriesForm()
    query = Entry.objects.filter(last_modified__gte=form.last_modified_from.data,
                                 last_modified__lte=form.last_modified_to.data,
                                 entry_type=form.entry_type.data)
    return render_template('dictionary.html', form=form, query=query)
