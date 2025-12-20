# Domain Modeling Rules Analysis

## Analysis of Domain Modeling Rules That Could Have Helped

Based on the domain model evolution, here's what domain modeling rules existed and what was missing.

**Focus:** Domain modeling rules only (resource-oriented design, domain language, domain grouping, dependency chaining, delegation, encapsulation, helper ownership, etc.)

---

## Existing Domain Modeling Rules That Helped (But Could Be Improved)

### 1. `use_resource_oriented_design.json` ✅
**Status:** Exists in both code and shape rules  
**Domain Focus:** Prevents manager/doer patterns, encourages resource-oriented classes  
**How it helped:** Caught manager/doer patterns  
**Gap:** Doesn't specifically address:
- Helper ownership (which resource owns which helper)
- Base class responsibilities
- Factory pattern for object creation

**Recommendation:** Enhance to include helper ownership guidance

### 2. `delegate_to_lowest_level.json` ✅
**Status:** Exists in both code and shape rules  
**Domain Focus:** Ensures delegation to collection classes, proper responsibility placement  
**How it helped:** Encouraged delegation to collection classes  
**Gap:** Doesn't address:
- Over-encapsulation (parent navigating to child to sub-child vs wrapping)
- Helper placement (which resource owns helpers)
- Avoiding unnecessary wrapping layers

**Recommendation:** Add guidance about avoiding over-encapsulation

### 3. `use_domain_language.json` ✅
**Status:** Exists in both code and shape rules  
**Domain Focus:** Ensures domain-specific language, not generic terms  
**How it helped:** Prevented generic terms  
**Gap:** Doesn't address:
- Self-creating objects (objects that know how to create themselves)
- Factory methods vs direct instantiation

**Recommendation:** Add guidance about self-creating domain objects

### 4. `chain_dependencies_properly.json` ✅
**Status:** Exists in both code and shape rules  
**Domain Focus:** Ensures proper dependency injection, dependency chaining  
**How it helped:** Ensured proper dependency injection  
**Gap:** Doesn't address:
- Bidirectional relationships and their implications
- Lowest component for state/behavior placement
- Aggregation vs direct ownership

**Recommendation:** Add guidance about relationship directionality

### 5. `group_by_domain.json` ✅
**Status:** Exists in both code and shape rules  
**Domain Focus:** Organizes by domain area, not technical layers  
**How it helped:** Organized by domain  
**Gap:** Doesn't address:
- Base class responsibilities
- Inheritance hierarchies in domain models

**Recommendation:** Add guidance about base classes and inheritance

### 6. `encapsulate_through_properties.json` ✅ (Shape only)
**Status:** Exists in shape rules  
**Domain Focus:** Encapsulates state through properties, hides internal representation  
**How it helped:** Encouraged property-based encapsulation  
**Gap:** Doesn't address:
- Helper ownership through properties
- Base class property responsibilities

**Recommendation:** Add guidance about helper properties

---

## Missing Rules That Would Have Helped

### 1. **Self-Creating Objects** ❌
**Issue:** Original model had Rule creating Violations, but Violation should create itself  
**Missing Rule:** Objects should know how to create themselves from their context

**What it should cover:**
- Objects create themselves from rule/context, not delegated to other objects
- Factory methods belong to the object being created, not external factories
- Self-creation methods show what context/parameters are needed

**Example:**
```
Violation
    Creates from rule and context: Rule  ✅ (self-creating)
    
NOT:
Rule
    Creates violation: Violation  ❌ (delegated creation)
```

---

### 2. **Helper Ownership** ❌
**Issue:** Original model had helpers floating around without clear ownership  
**Missing Rule:** Helpers must be owned by the resource that uses them

**What it should cover:**
- Helpers are properties of owning resources
- File owns BlockExtractor (File uses it to extract blocks)
- Block owns SimilarityCalculator (Block uses it for similarity)
- Base Scanner owns common helpers (all scanners use them)
- Show ownership with "Has X: HelperType" notation

**Example:**
```
File
    Has blocks: Block,BlockExtractor  ✅ (File owns BlockExtractor)
    
Block
    Has similarity: Block,SimilarityCalculator  ✅ (Block owns SimilarityCalculator)
    
NOT:
BlockExtractor (standalone)  ❌ (no owner)
```

---

### 3. **Violation/Aggregate Placement** ❌
**Issue:** Original model had violations on multiple levels (Rule, File, Scope, Block)  
**Missing Rule:** State/aggregates belong at the lowest component, with references at higher levels

**What it should cover:**
- Identify lowest component that should own state/behavior
- Aggregates (like violations) belong at lowest level (Block)
- Higher levels (Scan) reference/collect, don't duplicate
- Navigation path: Block → File → Scope (not direct ownership)
- Avoid bidirectional ownership (if A owns B, B shouldn't own A)

**Example:**
```
Block
    Has violations: Violation  ✅ (lowest level)
    
Scan
    Has violations: Violation  ✅ (collects from blocks)
    
NOT:
Scope
    Has violations: Violation  ❌ (should navigate Block → File → Scope)
```

---

### 4. **Factory Pattern for Object Selection** ❌
**Issue:** Original model hardcoded scanner selection  
**Missing Rule:** Use factory methods for selecting/creating objects based on context

**What it should cover:**
- Factory methods select appropriate objects based on rule/context
- Factory belongs to the registry/selector, not the objects being created
- Avoid hardcoding all possible objects in parent
- Factory pattern: "Selects X by Y: Registry, Y"

**Example:**
```
Scanner Orchestrator
    Selects scanner helpers by rule: ScannerRegistry, Rule, Scanner  ✅ (factory)
    
NOT:
Scan
    Has scanner: ImportPlacementScanner, BadCommentsScanner, ...  ❌ (hardcoded)
```

---

### 5. **Base Class Responsibilities** ❌
**Issue:** Original model didn't have base Scanner with common responsibilities  
**Missing Rule:** Base classes should own responsibilities shared by all subclasses

**What it should cover:**
- Base classes own common helper responsibilities
- Subclasses extend base, inherit common responsibilities
- Show inheritance with ": BaseClass" notation
- Common helpers go in base class, not duplicated in subclasses

**Example:**
```
Scanner
    Checks file naming: File,FileNamingChecker  ✅ (base class)
    Checks class naming: Block,ClassNamingChecker
    Analyzes code structure: Block,CodeStructureAnalyzer
    
ImportPlacementScanner : Scanner  ✅ (extends base)
    Scans import placement: Block
```

---

### 6. **Avoid Over-Encapsulation** ❌
**Issue:** User wanted parent → child → sub-child navigation, not wrapping  
**Missing Rule:** Avoid unnecessary wrapping layers; navigate through ownership chain

**What it should cover:**
- Parent navigates to child to sub-child (A → B → C)
- Don't create wrapper methods that just delegate
- Don't add unnecessary abstraction layers
- Direct navigation preferred over wrapping

**Example:**
```
Scope
    Has files: File  ✅
    (navigate: Scope → File → Block → Violation)
    
NOT:
Scope
    Get violations: Violation  ❌ (wrapping, should navigate)
```

---

### 7. **Relationship Bidirectionality** ❌
**Issue:** User asked about bidirectional relationships and their implications  
**Missing Rule:** Relationships should be unidirectional; avoid circular ownership

**What it should cover:**
- If A references B, B shouldn't reference A (unless necessary)
- Ownership is one-way: owner → owned
- References can be bidirectional, but ownership is not
- Lowest component owns state; higher levels reference

**Example:**
```
Violation
    References rule: Rule  ✅ (reference, not ownership)
    References block: Block  ✅ (reference, not ownership)
    References scan: Scan  ✅ (reference, not ownership)
    
NOT:
Rule
    Has violations: Violation  ❌ (violations owned by Block/Scan)
```

---

## Recommended New Domain Modeling Rules

### Rule 1: `ensure_self_creating_objects.json` (NEW)
**Priority:** HIGH  
**Focus:** Domain objects should know how to create themselves

**Description:**
"CRITICAL: Domain objects must know how to create themselves from their context. Objects should have creation methods that show what context/parameters they need, rather than delegating creation to other objects."

**Examples:**
- ✅ Violation "Creates from rule and context: Rule"
- ❌ Rule "Creates violation: Violation"

---

### Rule 2: `assign_helper_ownership.json` (NEW)
**Priority:** HIGH  
**Focus:** Helpers must be owned by the resource that uses them

**Description:**
"CRITICAL: Helper objects must be owned by the resource that uses them. Show ownership with 'Has X: HelperType' notation. Base classes own helpers used by all subclasses. Resources own helpers they directly use."

**Examples:**
- ✅ File "Has blocks: Block,BlockExtractor" (File owns BlockExtractor)
- ✅ Block "Has similarity: Block,SimilarityCalculator" (Block owns SimilarityCalculator)
- ✅ Scanner "Checks file naming: File,FileNamingChecker" (base Scanner owns common helpers)
- ❌ BlockExtractor (standalone, no owner)

---

### Rule 3: `place_state_at_lowest_component.json` (NEW)
**Priority:** HIGH  
**Focus:** State/aggregates belong at lowest component; higher levels reference/collect and navigate through ownership chain (no wrapper layers)

**Description:**
"CRITICAL: State and aggregates must be placed at the lowest component that logically owns them. Higher-level objects reference or collect (never own) and should navigate the ownership chain (Parent → Child → Sub-child) instead of adding wrapper methods. Identify the lowest component through the question: 'What is the smallest unit that should have this state?'"

**Examples:**
- ✅ Block "Has violations: Violation" (lowest level)
- ✅ Scan "Has violations: Violation" (collects from blocks)
- ❌ Scope "Has violations: Violation" (should navigate Block → File → Scope)
- ❌ Rule "Has violations: Violation" (violations owned by Block/Scan)

---

### Rule 4: `use_factory_for_object_selection.json` (NEW)
**Priority:** MEDIUM  
**Focus:** Use factory methods for selecting objects based on context

**Description:**
"CRITICAL: When selecting objects based on context (rule, type, etc.), use factory methods rather than hardcoding all possibilities. Factory methods belong to registry/selector objects, not the objects being created."

**Examples:**
- ✅ Scanner Orchestrator "Selects scanner helpers by rule: ScannerRegistry, Rule, Scanner"
- ✅ ScannerRegistry "Finds scanner by rule: Rule"
- ❌ Scan "Has scanner: ImportPlacementScanner, BadCommentsScanner, ..." (hardcoded)

---

### Rule 5: `assign_base_class_responsibilities.json` (NEW)
**Priority:** MEDIUM  
**Focus:** Base classes own responsibilities shared by all subclasses

**Description:**
"CRITICAL: Base classes must own responsibilities and helpers that are shared by all subclasses. Subclasses extend the base class and inherit common responsibilities. Show inheritance with ': BaseClass' notation."

**Examples:**
- ✅ Scanner (base) "Checks file naming: File,FileNamingChecker"
- ✅ ImportPlacementScanner : Scanner (extends base)
- ❌ Each scanner duplicating common responsibilities

---

### Rule 6: `ensure_unidirectional_ownership.json` (NEW)
**Priority:** MEDIUM  
**Focus:** Ownership is unidirectional; avoid circular ownership

**Description:**
"CRITICAL: Ownership relationships must be unidirectional. If A owns B, B should not own A. References can be bidirectional, but ownership is one-way. Lowest component owns state; higher levels reference."

**Examples:**
- ✅ Violation "References rule: Rule" (reference, not ownership)
- ✅ Violation "References block: Block" (reference, not ownership)
- ❌ Rule "Has violations: Violation" (violations owned by Block/Scan, not Rule)

---

## Summary: Domain Modeling Rules That Would Have Helped

### Existing Domain Modeling Rules (Enhanced):
1. ✅ `use_resource_oriented_design.json` - Add helper ownership guidance
2. ✅ `delegate_to_lowest_level.json` - Add over-encapsulation guidance
3. ✅ `use_domain_language.json` - Add self-creating objects guidance
4. ✅ `chain_dependencies_properly.json` - Add bidirectional relationship guidance
5. ✅ `group_by_domain.json` - Add base class guidance
6. ✅ `encapsulate_through_properties.json` - Add helper property guidance

### New Domain Modeling Rules Needed:
1. ❌ `ensure_self_creating_objects.json` - HIGH priority (domain object creation)
2. ❌ `assign_helper_ownership.json` - HIGH priority (domain helper ownership)
3. ❌ `place_state_at_lowest_component.json` - HIGH priority (domain state placement)
4. ❌ `use_factory_for_object_selection.json` - MEDIUM priority (domain factory pattern)
5. ❌ `assign_base_class_responsibilities.json` - MEDIUM priority (domain inheritance)
6. ❌ `ensure_unidirectional_ownership.json` - MEDIUM priority (domain relationships)

---

## Implementation Priority for Domain Modeling Rules

**Phase 1 (Critical - Would have prevented all major domain modeling issues):**
1. `assign_helper_ownership.json` - Would have caught helpers without domain owners
2. `place_state_at_lowest_component.json` - Would have caught domain state on wrong levels
3. `ensure_self_creating_objects.json` - Would have caught delegated domain object creation

**Phase 2 (Important - Would have improved domain design):**
4. `use_factory_for_object_selection.json` - Would have caught hardcoded domain object selections
5. `assign_base_class_responsibilities.json` - Would have caught missing domain base classes

**Phase 3 (Nice to have - Domain modeling refinements):**
6. `ensure_unidirectional_ownership.json` - Would have caught circular domain ownership

