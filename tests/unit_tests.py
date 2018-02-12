import pytest
from datetime import datetime

from app.models.ticket import Ticket
from app.resources.lib.util import abort_if_ticket_id_invalid
from app.resources.ticketResource import abort_if_invalid_update
from app.models.ticket import Ticket

def test_invalid_id():
	try:
		abort_if_ticket_id_invalid('0123456789ab0123456789ab')
	except Exception as ex:
		assert (type(ex).__name__ == 'NotFound')

def test_valid_id():
	ticket = Ticket(title='test', creator="hi@gmail.com", created=datetime.now())
	ticket.save()
	abort_if_ticket_id_invalid(ticket.id)
	ticket.delete()

def test_invalid_status():
	args = dict()
	args['assignee'] = "test"
	args['status'] = "invalid"
	try:
		abort_if_invalid_update(args)
	except Exception as ex:
		assert (type(ex).__name__ == 'BadRequest')

def test_invalid_args():
	args = dict()
	try:
		abort_if_invalid_update(args)
	except Exception as ex:
		assert (type(ex).__name__ == 'BadRequest')

def test_valid_update():
	args = dict()
	args['assignee'] = "test"
	args['status'] = "done"
	abort_if_invalid_update(args)	

