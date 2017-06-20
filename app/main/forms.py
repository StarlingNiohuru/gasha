from datetime import datetime, timedelta

from flask_wtf import FlaskForm
from wtforms import DateTimeField, SelectField, SubmitField
from config import ENTRY_TYPE_CHOICE


class ShowEntriesForm(FlaskForm):
    last_modified_from = DateTimeField("Last modified from", default=datetime.now())
    last_modified_to = DateTimeField("Last modified to", default=datetime.now() - timedelta(days=1))
    entry_type = SelectField("Entries type", choices=list(ENTRY_TYPE_CHOICE), default=0)
    submit = SubmitField('Show entries')
