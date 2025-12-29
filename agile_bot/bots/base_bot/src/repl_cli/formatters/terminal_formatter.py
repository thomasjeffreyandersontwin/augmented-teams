from agile_bot.bots.base_bot.src.repl_cli.formatters.output_formatter import OutputFormatter


class TerminalFormatter(OutputFormatter):
    
    def section_separator(self) -> str:
        """Heavy line for major section breaks"""
        return "=" * 60
    
    def subsection_separator(self) -> str:
        """Light line for subsection breaks"""
        return "-" * 60
    
    def status_marker(self, is_current: bool, is_completed: bool) -> str:
        if is_completed:
            return "[OK]"
        elif is_current:
            return "[*]"
        else:
            return "[ ]"
    
    def list_item(self, content: str, indent_level: int = 0) -> str:
        indent = "  " * indent_level
        return f"{indent}{content}"
    
    def highlight(self, text: str) -> str:
        return text

