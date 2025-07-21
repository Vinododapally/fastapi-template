
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.openapi.docs import get_swagger_ui_html

from app.dbconfig.database import init_db

app= FastAPI(title="FastAPI Application",description="A simple FastAPI application",openapi_url="/api/v1/openapi.json")

app.add_middleware(GZipMiddleware, minimum_size=1000)

app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

@app.get("/api/v1/docs", include_in_schema=False)
def custom_swagger_ui_html():
    """
    Custom Swagger UI HTML endpoint.
    """
    return get_swagger_ui_html(openapi_url="/api/v1/openapi.json", title=" FastAPI Swagger UI")

@app.get("/health",tags=["Health Check"],summary="Health Check",description="Endpoint to check the health of the service")
def health_check():
    """
    Health check endpoint.

    """
    return {"status": "UP", "message": "Service is running"}


def init_and_run():
    """
    Initialize and run the FastAPI application.
    """
    init_db()  # Initialize the database
    uvicorn.run(app, host="127.0.0.1", port=8000)

if __name__== "__main__":
    """
    Entry point for the application.
    """
    init_and_run()