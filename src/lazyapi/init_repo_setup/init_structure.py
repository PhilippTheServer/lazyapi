"""FastAPI project structure builder."""

from .init_config import ProjectStructure, DirectorySpec, FileSpec, CommandSpec
from ..shared.content_generators import EmptyFileGenerator
from .init_generators import (
    ReadmeGenerator,
    DockerfileGenerator,
    DockerComposeGenerator,
    EnvExampleGenerator,
    MainAppGenerator,
    CoreConfigGenerator,
)


def get_fastapi_structure() -> ProjectStructure:
    """
    Define the FastAPI project structure.

    This is feature-specific configuration - knows about FastAPI projects.
    """
    empty_gen = EmptyFileGenerator()

    return ProjectStructure(
        directories=[
            DirectorySpec(path="src/app"),
            DirectorySpec(path="tests"),
        ],
        files=[
            FileSpec(path="src/app/__init__.py", generator=empty_gen),
            FileSpec(path="src/app/main.py", generator=MainAppGenerator),
            FileSpec(path="src/app/routes.py", generator=empty_gen),
            FileSpec(path="src/app/models.py", generator=empty_gen),
            FileSpec(path="src/app/config.py", generator=CoreConfigGenerator()),
            FileSpec(path="src/Dockerfile", generator=DockerfileGenerator()),
            FileSpec(path="docker-compose.dev.yml", generator=DockerComposeGenerator()),
            FileSpec(path=".env.example", generator=EnvExampleGenerator()),
            FileSpec(path="README.md", generator=ReadmeGenerator()),
        ],
        commands=[
            CommandSpec(command=["git", "init"]),
            CommandSpec(command=["uv", "init", "--no-readme"]),
            CommandSpec(command=["uv", "sync"]),
        ],
    )
