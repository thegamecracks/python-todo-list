FROM python:3.11.2-slim

# Copy dependency metadata
COPY install_dependencies.py LICENSE pyproject.toml README.md ./

# Install dependencies
RUN python install_dependencies.py

# Copy source code
COPY src/ /src

# Install the source code
RUN pip install .

EXPOSE 8000

# Run the webserver
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "todo_list.app:app"]
