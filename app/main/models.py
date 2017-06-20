from datetime import datetime
from app import db_mongo
from config import DEFINITION_TYPE_CHOICE, ENTRY_TYPE_CHOICE, MAIN_LANGUAGE


class Remark(db_mongo.EmbeddedDocument):
    remark_in_self = db_mongo.StringField()
    remark_in_English = db_mongo.StringField()
    remark_in_Chinese = db_mongo.StringField()
    remark_in_Japanese = db_mongo.StringField()
    remark_in_Russian = db_mongo.StringField()


class Example(db_mongo.EmbeddedDocument):
    label = db_mongo.IntField(required=True)
    example_in_self = db_mongo.StringField()
    example_in_English = db_mongo.StringField()
    example_in_Chinese = db_mongo.StringField()
    example_in_Japanese = db_mongo.StringField()
    example_in_Russian = db_mongo.StringField()


class Definition(db_mongo.EmbeddedDocument):
    label = db_mongo.IntField(required=True)
    POS_CHOICE = (
        (-1, 'None'),
        (0, 'noun'),
        (1, 'pronoun'),
        (2, 'verb'),
        (3, 'intransitive_verb'),
        (4, 'transitive_verb'),
        (5, 'adjective'),
        (6, 'adverb'),
        (7, 'numeral'),
        (8, 'preposition'),
        (9, 'conjunction'),
        (10, 'auxiliary'),
        (11, 'interjection'),
        (12, 'other'),
    )
    POS = db_mongo.IntField(choices=POS_CHOICE)
    definition_type = db_mongo.IntField(choices=DEFINITION_TYPE_CHOICE)
    definition_in_self = db_mongo.StringField()
    definition_in_English = db_mongo.StringField()
    definition_in_Chinese = db_mongo.StringField()
    definition_in_Japanese = db_mongo.StringField()
    definition_in_Russian = db_mongo.StringField()
    example = db_mongo.ListField(db_mongo.EmbeddedDocumentField(Example))


class Entry(db_mongo.Document):
    created_time = db_mongo.DateTimeField(default=datetime.now())
    last_modified = db_mongo.DateTimeField()
    last_editor = db_mongo.StringField(default='admin')
    entry_name = db_mongo.StringField(unique=True, required=True)
    entry_type = db_mongo.IntField(choices=ENTRY_TYPE_CHOICE, default=MAIN_LANGUAGE)
    pronunciation = db_mongo.StringField()
    related_entries = db_mongo.ListField(db_mongo.StringField(), default=[])
    remark = db_mongo.EmbeddedDocumentField(Remark)
    definition = db_mongo.ListField(db_mongo.EmbeddedDocumentField(Definition))
