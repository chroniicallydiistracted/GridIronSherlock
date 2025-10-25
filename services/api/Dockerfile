FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY services /app/services
COPY CONTRACTS /app/CONTRACTS

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -e services/api

ENV CONTRACTS_DIR=/app/CONTRACTS

WORKDIR /app/services/api

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
