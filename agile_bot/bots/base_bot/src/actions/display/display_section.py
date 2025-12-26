"""Display section formatting for markdown output."""

from typing import List


class HeaderLineCollection:
    """Collection class for header lines"""
    def __init__(self, lines: List[str]):
        self._lines = lines
    
    def add_to_instructions(self, instructions) -> None:
        for line in self._lines:
            instructions.add_display(line)


class DisplaySection:
    
    def __init__(self, title: str, level: int = 2):
        self._title = title
        self._level = level
    
    @property
    def header_lines(self) -> List[str]:
        return [
            '---',
            '',
            f"{'#' * self._level} {self._title}",
            ''
        ]
    
    def add_to(self, instructions) -> None:
        # Delegate to collection class
        collection = HeaderLineCollection(self.header_lines)
        collection.add_to_instructions(instructions)

