"""Configuration for FastAPI project structure."""

from dataclasses import dataclass
from typing import List
from ..shared.interfaces import IContentGenerator


@dataclass
class FileSpec:
    """Specification for a file to generate."""

    path: str
    generator: IContentGenerator


@dataclass
class DirectorySpec:
    """Specification for a directory to create."""

    path: str


@dataclass
class CommandSpec:
    """Specification for a command to execute."""

    command: List[str]
    description: str


@dataclass
class ProjectStructure:
    """Complete project structure specification."""

    directories: List[DirectorySpec]
    files: List[FileSpec]
    commands: List[CommandSpec]
