"""Feature-specific validators for repo-setup."""

import re
import shutil
from typing import Any
from ..shared.interfaces import IValidator, IFileOperations


class ProjectNameValidator(IValidator):
    """Validate FastAPI project names."""

    PATTERN = re.compile(r"^[a-z0-9][a-z0-9_-]*[a-z0-9]$|^[a-z0-9]$")

    def __init__(self):
        self._error_message = ""

    def validate(self, value: Any) -> bool:
        """Validate project name."""
        if not isinstance(value, str):
            self._error_message = "Project name must be a string"
            return False

        if not value:
            self._error_message = "Project name cannot be empty"
            return False

        if len(value) > 100:
            self._error_message = "Project name too long (max 100 characters)"
            return False

        if not self.PATTERN.match(value):
            self._error_message = (
                "Project name must start and end with alphanumeric characters "
                "and contain only lowercase letters, numbers, hyphens, and underscores"
            )
            return False

        reserved = {".", "..", "test", "src", "lib"}
        if value in reserved:
            self._error_message = f"'{value}' is a reserved name"
            return False

        self._error_message = ""
        return True

    def get_error_message(self) -> str:
        """Get error message."""
        return self._error_message


class ProjectPathValidator(IValidator):
    """Validate project path doesn't exist."""

    def __init__(self, file_ops: IFileOperations):
        self._file_ops = file_ops
        self._error_message = ""

    def validate(self, value: Any) -> bool:
        """Validate project path."""
        from pathlib import Path

        if not isinstance(value, (str, Path)):
            self._error_message = "Path must be a string or Path object"
            return False

        path = Path(value)

        if self._file_ops.directory_exists(path):
            self._error_message = f"Directory '{path.name}' already exists"
            return False

        self._error_message = ""
        return True

    def get_error_message(self) -> str:
        """Get error message."""
        return self._error_message


class PrerequisiteValidator(IValidator):
    """Validate required tools are installed."""

    def __init__(self, required_commands: list[str]):
        self._required_commands = required_commands
        self._error_message = ""

    def validate(self, value: Any = None) -> bool:
        """Validate prerequisites are installed."""
        missing = []

        for command in self._required_commands:
            if not shutil.which(command):
                missing.append(command)

        if missing:
            self._error_message = (
                f"Required tools not found: {', '.join(missing)}. "
                "Please install them before continuing."
            )
            return False

        self._error_message = ""
        return True

    def get_error_message(self) -> str:
        """Get error message."""
        return self._error_message
