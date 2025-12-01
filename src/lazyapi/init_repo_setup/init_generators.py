"""FastAPI-specific content generators for repo-setup feature."""

from pathlib import Path
from ..shared.content_generators import FileTemplateGenerator


# ============================================================================
# Common Generators (used by both basic and scaled)
# ============================================================================


class DockerfileGenerator(FileTemplateGenerator):
    """Generate Dockerfile for FastAPI project."""

    def __init__(self):
        super().__init__(Path("Dockerfile"))


class DockerComposeGenerator(FileTemplateGenerator):
    """Generate docker-compose.dev.yml for FastAPI project."""

    def __init__(self):
        super().__init__(Path("docker-compose.dev.yml"))


class EnvExampleGenerator(FileTemplateGenerator):
    """Generate .env.example for FastAPI project."""

    def __init__(self):
        super().__init__(Path(".env.example"))


# ============================================================================
# Basic Structure Generators
# ============================================================================


class BasicReadmeGenerator(FileTemplateGenerator):
    """Generate README.md for basic FastAPI project."""

    def __init__(self):
        super().__init__(Path("README.basic.md"))


# ============================================================================
# Scaled Structure Generators
# ============================================================================


class ScaledReadmeGenerator(FileTemplateGenerator):
    """Generate README.md for scaled FastAPI project."""

    def __init__(self):
        super().__init__(Path("README.scaled.md"))


class ScaledCoreConfigGenerator(FileTemplateGenerator):
    """Generate core configuration module for scaled project."""

    def __init__(self):
        super().__init__(Path("core_config.py"))


class ScaledMainAppGenerator(FileTemplateGenerator):
    """Generate main.py for scaled project."""

    def __init__(self):
        super().__init__(Path("main.scaled.py"))
