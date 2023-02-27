FROM python:3.11.2-slim

# Copy dependency metadata
COPY install_dependencies.py LICENSE pyproject.toml README.md ./

# Install dependencies
RUN python install_dependencies.py

# Copy source code
COPY src/ /src

# Install the source code
RUN pip install .

# Run the module
CMD ["python", "-m", "todo_list"]
