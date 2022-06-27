python3 manage.py migrate
python3 manage.py collectstatic --noinput
gunicorn main.wsgi:application --bind 0.0.0.0:8080
