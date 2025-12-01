"""Generic content generators - feature-agnostic utilities."""

from typing import Dict, Any
from pathlib import Path
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


class FileTemplateGenerator(IContentGenerator):
    """
    Generate content from template files.

    Reads template files and applies string formatting.
    """

    def __init__(self, template_path: Path):
        """
        Initialize with template file path.

        Args:
            template_path: Path to template file relative to templates directory
        """
        self._template_path = template_path

    def generate(self, context: Dict[str, Any]) -> str:
        """
        Generate content by reading template file and formatting with context.

        Args:
            context: Dictionary with values for placeholders

        Returns:
            Formatted string from template file
        """
        templates_dir = Path(__file__).parent.parent / "templates"
        template_file = templates_dir / self._template_path

        if not template_file.exists():
            raise FileNotFoundError(f"Template file not found: {template_file}")

        template_content = template_file.read_text()
        return template_content.format(**context)
