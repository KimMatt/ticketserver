## Ticket Server
##### Simple Flask server using Mongo Engine

###API
**GET** /tickets?filter=[date|status]
> Return list of all tickets, optional filter argument

**POST** /tickets
> Submit a ticket. Required to include `creator` and `title` in the body.

**GET** /ticket/<ticket_id>
> Return json data about a single ticket

**PUT** /ticket/<ticket_id>
> Update the ticket by changing `status` or `assignee` by including them as arguments in the body.

**PUT** /comment/<ticket_id>
>	Add a comment to `ticket_id`

### Testing

Run `pytest tests/*` from root project directory.

### Deploy

You'll need docker and docker-compose. Simply run the command `docker-compose up` at the root project directory.

To manually start the server (with python 3) run `python3 server.py`
