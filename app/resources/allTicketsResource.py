from flask_restful import (reqparse, abort, Resource, fields, marshal_with)
from app.models.ticket import Ticket
from app.resources.lib.fields import TICKET_FIELDS, TICKET_LIST_FIELDS, TICKET_ID_FIELD
from app.resources.lib.util import abort_if_ticket_id_invalid
from datetime import datetime
import json

ticketParser = reqparse.RequestParser()
ticketParser.add_argument('title', type=str, required=True, help='No `title` provided', location='json')
ticketParser.add_argument('creator', type=str, required=True, help='No `creator` provided', location='json')

filterParser = reqparse.RequestParser()
filterParser.add_argument('filter', type=str, required=False, location="args")

class AllTicketsResource(Resource):


	@marshal_with(TICKET_ID_FIELD)
	def post(self):

		args = ticketParser.parse_args()
		ticket = Ticket(title = args['title'], creator = args['creator'], created=datetime.now())
		ticket.save()
		return {'ticket_id' : ticket.id}

	@marshal_with(TICKET_LIST_FIELDS)
	def get(self):

		args = filterParser.parse_args()
		filter = args.get('filter')

		if filter is None:
			return {'tickets': Ticket.objects}
		elif filter == 'status':
			return {'tickets' : Ticket.objects.order_by('+status')}
		elif filter == 'date':
			return {'tickets': Ticket.objects.order_by('+date')}
		else:
			abort(400, message="invalid filter field, must be `status` or `date`")
