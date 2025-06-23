#!/bin/sh

# Wait for PostgreSQL to be available
echo "Waiting for postgres..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "PostgreSQL started"

# Run migrations and start server
python manage.py migrate
exec "$@"
