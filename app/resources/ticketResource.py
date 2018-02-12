from flask_restful import (reqparse, abort, Resource, fields, marshal_with)
from app.models.ticket import Ticket, STATUS_TYPES
from app.resources.lib.fields import COMMENT_FIELDS, TICKET_FIELDS
from app.resources.lib.util import abort_if_ticket_id_invalid
from datetime import datetime

updateParser = reqparse.RequestParser();
updateParser.add_argument('assignee', type=str, required=False, location='json')
updateParser.add_argument('status', type=str, required=False, location='json')

def abort_if_invalid_update(args):

	if(args.get('assignee') is None and args.get('status') is None):
		abort(400, message="Must provide an update argument, `assignee` or `status` or both")
	if(args.get('status') and args.get('status').lower() not in STATUS_TYPES):
		abort(400, message="Status must be either `backlog`, `in progress`, `review`, or `done`")

class TicketResource(Resource):

	@marshal_with(TICKET_FIELDS)
	def get(self, ticket_id):
		abort_if_ticket_id_invalid(ticket_id)
		return Ticket.objects.get(id=ticket_id)

	def put(self, ticket_id):

		abort_if_ticket_id_invalid(ticket_id)
		args = updateParser.parse_args()
		abort_if_invalid_update(args)

		ticket = Ticket.objects.get(id=ticket_id)
		if(args.get('status')):
			ticket.status = args['status'].lower()
			if(args['status'].lower() == 'done'):
				ticket.closed = datetime.now()
		if(args.get('assignee')):
			ticket.assignee = args['assignee']
		ticket.save()
    	
