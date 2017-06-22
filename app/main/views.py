from flask import render_template, url_for, flash
from flask_login import login_required, current_user
from mongoengine import DoesNotExist
from werkzeug.utils import redirect

from app.main.forms import ShowEntriesForm, EditEntryForm
from app.main.models import Entry
from config import ENTRY_TYPE_CHOICE
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
    entry_type_list = [int(x[0]) for x in ENTRY_TYPE_CHOICE] if form.entry_type.data == '-2' else [
        int(form.entry_type.data)]
    query = Entry.objects.filter(last_modified__gte=form.last_modified_from.data,
                                 last_modified__lte=form.last_modified_to.data,
                                 entry_type__in=entry_type_list)
    return render_template('dictionary.html', form=form, query=query, entry_type_dict=dict(ENTRY_TYPE_CHOICE))


@main.route('/edit/<entry_name>')
@login_required
def edit_entry(entry_name):
    try:
        entry = Entry.objects.get(entry_name=entry_name)
    except DoesNotExist:
        flash('The entry %s is not exist, back to dashboard.' % entry_name)
        return redirect(url_for('.dictionary'))
    else:
        form = EditEntryForm()
        form.entry_name.data = entry.entry_name
        form.entry_type.data = entry.entry_type
        form.pronunciation.data = entry.pronunciation
        return render_template('entry.html', form=form)
