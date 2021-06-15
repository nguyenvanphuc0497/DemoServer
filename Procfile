web: gunicorn demo-server.wsgi
web2: daphne demo-server.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channel_layer -v2