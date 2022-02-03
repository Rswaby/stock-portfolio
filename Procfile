web: gunicorn backend.wsgi --log-file -
release: python manage.py makemigrations --noinput
release: python manage.py collectstactic --noinput
release: python manage.py migrate --noinput