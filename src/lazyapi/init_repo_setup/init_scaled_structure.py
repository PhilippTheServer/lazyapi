"""Scaled FastAPI project structure configuration."""

from .init_config import ProjectStructure, DirectorySpec, FileSpec, CommandSpec
from ..shared.content_generators import EmptyFileGenerator
from .init_generators import (
    ScaledReadmeGenerator,
    ScaledCoreConfigGenerator,
    ScaledMainAppGenerator,
    ScaledDockerfileGenerator,
    ScaledDockerComposeGenerator,
)


def get_scaled_fastapi_structure() -> ProjectStructure:
    """
    Define the scaled/feature-based FastAPI project structure.

    This creates a more complex, production-ready structure.
    """
    empty_gen = EmptyFileGenerator()

    return ProjectStructure(
        directories=[
            # Main app directory
            DirectorySpec(path="src/app"),
            # Shared utilities
            DirectorySpec(path="src/app/shared"),
            # Services directory for features
            DirectorySpec(path="src/app/services"),
            # Tests
            DirectorySpec(path="tests"),
        ],
        files=[
            # Root level
            FileSpec(path="README.md", generator=ScaledReadmeGenerator()),
            FileSpec(
                path="docker-compose.dev.yml", generator=ScaledDockerComposeGenerator()
            ),
            FileSpec(path=".env.example", generator=empty_gen),
            FileSpec(path=".gitignore", generator=empty_gen),
            # Source structure
            FileSpec(path="src/Dockerfile", generator=ScaledDockerfileGenerator()),
            # App
            FileSpec(path="src/app/__init__.py", generator=empty_gen),
            FileSpec(path="src/app/main.py", generator=ScaledMainAppGenerator()),
            FileSpec(path="src/app/config.py", generator=ScaledCoreConfigGenerator()),
            # Shared utilities
            FileSpec(path="src/app/shared/__init__.py", generator=empty_gen),
            FileSpec(path="src/app/shared/logger.py", generator=empty_gen),
            # Services (features will be added here)
            FileSpec(path="src/app/services/__init__.py", generator=empty_gen),
            # Tests
            FileSpec(path="tests/__init__.py", generator=empty_gen),
        ],
        commands=[
            CommandSpec(command=["git", "init"]),
            CommandSpec(command=["uv", "init", "--no-readme"]),
            CommandSpec(command=["rm", "-f", "main.py"]),
            CommandSpec(command=["uv", "add", "fastapi"]),
            CommandSpec(command=["uv", "add", "uvicorn[standard]"]),
            CommandSpec(command=["uv", "add", "pydantic-settings"]),
            CommandSpec(command=["uv", "add", "sqlalchemy"]),
            CommandSpec(command=["uv", "add", "alembic"]),
            CommandSpec(command=["uv", "add", "python-dotenv"]),
            CommandSpec(command=["uv", "sync"]),
        ],
    )
