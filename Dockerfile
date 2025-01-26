FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y build-essential libpq-dev \
    && useradd -m genas_user \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R genas_user:genas_user /app

EXPOSE 8080

RUN python manage.py collectstatic --noinput

USER genas_user
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "core.wsgi:application"]