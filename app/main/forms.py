from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import DateTimeField, SelectField, SubmitField
from config import ENTRY_TYPE_CHOICE


class ShowEntriesForm(FlaskForm):
    last_modified_from = DateTimeField("Last modified from", default=datetime(2017, 1, 1))
    last_modified_to = DateTimeField("Last modified to", default=datetime.now())
    entry_type = SelectField("Entries type", choices=[(-2, 'All')] + list(ENTRY_TYPE_CHOICE), default=-2)
    submit = SubmitField('Show entries')
