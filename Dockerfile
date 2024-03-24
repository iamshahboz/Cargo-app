
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
COPY .env /app/
COPY uszips.csv /app/

COPY cargo/management/commands/create_cars.py /app/
COPY cargo/management/commands/import_locations.py /app/




CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]