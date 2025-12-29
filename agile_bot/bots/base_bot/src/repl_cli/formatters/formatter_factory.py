import sys
from agile_bot.bots.base_bot.src.repl_cli.formatters.output_formatter import OutputFormatter
from agile_bot.bots.base_bot.src.repl_cli.formatters.terminal_formatter import TerminalFormatter
from agile_bot.bots.base_bot.src.repl_cli.formatters.markdown_formatter import MarkdownFormatter


class FormatterFactory:
    
    @staticmethod
    def create_formatter(tty_detected: bool = None) -> OutputFormatter:
        if tty_detected is None:
            tty_detected = sys.stdout.isatty()
        
        if tty_detected:
            return TerminalFormatter()
        else:
            return MarkdownFormatter()
    
    @staticmethod
    def create_terminal_formatter() -> OutputFormatter:
        return TerminalFormatter()
    
    @staticmethod
    def create_markdown_formatter() -> OutputFormatter:
        return MarkdownFormatter()

