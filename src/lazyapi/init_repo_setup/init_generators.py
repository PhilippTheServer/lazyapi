"""FastAPI-specific content generators for repo-setup feature."""

from typing import Dict, Any
from ..shared.interfaces import IContentGenerator


class ReadmeGenerator(IContentGenerator):
    """Generate README.md for FastAPI project."""

    def generate(self, context: Dict[str, Any]) -> str:
        """Generate README content."""
        project_name = context.get("project_name", "my-api")
        return f"# {project_name}\n\nA FastAPI project.\n"


class DockerfileGenerator(IContentGenerator):
    """Generate Dockerfile for FastAPI project."""

    def generate(self, context: Dict[str, Any]) -> str:
        """Generate Dockerfile content."""
        return """FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
RUN pip install uv && uv sync

COPY src/ src/

CMD ["uvicorn", "src.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
"""


class DockerComposeGenerator(IContentGenerator):
    """Generate docker-compose.dev.yml for FastAPI project."""

    def generate(self, context: Dict[str, Any]) -> str:
        """Generate docker-compose content."""
        project_name = context.get("project_name", "my-api")
        return f"""version: '3.8'

services:
  api:
    build: .
    container_name: {project_name}
    ports:
      - "8000:8000"
    volumes:
      - ./src:/app/src
    environment:
      - ENV=development
"""


class EnvExampleGenerator(IContentGenerator):
    """Generate .env.example for FastAPI project."""

    def generate(self, context: Dict[str, Any]) -> str:
        """Generate .env.example content."""
        return """# Environment variables
ENV=development
LOG_LEVEL=info
"""
