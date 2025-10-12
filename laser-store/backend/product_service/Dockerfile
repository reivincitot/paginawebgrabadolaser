FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# dependencias del sistema para psycopg2
RUN apt-get update && apt-get install -y build-essential libpq-dev --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# copiar requirements y instalar
COPY backend/product_service/requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt

# copiar código de la app (en desarrollo se montará como volumen)
COPY backend/product_service/ /app/

# comando por defecto (en producción usar gunicorn; en dev puedes reemplazar por runserver)
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]