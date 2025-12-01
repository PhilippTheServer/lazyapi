"""Generic interfaces following Interface Segregation Principle."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Any, Dict


class IValidator(ABC):
    """Generic validator interface."""

    @abstractmethod
    def validate(self, value: Any) -> bool:
        """
        Validate a value.

        Args:
            value: Value to validate

        Returns:
            True if valid, False otherwise
        """
        pass

    @abstractmethod
    def get_error_message(self) -> str:
        """Get error message for failed validation."""
        pass


class IFileOperations(ABC):
    """Generic file system operations interface."""

    @abstractmethod
    def create_directory(self, path: Path, parents: bool = True) -> None:
        """Create a directory."""
        pass

    @abstractmethod
    def write_file(self, path: Path, content: str) -> None:
        """Write content to a file."""
        pass

    @abstractmethod
    def file_exists(self, path: Path) -> bool:
        """Check if file exists."""
        pass

    @abstractmethod
    def directory_exists(self, path: Path) -> bool:
        """Check if directory exists."""
        pass


class ICommandExecutor(ABC):
    """Generic command execution interface."""

    @abstractmethod
    def execute(self, command: List[str], cwd: Path = None) -> None:
        """
        Execute a shell command.

        Args:
            command: Command and arguments to execute
            cwd: Working directory for execution
        """
        pass


class IContentGenerator(ABC):
    """Generic content generation interface."""

    @abstractmethod
    def generate(self, context: Dict[str, Any]) -> str:
        """
        Generate content based on context.

        Args:
            context: Dictionary with generation parameters

        Returns:
            Generated content as string
        """
        pass
