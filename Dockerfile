FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ARG APP_ENV

ENV APP_ENV=$APP_ENV

EXPOSE 8000

# Entrypoint for FastAPI with uvicorn, app instance in main.py as "app"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]