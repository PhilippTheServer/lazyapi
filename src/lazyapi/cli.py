"""CLI entrypoint for LazyAPI."""

import click
from pathlib import Path

from .services import FileOperations, ShellExecutor
from .init_repo_setup import (
    ProjectInitializer,
    ProjectNameValidator,
    ProjectPathValidator,
    PrerequisiteValidator,
    get_fastapi_structure,
)
from .shared import LazyAPIError


@click.group()
@click.version_option()
def cli():
    """LazyAPI - A CLI tool for scaffolding FastAPI projects."""
    pass


@cli.command()
@click.option(
    "--name",
    "-n",
    prompt="Enter the repository name",
    help="Name of the FastAPI project to create",
)
def init(name: str):
    """Initialize a new FastAPI project structure."""
    # Create generic services (dependency injection)
    file_ops = FileOperations()
    shell_exec = ShellExecutor()

    # Validate prerequisites
    prereq_validator = PrerequisiteValidator(["git", "uv"])
    if not prereq_validator.validate():
        click.echo(f"Error: {prereq_validator.get_error_message()}", err=True)
        raise click.Abort()

    # Validate project name
    name_validator = ProjectNameValidator()
    if not name_validator.validate(name):
        click.echo(f"Error: {name_validator.get_error_message()}", err=True)
        raise click.Abort()

    # Validate project path
    project_path = Path.cwd() / name
    path_validator = ProjectPathValidator(file_ops)
    if not path_validator.validate(project_path):
        click.echo(f"Error: {path_validator.get_error_message()}", err=True)
        raise click.Abort()

    click.echo(f"Creating FastAPI project: {name}")

    try:
        # Get feature-specific structure
        structure = get_fastapi_structure()

        # Initialize project using feature implementation
        initializer = ProjectInitializer(file_ops, shell_exec, structure)
        initializer.initialize(project_path, name)

        click.echo(f"✓ Successfully created project '{name}'")
        click.echo("\nNext steps:")
        click.echo(f"  cd {name}")
        click.echo("  source .venv/bin/activate")
        click.echo("  uvicorn src.app.main:app --reload")

    except LazyAPIError as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"Unexpected error: {e}", err=True)
        raise click.Abort()


if __name__ == "__main__":
    cli()
