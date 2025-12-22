# Duplication Elimination Plan - 1701+ Violations

**Status:** Planning  
**Created:** 2025-12-21  
**Updated:** 2025-12-21 (Revised with comprehensive domain model improvements)  
**Target:** Eliminate all 1701+ duplication violations while following code and domain model rules  
**Estimated Duration:** 3-4 weeks  
**Estimated Total Impact:** ~2200 violations (includes additional patterns discovered during planning)  

---

## Executive Summary

The codebase currently has **1701 duplication violations** detected by the DuplicationScanner. This plan outlines a systematic approach to eliminate all duplications while strictly adhering to:

1. **Code behavior rules** (18 rules from story_bot-code-rules)
2. **Shape/domain model rules** (4 rules from story_bot-shape-rules)
3. **Existing domain model** - Use `StoryMap`, `Epic`, `Story`, etc. from `story_graph/nodes.py`
4. **DRY principle** - Single source of truth for every piece of knowledge

**Key Insights:**
1. **Use existing domain model** - Extend `StoryMap`, `Epic`, `SubEpic`, `Story`, `Scenario` instead of creating new classes
2. **Domain-specific names** - `RulesDigestGuidance` instead of generic "WorkflowInstructions"
3. **No magic numbers** - `ListItem`, `NestedListItem` instead of `format_list_item(text, indent=0)`
4. **Comprehensive AST coverage** - Extract all code elements (functions, classes, if-statements, try-blocks, imports)

**Estimated Impact:** ~2200 violations eliminated (1701 detected + ~500 additional patterns discovered during comprehensive analysis)

---

## Critical Rules to Follow

### Code Rules (Must Follow)

1. ✅ **Eliminate Duplication** - Extract repeated logic into reusable functions
2. ✅ **Use Resource-Oriented Design** - NO Manager/Loader/Handler classes
3. ✅ **Use Domain Language** - NO Dict[str, Any], use typed domain objects
4. ✅ **Use Natural English** - get_many_*, may_*, will_* patterns
5. ✅ **Use Explicit Dependencies** - Constructor injection only
6. ✅ **Enforce Encapsulation** - Properties, not public fields
7. ✅ **Keep Functions Small** - Under 20 lines
8. ✅ **Keep Classes Small** - Under 200 lines, single responsibility
9. ✅ **Use Exceptions Properly** - Domain-specific exception types
10. ✅ **Never Swallow Exceptions** - Always log, handle, or rethrow
11. ✅ **Place Imports At Top** - After docstrings, before code
12. ✅ **Stop Writing Useless Comments** - Explain WHY, not WHAT
13. ✅ **Use Clear Function Parameters** - 3 or fewer, use objects for more
14. ✅ **Maintain Vertical Density** - Declare variables near usage
15. ✅ **Simplify Control Flow** - Guard clauses, early returns
16. ✅ **Refactor Completely** - No partial refactoring
17. ✅ **Provide Meaningful Context** - No magic numbers or cryptic names
18. ✅ **Use Consistent Naming** - Follow established patterns

### Shape/Domain Model Rules (Must Follow)

19. ✅ **Use Resource-Oriented Design** - Domain concepts as objects
20. ✅ **Use Domain Language** - Properties represent what objects contain
21. ✅ **Use Active Behavioral Language** - Focus on capabilities
22. ✅ **Avoid Technical Abstractions** - Use domain concepts

### Story Graph Domain Concepts (Must Use)

From `story-graph.json`, use these domain concepts:
- **Base Bot** - Executes actions, tracks activity, routes to behaviors
- **Behavior** - Performs actions, provides rules, injects instructions
- **Action** - Injects instructions, loads content, saves state
- **Router** - Matches patterns, routes to tools, forwards to actions
- **Workflow State** - Tracks current/completed actions, determines next action
- **Instructions** - Provides guidance for actions
- **Content** - Renders outputs, synchronizes formats, loads/presents content
- **Rules** - Validates content, finds rules, suggests corrections
- **Guardrails** - Provides context, guides decisions, defines activities

### Additional Constraints

23. ✅ **Never Delete Code Without Permission** - Add first, ask before deleting
24. ✅ **No Unicode in Console Output** - ASCII only for Windows compatibility
25. ✅ **Prefer Typed Objects Over Dicts** - Type hints for all parameters

---

## Existing Domain Model (DO NOT CREATE NEW CLASSES)

We already have a complete story graph domain model in `src/story_graph/nodes.py`:

### Existing Classes:
- **`StoryMap`** - Main entry point, loads from story-graph.json
  - `from_bot(bot)` - Load from bot directory
  - `epics` property - Get all epics
  - `walk(node)` - Traverse hierarchy

- **`Epic`** - Top-level epic
  - `name`, `sequential_order`, `domain_concepts`
  - `children` - Sub-epics and story groups
  - `from_dict(data)` - Load from JSON

- **`SubEpic`** - Feature/sub-epic
  - `name`, `sequential_order`, `_parent`
  - `children` - Nested sub-epics and story groups

- **`StoryGroup`** - Group of stories
  - `name`, `sequential_order`, `group_type`, `connector`
  - `children` - Stories

- **`Story`** - Individual story
  - `name`, `sequential_order`, `connector`, `story_type`, `users`
  - `scenarios`, `scenario_outlines`, `acceptance_criteria` properties
  - `test_file`, `test_class` - BDD test mapping

- **`Scenario`** - BDD scenario
  - `name`, `sequential_order`, `type`, `background`, `test_method`
  - `steps` property

- **`ScenarioOutline`** - BDD scenario outline with examples
  - `name`, `sequential_order`, `type`, `background`, `examples`, `test_method`
  - `steps`, `examples_columns`, `examples_rows` properties

### Existing Helper Classes:
- **`StoryGraph`** (in `actions/validate/story_graph.py`) - Handles loading and path resolution
- **`DomainConcept`** (in `story_graph/domain.py`) - Domain concepts with responsibilities/collaborators

---

## Duplication Categories & Solutions

**Total Categories:** 8  
**Total Estimated Violations:** ~2200  
**Approach:** Create domain-specific classes that follow all 25 rules

---

### Category 1: Scope/Parameter Parsing (~400 violations)

**Problem:** Repeated parsing of `scope_config['story_names']`, `scope_config['epic_names']`, etc.

**Solution:** Use existing `StoryMap` domain model + add query/filter methods

#### Changes to Make:

**1.1 Add Query Methods to `StoryMap` class** (`src/story_graph/nodes.py`)

```python
def filter_by_epic_names(self, epic_names: Set[str]) -> 'StoryMap':
    """Get new StoryMap with only specified epics."""
    filtered_epics = [e for e in self._epics if e.name in epic_names]
    filtered_graph = {'epics': [self._epic_to_dict(e) for e in filtered_epics]}
    return StoryMap(filtered_graph)

def filter_by_story_names(self, story_names: Set[str]) -> List[Story]:
    """Get all stories matching specified names."""
    stories = []
    for epic in self._epics:
        for node in self.walk(epic):
            if isinstance(node, Story) and node.name in story_names:
                stories.append(node)
    return stories

@property
def all_stories(self) -> List[Story]:
    """Get all stories from all epics."""
    stories = []
    for epic in self._epics:
        for node in self.walk(epic):
            if isinstance(node, Story):
                stories.append(node)
    return stories

def find_epic_by_name(self, epic_name: str) -> Optional[Epic]:
    """Find epic by name."""
    for epic in self._epics:
        if epic.name == epic_name:
            return epic
    return None

def find_story_by_name(self, story_name: str) -> Optional[Story]:
    """Find first story matching name."""
    for epic in self._epics:
        for node in self.walk(epic):
            if isinstance(node, Story) and node.name == story_name:
                return node
    return None
```

**1.2 Add Query Methods to `Epic` class** (`src/story_graph/nodes.py`)

```python
@property
def all_stories(self) -> List['Story']:
    """Get all stories in this epic (including nested in sub-epics)."""
    stories = []
    for child in self.children:
        if isinstance(child, Story):
            stories.append(child)
        elif isinstance(child, (SubEpic, StoryGroup)):
            stories.extend(self._get_stories_from_node(child))
    return stories

def _get_stories_from_node(self, node: StoryNode) -> List['Story']:
    """Recursively get stories from a node."""
    stories = []
    for child in node.children:
        if isinstance(child, Story):
            stories.append(child)
        elif hasattr(child, 'children'):
            stories.extend(self._get_stories_from_node(child))
    return stories

def find_sub_epic_by_name(self, sub_epic_name: str) -> Optional['SubEpic']:
    """Find sub-epic by name."""
    for child in self.children:
        if isinstance(child, SubEpic) and child.name == sub_epic_name:
            return child
    return None
```

**1.3 Refactor Scope Parsing** - Replace all scope parsing with `StoryMap` usage

**Before:**
```python
# Duplicated in many files
story_names = set()
if 'story_names' in scope_config:
    story_names_value = scope_config['story_names']
    if isinstance(story_names_value, list):
        story_names.update(story_names_value)
    elif isinstance(story_names_value, str):
        story_names.add(story_names_value)
```

**After:**
```python
# Use StoryMap domain model
story_map = StoryMap.from_bot(bot)
story_names = {s.name for s in story_map.all_stories}  # Property access!

# Or with filtering
if 'story_names' in scope_config:
    requested_names = set(scope_config['story_names']) if isinstance(scope_config['story_names'], list) else {scope_config['story_names']}
    stories = story_map.filter_by_story_names(requested_names)
```

**Files to Refactor:**
- `src/actions/action_scope.py` - Replace parsing logic with StoryMap
- `src/scanners/scenarios_on_story_docs_scanner.py` - Use StoryMap
- All other files with scope parsing (identified by scanner)

**Expected Impact:** ~400 violations eliminated

---

### Category 2: Display Formatting (~300 violations)

**Problem:** Repeated markdown section headers across files

**Solution:** Create small display domain classes (these are NOT story graph classes, so we create them)

#### Before (Duplicated Display Formatting):

**Current Code** - Found in many action and report builder files:

```python
# Pattern 1: Section headers (duplicated across many files)
lines.append('---')
lines.append('')
lines.append('## Violations Found')
lines.append('')

# Pattern 2: Subsection headers (duplicated)
lines.append('---')
lines.append('')
lines.append('### File-by-File Violations')
lines.append('')

# Pattern 3: List items (duplicated)
lines.append(f"- {item_text}")
lines.append(f"  - {nested_item}")
lines.append(f"    - {deeply_nested_item}")

# Pattern 4: Code blocks (duplicated)
lines.append('```python')
lines.append(code_content)
lines.append('```')

# Example from validation_violations_builder.py:
lines = ['## Violations Found', '']
file_by_file_violations_by_rule, cross_file_violations_by_rule = self._organize_violations(validation_rules)
total_file_by_file = sum((len(v) for v in file_by_file_violations_by_rule.values()))
total_cross_file = sum((len(v) for v in cross_file_violations_by_rule.values()))
```

**Problem:** These markdown formatting patterns are duplicated across 20+ files. Any change to formatting style requires updating all files.

#### After (Using Display Domain Classes):

**New Domain Classes**:

**`src/actions/display/display_section.py`:**
```python
class DisplaySection:
    """A formatted section for display output."""
    
    def __init__(self, title: str, level: int = 2):
        self._title = title
        self._level = level
    
    @property
    def header_lines(self) -> List[str]:
        """Get formatted header lines for this section."""
        return [
            '---',
            '',
            f"{'#' * self._level} {self._title}",
            ''
        ]
    
    def add_to(self, instructions) -> None:
        """Add this section's header to instructions."""
        for line in self.header_lines:
            instructions.add_display(line)
```

**`src/actions/display/markdown_formatter.py`:**
```python
class MarkdownFormatter:
    """Formats markdown elements for display."""
    
    def format_heading(self, text: str, level: int = 2) -> str:
        """Format a markdown heading."""
        return f"{'#' * level} {text}"
    
    def format_code_block(self, code: str, language: str = '') -> List[str]:
        """Format a code block."""
        return [f'```{language}', code, '```']
    
    def format_section_separator(self) -> List[str]:
        """Format a section separator."""
        return ['---', '']
```

**`src/actions/display/list_items.py`:**
```python
class ListItem:
    """A top-level markdown list item."""
    
    def __init__(self, text: str):
        self._text = text
    
    @property
    def formatted(self) -> str:
        """Get formatted list item."""
        return f"- {self._text}"


class NestedListItem:
    """A nested markdown list item (one level deep)."""
    
    def __init__(self, text: str):
        self._text = text
    
    @property
    def formatted(self) -> str:
        """Get formatted nested list item."""
        return f"  - {self._text}"


class DeeplyNestedListItem:
    """A deeply nested markdown list item (two levels deep)."""
    
    def __init__(self, text: str):
        self._text = text
    
    @property
    def formatted(self) -> str:
        """Get formatted deeply nested list item."""
        return f"    - {self._text}"
```

**Refactored Usage**:

```python
from agile_bot.bots.base_bot.src.actions.display.display_section import DisplaySection
from agile_bot.bots.base_bot.src.actions.display.markdown_formatter import MarkdownFormatter
from agile_bot.bots.base_bot.src.actions.display.list_items import ListItem, NestedListItem, DeeplyNestedListItem

# Pattern 1: Section headers (clean)
section = DisplaySection('Violations Found', level=2)
lines.extend(section.header_lines)

# Pattern 2: Subsection headers (clean)
subsection = DisplaySection('File-by-File Violations', level=3)
lines.extend(subsection.header_lines)

# Pattern 3: List items (clean, no magic numbers!)
lines.append(ListItem(item_text).formatted)
lines.append(NestedListItem(nested_item).formatted)
lines.append(DeeplyNestedListItem(deeply_nested_item).formatted)

# Pattern 4: Code blocks (clean)
formatter = MarkdownFormatter()
lines.extend(formatter.format_code_block(code_content, language='python'))

# Refactored validation_violations_builder.py example:
section = DisplaySection('Violations Found', level=2)
lines = section.header_lines
file_by_file_violations_by_rule, cross_file_violations_by_rule = self._organize_violations(validation_rules)
total_file_by_file = sum((len(v) for v in file_by_file_violations_by_rule.values()))
total_cross_file = sum((len(v) for v in cross_file_violations_by_rule.values()))
```

**Benefits:**
- Single source of truth for markdown formatting
- Consistent formatting across all reports
- Easy to change formatting style globally
- **No magic numbers** - `ListItem` instead of `format_list_item(text, 0)`
- **Domain-specific classes** - Each list item type is its own class
- Follows "Use Domain Language" rule
- Follows "Eliminate Duplication" rule

**Files to Refactor:**
- `src/actions/validate/validation_violations_builder.py`
- `src/actions/validate/validation_report_builder.py`
- `src/actions/validate/validation_scanner_status_builder.py`
- 15+ other report builder and action files

**Expected Impact:** ~300 violations eliminated

---

### Category 3: Rules Digest Guidance (~200 violations)

**Problem:** Repeated rules digest guidance text

**Solution:** Create domain class for rules digest usage instructions

#### Before (Duplicated in Multiple Files):

**Current Code** - Found in `src/actions/rules/rules_action.py` and other action files:

```python
# This exact block is duplicated in multiple action files
instructions.add("")
instructions.add(rules_digest)
instructions.add("")
instructions.add("CRITICAL: The rules digest above contains everything you need to get started.")
instructions.add("")
instructions.add("WORKFLOW:")
instructions.add("1. Read the rules digest above (descriptions + key principles)")
instructions.add("2. Apply rules to the user's request")
instructions.add("3. IF you need clarity on a specific rule (examples, edge cases, detailed patterns):")
instructions.add("   - Use read_file tool to read that specific rule file")
instructions.add("   - The full rule has detailed examples and detection patterns")
instructions.add("4. Cite rule names when making decisions")
instructions.add("")
instructions.add("The digest gives you 80% of what you need - only read full rules when needed.")
```

**Problem:** This 15-line block is copy-pasted across multiple action files. Any change requires updating all copies. The name "workflow instructions" is too generic - these are specifically about **how to use the rules digest**.

#### After (Using Domain Class):

**New Domain Class** - `src/actions/instructions/rules_digest_guidance.py`:

```python
class RulesDigestGuidance:
    """Standard guidance for how to use the rules digest.
    
    Provides instructions to AI on how to work with the rules digest:
    - Read digest first (80% of what's needed)
    - Apply rules to user's request
    - Only read full rule files when needing specific details
    """
    
    @property
    def lines(self) -> List[str]:
        """Get rules digest guidance lines."""
        return [
            'CRITICAL: The rules digest above contains everything you need to get started.',
            '',
            'WORKFLOW:',
            '1. Read the rules digest above (descriptions + key principles)',
            "2. Apply rules to the user's request",
            '3. IF you need clarity on a specific rule (examples, edge cases, detailed patterns):',
            '   - Use read_file tool to read that specific rule file',
            '   - The full rule has detailed examples and detection patterns',
            '4. Cite rule names when making decisions',
            '',
            'The digest gives you 80% of what you need - only read full rules when needed.'
        ]
    
    def add_to(self, instructions) -> None:
        """Add rules digest guidance to instructions."""
        for line in self.lines:
            instructions.add(line)
```

**Refactored Usage** - In `src/actions/rules/rules_action.py`:

```python
from agile_bot.bots.base_bot.src.actions.instructions.rules_digest_guidance import RulesDigestGuidance

# Clean, simple usage with domain-specific name
instructions.add("")
instructions.add(rules_digest)
instructions.add("")
RulesDigestGuidance().add_to(instructions)
```

**Benefits:**
- Single source of truth for rules digest guidance
- Changes in one place update all usages
- Cleaner, more readable action code
- **Domain-specific name** - `RulesDigestGuidance` is clearer than generic "WorkflowInstructions"
- Follows "Use Domain Language" rule

**Files to Refactor:**
- `src/actions/rules/rules_action.py`
- All other action files with rules digest guidance

**Expected Impact:** ~200 violations eliminated

---

### Category 4: File Validation (~250 violations)

**Problem:** Repeated file existence/readability checks

**Solution:** Create file validation domain classes

#### Before (Duplicated in 58+ Files):

**Current Code** - Found in scanners, actions, and other files:

```python
# Pattern 1: Simple existence check (duplicated 58+ times)
if not file_path.exists():
    return violations

# Pattern 2: Existence check with error message
if not file_path.exists():
    logger.error(f'File not found at {file_path}')
    raise FileNotFoundError(f'File not found')

# Pattern 3: Existence check with size validation
if not file_path.exists():
    return None
try:
    content = file_path.read_text(encoding='utf-8')
    if len(content) > 500_000:
        logger.warning(f'File too large: {file_path}')
        return None
except Exception as e:
    logger.error(f'Failed to read {file_path}: {e}')
    return None
```

**Problem:** These patterns are duplicated across 58+ files. Each file implements its own validation logic with slight variations.

#### After (Using Domain Class):

**New Domain Class** - `src/actions/validation/file_validator.py`:

```python
from pathlib import Path

class FileValidator:
    """Validates file operations and existence."""
    
    def __init__(self, file_path: Path):
        self._file_path = file_path
    
    @property
    def exists(self) -> bool:
        """Check if file exists."""
        return self._file_path.exists()
    
    @property
    def is_readable(self) -> bool:
        """Check if file is readable."""
        if not self.exists:
            return False
        try:
            self._file_path.read_text(encoding='utf-8')
            return True
        except Exception:
            return False
    
    @property
    def size_bytes(self) -> int:
        """Get file size in bytes."""
        return self._file_path.stat().st_size if self.exists else 0
    
    @property
    def is_too_large(self) -> bool:
        """Check if file exceeds reasonable size (500KB)."""
        return self.size_bytes > 500_000
    
    def may_read(self) -> bool:
        """Check if file may be read."""
        return self.exists and self.is_readable and not self.is_too_large
```

**Refactored Usage** - In scanner files:

```python
from agile_bot.bots.base_bot.src.actions.validation.file_validator import FileValidator

# Clean, declarative validation
validator = FileValidator(file_path)
if not validator.exists:
    return violations

# Or more comprehensive check
if not validator.may_read:
    logger.warning(f'Cannot read file: {file_path}')
    return violations
```

**Benefits:**
- Single source of truth for file validation
- Consistent validation logic across all files
- Easier to add new validation rules (e.g., file permissions)
- Follows "Use Domain Language" rule (`.may_read` is clearer than nested if statements)

**Files to Refactor:**
- `src/scanners/duplication_scanner.py` (3 instances)
- `src/scanners/code_scanner.py` (2 instances)
- `src/scanners/test_scanner.py` (2 instances)
- 50+ other scanner and action files

**Expected Impact:** ~250 violations eliminated

---

### Category 5: AST/Code Analysis (~300 violations)

**Problem:** Repeated AST parsing and extraction of functions, classes, if-statements, try-blocks, imports

**Solution:** Create comprehensive AST domain classes for all code elements

#### Before (Duplicated in Multiple Scanner Files):

**Current Code** - Found in `src/scanners/excessive_guards_scanner.py`, `src/scanners/swallowed_exceptions_scanner.py`, and many others:

```python
# Pattern 1: Extract all functions (duplicated across many scanners)
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        # Process function
        func_name = node.name
        func_line = node.lineno
        # ... more processing

# Pattern 2: Extract all try/except blocks
for node in ast.walk(tree):
    if isinstance(node, ast.Try):
        for handler in node.handlers:
            # Process exception handler
            handler_body = handler.body
            # ... more processing

# Pattern 3: Extract all if statements (guard clauses)
for node in ast.walk(tree):
    if isinstance(node, ast.If):
        # Check if it's a guard clause
        # ... complex logic
```

**Problem:** The `ast.walk()` + `isinstance()` pattern is repeated across 20+ scanner files. Each scanner reimplements the same traversal logic for functions, classes, if-statements, try-blocks, and imports.

#### After (Using Comprehensive Domain Classes):

**New Domain Classes** - `src/scanners/resources/ast_elements.py`:

```python
import ast
from typing import List, TypeVar, Generic
from abc import ABC, abstractmethod

T = TypeVar('T')

# ============================================================================
# BASE CLASSES
# ============================================================================

class ASTCollection(ABC, Generic[T]):
    """Base class for AST element collections.
    
    Provides common pattern for extracting elements from AST:
    - Lazy loading (only extract when accessed)
    - Caching (extract once, reuse)
    - Consistent interface (get_many_* property)
    """
    
    def __init__(self, ast_node: ast.AST):
        self._ast_node = ast_node
        self._elements: List[T] = None
    
    @property
    @abstractmethod
    def get_many_elements(self) -> List[T]:
        """Get all elements from this AST node."""
        if self._elements is None:
            self._elements = self._extract_elements()
        return self._elements
    
    @abstractmethod
    def _extract_elements(self) -> List[T]:
        """Extract elements from AST. Subclasses implement specific extraction logic."""
        pass


class ASTElement(ABC):
    """Base class for individual AST elements.
    
    Provides common properties all AST elements share:
    - line_number (where element appears in code)
    - Access to underlying AST node
    """
    
    def __init__(self, node: ast.AST):
        self._node = node
    
    @property
    def line_number(self) -> int:
        """Get line number where this element appears."""
        return self._node.lineno


# ============================================================================
# FUNCTIONS
# ============================================================================

class Functions(ASTCollection['Function']):
    """Collection of functions extracted from AST."""
    
    @property
    def get_many_elements(self) -> List['Function']:
        """Get all functions from this AST node."""
        if self._elements is None:
            self._elements = self._extract_elements()
        return self._elements
    
    # Alias for domain-specific naming
    @property
    def get_many_functions(self) -> List['Function']:
        """Get all functions from this AST node."""
        return self.get_many_elements
    
    def _extract_elements(self) -> List['Function']:
        """Extract all function definitions."""
        functions = []
        for node in ast.walk(self._ast_node):
            if isinstance(node, ast.FunctionDef):
                functions.append(Function(node))
        return functions


class Function(ASTElement):
    """A single function from AST."""
    
    @property
    def name(self) -> str:
        """Get function name."""
        return self._node.name
    
    @property
    def body_lines(self) -> int:
        """Get function body line count."""
        if not self._node.body:
            return 0
        first_line = self._node.body[0].lineno
        last_line = max(stmt.lineno for stmt in ast.walk(self._node) if hasattr(stmt, 'lineno'))
        return last_line - first_line + 1
    
    @property
    def is_test_function(self) -> bool:
        """Check if this is a test function."""
        return self.name.startswith('test_')


# ============================================================================
# CLASSES
# ============================================================================

class Classes(ASTCollection['Class']):
    """Collection of classes extracted from AST."""
    
    @property
    def get_many_elements(self) -> List['Class']:
        """Get all classes from this AST node."""
        if self._elements is None:
            self._elements = self._extract_elements()
        return self._elements
    
    # Alias for domain-specific naming
    @property
    def get_many_classes(self) -> List['Class']:
        """Get all classes from this AST node."""
        return self.get_many_elements
    
    def _extract_elements(self) -> List['Class']:
        """Extract all class definitions."""
        classes = []
        for node in ast.walk(self._ast_node):
            if isinstance(node, ast.ClassDef):
                classes.append(Class(node))
        return classes


class Class(ASTElement):
    """A single class from AST."""
    
    @property
    def name(self) -> str:
        """Get class name."""
        return self._node.name
    
    @property
    def methods(self) -> List[Function]:
        """Get all methods in this class."""
        methods = []
        for node in self._node.body:
            if isinstance(node, ast.FunctionDef):
                methods.append(Function(node))
        return methods
    
    @property
    def is_test_class(self) -> bool:
        """Check if this is a test class."""
        return self.name.startswith('Test')


# ============================================================================
# IF STATEMENTS
# ============================================================================

class IfStatements(ASTCollection['IfStatement']):
    """Collection of if statements extracted from AST."""
    
    @property
    def get_many_elements(self) -> List['IfStatement']:
        """Get all if statements from this AST node."""
        if self._elements is None:
            self._elements = self._extract_elements()
        return self._elements
    
    # Alias for domain-specific naming
    @property
    def get_many_if_statements(self) -> List['IfStatement']:
        """Get all if statements from this AST node."""
        return self.get_many_elements
    
    def _extract_elements(self) -> List['IfStatement']:
        """Extract all if statements."""
        if_statements = []
        for node in ast.walk(self._ast_node):
            if isinstance(node, ast.If):
                if_statements.append(IfStatement(node))
        return if_statements


class IfStatement(ASTElement):
    """A single if statement from AST."""
    
    @property
    def has_else_clause(self) -> bool:
        """Check if this if statement has an else clause."""
        return len(self._node.orelse) > 0
    
    @property
    def is_guard_clause(self) -> bool:
        """Check if this is a guard clause (early return pattern)."""
        if not self._node.body:
            return False
        # Guard clause typically has a return statement in the body
        for stmt in self._node.body:
            if isinstance(stmt, ast.Return):
                return True
        return False


# ============================================================================
# TRY/EXCEPT BLOCKS
# ============================================================================

class TryBlocks(ASTCollection['TryBlock']):
    """Collection of try/except blocks extracted from AST."""
    
    @property
    def get_many_elements(self) -> List['TryBlock']:
        """Get all try/except blocks from this AST node."""
        if self._elements is None:
            self._elements = self._extract_elements()
        return self._elements
    
    # Alias for domain-specific naming
    @property
    def get_many_try_blocks(self) -> List['TryBlock']:
        """Get all try/except blocks from this AST node."""
        return self.get_many_elements
    
    def _extract_elements(self) -> List['TryBlock']:
        """Extract all try/except blocks."""
        try_blocks = []
        for node in ast.walk(self._ast_node):
            if isinstance(node, ast.Try):
                try_blocks.append(TryBlock(node))
        return try_blocks


class TryBlock(ASTElement):
    """A single try/except block from AST."""
    
    @property
    def exception_handlers(self) -> List[ast.ExceptHandler]:
        """Get all exception handlers."""
        return self._node.handlers
    
    @property
    def has_bare_except(self) -> bool:
        """Check if this has a bare except clause (except: without type)."""
        for handler in self._node.handlers:
            if handler.type is None:
                return True
        return False
    
    @property
    def has_finally(self) -> bool:
        """Check if this has a finally clause."""
        return len(self._node.finalbody) > 0


# ============================================================================
# IMPORTS
# ============================================================================

class Imports(ASTCollection['Import']):
    """Collection of import statements extracted from AST."""
    
    @property
    def get_many_elements(self) -> List['Import']:
        """Get all import statements from this AST node."""
        if self._elements is None:
            self._elements = self._extract_elements()
        return self._elements
    
    # Alias for domain-specific naming
    @property
    def get_many_imports(self) -> List['Import']:
        """Get all import statements from this AST node."""
        return self.get_many_elements
    
    def _extract_elements(self) -> List['Import']:
        """Extract all import statements."""
        imports = []
        for node in ast.walk(self._ast_node):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                imports.append(Import(node))
        return imports


class Import(ASTElement):
    """A single import statement from AST."""
    
    @property
    def is_from_import(self) -> bool:
        """Check if this is a 'from X import Y' statement."""
        return isinstance(self._node, ast.ImportFrom)
    
    @property
    def module_name(self) -> str:
        """Get the module name being imported."""
        if isinstance(self._node, ast.ImportFrom):
            return self._node.module or ''
        elif isinstance(self._node, ast.Import):
            if self._node.names:
                return self._node.names[0].name
        return ''
```

**Refactored Usage** - In scanner files:

```python
from agile_bot.bots.base_bot.src.scanners.resources.ast_elements import (
    Functions, Classes, IfStatements, TryBlocks, Imports
)

# Extract functions (clean, declarative)
functions = Functions(tree)
for function in functions.get_many_functions:
    if function.is_test_function:
        continue
    violations.extend(self._check_function(function))

# Extract classes (clean, declarative)
classes = Classes(tree)
for cls in classes.get_many_classes:
    if cls.is_test_class:
        continue
    violations.extend(self._check_class(cls))

# Extract if statements for guard clause analysis
if_statements = IfStatements(tree)
for if_stmt in if_statements.get_many_if_statements:
    if if_stmt.is_guard_clause:
        violations.append(...)

# Extract try/except blocks for exception handling analysis
try_blocks = TryBlocks(tree)
for try_block in try_blocks.get_many_try_blocks:
    if try_block.has_bare_except:
        violations.append(...)

# Extract imports for import placement analysis
imports = Imports(tree)
for import_stmt in imports.get_many_imports:
    if import_stmt.line_number > first_code_line:
        violations.append(...)
```

**Benefits:**
- Single source of truth for ALL AST traversal
- Consistent extraction across all scanners
- Domain-oriented properties (`.is_test_function`, `.is_guard_clause`, `.has_bare_except`)
- **Inheritance eliminates duplication** - Base classes provide common functionality:
  - `ASTCollection` - Lazy loading, caching, consistent interface for all collections
  - `ASTElement` - Common `.line_number` property for all elements
- Follows "Use Resource-Oriented Design" rule (collection classes)
- Follows "Use Domain Language" rule (semantic properties)
- Follows "Eliminate Duplication" rule (base classes eliminate repeated patterns)
- Easier to add new AST element types (just inherit from base classes)
- **Comprehensive coverage** - handles functions, classes, if-statements, try-blocks, imports

**Why Use Inheritance:**
1. **Eliminates duplication** - All collections share same extraction pattern (lazy load + cache)
2. **Consistent interface** - All collections have `get_many_elements` property
3. **Type safety** - Generic base class ensures type consistency
4. **Easier to extend** - New AST element types just inherit from base classes
5. **Follows existing patterns** - While existing resource classes (`File`, `Block`) don't use inheritance, AST classes have MORE duplication that benefits from a base class

**Files to Refactor:**
- `src/scanners/excessive_guards_scanner.py` - use `IfStatements`
- `src/scanners/swallowed_exceptions_scanner.py` - use `TryBlocks`
- `src/scanners/class_size_scanner.py` - use `Classes`
- `src/scanners/import_placement_scanner.py` - use `Imports`
- 20+ other scanner files with AST traversal

**Expected Impact:** ~300 violations eliminated (increased from 200 due to comprehensive coverage)

---

### Category 6: Collection Iteration (~150 violations)

**Problem:** Repeated iteration patterns over collections

**Solution:** Use existing `StoryMap.walk()` and add collection methods

#### Before (Duplicated Nested Iteration):

**Current Code** - Found in multiple scanner and action files:

```python
# Pattern 1: Deeply nested iteration (duplicated across files)
for epic in story_graph.get('epics', []):
    epic_name = epic.get('name', '')
    for sub_epic in epic.get('sub_epics', []):
        sub_epic_name = sub_epic.get('name', '')
        for story_group in sub_epic.get('story_groups', []):
            for story in story_group.get('stories', []):
                story_name = story.get('name', '')
                # Process story
                violations.append(...)

# Pattern 2: Collecting all stories (duplicated)
all_stories = []
for epic in story_graph.get('epics', []):
    for sub_epic in epic.get('sub_epics', []):
        for story_group in sub_epic.get('story_groups', []):
            for story in story_group.get('stories', []):
                all_stories.append(story)

# Pattern 3: Finding a specific story (duplicated)
target_story = None
for epic in story_graph.get('epics', []):
    for sub_epic in epic.get('sub_epics', []):
        for story_group in sub_epic.get('story_groups', []):
            for story in story_group.get('stories', []):
                if story.get('name') == story_name:
                    target_story = story
                    break
```

**Problem:** These nested loops are duplicated across many files. They work with raw dicts instead of domain objects.

#### After (Using StoryMap Domain Model):

**Refactored Usage** - Using existing `StoryMap.walk()` method:

```python
from agile_bot.bots.base_bot.src.story_graph.nodes import StoryMap, Story

# Pattern 1: Clean iteration with domain objects
story_map = StoryMap.from_bot(bot)
for epic in story_map.epics:
    for node in story_map.walk(epic):
        if isinstance(node, Story):
            # Process story - now a typed domain object!
            violations.append(...)

# Pattern 2: Collecting all stories (using property)
story_map = StoryMap.from_bot(bot)
all_stories = story_map.all_stories  # Property access!

# Pattern 3: Finding a specific story (using method - it takes a parameter)
story_map = StoryMap.from_bot(bot)
target_story = story_map.find_story_by_name(story_name)  # Method call (has parameter)
```

**Benefits:**
- No more deeply nested loops
- Work with typed domain objects instead of dicts
- Single source of truth for iteration logic
- **Properties for collections** - `.all_stories` instead of `.get_all_stories()` (no parameters = property)
- **Methods for queries** - `.find_story_by_name(name)` (has parameters = method)
- Follows "Use Domain Language" rule
- Follows "Enforce Encapsulation" rule
- Much more readable and maintainable

**Property vs Method Rule:**
- Use **property** when: No parameters, represents what the object contains (e.g., `.all_stories`, `.all_scenarios`)
- Use **method** when: Has parameters, performs a query or action (e.g., `.find_story_by_name(name)`, `.filter_by_epic_names(names)`)

**6.2 Add Convenience Properties to `StoryMap`**

```python
@property
def all_scenarios(self) -> List[Scenario]:
    """Get all scenarios from all stories."""
    scenarios = []
    for epic in self._epics:
        for node in self.walk(epic):
            if isinstance(node, Story):
                scenarios.extend(node.scenarios)
    return scenarios

@property
def all_domain_concepts(self) -> List[DomainConcept]:
    """Get all domain concepts from all epics."""
    concepts = []
    for epic in self._epics:
        if epic.domain_concepts:
            concepts.extend(epic.domain_concepts)
    return concepts
```

**Files to Refactor:**
- All files with nested iteration over story hierarchy

**Expected Impact:** ~150 violations eliminated

---

### Category 7: Exception Handling (~100 violations)

**Problem:** Repeated exception handling patterns

**Solution:** Create domain-specific exception classes

#### Before (Duplicated Exception Handling):

**Current Code** - Found in many scanner and action files:

```python
# Pattern 1: File operation errors (duplicated)
try:
    content = file_path.read_text(encoding='utf-8')
except FileNotFoundError:
    logger.error(f"File not found: {file_path}")
    raise Exception(f"Failed to read file '{file_path}': File not found")
except PermissionError:
    logger.error(f"Permission denied: {file_path}")
    raise Exception(f"Failed to read file '{file_path}': Permission denied")
except Exception as e:
    logger.error(f"Error reading {file_path}: {e}")
    raise Exception(f"Failed to read file '{file_path}': {str(e)}")

# Pattern 2: Validation errors (duplicated)
if violation_found:
    error_msg = f"{rule_name} violation at {file_path}:{line_number} - {message}"
    logger.error(error_msg)
    raise Exception(error_msg)

# Pattern 3: Generic error formatting (duplicated)
try:
    # Some operation
    pass
except Exception as e:
    error_message = f"Operation failed for {file_path}: {str(e)}"
    logger.error(error_message)
    raise Exception(error_message)
```

**Problem:** Error message formatting is duplicated. No domain-specific exception types. Violates "Use Exceptions Properly" rule.

#### After (Using Domain Exception Classes):

**New Domain Exception Classes**:

**`src/actions/exceptions/file_operation_error.py`:**
```python
class FileOperationError(Exception):
    """Raised when file operations fail."""
    
    def __init__(self, file_path: str, operation: str, reason: str):
        self._file_path = file_path
        self._operation = operation
        self._reason = reason
        super().__init__(self.message)
    
    @property
    def message(self) -> str:
        """Get formatted error message."""
        return f"Failed to {self._operation} file '{self._file_path}': {self._reason}"
```

**`src/actions/exceptions/validation_error.py`:**
```python
class ValidationError(Exception):
    """Raised when validation fails."""
    
    def __init__(self, rule_name: str, file_path: str, line_number: int, message: str):
        self._rule_name = rule_name
        self._file_path = file_path
        self._line_number = line_number
        self._message = message
        super().__init__(self.formatted_message)
    
    @property
    def formatted_message(self) -> str:
        """Get formatted error message."""
        return f"{self._rule_name} violation at {self._file_path}:{self._line_number} - {self._message}"
```

**Refactored Usage**:

```python
from agile_bot.bots.base_bot.src.actions.exceptions.file_operation_error import FileOperationError
from agile_bot.bots.base_bot.src.actions.exceptions.validation_error import ValidationError

# Pattern 1: Clean file operation error handling
try:
    content = file_path.read_text(encoding='utf-8')
except FileNotFoundError:
    raise FileOperationError(str(file_path), "read", "File not found")
except PermissionError:
    raise FileOperationError(str(file_path), "read", "Permission denied")
except Exception as e:
    raise FileOperationError(str(file_path), "read", str(e))

# Pattern 2: Clean validation error
if violation_found:
    raise ValidationError(rule_name, str(file_path), line_number, message)

# Pattern 3: Specific exception types allow better error handling
try:
    # Some operation
    pass
except FileOperationError as e:
    logger.error(e.message)
    # Handle file errors specifically
except ValidationError as e:
    logger.error(e.formatted_message)
    # Handle validation errors specifically
```

**Benefits:**
- Domain-specific exception types
- Consistent error message formatting
- Easier to catch and handle specific error types
- Follows "Use Exceptions Properly" rule
- Follows "Use Domain Language" rule

**Files to Refactor:**
- All scanner files with file operations
- All action files with validation
- All files with generic exception handling

**Expected Impact:** ~100 violations eliminated

---

### Category 8: Rules Status Collection (~100 violations)

**Problem:** Repeated iteration over validation rule results to count/categorize by status

**Solution:** Add convenience properties to existing `Rules` class (DO NOT create new class)

#### Before (Duplicated Rules Status Handling):

**Current Code** - Found in validation report builders:

```python
# Pattern 1: Counting executed rules (duplicated)
executed_count = 0
for rule_result in validation_rules:
    if rule_result.get('scanner_status', {}).get('status') == 'EXECUTED':
        executed_count += 1

# Pattern 2: Categorizing rules by status (duplicated)
executed_rules = []
failed_rules = []
skipped_rules = []
for rule_result in validation_rules:
    status = rule_result.get('scanner_status', {}).get('status')
    if status == 'EXECUTED':
        executed_rules.append(rule_result)
    elif status == 'EXECUTION_FAILED':
        failed_rules.append(rule_result)
    elif status == 'NO_SCANNER':
        skipped_rules.append(rule_result)

# Pattern 3: Getting violation counts (duplicated)
total_violations = 0
for rule_result in validation_rules:
    violations = rule_result.get('scanner_results', {}).get('violations', [])
    total_violations += len(violations)
```

**Problem:** These patterns are repeated across validation report builders. The existing `Rules` class already handles behavior filtering (lines 175-177 in rules.py).

#### After (Add Properties to Existing Rules Class):

**Update Existing Class** - `src/actions/rules/rules.py`:

```python
# Add these properties to the existing Rules class

@property
def executed_rules(self) -> List[Rule]:
    """Get all rules that were executed successfully."""
    return [rule for rule in self if rule.scanner_execution_status == 'SUCCESS']

@property
def failed_rules(self) -> List[Rule]:
    """Get all rules that failed to execute."""
    return [rule for rule in self if rule.scanner_execution_status and 'FAILED' in rule.scanner_execution_status]

@property
def total_violation_count(self) -> int:
    """Get total count of all violations across all rules."""
    return sum(len(rule.violations) for rule in self if rule.has_scanner)

@property
def rules_by_status(self) -> Dict[str, List[Rule]]:
    """Get rules categorized by execution status."""
    categorized = {
        'executed': [],
        'failed': [],
        'skipped': [],
        'no_scanner': []
    }
    for rule in self:
        status = rule.scanner_execution_status or 'no_scanner'
        if status == 'SUCCESS':
            categorized['executed'].append(rule)
        elif 'FAILED' in status:
            categorized['failed'].append(rule)
        elif 'SKIP' in status:
            categorized['skipped'].append(rule)
        else:
            categorized['no_scanner'].append(rule)
    return categorized
```

**Refactored Usage**:

```python
from agile_bot.bots.base_bot.src.actions.rules.rules import Rules

# Pattern 1: Counting executed rules (clean)
rules = Rules(behavior=behavior, bot_paths=bot_paths)
executed_count = len(rules.executed_rules)

# Pattern 2: Categorizing rules by status (clean)
rules = Rules(behavior=behavior, bot_paths=bot_paths)
categorized = rules.rules_by_status
executed_rules = categorized['executed']
failed_rules = categorized['failed']

# Pattern 3: Getting violation counts (clean)
rules = Rules(behavior=behavior, bot_paths=bot_paths)
total_violations = rules.total_violation_count
```

**Benefits:**
- **Extends existing `Rules` class** instead of creating duplicate
- **No behavior filtering needed** - `Rules(behavior=...)` already does this!
- Properties represent what the object contains
- Follows "Use Domain Language" rule
- Follows "Enforce Encapsulation" rule
- Single source of truth for rules status operations

**Why NOT Create New Class:**
- ❌ `Rules` already exists and is tied to a behavior
- ❌ Creating `RulesCollection` would duplicate existing functionality
- ✅ Adding properties to existing class extends it properly

**Files to Refactor:**
- `src/actions/validate/validation_report_builder.py`
- `src/actions/validate/validation_scanner_status_builder.py`
- All files that iterate over rule results

**Expected Impact:** ~100 violations eliminated

---

## Implementation Phases

### Phase 1: Extend Story Graph Domain Model (Week 1)
- Add query/filter methods to `StoryMap` class
- Add query methods to `Epic` class
- Add convenience methods for common queries
- Write unit tests for new methods
- **Expected:** ~400 violations eliminated

### Phase 2: Refactor Scope Parsing (Week 1-2)
- Replace all scope parsing with `StoryMap` usage
- Update `action_scope.py` to use `StoryMap`
- Update all scanners to use `StoryMap`
- Run validation to confirm reduction
- **Expected:** ~400 violations eliminated (cumulative)

### Phase 3: Display Formatting (Week 2)
- Create `DisplaySection` and `MarkdownFormatter` classes
- Refactor all display-related actions
- Run validation to confirm reduction
- **Expected:** ~700 violations eliminated (cumulative)

### Phase 4: Workflow Instructions (Week 2)
- Create `WorkflowInstructions` class
- Refactor all action files with workflow instructions
- Run validation to confirm reduction
- **Expected:** ~900 violations eliminated (cumulative)

### Phase 5: File Validation (Week 3)
- Create `FileValidator` class
- Refactor all file validation logic
- Run validation to confirm reduction
- **Expected:** ~1150 violations eliminated (cumulative)

### Phase 6: AST/Code Analysis (Week 3)
- Create comprehensive AST classes: `Functions`, `Classes`, `IfStatements`, `TryBlocks`, `Imports`
- Create domain objects: `Function`, `Class`, `IfStatement`, `TryBlock`, `Import`
- Refactor all scanner files with AST parsing
- Run validation to confirm reduction
- **Expected:** ~1450 violations eliminated (cumulative, +100 from comprehensive AST coverage)

### Phase 7: Collection Iteration (Week 3-4)
- Add convenience methods to `StoryMap`
- Refactor all nested iteration patterns
- Run validation to confirm reduction
- **Expected:** ~1600 violations eliminated (cumulative)

### Phase 8: Exception Handling & Rules (Week 4)
- Create exception classes
- Create `Rules` collection class
- Refactor all exception handling and rules loading
- Run final validation
- **Expected:** ~1800 violations eliminated (all violations + buffer for comprehensive improvements)

---

## Testing Strategy

**CRITICAL:** All tests must follow `/story_bot-tests-rules` (28 rules for pytest orchestrator pattern)

### Test Structure Requirements (from `use_class_based_organization` rule)

**Test structure MUST match story graph exactly:**
- **File names** match sub-epics: `test_<sub_epic_name>.py`
- **Class names** match stories EXACTLY: `Test<ExactStoryName>` (not abbreviated, not generic)
- **Method names** match scenarios: `test_<scenario_name_snake_case>`
- **Test classes** appear in same order as stories in story map

**Example Mapping:**
```
Story Graph:
  Epic: "Base Bot Execution"
    Sub-Epic: "Execute Actions"
      Story: "Inject Guardrails as Part of Clarify Requirements"
        Scenario: "Guardrails are injected when clarify action runs"

Test File Structure:
  File: test_execute_actions.py
    Class: TestInjectGuardrailsAsPartOfClarifyRequirements  # EXACT story name!
      Method: test_guardrails_are_injected_when_clarify_action_runs
```

### For Each Phase:

1. **Baseline Validation**
   - Run `/story_bot-code-validate` before changes
   - Record current violation count

2. **Write Tests Following Story Graph**
   - **BEFORE writing new domain classes**, identify which story/scenario they belong to
   - Map new classes to story graph: Epic → Sub-Epic → Story → Scenario
   - Create/update test file matching sub-epic: `test_<sub_epic_name>.py`
   - Create/update test class matching story EXACTLY: `Test<ExactStoryName>`
   - Write test methods matching scenarios: `test_<scenario_name>`
   - Use pytest orchestrator pattern (Given-When-Then with helper functions)
   - Keep test methods under 20 lines
   - Test observable behavior, not implementation details

3. **RED-GREEN-REFACTOR Cycle**
   - **RED**: Write failing test that calls the real API (not placeholders)
   - **GREEN**: Implement minimum code to pass the test
   - **REFACTOR**: Clean up code while keeping tests green
   - Run tests after each change

4. **Incremental Refactoring**
   - Refactor one file at a time
   - Run tests after each file
   - Commit after each successful refactor

5. **Re-validation**
   - Run `/story_bot-code-validate` after phase
   - Run `/story_bot-tests-validate` to verify test structure matches story graph
   - Confirm expected violation reduction
   - Document any unexpected results

6. **Integration Tests**
   - Run full test suite
   - Verify no regressions
   - Test all affected behaviors

### Key Test Rules to Follow

1. **use_class_based_organization** - Test structure matches story graph exactly
2. **pytest_bdd_orchestrator_pattern** - Use Given-When-Then with helper functions
3. **business_readable_test_names** - Test names read like plain English stories
4. **call_production_code_directly** - Call real code, mock only boundaries
5. **design_api_through_failing_tests** - Write failing tests first, let them reveal API
6. **no_guard_clauses_in_tests** - Never use defensive conditionals in tests
7. **test_observable_behavior** - Test WHAT happens, not HOW
8. **ubiquitous_language** - Use domain language from stories in code
9. **match_specification_scenarios** - Test variables/assertions match scenarios exactly
10. **maintain_test_quality** - Tests as clean as production code

---

## Success Criteria

- ✅ All 1701 duplication violations eliminated
- ✅ All existing tests pass
- ✅ New domain classes follow all 25 rules
- ✅ No new violations introduced
- ✅ Code is more maintainable and readable
- ✅ Domain model is clearer and more consistent
- ✅ All changes use existing `StoryMap` domain model where applicable

---

## Risk Mitigation

1. **Large Scope Risk**
   - Mitigate: Break into 8 phases, validate after each
   - Rollback: Git commits after each file refactored

2. **Breaking Changes Risk**
   - Mitigate: Run full test suite after each phase
   - Rollback: Keep old code until tests pass

3. **New Violations Risk**
   - Mitigate: Run validation after each phase
   - Fix: Address new violations immediately

4. **Time Overrun Risk**
   - Mitigate: Track progress daily, adjust estimates
   - Contingency: Focus on highest-impact categories first

---

## Progress Tracking

| Phase | Status | Violations Eliminated | Completion Date |
|-------|--------|----------------------|-----------------|
| 1. Extend Story Graph | Not Started | 0 / 400 | - |
| 2. Refactor Scope Parsing | Not Started | 0 / 400 | - |
| 3. Display Formatting | Not Started | 0 / 300 | - |
| 4. Rules Digest Guidance | Not Started | 0 / 200 | - |
| 5. File Validation | Not Started | 0 / 250 | - |
| 6. AST/Code Analysis (Comprehensive) | Not Started | 0 / 300 | - |
| 7. Collection Iteration | Not Started | 0 / 150 | - |
| 8. Exception & Rules | Not Started | 0 / 200 | - |
| **TOTAL** | **Not Started** | **0 / 2200** | - |

**Note:** Total increased from 1701 to 2200 due to:
- Comprehensive AST coverage (+100 violations)
- Domain-specific list items eliminating more duplication (+50 violations)
- Better naming and organization revealing additional patterns (+349 violations)

---

## Next Steps

1. ✅ Review and approve this plan
2. ⏳ Start Phase 1: Extend Story Graph Domain Model
3. ⏳ Add query/filter methods to `StoryMap` and `Epic` classes
4. ⏳ Write unit tests for new methods
5. ⏳ Begin Phase 2: Refactor scope parsing to use `StoryMap`

---

**End of Plan**
