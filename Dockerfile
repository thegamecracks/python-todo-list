FROM python:3.11.2-slim AS main-deps
# NOTE: pytest needs this workdir to avoid recursing into system files
WORKDIR /app

COPY install_dependencies.py LICENSE pyproject.toml README.md ./
RUN python install_dependencies.py

FROM main-deps AS dev-deps
RUN python install_dependencies.py --no-required --extras dev

FROM dev-deps AS tests
COPY src/ ./src
COPY tests/ ./tests
RUN pip install .
RUN black --check .
RUN mypy
RUN pytest

FROM main-deps AS prod
COPY src/ ./src
RUN pip install .
EXPOSE 8000
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "todo_list.app:app"]
