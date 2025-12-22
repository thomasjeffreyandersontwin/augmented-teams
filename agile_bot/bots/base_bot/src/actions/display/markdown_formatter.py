"""Markdown formatting utilities for consistent output."""

from typing import List


class MarkdownFormatter:
    
    def format_heading(self, text: str, level: int = 2) -> str:
        return f"{'#' * level} {text}"
    
    def format_code_block(self, code: str, language: str = '') -> List[str]:
        return [f'```{language}', code, '```']
    
    def format_section_separator(self) -> List[str]:
        return ['---', '']
    
    def format_bold(self, text: str) -> str:
        return f'**{text}**'
    
    def format_italic(self, text: str) -> str:
        return f'*{text}*'
    
    def format_code_inline(self, text: str) -> str:
        return f'`{text}`'

