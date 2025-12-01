"""FastAPI-specific content generators for repo-setup feature."""

from ..shared.content_generators import TemplateContentGenerator, StaticContentGenerator


# ============================================================================
# Basic Structure Generators
# ============================================================================


class BasicReadmeGenerator(TemplateContentGenerator):
    """Generate README.md for basic FastAPI project."""

    def __init__(self):
        super().__init__("# {project_name}\n\nA FastAPI project.\n")


class BasicDockerfileGenerator(StaticContentGenerator):
    """Generate Dockerfile for basic FastAPI project."""

    def __init__(self):
        super().__init__("""FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install uv && uv sync

COPY src/ src/

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
""")


class BasicDockerComposeGenerator(TemplateContentGenerator):
    """Generate docker-compose.dev.yml for basic FastAPI project."""

    def __init__(self):
        super().__init__("""services:
  api:
    build: .
    container_name: {project_name}
    expose:
      - "8000"
    volumes:
      - ./src/app:/code
    env_file:
      - .env.example
    environment:
      - ENV=development
""")


class BasicEnvExampleGenerator(StaticContentGenerator):
    """Generate .env.example for basic FastAPI project."""

    def __init__(self):
        super().__init__("""# Environment variables
ENV=development
LOG_LEVEL=info
""")


# ============================================================================
# Scaled Structure Generators
# ============================================================================


class ScaledReadmeGenerator(TemplateContentGenerator):
    """Generate README.md for scaled FastAPI project."""

    def __init__(self):
        super().__init__("""# {project_name}

A feature-based FastAPI project with scalable architecture.

## Structure

```
src/
├── core/           # Business logic, domain models
├── features/       # Feature modules
├── api/            # API routes and endpoints
└── infrastructure/ # External services, database
```

## Setup

```bash
cd {project_name}
source .venv/bin/activate
uvicorn src.main:app --reload
```
""")


class ScaledCoreConfigGenerator(StaticContentGenerator):
    """Generate core configuration module for scaled project."""

    def __init__(self):
        super().__init__('''"""Core configuration."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    app_name: str = "FastAPI"
    debug: bool = False
    
    class Config:
        env_file = ".env"


settings = Settings()
''')


class ScaledMainAppGenerator(TemplateContentGenerator):
    """Generate main.py for scaled project."""

    def __init__(self):
        super().__init__('''"""Main FastAPI application."""

from fastapi import FastAPI
from src.core.config import settings

app = FastAPI(
    title="{project_name}",
    debug=settings.debug,
)


@app.get("/")
def root():
    """Root endpoint."""
    return {{"message": "Welcome to {project_name}"}}


@app.get("/health")
def health():
    """Health check endpoint."""
    return {{"status": "healthy"}}
''')


class ScaledDockerfileGenerator(StaticContentGenerator):
    """Generate Dockerfile for scaled project."""

    def __init__(self):
        super().__init__("""FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY pyproject.toml .
RUN pip install uv && uv sync

# Copy application
COPY src/ src/

# Expose port
EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
""")


class ScaledDockerComposeGenerator(TemplateContentGenerator):
    """Generate docker-compose for scaled project."""

    def __init__(self):
        super().__init__("""services:
  api:
    build: .
    container_name: {project_name}-api
    expose:
      - "8000"
    volumes:
      - ./src/app:/code
    env_file:
      - .env.example
    environment:
      - DEBUG=true
      - LOG_LEVEL=info
""")
