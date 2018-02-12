from flask import Flask
from flask_restful import Api
from app.resources.commentResource import CommentResource
from app.resources.allTicketsResource import AllTicketsResource
from app.resources.ticketResource import TicketResource

def create_app():

	app = Flask(__name__)
	api = Api(app)

	api.add_resource(AllTicketsResource, '/tickets')
	api.add_resource(TicketResource, '/ticket/<string:ticket_id>')
	api.add_resource(CommentResource, '/comment/<string:ticket_id>')

	return app