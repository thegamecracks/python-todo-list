# python-todo-list
 A web-based todo list built on FastAPI and SQLAlchemy.

## Usage

This requires Docker Compose to be installed, along with Docker's [BuildKit]
being enabled.

1. Create a `.env` file using the [example.env] as a template.
   Adjust passwords as necessary.

2. Start the services with `docker compose up --build --exit-code-from app`.

3. Go to http://localhost:5000 to access the website.

4. To cleanup the containers/volumes, use `docker compose down --volumes`.

[BuildKit]: https://docs.docker.com/build/buildkit/
[example.env]: example.env

## Development

To run tests, use `docker build --target tests .`.

If you need to administrate the database during runtime, a pgAdmin instance
is provided at the address http://localhost:5433. You can log into pgAdmin
using the appropriate email/password credentials defined in [`.env`](example.env)
and then add the database. Note that the hostname specified in the Connections tab
should be called "db".

## Todo

- [X] Set up Dockerfile / docker-compose.yml (test by printing "hello world!")
- [X] Set up FastAPI app (test by accessing from Docker)
- [X] Set up todo SQLAlchemy models
- [X] Set up PostgreSQL database with docker (test by committing / fetching data)
- [ ] Create endpoints to interface with todo
- [ ] Add website as front-end for API
- [ ] Add user authentication via API tokens
- [ ] Add login/register page
