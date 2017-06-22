from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import DateTimeField, SelectField, SubmitField, StringField, FormField, FieldList
from config import ENTRY_TYPE_CHOICE
from .models import DEFINITION_TYPE_CHOICE, Definition


class ShowEntriesForm(FlaskForm):
    last_modified_from = DateTimeField("Last modified from", default=datetime(2017, 1, 1))
    last_modified_to = DateTimeField("Last modified to", default=datetime.now())
    entry_type = SelectField("Entries type", choices=[(-2, 'All')] + list(ENTRY_TYPE_CHOICE), default=-2)
    submit = SubmitField('Show entries')


class EditDefinitionForm(FlaskForm):
    POS = SelectField("POS", choices=Definition.POS_CHOICE)
    definition_type = SelectField("Definition type", choices=DEFINITION_TYPE_CHOICE)
    definition_in_self = StringField("Definition in self")
    definition_in_English = StringField("Definition in English")
    definition_in_Chinese = StringField("Definition in Chinese")


class EditEntryForm(FlaskForm):
    entry_name = StringField("Entry name")
    entry_type = SelectField("Entry type", choices=list(ENTRY_TYPE_CHOICE), default=0)
    pronunciation = StringField("Pronunciation")
    definitions = FieldList(FormField(EditDefinitionForm), min_entries=0)
