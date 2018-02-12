from flask_restful import fields

TICKET_ID_FIELD = {
	'ticket_id': fields.String()
}

COMMENT_FIELDS = {
	'author': fields.String,
	'text': fields.String
}

TICKET_FIELDS = {
	'id': fields.String,
	'title': fields.String,
	'comments': fields.List(fields.Nested(COMMENT_FIELDS)),
	'created': fields.DateTime(dt_format='rfc822'),
	'closed': fields.DateTime(dt_format='rfc822'),
	'deleted': fields.DateTime(dt_format='rfc822'),
	'creator': fields.String,
	'assignee': fields.String,
	'status': fields.String
}

TICKET_LIST_FIELDS = {
	'tickets': fields.List(fields.Nested(TICKET_FIELDS))
}