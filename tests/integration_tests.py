import os

os.environ["TESTING"] = "TRUE"

import pytest
from app import app as application
from mongoengine import connect
import json

@pytest.fixture(scope="module")
def app():
	app = application.create_app()
	
	# So the server uses a test database
	yield app.test_client()

	# To drop the test database
	os.environ["TESTING"] = "FALSE"
	db = connect('yolk_test')
	db.drop_database('yolk_test')


def test_empty_tickets(app):
	res = app.get('/tickets')
	assert res.status_code == 200

def test_add_ticket(app):
	res = app.post('/tickets', data=json.dumps({'title':'My computer is broken.','creator':'test@test.com'}),
	content_type='application/json')
	assert res.status_code == 200

def test_ticket_added(app):
	res = app.get('/tickets')
	assert b'\"title\": \"My computer is broken.\"' in res.data
	assert b'\"creator\": "test@test.com\"' in res.data

def test_status(app):
	res = app.post('/tickets', data=json.dumps({'title':'My computer is on fire.','creator':'test@test.com'}),
		content_type='application/json')
	ticket_id = res.data.decode("utf-8").split(' ')[1].split('\"')[1]
	res = app.put('/ticket/' + ticket_id, data=json.dumps({'status':'done'}), content_type='application/json')
	assert res.status_code == 200
	res = app.get('/ticket/' + ticket_id)
	assert b'\"status\": \"done\"' in res.data

def test_bad_status(app):
	res = app.post('/tickets', data=json.dumps({'title':'My computer is gone.','creator':'test@test.com'}),
		content_type='application/json')
	ticket_id = res.data.decode("utf-8").split(' ')[1].split('\"')[1]
	res = app.put('/ticket/' + ticket_id, data=json.dumps({'status':'whoops'}), content_type='application/json')
	assert res.status_code == 400

def test_assignee(app):
	res = app.post('/tickets', data=json.dumps({'title':'I am on fire.','creator':'test@test.com'}),
		content_type='application/json')
	ticket_id = res.data.decode("utf-8").split(' ')[1].split('\"')[1]
	res = app.put('/ticket/' + ticket_id, data=json.dumps({'assignee':'itguy@test.com'}), content_type='application/json')
	assert res.status_code == 200
	res = app.get('/ticket/' + ticket_id)
	assert b'\"assignee\": \"itguy@test.com\"' in res.data

def test_comment(app):
	res = app.post('/tickets', data=json.dumps({'title':'I don\'t have insurance','creator':'test@test.com'}),
		content_type='application/json')
	ticket_id = res.data.decode("utf-8").split(' ')[1].split('\"')[1]
	res = app.put('/comment/' + ticket_id, data=json.dumps({'author':'test@test.com', 'text':'Hurry the !@#$ up.'}), content_type='application/json')
	assert res.status_code == 200
	res = app.get('/ticket/' + ticket_id)
	assert b'\"comments\": [{\"author\": \"test@test.com\", \"text\": \"Hurry the !@#$ up.\"}]' in res.data

