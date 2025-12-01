"""Feature implementation: Initialize FastAPI project."""

from pathlib import Path
from ..shared.interfaces import IFileOperations, ICommandExecutor
from ..shared.exceptions import LazyAPIError
from .init_config import ProjectStructure


class ProjectInitializer:
    """
    Initialize a new FastAPI project.

    This is feature-specific code that uses generic services.
    """

    def __init__(
        self,
        file_ops: IFileOperations,
        shell_exec: ICommandExecutor,
        structure: ProjectStructure,
    ):
        """
        Initialize with dependencies.

        Args:
            file_ops: File operations service
            shell_exec: Shell executor service
            structure: Project structure configuration
        """
        self._file_ops = file_ops
        self._shell_exec = shell_exec
        self._structure = structure

    def initialize(self, project_path: Path, project_name: str) -> None:
        """
        Initialize a new FastAPI project.

        Args:
            project_path: Path where project should be created
            project_name: Name of the project

        Raises:
            LazyAPIError: If initialization fails
        """
        try:
            # Create root directory
            self._file_ops.create_directory(project_path)

            # Create subdirectories
            for dir_spec in self._structure.directories:
                dir_path = project_path / dir_spec.path
                dir_path.mkdir(parents=True, exist_ok=True)

            # Generate and write files
            context = {"project_name": project_name}
            for file_spec in self._structure.files:
                file_path = project_path / file_spec.path
                content = file_spec.generator.generate(context)
                self._file_ops.write_file(file_path, content)

            # Execute commands
            for cmd_spec in self._structure.commands:
                self._shell_exec.execute(cmd_spec.command, cwd=project_path)

        except Exception as e:
            raise LazyAPIError(f"Failed to initialize project: {e}") from e
