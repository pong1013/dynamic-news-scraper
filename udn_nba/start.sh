#!/bin/bash

# Start Redis server
redis-server --port 6379 &

sleep 3

# Apply migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Start Celery worker and beat
celery -A udn_nba worker --loglevel=info &
celery -A udn_nba beat --loglevel=info &

# Start Django development server
exec python3 manage.py runserver 0.0.0.0:8000
