# Dockerfile multi-stage para optimizar la imagen
FROM python:3.11-slim as builder

# Variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Copiar solo requirements primero (cache de Docker)
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Etapa final
FROM python:3.11-slim

WORKDIR /app

# Copiar dependencias instaladas
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copiar código de la aplicación
COPY App/ ./App/
COPY .env.example .env

# Exponer puerto
EXPOSE 5000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:5000/health')"

# Comando por defecto
CMD ["python", "App/main.py"]
