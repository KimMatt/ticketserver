from flask_restful import abort
from app.models.ticket import Ticket
from mongoengine.queryset import DoesNotExist

def abort_if_ticket_id_invalid(ticket_id):
	
	try:
		Ticket.objects.get(id=ticket_id)
	except DoesNotExist:
		abort(404, message="No ticket with given `ticket_id` found")