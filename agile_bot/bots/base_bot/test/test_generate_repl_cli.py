import pytest
from agile_bot.bots.base_bot.src.repl_cli.formatters.output_formatter import OutputFormatter
from agile_bot.bots.base_bot.src.repl_cli.formatters.terminal_formatter import TerminalFormatter
from agile_bot.bots.base_bot.src.repl_cli.formatters.markdown_formatter import MarkdownFormatter
from agile_bot.bots.base_bot.src.repl_cli.formatters.formatter_factory import FormatterFactory


@pytest.fixture
def bot_directory(tmp_path):
    return tmp_path / "bot"


@pytest.fixture
def workspace_directory(tmp_path):
    return tmp_path / "workspace"


def given_terminal_formatter():
    return TerminalFormatter()


def given_markdown_formatter():
    return MarkdownFormatter()


def when_formatter_formats_separator(formatter):
    return formatter.section_separator()


def when_formatter_formats_status_marker(formatter, is_current, is_completed):
    return formatter.status_marker(is_current=is_current, is_completed=is_completed)


def when_formatter_formats_list_item(formatter, content, indent_level):
    return formatter.list_item(content, indent_level=indent_level)


def when_formatter_formats_highlight(formatter, text):
    return formatter.highlight(text)


def when_factory_creates_formatter(tty_detected):
    return FormatterFactory.create_formatter(tty_detected=tty_detected)


def when_factory_creates_terminal_formatter():
    return FormatterFactory.create_terminal_formatter()


def when_factory_creates_markdown_formatter():
    return FormatterFactory.create_markdown_formatter()


def then_result_equals(result, expected):
    assert result == expected


def then_formatter_is_instance_of(formatter, expected_type):
    assert isinstance(formatter, expected_type)


class TestFormatOutputForAI:
    
    def test_terminal_mode_uses_plain_text_formatting_for_separator(self):
        # Given: Terminal formatter is created
        formatter = given_terminal_formatter()
        
        # When: Separator is formatted
        result = when_formatter_formats_separator(formatter)
        
        # Then: Separator uses equals signs
        then_result_equals(result, "=" * 60)
    
    def test_terminal_mode_uses_plain_text_formatting_for_completed_marker(self):
        # Given: Terminal formatter is created
        formatter = given_terminal_formatter()
        
        # When: Completed status marker is formatted
        result = when_formatter_formats_status_marker(formatter, is_current=False, is_completed=True)
        
        # Then: Marker is plain text [OK]
        then_result_equals(result, "[OK]")
    
    def test_terminal_mode_uses_plain_text_formatting_for_current_marker(self):
        # Given: Terminal formatter is created
        formatter = given_terminal_formatter()
        
        # When: Current status marker is formatted
        result = when_formatter_formats_status_marker(formatter, is_current=True, is_completed=False)
        
        # Then: Marker is plain text [*]
        then_result_equals(result, "[*]")
    
    def test_terminal_mode_uses_plain_text_formatting_for_pending_marker(self):
        # Given: Terminal formatter is created
        formatter = given_terminal_formatter()
        
        # When: Pending status marker is formatted
        result = when_formatter_formats_status_marker(formatter, is_current=False, is_completed=False)
        
        # Then: Marker is plain text [ ]
        then_result_equals(result, "[ ]")
    
    def test_terminal_mode_uses_space_indentation_for_list_items(self):
        # Given: Terminal formatter is created
        formatter = given_terminal_formatter()
        
        # When: List item is formatted with indent level 2
        result = when_formatter_formats_list_item(formatter, "test", indent_level=2)
        
        # Then: Item uses space indentation
        then_result_equals(result, "    test")
    
    def test_terminal_mode_returns_text_as_is_for_highlight(self):
        # Given: Terminal formatter is created
        formatter = given_terminal_formatter()
        
        # When: Text is highlighted
        result = when_formatter_formats_highlight(formatter, "important")
        
        # Then: Text is returned as-is
        then_result_equals(result, "important")
    
    def test_piped_mode_uses_markdown_formatting_for_separator(self):
        # Given: Markdown formatter is created
        formatter = given_markdown_formatter()
        
        # When: Separator is formatted
        result = when_formatter_formats_separator(formatter)
        
        # Then: Separator uses Unicode box-drawing characters
        then_result_equals(result, "━" * 90)
    
    def test_piped_mode_uses_markdown_formatting_for_completed_checkbox(self):
        # Given: Markdown formatter is created
        formatter = given_markdown_formatter()
        
        # When: Completed status marker is formatted
        result = when_formatter_formats_status_marker(formatter, is_current=False, is_completed=True)
        
        # Then: Marker uses markdown bullet with checkbox emoji (REPL_CLI uses ☑)
        then_result_equals(result, "- ☑")
    
    def test_piped_mode_uses_markdown_formatting_for_current_checkbox(self):
        # Given: Markdown formatter is created
        formatter = given_markdown_formatter()
        
        # When: Current status marker is formatted
        result = when_formatter_formats_status_marker(formatter, is_current=True, is_completed=False)
        
        # Then: Marker uses markdown bullet with emoji
        then_result_equals(result, "- ➤")
    
    def test_piped_mode_uses_markdown_formatting_for_pending_checkbox(self):
        # Given: Markdown formatter is created
        formatter = given_markdown_formatter()
        
        # When: Pending status marker is formatted
        result = when_formatter_formats_status_marker(formatter, is_current=False, is_completed=False)
        
        # Then: Marker uses markdown bullet with checkbox emoji
        then_result_equals(result, "- ☐")
    
    def test_piped_mode_uses_markdown_lists_for_list_items(self):
        # Given: Markdown formatter is created
        formatter = given_markdown_formatter()
        
        # When: List item is formatted with no indent
        result = when_formatter_formats_list_item(formatter, "test", indent_level=0)
        
        # Then: Item uses markdown list syntax
        then_result_equals(result, "- test")
    
    def test_piped_mode_indents_markdown_list_items(self):
        # Given: Markdown formatter is created
        formatter = given_markdown_formatter()
        
        # When: List item is formatted with indent level 1
        result = when_formatter_formats_list_item(formatter, "test", indent_level=1)
        
        # Then: Item uses indented markdown list
        then_result_equals(result, "  - test")
    
    def test_piped_mode_uses_bold_for_highlight(self):
        # Given: Markdown formatter is created
        formatter = given_markdown_formatter()
        
        # When: Text is highlighted
        result = when_formatter_formats_highlight(formatter, "important")
        
        # Then: Text uses markdown bold
        then_result_equals(result, "**important**")
    
    def test_formatter_created_at_session_initialization_for_tty(self):
        # Given: REPL session is starting
        # When: Factory creates formatter for TTY mode
        formatter = when_factory_creates_formatter(tty_detected=True)
        
        # Then: Factory creates terminal formatter
        then_formatter_is_instance_of(formatter, TerminalFormatter)
    
    def test_formatter_created_for_piped_mode(self):
        # Given: REPL session is starting
        # When: Factory creates formatter for piped mode
        formatter = when_factory_creates_formatter(tty_detected=False)
        
        # Then: Factory creates markdown formatter for AI agent consumption
        then_formatter_is_instance_of(formatter, MarkdownFormatter)
    
    def test_factory_creates_terminal_formatter_when_requested(self):
        # Given: Factory is available
        # When: Terminal formatter is explicitly requested
        formatter = when_factory_creates_terminal_formatter()
        
        # Then: Factory creates terminal formatter
        then_formatter_is_instance_of(formatter, TerminalFormatter)
    
    def test_factory_creates_markdown_formatter_when_requested(self):
        # Given: Factory is available
        # When: Markdown formatter is explicitly requested
        formatter = when_factory_creates_markdown_formatter()
        
        # Then: Factory creates markdown formatter
        then_formatter_is_instance_of(formatter, MarkdownFormatter)

