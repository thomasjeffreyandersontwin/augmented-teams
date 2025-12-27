# Format Output for AI - Implementation Plan

## Story Overview

**Story Name:** Format Output for AI  
**Sub-Epic:** Generate REPL CLI  
**Epic:** Build Agile Bot  
**Priority:** High  

## Problem Statement

The new REPL CLI outputs plain text formatting (`[*]`, `[x]`, `[ ]` markers) to both human terminals and AI agents. When AI agents invoke the CLI via piped mode (`echo 'cmd' | python repl_main.py`), they should receive rich Markdown formatting for better parsing and display in chat interfaces.

The system already detects TTY vs piped mode via `sys.stdin.isatty()`, but doesn't use this to change output formatting.

## Acceptance Criteria

Following **behavioral_ac_at_story_level**, **stories_have_4_to_9_acceptance_criteria**, and **use_verb_noun_format_for_story_elements** rules:

1. WHEN REPL session starts THEN session detects TTY mode AND session creates appropriate formatter via factory

2. WHEN TTY mode is detected THEN factory creates terminal formatter AND formatter uses plain text markers AND formatter uses dash separators

3. WHEN piped mode is detected THEN factory creates markdown formatter AND formatter uses emoji markers AND formatter uses markdown separators AND formatter uses markdown headings

4. WHEN formatter is created THEN session injects formatter into REPLStatus

5. WHEN REPLStatus builds hierarchical display THEN status uses formatter for section separators AND status uses formatter for status markers AND status uses formatter for list items

6. WHEN cursor command generator runs THEN generator creates base command file with piped syntax AND generator creates per-behavior command files with piped syntax AND generator updates bot registry with REPL path

7. WHEN terminal mode displays output THEN output matches current plain text format exactly

8. WHEN piped mode displays output THEN output contains markdown formatting AND output uses rich status markers

## Domain Concepts

Following **verb_noun_format**, **active_business_and_behavioral_language**, and **outcome_oriented_language** rules:

- **OutputFormatter** - Formats output text for display
- **TerminalFormatter** - Formats output for terminal display
- **MarkdownFormatter** - Formats output for markdown display
- **FormatterFactory** - Creates formatter based on mode
- **REPLSession** - Manages REPL session and formatter creation
- **REPLStatus** - Displays status using formatter

## Scenarios

Following **given_describes_state_not_actions**, **write_plain_english_scenarios**, and **scenarios_cover_all_cases** rules:

### Background
- Given REPL CLI is initialized
- And bot has behaviors and actions configured

### Scenario 1: Terminal mode uses plain text formatting
- Given user runs REPL in terminal
- When REPL displays status
- Then status uses plain text markers
- And status uses dash separators
- And status uses space indentation

### Scenario 2: Piped mode uses markdown formatting
- Given AI agent pipes command to REPL
- When REPL displays status
- Then status uses emoji markers
- And status uses markdown headings
- And status uses markdown separators
- And status uses markdown lists

### Scenario 3: Formatter created at session initialization
- Given REPL session is starting
- When session detects TTY mode
- Then session creates terminal formatter
- And session injects formatter into status

### Scenario 4: Formatter created for piped mode
- Given REPL session is starting
- When session detects piped mode
- Then session creates markdown formatter
- And session injects formatter into status

### Scenario 5: Status uses formatter for all output
- Given REPLStatus has formatter injected
- When status builds hierarchical display
- Then status uses formatter for separators
- And status uses formatter for status markers
- And status uses formatter for list items

### Scenario 6: Cursor commands use piped syntax
- Given cursor command generator runs
- When generator creates behavior command file
- Then command uses piped input format
- And command invokes REPL with dot notation

## Test Structure

Following **use_class_based_organization**, **pytest_bdd_orchestrator_pattern**, and **use_given_when_then_helpers** rules:

### File: `test/repl_cli/formatters/test_terminal_formatter.py`

```python
class TestTerminalFormatter:
    """Story: Format Output for AI - Terminal Formatter"""
    
    def test_terminal_formatter_returns_plain_text_heading(self):
        # Given
        formatter = given_terminal_formatter()
        # When
        result = when_format_heading(formatter, "Test Heading", level=2)
        # Then
        then_result_is_plain_text(result, "Test Heading")
    
    def test_terminal_formatter_uses_bracket_status_markers(self):
        # Given
        formatter = given_terminal_formatter()
        # When
        current_marker = when_format_status_marker(formatter, is_current=True, is_completed=False)
        completed_marker = when_format_status_marker(formatter, is_current=False, is_completed=True)
        pending_marker = when_format_status_marker(formatter, is_current=False, is_completed=False)
        # Then
        then_marker_equals(current_marker, "[*]")
        then_marker_equals(completed_marker, "[x]")
        then_marker_equals(pending_marker, "[ ]")
    
    def test_terminal_formatter_uses_dash_separator(self):
        # Given
        formatter = given_terminal_formatter()
        # When
        separator = when_format_section_separator(formatter)
        # Then
        then_separator_is_dashes(separator, length=60)
```

### File: `test/repl_cli/formatters/test_markdown_formatter.py`

```python
class TestMarkdownFormatter:
    """Story: Format Output for AI - Markdown Formatter"""
    
    def test_markdown_formatter_returns_markdown_heading(self):
        # Given
        formatter = given_markdown_formatter()
        # When
        result = when_format_heading(formatter, "Test Heading", level=2)
        # Then
        then_result_is_markdown_heading(result, "## Test Heading")
    
    def test_markdown_formatter_uses_emoji_status_markers(self):
        # Given
        formatter = given_markdown_formatter()
        # When
        current_marker = when_format_status_marker(formatter, is_current=True, is_completed=False)
        completed_marker = when_format_status_marker(formatter, is_current=False, is_completed=True)
        pending_marker = when_format_status_marker(formatter, is_current=False, is_completed=False)
        # Then
        then_marker_is_emoji(current_marker, "▶️")
        then_marker_is_emoji(completed_marker, "✅")
        then_marker_is_emoji(pending_marker, "⬜")
    
    def test_markdown_formatter_uses_markdown_separator(self):
        # Given
        formatter = given_markdown_formatter()
        # When
        separator = when_format_section_separator(formatter)
        # Then
        then_separator_is_markdown(separator, "---")
```

### File: `test/repl_cli/formatters/test_formatter_factory.py`

```python
class TestFormatterFactory:
    """Story: Format Output for AI - Formatter Factory"""
    
    def test_factory_creates_terminal_formatter_when_tty_detected(self):
        # Given
        tty_detected = True
        # When
        formatter = when_factory_creates_formatter(tty_detected)
        # Then
        then_formatter_is_terminal_formatter(formatter)
    
    def test_factory_creates_markdown_formatter_when_piped_mode(self):
        # Given
        tty_detected = False
        # When
        formatter = when_factory_creates_formatter(tty_detected)
        # Then
        then_formatter_is_markdown_formatter(formatter)
```

### File: `test/repl_cli/test_repl_session_formatter_integration.py`

```python
class TestREPLSessionFormatterIntegration:
    """Story: Format Output for AI - REPL Session Integration"""
    
    def test_repl_session_creates_formatter_at_initialization(self):
        # Given
        bot = given_bot_with_behaviors()
        workspace = given_workspace_directory()
        # When
        session = when_repl_session_initialized(bot, workspace)
        # Then
        then_session_has_formatter(session)
    
    def test_repl_session_injects_formatter_into_status(self):
        # Given
        bot = given_bot_with_behaviors()
        workspace = given_workspace_directory()
        # When
        session = when_repl_session_initialized(bot, workspace)
        # Then
        then_status_has_formatter(session.status, session.formatter)
```

### File: `test/repl_cli/test_repl_status_uses_formatter.py`

```python
class TestREPLStatusUsesFormatter:
    """Story: Format Output for AI - REPL Status Uses Formatter"""
    
    def test_repl_status_uses_formatter_for_hierarchical_display(self):
        # Given
        formatter = given_mock_formatter()
        bot = given_bot_with_behaviors()
        status = given_repl_status_with_formatter(bot, formatter)
        # When
        output = when_status_builds_hierarchical_display(status)
        # Then
        then_formatter_methods_were_called(formatter, ['section_separator', 'status_marker', 'list_item'])
```

## Production Code Structure

Following **use_explicit_dependencies**, **keep_classes_small_with_single_responsibility**, and **use_domain_language** rules:

### File: `src/repl_cli/formatters/output_formatter.py`

```python
from abc import ABC, abstractmethod

class OutputFormatter(ABC):
    """Formats output text for display."""
    
    @abstractmethod
    def heading(self, text: str, level: int = 1) -> str:
        """Format heading at specified level."""
        pass
    
    @abstractmethod
    def list_item(self, text: str, indent_level: int = 0, marker: str = None) -> str:
        """Format list item with indentation."""
        pass
    
    @abstractmethod
    def section_separator(self) -> str:
        """Format section divider."""
        pass
    
    @abstractmethod
    def status_marker(self, is_current: bool, is_completed: bool) -> str:
        """Format status indicator."""
        pass
    
    @abstractmethod
    def bold(self, text: str) -> str:
        """Format bold text."""
        pass
    
    @abstractmethod
    def code_inline(self, text: str) -> str:
        """Format inline code."""
        pass
```

### File: `src/repl_cli/formatters/terminal_formatter.py`

```python
from agile_bot.bots.base_bot.src.repl_cli.formatters.output_formatter import OutputFormatter

class TerminalFormatter(OutputFormatter):
    """Formats output for terminal display using plain text."""
    
    def heading(self, text: str, level: int = 1) -> str:
        return text
    
    def list_item(self, text: str, indent_level: int = 0, marker: str = None) -> str:
        indent = "  " * indent_level
        return f"{indent}{text}"
    
    def section_separator(self) -> str:
        return "-" * 60
    
    def status_marker(self, is_current: bool, is_completed: bool) -> str:
        if is_completed:
            return "[x]"
        elif is_current:
            return "[*]"
        return "[ ]"
    
    def bold(self, text: str) -> str:
        return text
    
    def code_inline(self, text: str) -> str:
        return text
```

### File: `src/repl_cli/formatters/markdown_formatter.py`

```python
from agile_bot.bots.base_bot.src.repl_cli.formatters.output_formatter import OutputFormatter

class MarkdownFormatter(OutputFormatter):
    """Formats output for markdown display with rich formatting."""
    
    def heading(self, text: str, level: int = 1) -> str:
        return f"{'#' * level} {text}"
    
    def list_item(self, text: str, indent_level: int = 0, marker: str = None) -> str:
        indent = "  " * indent_level
        prefix = marker if marker else "-"
        return f"{indent}{prefix} {text}"
    
    def section_separator(self) -> str:
        return "---"
    
    def status_marker(self, is_current: bool, is_completed: bool) -> str:
        if is_completed:
            return "✅"
        elif is_current:
            return "▶️"
        return "⬜"
    
    def bold(self, text: str) -> str:
        return f"**{text}**"
    
    def code_inline(self, text: str) -> str:
        return f"`{text}`"
```

### File: `src/repl_cli/formatters/formatter_factory.py`

```python
from agile_bot.bots.base_bot.src.repl_cli.formatters.output_formatter import OutputFormatter
from agile_bot.bots.base_bot.src.repl_cli.formatters.terminal_formatter import TerminalFormatter
from agile_bot.bots.base_bot.src.repl_cli.formatters.markdown_formatter import MarkdownFormatter

class FormatterFactory:
    """Creates formatter based on TTY detection."""
    
    @staticmethod
    def create(tty_detected: bool) -> OutputFormatter:
        if tty_detected:
            return TerminalFormatter()
        else:
            return MarkdownFormatter()
```

### Modifications to `src/repl_cli/repl_session.py`

```python
# Add import
from agile_bot.bots.base_bot.src.repl_cli.formatters.formatter_factory import FormatterFactory

class REPLSession:
    def __init__(self, bot, workspace_directory: Path):
        self.cli_bot = CLIBot(bot, self)
        self.workspace_directory = Path(workspace_directory)
        
        # Detect TTY and create formatter
        tty_result = self.detect_tty()
        self.formatter = FormatterFactory.create(tty_result.tty_detected)
        
        # Inject formatter into components
        self.help = REPLHelp(bot)
        self.status = REPLStatus(self.cli_bot, self, self.formatter)
        self._commands = register_commands(self)
        self._dot_notation_handler = DotNotationCommand(self)
```

### Modifications to `src/repl_cli/repl_status.py`

```python
from agile_bot.bots.base_bot.src.repl_cli.formatters.output_formatter import OutputFormatter

class REPLStatus:
    def __init__(self, bot, state_provider, formatter: OutputFormatter):
        self.bot = bot
        self.state = state_provider
        self.formatter = formatter
    
    @property
    def hierarchical_status(self) -> str:
        lines = []
        
        # Use formatter for separator
        lines.append(self.formatter.section_separator())
        
        # ... existing logic ...
        
        for behavior in self.bot.behaviors:
            # Use formatter for status marker
            marker = self.formatter.status_marker(is_current, is_completed)
            # Use formatter for list item
            lines.append(self.formatter.list_item(f"{marker} {b_name}", indent_level=0))
            
            # Actions
            for action in behavior.actions:
                a_marker = self.formatter.status_marker(is_current_action, is_completed_action)
                lines.append(self.formatter.list_item(f"{a_marker} {a_name}", indent_level=1))
        
        lines.append("")
        lines.append(self.formatter.section_separator())
        
        return "\n".join(lines)
```

## Cursor Command Generation

### File: `src/repl_cli/repl_command_generator.py`

```python
from pathlib import Path
from typing import Dict, Any
import json

class REPLCommandGenerator:
    """Generates Cursor IDE slash commands for REPL CLI."""
    
    def __init__(self, workspace_root: Path, bot_directory: Path, bot_name: str):
        self.workspace_root = workspace_root
        self.bot_directory = bot_directory
        self.bot_name = bot_name
        self.commands_dir = workspace_root / '.cursor' / 'commands'
    
    def generate_commands(self, bot, repl_path: Path) -> Dict[str, Any]:
        """Generate all cursor command files for this bot's REPL."""
        self.commands_dir.mkdir(parents=True, exist_ok=True)
        
        files_created = []
        
        base_file = self._create_base_commands(bot, repl_path)
        files_created.append(base_file)
        
        for behavior in bot.behaviors:
            behavior_file = self._create_behavior_commands(behavior, repl_path)
            files_created.append(behavior_file)
        
        return {
            'bot_name': self.bot_name,
            'commands_generated': len(files_created),
            'files': [str(f) for f in files_created]
        }
    
    def _create_base_commands(self, bot, repl_path: Path) -> Path:
        """Create base command file with status, help, navigation."""
        lines = [
            f"# {self.bot_name} - {bot.goal or 'Bot CLI'}",
            "",
            "## Quick Navigation",
            "",
            "### Check Status",
            f"echo 'status' | python {repl_path}",
            "",
            "### Get Help",
            f"echo 'help' | python {repl_path}",
            "",
            "## Available Behaviors",
            ""
        ]
        
        for behavior in bot.behaviors:
            desc = getattr(behavior, 'description', '') or behavior.name
            lines.append(f"- **{behavior.name}** - {desc}")
            lines.append(f"  - See: `/{self.bot_name}-{behavior.name}`")
        
        content = "\n".join(lines)
        file_path = self.commands_dir / f'{self.bot_name}.md'
        file_path.write_text(content, encoding='utf-8')
        return file_path
    
    def _create_behavior_commands(self, behavior, repl_path: Path) -> Path:
        """Create behavior-specific command file."""
        desc = getattr(behavior, 'description', '') or behavior.name
        lines = [
            f"# {self.bot_name}-{behavior.name} - {desc}",
            "",
            "## Quick Reference",
            ""
        ]
        
        for action in behavior.actions:
            action_desc = getattr(action, 'description', '') or action.name
            lines.extend([
                f"### {action.name.title()} - {action_desc}",
                f"echo '{behavior.name}.{action.name}.instructions' | python {repl_path}",
                ""
            ])
        
        content = "\n".join(lines)
        file_path = self.commands_dir / f'{self.bot_name}-{behavior.name}.md'
        file_path.write_text(content, encoding='utf-8')
        return file_path
```

## Implementation Phases

### Phase 1: Create Formatter Infrastructure (2 hours)
1. Create `formatters/` directory
2. Implement `OutputFormatter` abstract base class
3. Implement `TerminalFormatter` 
4. Implement `MarkdownFormatter`
5. Implement `FormatterFactory`
6. Write unit tests for all formatters

### Phase 2: Integrate with REPLSession (1 hour)
1. Modify `REPLSession.__init__` to create formatter
2. Pass formatter to `REPLStatus` constructor
3. Update `REPLStatus.__init__` signature

### Phase 3: Update REPLStatus (1 hour)
1. Replace direct string formatting in `hierarchical_status()`
2. Use `formatter.section_separator()`
3. Use `formatter.status_marker()`
4. Use `formatter.list_item()`

### Phase 4: Testing (2 hours)
1. Test TerminalFormatter output matches current
2. Test MarkdownFormatter produces valid markdown
3. Integration test with mocked TTY detection
4. Manual test with actual pipe

### Phase 5: Cursor Command Generation (1.5 hours)
1. Implement `REPLCommandGenerator`
2. Generate base and behavior command files
3. Update bot registry
4. Test generated commands

### Phase 6: Documentation (30 minutes)
1. NO docstrings! or comments in classes
2. Update REPL documentation
3. Document cursor command generation

## Estimated Effort

**Total: 8 hours**

## Rules Applied

### Shape Rules
- ✅ verb_noun_format: "Format Output", "Create Formatter", "Display Status"
- ✅ active_business_and_behavioral_language: "Formatter formats output", "Session creates formatter"
- ✅ outcome_oriented_language: Focus on formatted output, not "showing" or "displaying"
- ✅ valuable: Delivers independent value - AI gets better formatted output
- ✅ small_and_testable: Can be tested independently with clear acceptance criteria

### Scenarios Rules
- ✅ given_describes_state_not_actions: "Given REPL is initialized" (state), not "Given REPL initializes" (action)
- ✅ write_plain_english_scenarios: No variables or placeholders in scenarios
- ✅ scenarios_cover_all_cases: Happy path (terminal), edge case (piped), integration

### Tests Rules
- ✅ use_class_based_organization: File=sub-epic, Class=story, Method=scenario
- ✅ pytest_bdd_orchestrator_pattern: Test shows Given-When-Then flow
- ✅ use_given_when_then_helpers: Reusable helper functions
- ✅ call_production_code_directly: No mocking of business logic
- ✅ cover_all_behavior_paths: Normal, edge, and failure scenarios

### Code Rules
- ✅ use_explicit_dependencies: Formatter injected via constructor
- ✅ keep_classes_small_with_single_responsibility: Each formatter does one thing
- ✅ use_domain_language: OutputFormatter, TerminalFormatter, not GenericFormatter
- ✅ eliminate_duplication: Factory pattern eliminates if-else duplication
- ✅ use_clear_function_parameters: 0-2 parameters, typed objects

## Success Criteria

- [ ] Terminal mode produces identical output to current version
- [ ] Piped mode produces rich Markdown output
- [ ] All existing tests pass
- [ ] New tests achieve 80%+ coverage
- [ ] Cursor commands generated for all behaviors
- [ ] Bot registry updated with REPL CLI path
- [ ] No breaking changes to CLI commands or behavior

