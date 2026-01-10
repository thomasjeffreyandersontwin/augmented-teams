"""
CLI Typed Results

Domain model types for CLI Session responses.
These define the contract/API between CLI Session and its consumers.
"""

from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class CLICommandResponse:
    """Response from a CLI command execution."""
    output: str
    response: str = ""
    status: Optional[str] = None
    action: Optional[str] = None
    scope_stored: bool = False
    scope: Optional[Dict] = None
    context_passed_to_action: Optional[Dict] = None
    cli_terminated: bool = False


@dataclass
class TTYDetectionResult:
    """Result of TTY detection."""
    tty_detected: bool
    interactive_prompts_enabled: bool
