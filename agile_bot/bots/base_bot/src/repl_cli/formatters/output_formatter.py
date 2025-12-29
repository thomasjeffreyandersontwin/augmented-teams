from abc import ABC, abstractmethod


class OutputFormatter(ABC):
    
    @abstractmethod
    def section_separator(self) -> str:
        """Heavy line for major section breaks"""
        pass
    
    def subsection_separator(self) -> str:
        """Light line for subsection breaks - defaults to same as section_separator"""
        return self.section_separator()
    
    @abstractmethod
    def status_marker(self, is_current: bool, is_completed: bool) -> str:
        pass
    
    @abstractmethod
    def list_item(self, content: str, indent_level: int = 0) -> str:
        pass
    
    @abstractmethod
    def highlight(self, text: str) -> str:
        pass
    
    # Emoji/icon methods for different contexts
    def bot_icon(self) -> str:
        """Icon for bot/AI context"""
        return ""
    
    def workspace_icon(self) -> str:
        """Icon for workspace/folder context"""
        return ""
    
    def path_icon(self) -> str:
        """Icon for file path context"""
        return ""
    
    def scope_icon(self) -> str:
        """Icon for scope/target context"""
        return ""
    
    def position_icon(self) -> str:
        """Icon for current position/location"""
        return ""
    
    def currently_executing_icon(self) -> str:
        """Icon for currently executing action"""
        return ""
    
    def file_icon(self) -> str:
        """Icon for file references"""
        return ""

