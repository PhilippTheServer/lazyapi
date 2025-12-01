"""Feature-agnostic exceptions for LazyAPI."""


class LazyAPIError(Exception):
    """Base exception for all LazyAPI errors."""

    pass


class ValidationError(LazyAPIError):
    """Raised when validation fails."""

    pass


class FileSystemError(LazyAPIError):
    """Raised when file system operations fail."""

    pass


class CommandExecutionError(LazyAPIError):
    """Raised when command execution fails."""

    pass
