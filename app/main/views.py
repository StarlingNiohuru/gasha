from flask import render_template, url_for, jsonify, request
from flask_login import login_required, current_user
from werkzeug.utils import redirect

from app.main.forms import ShowEntriesForm, EditEntryForm, EditDefinitionForm
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
    edit_entry_form = EditEntryForm()
    edit_def_form = EditDefinitionForm()
    return render_template('dictionary.html', form=form, query=query, entry_type_dict=dict(ENTRY_TYPE_CHOICE),
                           edit_entry_form=edit_entry_form, edit_def_form=edit_def_form)


@main.route('/edit', methods=['POST'])
@login_required
def edit_entry():
    entry_name = request.get_json()['entry_name']
    entry = Entry.objects.get(entry_name=entry_name)
    return jsonify(entry.to_json())
