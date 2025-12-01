"""Generic validation framework."""

from typing import List, Any
from .interfaces import IValidator


class CompositeValidator(IValidator):
    """
    Composite validator that runs multiple validators.

    Follows Composite Pattern for combining validators.
    """

    def __init__(self, validators: List[IValidator]):
        """
        Initialize with list of validators.

        Args:
            validators: List of validator instances
        """
        self._validators = validators
        self._error_message = ""

    def validate(self, value: Any) -> bool:
        """
        Validate against all validators.

        Args:
            value: Value to validate

        Returns:
            True if all validators pass, False otherwise
        """
        for validator in self._validators:
            if not validator.validate(value):
                self._error_message = validator.get_error_message()
                return False

        self._error_message = ""
        return True

    def get_error_message(self) -> str:
        """Get error message from failed validator."""
        return self._error_message
