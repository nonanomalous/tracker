#!/bin/sh
(cd /app/tracker; gunicorn student_tracker.wsgi --user www-data --bind 0.0.0.0:8000 --workers 3) &
nginx -g "daemon off;"
