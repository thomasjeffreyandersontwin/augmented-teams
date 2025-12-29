import pytest
from unittest.mock import Mock
from agile_bot.bots.base_bot.src.repl_cli.formatters.output_formatter import OutputFormatter
from agile_bot.bots.base_bot.src.repl_cli.formatters.terminal_formatter import TerminalFormatter
from agile_bot.bots.base_bot.src.repl_cli.formatters.markdown_formatter import MarkdownFormatter
from agile_bot.bots.base_bot.src.repl_cli.formatters.formatter_factory import FormatterFactory
from agile_bot.bots.base_bot.src.repl_cli.repl_status import REPLStatus


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


def then_separator_equals(formatter, expected_separator):
    result = formatter.section_separator()
    assert result == expected_separator


def then_status_marker_equals(formatter, is_current, is_completed, expected_marker):
    result = formatter.status_marker(is_current=is_current, is_completed=is_completed)
    assert result == expected_marker


def then_list_item_equals(formatter, content, indent_level, expected_output):
    result = formatter.list_item(content, indent_level=indent_level)
    assert result == expected_output


def then_highlight_equals(formatter, text, expected_output):
    result = formatter.highlight(text)
    assert result == expected_output


def then_formatter_is_type(formatter, expected_type):
    assert isinstance(formatter, expected_type)


class TestTerminalFormatter:
    
    def test_returns_dashes_for_section_separator(self):
        formatter = given_terminal_formatter()
        then_separator_equals(formatter, "-" * 60)
    
    def test_returns_completed_status_marker(self):
        formatter = given_terminal_formatter()
        then_status_marker_equals(formatter, is_current=False, is_completed=True, expected_marker="[OK]")
    
    def test_returns_current_status_marker(self):
        formatter = given_terminal_formatter()
        then_status_marker_equals(formatter, is_current=True, is_completed=False, expected_marker="[*]")
    
    def test_returns_pending_status_marker(self):
        formatter = given_terminal_formatter()
        then_status_marker_equals(formatter, is_current=False, is_completed=False, expected_marker="[ ]")
    
    def test_indents_list_items_by_level(self):
        formatter = given_terminal_formatter()
        then_list_item_equals(formatter, "test", indent_level=2, expected_output="    test")
    
    def test_returns_text_as_is_for_highlight(self):
        formatter = given_terminal_formatter()
        then_highlight_equals(formatter, "important", expected_output="important")


class TestMarkdownFormatter:
    
    def test_returns_markdown_separator(self):
        formatter = given_markdown_formatter()
        then_separator_equals(formatter, "---")
    
    def test_returns_markdown_completed_checkbox(self):
        formatter = given_markdown_formatter()
        then_status_marker_equals(formatter, is_current=False, is_completed=True, expected_marker="- ●")
    
    def test_returns_markdown_current_checkbox(self):
        formatter = given_markdown_formatter()
        then_status_marker_equals(formatter, is_current=True, is_completed=False, expected_marker="- ➤")
    
    def test_returns_markdown_pending_checkbox(self):
        formatter = given_markdown_formatter()
        then_status_marker_equals(formatter, is_current=False, is_completed=False, expected_marker="- ○")
    
    def test_creates_markdown_list_items(self):
        formatter = given_markdown_formatter()
        then_list_item_equals(formatter, "test", indent_level=0, expected_output="- test")
    
    def test_indents_markdown_list_items_by_level(self):
        formatter = given_markdown_formatter()
        then_list_item_equals(formatter, "test", indent_level=1, expected_output="  - test")
    
    def test_wraps_text_in_bold_for_highlight(self):
        formatter = given_markdown_formatter()
        then_highlight_equals(formatter, "important", expected_output="**important**")


class TestFormatterFactory:
    
    def test_creates_terminal_formatter_for_tty(self):
        formatter = FormatterFactory.create_formatter(tty_detected=True)
        then_formatter_is_type(formatter, TerminalFormatter)
    
    def test_creates_markdown_formatter_for_piped_output(self):
        formatter = FormatterFactory.create_formatter(tty_detected=False)
        then_formatter_is_type(formatter, MarkdownFormatter)
    
    def test_creates_terminal_formatter_when_requested(self):
        formatter = FormatterFactory.create_terminal_formatter()
        then_formatter_is_type(formatter, TerminalFormatter)
    
    def test_creates_markdown_formatter_when_requested(self):
        formatter = FormatterFactory.create_markdown_formatter()
        then_formatter_is_type(formatter, MarkdownFormatter)


class TestStatusDisplayFormatterUsage:
    """Test that REPLStatus uses the formatter correctly for status markers"""
    
    def given_mock_bot_with_behaviors(self):
        """Create a mock bot with behaviors and actions"""
        mock_action = Mock()
        mock_action.name = "test_action"
        mock_action.description = "Test action"
        
        mock_behavior = Mock()
        mock_behavior.name = "test_behavior"
        mock_behavior.description = "Test behavior"
        mock_behavior.actions = [mock_action]
        
        mock_bot = Mock()
        mock_bot.behaviors = [mock_behavior]
        return mock_bot
    
    def given_mock_state_provider(self):
        """Create a mock state provider"""
        # Create mock action
        mock_action = Mock()
        mock_action.name = "test_action"
        
        # Create mock behavior with actions
        mock_behavior = Mock()
        mock_behavior.name = "test_behavior"
        mock_behavior.actions = [mock_action]
        
        mock_state = Mock()
        mock_state.progress_path = "test_behavior.test_action"
        mock_state.stage_name = "instructions"
        mock_state.current_behavior_name = "test_behavior"
        mock_state.current_action_name = "test_action"
        mock_state.current_behavior = mock_behavior
        mock_state.completed_behaviors = []
        mock_state.completed_action_names = []
        mock_state.has_current_action = True
        mock_state._get_scope_display_lines = Mock(return_value=[])
        return mock_state
    
    def test_status_uses_terminal_formatter_markers(self):
        # Given: REPLStatus with TerminalFormatter
        formatter = TerminalFormatter()
        bot = self.given_mock_bot_with_behaviors()
        state = self.given_mock_state_provider()
        status = REPLStatus(bot, state, formatter)
        
        # When: Generate hierarchical status
        result = status.hierarchical_status
        
        # Then: Output contains terminal formatter markers [x], [*], [ ]
        assert "[*]" in result  # Current marker
        assert "[ ]" in result  # Pending marker
        # Should NOT contain markdown list markers
        assert "- [*]" not in result
        assert "- [ ]" not in result
    
    def test_status_uses_markdown_formatter_markers(self):
        # Given: REPLStatus with MarkdownFormatter
        formatter = MarkdownFormatter()
        bot = self.given_mock_bot_with_behaviors()
        state = self.given_mock_state_provider()
        status = REPLStatus(bot, state, formatter)
        
        # When: Generate hierarchical status
        result = status.hierarchical_status
        
        # Then: Output contains markdown formatter emoji markers after dashes
        assert "- ➤" in result or "- ○" in result or "- ●" in result  # Emoji markers with dash
        # Verify it's using emojis, not plain brackets
        assert "[*]" not in result  # Should not have terminal formatter markers
        assert "[ ]" not in result  # Should not have terminal formatter markers
    
    def test_status_legend_uses_formatter(self):
        # Given: REPLStatus with MarkdownFormatter
        formatter = MarkdownFormatter()
        bot = self.given_mock_bot_with_behaviors()
        state = self.given_mock_state_provider()
        status = REPLStatus(bot, state, formatter)
        
        # When: Generate full status (which includes legend)
        result = status.full_status
        
        # Then: Legend line uses formatter emoji markers after dashes
        legend = result[-1]  # Legend is typically the last line
        # Should contain emoji markers with dash from the formatter
        assert '- ➤' in legend or '- ○' in legend or '- ●' in legend

