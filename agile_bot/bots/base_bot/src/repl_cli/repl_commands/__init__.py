from .repl_command import REPLCommand
from .navigation import NextCommand, BackCommand, GoCommand
from .workflow import InstructionsCommand, SubmitCommand, ConfirmCommand
from .meta import HelpCommand, StatusCommand, ExitCommand, CurrentCommand, LoopBackCommand
from .state import BehaviorCommand, ActionCommand, WorkspaceCommand, ScopeCommand
from .dot_notation import DotNotationCommand


def register_commands(session) -> dict:
    commands = [
        NextCommand(session),
        BackCommand(session),
        GoCommand(session),
        InstructionsCommand(session),
        SubmitCommand(session),
        ConfirmCommand(session),
        HelpCommand(session),
        StatusCommand(session),
        ExitCommand(session),
        CurrentCommand(session),
        LoopBackCommand(session),
        BehaviorCommand(session),
        ActionCommand(session),
        WorkspaceCommand(session),
        ScopeCommand(session),
    ]
    return {cmd.name: cmd for cmd in commands}


ACTION_SHORTCUTS = {"clarify", "strategy", "build", "validate", "render"}

__all__ = [
    'REPLCommand',
    'register_commands',
    'ACTION_SHORTCUTS',
    'DotNotationCommand',
]

