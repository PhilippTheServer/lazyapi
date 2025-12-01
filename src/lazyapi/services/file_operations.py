"""Generic file system operations service."""

from pathlib import Path
from ..shared.interfaces import IFileOperations
from ..shared.exceptions import FileSystemError


class FileOperations(IFileOperations):
    """
    Generic file system operations.

    No knowledge of any specific feature - pure file operations.
    """

    def create_directory(self, path: Path, parents: bool = True) -> None:
        """
        Create a directory.

        Args:
            path: Directory path to create
            parents: Create parent directories if needed

        Raises:
            FileSystemError: If creation fails
        """
        try:
            path.mkdir(parents=parents, exist_ok=False)
        except FileExistsError as e:
            raise FileSystemError(f"Directory already exists: {path}") from e
        except PermissionError as e:
            raise FileSystemError(f"Permission denied: {path}") from e
        except OSError as e:
            raise FileSystemError(f"Failed to create directory {path}: {e}") from e

    def write_file(self, path: Path, content: str) -> None:
        """
        Write content to a file.

        Args:
            path: File path to write
            content: Content to write

        Raises:
            FileSystemError: If write fails
        """
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        except PermissionError as e:
            raise FileSystemError(f"Permission denied: {path}") from e
        except OSError as e:
            raise FileSystemError(f"Failed to write file {path}: {e}") from e

    def file_exists(self, path: Path) -> bool:
        """
        Check if file exists.

        Args:
            path: File path to check

        Returns:
            True if file exists, False otherwise
        """
        return path.exists() and path.is_file()

    def directory_exists(self, path: Path) -> bool:
        """
        Check if directory exists.

        Args:
            path: Directory path to check

        Returns:
            True if directory exists, False otherwise
        """
        return path.exists() and path.is_dir()
