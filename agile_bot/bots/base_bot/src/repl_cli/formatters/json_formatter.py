from .output_formatter import OutputFormatter


class JSONFormatter(OutputFormatter):
    """
    Formatter for JSON output.
    Returns minimal string markers that will be incorporated into JSON structures.
    Icons and separators are omitted or simplified for machine-readable output.
    """
    
    def section_separator(self) -> str:
        """No separator needed in JSON"""
        return ""
    
    def subsection_separator(self) -> str:
        """No separator needed in JSON"""
        return ""
    
    def status_marker(self, is_current: bool, is_completed: bool) -> str:
        """Return simple unicode markers for JSON"""
        if is_completed:
            return "☑"
        elif is_current:
            return "➤"
        else:
            return "☐"
    
    def list_item(self, content: str, indent_level: int = 0) -> str:
        """Return content without formatting for JSON"""
        return content
    
    def highlight(self, text: str) -> str:
        """No highlighting in JSON - return plain text"""
        return text
    
    def bot_icon(self) -> str:
        return "🤖"
    
    def workspace_icon(self) -> str:
        return "📂"
    
    def path_icon(self) -> str:
        return "📁"
    
    def scope_icon(self) -> str:
        return "🎯"
    
    def position_icon(self) -> str:
        return "📍"
    
    def currently_executing_icon(self) -> str:
        return "▶️"
    
    def file_icon(self) -> str:
        return "📄"
    
    # Additional formatting methods for JSON
    def format_heading(self, text: str, level: int = 2) -> str:
        """Return plain heading text for JSON"""
        return text
    
    def format_code_block(self, code: str, language: str = '') -> list:
        """Return code as-is for JSON"""
        return [code]
    
    def format_section_separator(self) -> list:
        """No separator in JSON"""
        return []
    
    def format_bold(self, text: str) -> str:
        """No formatting in JSON"""
        return text
    
    def format_italic(self, text: str) -> str:
        """No formatting in JSON"""
        return text
    
    def format_code_inline(self, text: str) -> str:
        """No formatting in JSON"""
        return text
