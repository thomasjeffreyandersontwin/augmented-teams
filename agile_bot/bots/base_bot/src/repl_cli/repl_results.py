"""
REPL Typed Results

Domain model types for REPL Session responses.
These define the contract/API between REPL Session and its consumers.

Based on "Typed Results" domain concept from stdio-cli-redesign.md.
"""

from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class REPLStateDisplay:
    """
    Result of displaying current REPL state.
    
    Returned by: REPLSession.display_current_state()
    
    Represents the REPL's current position in the workflow,
    including behavior, action, and breadcrumbs.
    """
    output: str
    state_loaded: bool = False
    current_behavior: Optional[str] = None
    current_action: Optional[str] = None
    breadcrumbs: Optional[str] = None


@dataclass
class REPLCommandResponse:
    """
    Result of executing a REPL command.
    
    Returned by: REPLSession.read_and_execute_command()
    
    Contains the command's output, status, and any state changes.
    """
    output: str
    response: str = ""
    status: Optional[str] = None
    action: Optional[str] = None
    scope_stored: bool = False
    scope: Optional[Dict] = None
    context_passed_to_action: Optional[Dict] = None
    repl_terminated: bool = False


@dataclass
class TTYDetectionResult:
    """
    Result of TTY detection.
    
    Returned by: REPLSession.detect_tty()
    
    Determines whether interactive prompts should be enabled
    based on whether stdin is a TTY.
    """
    tty_detected: bool
    interactive_prompts_enabled: bool


