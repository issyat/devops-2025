FROM python:3.11-slim

WORKDIR /app

# Install system dependencies and Poetry
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry psycopg2-binary

# Copy project files
COPY . .

# Configure Poetry and install dependencies
RUN poetry config virtualenvs.create false \
    && poetry lock \
    && poetry install --no-root

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]