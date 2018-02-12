from flask_restful import (reqparse, Resource)
from app.models.ticket import Ticket, Comment
from app.resources.lib.util import abort_if_ticket_id_invalid
from app.resources.lib.fields import COMMENT_FIELDS

commentParser = reqparse.RequestParser();
commentParser.add_argument('author', type=str, required=True, help='No `author` provided', location='json')
commentParser.add_argument('text', type=str, required=True, help='No `text` provided', location='json')

class CommentResource(Resource):

	def put(self, ticket_id):
		
		abort_if_ticket_id_invalid(ticket_id)
		ticket = Ticket.objects.get(id=ticket_id)
		args = commentParser.parse_args()
		ticket.comments.append(Comment(author=args['author'], text=args['text']))
		ticket.save()
