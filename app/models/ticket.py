from mongoengine import (Document, EmbeddedDocument, connect, ReferenceField, StringField, ListField, EmbeddedDocumentField, DateTimeField)
import os

db_name = ''
if(os.environ.get("ENVIRONMENT", None) == "PROD"):
	db_name = "yolk_prod"
elif(os.environ.get("TESTING", None) == "TRUE"):
	db_name = "yolk_test"
else:
	db_name = "yolk_dev"

connect(db_name)

STATUS_TYPES = ['backlog', 'in progress', 'review', 'done']

class Comment(EmbeddedDocument):
	text = StringField(required=True)
	author = StringField(required=True)

class Ticket(Document):
	title = StringField(required=True)
	comments = ListField(EmbeddedDocumentField(Comment))
	created = DateTimeField(required=True)
	closed = DateTimeField()
	deleted = DateTimeField()
	creator = StringField(required=True)
	assignee= StringField()
	status = StringField(choices=STATUS_TYPES)

