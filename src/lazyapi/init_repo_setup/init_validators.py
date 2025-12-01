"""Feature-specific validators for repo-setup."""

import re
import shutil
from pathlib import Path
from typing import Any
from ..shared.interfaces import IValidator, IFileOperations


class ProjectNameValidator(IValidator):
    """Validate FastAPI project names."""

    _PATTERN = re.compile(r"^[a-z0-9][a-z0-9_-]*[a-z0-9]$|^[a-z0-9]$")
    _RESERVED = {".", "..", "test", "src", "lib"}
    _error = ""

    def validate(self, value: Any) -> bool:
        """Validate project name."""
        if not isinstance(value, str) or not value:
            self._error = "Project name must be a non-empty string"
            return False
        if len(value) > 100:
            self._error = "Project name too long (max 100 characters)"
            return False
        if not self._PATTERN.match(value):
            self._error = (
                "Project name must be lowercase alphanumeric with hyphens/underscores"
            )
            return False
        if value in self._RESERVED:
            self._error = f"'{value}' is a reserved name"
            return False
        return True

    def get_error_message(self) -> str:
        return self._error


class ProjectPathValidator(IValidator):
    """Validate project path doesn't exist."""

    def __init__(self, file_ops: IFileOperations):
        self._file_ops = file_ops
        self._error = ""

    def validate(self, value: Any) -> bool:
        """Validate project path."""
        if not isinstance(value, (str, Path)):
            self._error = "Path must be a string or Path object"
            return False
        if self._file_ops.directory_exists(Path(value)):
            self._error = f"Directory '{Path(value).name}' already exists"
            return False
        return True

    def get_error_message(self) -> str:
        return self._error


class PrerequisiteValidator(IValidator):
    """Validate required tools are installed."""

    def __init__(self, required_commands: list[str]):
        self._required = required_commands
        self._error = ""

    def validate(self, value: Any = None) -> bool:
        """Validate prerequisites are installed."""
        missing = [cmd for cmd in self._required if not shutil.which(cmd)]
        if missing:
            self._error = f"Required tools not found: {', '.join(missing)}"
            return False
        return True

    def get_error_message(self) -> str:
        return self._error
