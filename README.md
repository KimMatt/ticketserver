## Ticket Server
##### Simple Flask server using Mongo Engine

### API
**GET** /tickets?filter=[date|status]
> Return list of all tickets. It takes in an optional filter argument in url.

**POST** /tickets
> Submit a ticket. `creator` and `title` are required in the body.

**GET** /ticket/<ticket_id>
> Return json data about a single ticket

**PUT** /ticket/<ticket_id>
> Update a ticket's `status` or `assignee` by including them as arguments in the body.

**PUT** /comment/<ticket_id>
>	Add a comment to `ticket_id`. Comment must include `author` and `text`.

### Testing

Run `pytest tests/*` from root project directory.

### Deploy

You'll need docker and docker-compose. Simply run the command `docker-compose up` at the root project directory.

To manually start the server (with python 3) run `pip3 install -r requirements.txt` then `python3 server.py`
