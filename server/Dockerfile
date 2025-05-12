FROM python:3.11-slim

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy project files
COPY . .

# Configure Poetry and install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-root

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]