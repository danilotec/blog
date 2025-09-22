FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate  && python manage.py collectstatic --noinput && gunicorn --bind 0.0.0.0:5000 --workers 3 --timeout 120 mysite.wsgi:application"]
