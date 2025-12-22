# Validation Status - code
Started: 2025-12-22 13:08:24
Files: 2


## Cross-File Duplication Analysis
Scanning 2 files...
Extracted 3 code blocks
Starting 3 pairwise comparisons...
Comparing: 33% (1/3) - 0 violations - ETA: 2s  
Comparing: 66% (2/3) - 0 violations - ETA: 0s  
Comparing: 100% (3/3) - 0 violations - ETA: 0s  
Complete: 3 comparisons, 0 violations

## stop_writing_useless_comments
**orchestrator.py** - 9 violation(s)

[X] ERROR (line 6)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class Orchestrator:
    """Orchestrates visiting behaviors and actions using a visitor pattern."""
    
```

[X] ERROR (line 16)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def generate(self) -> None:
        """Generate output by visiting all behaviors and actions."""
        self.visitor.visit_header(self.bot_name)
```

[X] ERROR (line 23)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def generate_help(self) -> None:
        """Backward compatibility alias for generate()."""
        self.generate()
```

[X] ERROR (line 27)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _render_action_help_section(self) -> None:
        """Backward compatibility - delegates to _visit_action_help_section."""
        self._visit_action_help_section()
```

[X] ERROR (line 31)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _visit_behaviors(self) -> None:
        """Visit all behaviors in sorted order."""
        behaviors_list = list(self.bot.behaviors)
```

[X] ERROR (line 38)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _visit_behavior(self, behavior) -> None:
        """Visit a behavior and create context for visitor."""
        behavior_name = behavior.name
```

[X] ERROR (line 53)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _get_additional_options(self, behavior_name: str) -> dict:
        """Get additional options for a behavior."""
        if behavior_name == 'code':
```

[X] ERROR (line 62)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _visit_action_help_section(self) -> None:
        """Visit all actions in the action help section."""
        self.visitor.visit_action_help_section_header()
```

[X] ERROR (line 68)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def _visit_action(self, action_name: str) -> None:
        """Visit a single action and create context for visitor."""
        action_description = self.data_collector.get_action_description(action_name)
```

---

## stop_writing_useless_comments
**visitor.py** - 6 violation(s)

[X] ERROR (line 5)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python

class Visitor(ABC):
    """Base visitor for artifact generation."""
    
```

[X] ERROR (line 9)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @abstractmethod
    def visit_header(self, bot_name: str) -> None:
        """Visit the header section."""
        pass
```

[X] ERROR (line 14)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @abstractmethod
    def visit_behavior(self, context: BehaviorHelpContext) -> None:
        """Visit a behavior."""
        pass
```

[X] ERROR (line 19)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @abstractmethod
    def visit_action(self, context: ActionHelpContext) -> None:
        """Visit an action."""
        pass
```

[X] ERROR (line 24)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    @abstractmethod
    def visit_action_help_section_header(self) -> None:
        """Visit the action help section header."""
        pass
```

[X] ERROR (line 28)
Useless docstring that repeats function/class name - delete it or explain WHY, not WHAT

```python
    
    def visit_footer(self) -> None:
        """Visit the footer section (optional)."""
        pass
```

---

## use_domain_language
**orchestrator.py** - 1 violation(s)

[!] WARNING (line 22)
Function "generate_help" uses generate/calculate. Use property instead (e.g., "recommended_trades" not "generate_recommendation").

---

Completed: 2025-12-22 13:08:25
Total violations: 16
Scanners executed: 30
