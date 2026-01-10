"""
Help domain objects for CLI command assistance.

Provides hierarchical help information:
- Commands (core navigation, other utility commands, examples)
- Scope (detailed scope usage and rules)
- Components (behaviors, actions, operations)
"""

from typing import List, Optional
from dataclasses import dataclass


@dataclass
class CoreCommands:
    """Core navigation and execution commands."""
    
    @property
    def navigation_pattern(self) -> str:
        """Returns the main navigation pattern."""
        return "echo '[behavior.][action.]operation' | python repl_main.py"
    
    @property
    def short_navigation_pattern(self) -> str:
        """Returns the short navigation pattern."""
        return "echo '[behavior][.action]' | python repl_main.py"
    
    @property
    def description_full(self) -> str:
        """Returns full navigation description."""
        return "navigate and perform operation"
    
    @property
    def description_short(self) -> str:
        """Returns short navigation description."""
        return "navigate to behavior/action"


@dataclass
class OtherCommands:
    """Utility commands for CLI."""
    
    @property
    def commands(self) -> List[tuple[str, str]]:
        """Returns list of (command, description) tuples."""
        return [
            ('status', 'Show full workflow hierarchy'),
            ('back', 'Go back to previous action'),
            ('current', 'Re-execute current operation'),
            ('next', 'Advance to next action'),
            ('path [dir]', 'Show/set working directory'),
            ('scope [filter]', 'Set scope filter (see Scope Command Details)'),
            ('scope all', 'Clear scope filter'),
            ('help', 'Show this help'),
            ('exit', 'Exit CLI'),
        ]


@dataclass
class CommandExamples:
    """Usage examples for CLI commands."""
    
    @property
    def examples(self) -> List[tuple[str, str]]:
        """Returns list of (command, description) tuples."""
        return [
            ('.', 'Execute current behavior.action.operation'),
            ('shape', 'Jump to behavior and execute first action.operation'),
            ('build', 'Jump to action and execute first operation'),
            ('submit scope="s1"', 'Jump to operation with params and execute'),
            ('shape.build', 'Jump to behavior.action and execute first operation'),
            ('shape.build.submit', 'Jump to behavior.action.operation and execute'),
        ]


@dataclass
class CommandsHelp:
    """Help for all CLI commands."""
    
    def __init__(self):
        self.core = CoreCommands()
        self.other = OtherCommands()
        self.examples = CommandExamples()


@dataclass
class ScopeHelp:
    """Detailed help for scope command."""
    
    @property
    def important_rules(self) -> List[str]:
        """Returns important scope rules."""
        return [
            "IMPORTANT: You can only have ONE scope type at a time (story OR files, never both).",
            "Setting a new scope REPLACES any previous scope.",
            "",
            "When passing file/folder paths to scope, you MUST provide the COMPLETE",
            "folder structure. Use ABSOLUTE paths or FULL relative paths from the work path.",
        ]
    
    @property
    def usage_patterns(self) -> List[tuple[str, str]]:
        """Returns list of (pattern, description) tuples."""
        return [
            ('scope', 'Show current scope'),
            ('scope all', 'Clear scope filter'),
            ('scope "Story Name"', 'Filter by story (replaces file scope)'),
            ('scope "file:C:/path/to/src/**/*.py"', 'Filter by files (replaces story scope)'),
        ]
    
    @property
    def correct_examples(self) -> List[tuple[str, str]]:
        """Returns list of (example, description) tuples."""
        return [
            ('scope "Enter Password, Authenticate User"', 'Story scope'),
            ('scope "file:C:/dev/augmented-teams/agile_bot/src/**/*.py"', 'File scope with glob'),
        ]
    
    @property
    def incorrect_examples(self) -> List[tuple[str, str]]:
        """Returns list of (example, reason) tuples for INCORRECT usage."""
        return [
            ('scope src', 'partial path - missing parent directories'),
            ('scope repl_cli', 'folder name only - incomplete structure'),
            ('scope ..\\src', 'relative navigation - use complete paths'),
        ]


@dataclass
class OperationsHelp:
    """Help for available operations."""
    
    @property
    def operations(self) -> List[tuple[str, str]]:
        """Returns list of (operation, parameters) tuples."""
        return [
            ('instructions', '[context, scope, or action-specific params]'),
            ('submit', '[scope, decisions, assumptions, or action-specific params]'),
            ('confirm', ''),
        ]


@dataclass
class ComponentsHelp:
    """Help for available components (behaviors, actions, operations)."""
    
    def __init__(self, behaviors_names: Optional[List[str]] = None, actions_list: Optional[List] = None):
        """Initialize ComponentsHelp.
        
        Args:
            behaviors_names: List of behavior names (delegates to Behaviors.names)
            actions_list: List of Action objects (delegates to Actions)
        """
        self._behaviors_names = behaviors_names or []
        self._actions_list = actions_list or []
        self.operations = OperationsHelp()
    
    @property
    def behaviors(self) -> str:
        """Returns pipe-separated behavior names."""
        return " | ".join(self._behaviors_names)
    
    @property
    def actions(self) -> List[tuple[str, str]]:
        """Returns list of (action_name, description) tuples."""
        result = []
        for action in self._actions_list:
            result.append((action.action_name, action.description))
        return result


class Help:
    """Main Help domain object.
    
    Provides hierarchical help information for the CLI:
    - Commands (core, other, examples)
    - Scope (rules, usage, examples)
    - Components (behaviors, actions, operations)
    """
    
    def __init__(self, bot=None):
        """Initialize Help.
        
        Args:
            bot: Bot instance for delegating to behaviors/actions
        """
        self.bot = bot
        self.commands = CommandsHelp()
        self.scope = ScopeHelp()
        
        # Components delegates to bot if available
        if bot:
            behaviors_names = bot.behaviors.names if hasattr(bot, 'behaviors') else []
            # Get all unique actions across all behaviors
            actions_list = []
            if hasattr(bot, 'behaviors'):
                for behavior in bot.behaviors:
                    for action in behavior.actions:
                        # Add if not already in list (by name)
                        if not any(a.action_name == action.action_name for a in actions_list):
                            actions_list.append(action)
            self.components = ComponentsHelp(behaviors_names, actions_list)
        else:
            self.components = ComponentsHelp()
    
    @property
    def available_commands(self) -> List[str]:
        """Legacy property - returns list of command names."""
        return ['status', 'back', 'current', 'next', 'path', 'scope', 'help', 'exit']
