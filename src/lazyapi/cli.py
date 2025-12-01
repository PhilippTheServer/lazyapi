"""CLI entrypoint for LazyAPI."""

import typer
from pathlib import Path
from typing import Optional
from typing_extensions import Annotated

from .services import FileOperations, ShellExecutor
from .init_repo_setup import (
    ProjectInitializer,
    ProjectNameValidator,
    ProjectPathValidator,
    PrerequisiteValidator,
)
from .init_repo_setup.init_structure import get_fastapi_structure
from .init_repo_setup.init_scaled_structure import get_scaled_fastapi_structure
from .shared import LazyAPIError

app = typer.Typer(
    name="lazyapi",
    help="LazyAPI - A CLI tool for scaffolding FastAPI projects.",
    add_completion=False,
)


@app.command()
def init(
    name: Annotated[
        Optional[str],
        typer.Option(
            "--name",
            "-n",
            help="Name of the FastAPI project to create",
            prompt="Enter the project name",
        ),
    ] = None,
    scale: Annotated[
        bool,
        typer.Option(
            "--scale",
            help="Create a scaled, feature-based project structure",
        ),
    ] = False,
    basic: Annotated[
        bool,
        typer.Option(
            "--basic",
            help="Create a basic project structure (default)",
        ),
    ] = False,
):
    """
    Initialize a new FastAPI project structure.
    
    Use --scale for a feature-based layout with shared utilities and services directory.
    Use --basic (or no flag) for a simple, compact project structure.
    """
    # Create generic services (dependency injection)
    file_ops = FileOperations()
    shell_exec = ShellExecutor()

    # Validate prerequisites
    prereq_validator = PrerequisiteValidator(["git", "uv"])
    if not prereq_validator.validate():
        typer.echo(f"Error: {prereq_validator.get_error_message()}", err=True)
        raise typer.Exit(code=1)

    # Validate project name
    name_validator = ProjectNameValidator()
    if not name_validator.validate(name):
        typer.echo(f"Error: {name_validator.get_error_message()}", err=True)
        raise typer.Exit(code=1)

    # Validate project path
    project_path = Path.cwd() / name
    path_validator = ProjectPathValidator(file_ops)
    if not path_validator.validate(project_path):
        typer.echo(f"Error: {path_validator.get_error_message()}", err=True)
        raise typer.Exit(code=1)

    # Determine structure type (--scale takes precedence)
    use_scaled = scale or not basic
    if scale and basic:
        typer.echo("Warning: Both --scale and --basic specified. Using --scale.", err=True)
        use_scaled = True
    
    structure_type = "scaled" if use_scaled else "basic"
    typer.echo(f"Creating {structure_type} FastAPI project: {name}")

    try:
        # Get feature-specific structure based on flag
        structure = get_scaled_fastapi_structure() if use_scaled else get_fastapi_structure()

        # Initialize project using feature implementation
        initializer = ProjectInitializer(file_ops, shell_exec, structure)
        initializer.initialize(project_path, name)

        typer.echo(f"✓ Successfully created {structure_type} project '{name}'")
        typer.echo("\nNext steps:")
        typer.echo(f"  cd {name}")
        typer.echo("  source .venv/bin/activate")
        typer.echo("  uvicorn src.app.main:app --reload")

    except LazyAPIError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
