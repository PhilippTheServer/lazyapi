"""Generic content generators - feature-agnostic utilities."""

from typing import Dict, Any
from .interfaces import IContentGenerator


class EmptyFileGenerator(IContentGenerator):
    """
    Generate empty files.

    Generic utility that can be reused by any feature needing empty files.
    """

    def generate(self, context: Dict[str, Any]) -> str:
        """Generate empty file content."""
        return ""


class StaticContentGenerator(IContentGenerator):
    """
    Generate static content.

    Generic utility for returning predefined static content.
    """

    def __init__(self, content: str):
        """
        Initialize with static content.

        Args:
            content: The static content to return
        """
        self._content = content

    def generate(self, context: Dict[str, Any]) -> str:
        """Return the static content."""
        return self._content


class TemplateContentGenerator(IContentGenerator):
    """
    Generate content using template string formatting.

    Generic utility for simple string interpolation.
    """

    def __init__(self, template: str):
        """
        Initialize with template string.

        Args:
            template: Template string with {key} placeholders
        """
        self._template = template

    def generate(self, context: Dict[str, Any]) -> str:
        """
        Generate content by formatting template with context.

        Args:
            context: Dictionary with values for placeholders

        Returns:
            Formatted string
        """
        return self._template.format(**context)
