"""Generic shell command execution service."""

import subprocess
from pathlib import Path
from typing import List, Optional
from ..shared.interfaces import ICommandExecutor
from ..shared.exceptions import CommandExecutionError


class ShellExecutor(ICommandExecutor):
    """
    Generic shell command executor.

    No knowledge of any specific commands - pure execution.
    """

    def execute(self, command: List[str], cwd: Optional[Path] = None) -> None:
        """
        Execute a shell command.

        Args:
            command: Command and arguments to execute
            cwd: Working directory for execution

        Raises:
            CommandExecutionError: If execution fails
        """
        try:
            subprocess.run(
                command,
                cwd=cwd,
                check=True,
                capture_output=True,
                text=True,
            )
        except subprocess.CalledProcessError as e:
            raise CommandExecutionError(
                f"Command '{' '.join(command)}' failed: {e.stderr}"
            ) from e
        except FileNotFoundError as e:
            raise CommandExecutionError(
                f"Command '{command[0]}' not found. Is it installed?"
            ) from e
