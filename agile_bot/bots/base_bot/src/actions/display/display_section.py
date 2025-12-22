"""Display section formatting for markdown output."""

from typing import List


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
        for line in self.header_lines:
            instructions.add_display(line)

