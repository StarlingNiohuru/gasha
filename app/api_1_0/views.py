from flask import jsonify
from mongoengine import DoesNotExist

from app.api_1_0 import api
from app.main.models import Entry


@api.route('/all_entries')
def get_all_entries():
    dictionary = Entry.objects.all()
    return jsonify(dictionary.to_json())


@api.route('/entries/<string:entry_name>')
def get_entry(entry_name):
    try:
        entry = Entry.objects.get(entry_name=entry_name)
        return jsonify(entry.to_json())
    except DoesNotExist:
        return jsonify('{}')
