FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Copy package metadata first for better caching
ARG APP_ROOT=services/api
COPY ${APP_ROOT}/pyproject.toml ${APP_ROOT}/README.md ./services/api/

RUN pip install --upgrade pip

# Copy application source and supporting files
COPY ${APP_ROOT}/app ./services/api/app
COPY ${APP_ROOT}/migrations ./services/api/migrations
COPY ${APP_ROOT}/__init__.py ${APP_ROOT}/mypy.ini ./services/api/

# Create namespace package root and install the API package
RUN mkdir -p /app/services \
 && printf '"""Service namespace for GridIron Sherlock."""\n' > /app/services/__init__.py \
 && pip install ./services/api

ENV CONTRACTS_DIR=/app/services/api/app/contracts \
    PYTHONPATH=/app

WORKDIR /app/services/api

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
