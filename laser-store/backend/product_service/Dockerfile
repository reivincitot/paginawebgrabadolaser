FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpq-dev --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Cambiado: copiar requirements.txt directamente al directorio de trabajo
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Cambiado: copiar todo al directorio de trabajo
COPY . .

# Cambiado: usar runserver en lugar de gunicorn
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
