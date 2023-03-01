# python-todo-list
 A web-based todo list built on FastAPI and SQLAlchemy.

## Running tests

```sh
docker build --target tests .
```

## Todo

- [X] Set up Dockerfile / docker-compose.yml (test by printing "hello world!")
- [X] Set up FastAPI app (test by accessing from Docker)
- [ ] Set up todo SQLAlchemy models
- [ ] Add TOML configuration mechanism for specifying config and secrets
  - Consider Pydantic models for de/serialization
- [ ] Set up PostgreSQL database with docker (test by committing / fetching data)
- [ ] Create endpoints to interface with todo
- [ ] Add website as front-end for API
- [ ] Add user authentication via API tokens
- [ ] Add login/register page
