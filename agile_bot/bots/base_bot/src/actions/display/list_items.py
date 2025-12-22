"""List item formatting for markdown output."""


class ListItem:
    
    def __init__(self, text: str):
        self._text = text
    
    @property
    def formatted(self) -> str:
        return f"- {self._text}"


class NestedListItem:
    
    def __init__(self, text: str):
        self._text = text
    
    @property
    def formatted(self) -> str:
        return f"  - {self._text}"


class DeeplyNestedListItem:
    
    def __init__(self, text: str):
        self._text = text
    
    @property
    def formatted(self) -> str:
        return f"    - {self._text}"

