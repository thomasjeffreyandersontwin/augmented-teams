# Domain Model Evolution - Scanner Validation System

This document traces the evolution of the domain model from the original version through user feedback to the final resource-oriented design.

## Original Domain Model (Initial Version)

```plaintext
DOMAIN MODEL (CRC Format) - Resource-Oriented
================================================================================

Scan
    Has violations: Violation
    Created for scope: Scope
    Performs scan on scope: Scope,Rule

Scope
    Has files: File
    Has blocks: Block

File
    Has lines: Line
    Has blocks: Block
    Parses safely: 
    Checks if test file: 
    Parses Python file: 

Line
    Belongs to file: File
    Has number: 
    Has content: 
    Extracts from AST node: 
    Extracts from position: 

Block
    Has content: 
    Has subblocks: Block
    Has similarity: Block
    Has violations: Violation
    References file: File
    Normalizes content:

Walk
    Has lines: Line
    Has similarity: Block 

Violation
    References rule: Rule
    References block: Block
    Creates from rule and context: Rule

Rule
    Defines validation: 
    Finds scanner helper: 
    Validates content: Scan,Scope
    
PatternCollection
    Contains pattern: 
    Matches text: 

ComplexityMetrics
    Calculates cognitive complexity: 
    Calculates cyclomatic complexity: 
    Calculates max nesting depth: 
    Calculates LCOM: 
    Detects function responsibilities: 
    Detects class responsibilities: 
```

**Issues with Original:**
- Violation creation delegated to Rule (not self-creating)
- No base Scanner class
- Helpers not clearly associated with owning resources
- Missing scanner helpers (GivenWhenThenHelpersScanner, etc.)
- No factory method for scanner selection
- Violations not properly scoped to Block and Scan

---

## User Feedback #1: Resource-Oriented Approach

**Feedback:**
> "You have a lot of doers, builders, and constructors in this pattern, which is not necessarily bad. But I'd like to see it have a more resource-oriented approach."
> 
> "For instance, a scanner might do a scan on a scope. That scope might be one file or many files. That scope can have blocks. Blocks can have subblocks. Walks can have similarity. Blocks can have content."
> 
> "scan could have violations. Those violations can refer to resource or resources. Can refer to blocks. Walks can have lines. Perhaps the resource can have files that have lines. You get the point. Please reorient this towards a resource-oriented approach. You can have these scanner builder whatever thingies, but they should be helpers within the actual domain object."

**Key Changes:**
- Moved helpers to be properties of owning resources
- File has BlockExtractor as helper
- Block has SimilarityCalculator, CodeStructureAnalyzer, etc. as helpers

---

## User Feedback #2: Violation Should Create Itself

**Feedback:**
> "@scanner-violations-fix-plan.txt (37-41) This one is smelly. To me, a violation should know how to create itself."
> 
> "The scanner should have the wherewithal to understand what the line was. That could go into a base_file_scanner of some kind or a base_code_scanner."

**Key Changes:**
- Violation "Creates from rule and context: Rule" - self-creating
- Base Scanner class introduced to handle common scanning logic

---

## User Feedback #3: Violation Placement - Block and Scan Only

**Feedback:**
> "Think about the bidirectionality of some of these relationships. If a violation belongs to a scan, I think you have that right. But it also references a rule, and that means that a rule can have violations. It also means that a file could have a violation. It also means that a block could have a violation. What is the lowest component that should have that violation? And try to narrow it down to not be connected to all these things directly."
> 
> "I think the lowest level is going to be a block, or many blocks, and in that way, all the violations of a file and a scope are taken by aggregating those things. And I think it's really the scope that goes and does all the aggregating."
> 
> "So I would put the actual violation against the block, I would also put it against the scope, and then I would also put it against the scan because the scan is going to be a unique instance of the activity."
> 
> "Actually, perhaps I don't think I even put it against the scope. It's really against the block and it's against the scan itself. Then everything else is something that you can interrogate from the block."

**Key Changes:**
- Violations ONLY on Block and Scan
- Scope does NOT have violations directly
- To get scope-level violations: navigate Block → File → Scope
- Violation references: Rule, Block, Scan

---

## User Feedback #4: Factory Method for Scanner Selection

**Feedback:**
> "@scanner-violations-fix-plan.txt (17-26) This is never hard code every single scanner to the scan. What you would do is have some kind of factory method that says based on what we're trying to do. Go hook up the right scanner(s)."
> 
> "You have to ask yourself: Are we going to instantiate a scan and run a scan method on it, or are you going to have a scanner that creates a scan? In this case, since this is the top of the domain, we likely have a scanner that's going to return a scan."

**Key Changes:**
- Scanner creates Scan (not Scan performing scan on itself)
- Scanner uses factory method via ScannerRegistry to select appropriate scanner helpers
- Scanner "Creates scan for scope: Scan,Scope,Rule"
- Scanner "Selects scanner helpers by rule: ScannerRegistry,Rule"

---

## User Feedback #5: Base Scanner Responsibilities

**Feedback:**
> "@scanner-violations-fix-plan.txt (140-156) The banner should have an association with all these things because that's going to be the one that's using it. So put responsibilities of these into the base scanner."
> 
> "All of the scanners need to extend the base scanner I put at the top."

**Key Changes:**
- Base Scanner class gets all helper responsibilities:
  - Checks file naming: File,FileNamingChecker
  - Checks class naming: Block,ClassNamingChecker
  - Checks method naming: Block,MethodNamingChecker
  - Analyzes code structure: Block,CodeStructureAnalyzer
  - Examines AST for violations: Block,CodeStructureAnalyzer
  - Identifies code patterns: Block,PatternCollection,CodeStructureAnalyzer
- All specific scanners extend base Scanner (shown with ": Scanner" notation)

---

## User Feedback #6: Helper Ownership and Primary Responsibilities

**Feedback:**
> "You need to show which resource object or which domain object is calling which helper. Each helper should probably be a property on one of the, either the domain object itself or the parent of the domain object. You have to choose."
> 
> "You need to put it on the owning resource. That's going to know about the calculator. Not necessarily the other way around, although it could be if it needs it to actually do the calculation."
> 
> "When thinking about assigning a helper to a resource, think about the primary responsibility or collaborator. For instance, a file has blocks, but to get to those blocks it needs to use the block extractor. See how I've done file. That's how you need to do all of these. You don't need to create extra responsibilities. Add it on to the primary responsibility in the domain."
> 
> "make sure you're not over-encapsulating the child of a resource with some of these methods. I would rather have the ultimate parent go to its child and then go to its sub-child and sub-child to get at the thing, vs a lot of unnecessary rapping, which is just boilerplate code in my opinion."

**Key Changes:**
- File "Has blocks: Block,BlockExtractor" - shows File uses BlockExtractor helper
- Block has helpers as properties: SimilarityCalculator, CodeStructureAnalyzer, ViolationReporter, ComplexityMetrics, ClassNamingChecker, MethodNamingChecker
- Avoid over-encapsulation - parent navigates to child to sub-child

---

## Final Domain Model (Current Version)

```plaintext
================================================================================
DOMAIN MODEL (CRC Format) - Resource-Oriented
================================================================================

Scanner Orchestrator
    Selects scanner helpers by rule: ScannerRegistry, Rule, Scanner
    Returns scan: Scan
   Performs scan on scope: Scan,Scope, Rule, Scanner

Scanner
    Performs scan for one rule: Scan,Scope,Rule
    Associated with rule: Rule
    Checks file naming: File,FileNamingChecker
    Checks class naming: Block,ClassNamingChecker
    Checks method naming: Block,MethodNamingChecker
    Analyzes code structure: Block,CodeStructureAnalyzer
    Examines AST for violations: Block,CodeStructureAnalyzer
    Identifies code patterns: Block,PatternCollection,CodeStructureAnalyzer

Scan
    Has violations: Violation
    Created for scope: Scope
   undergoes a scan: Scope,Rule, Scanner 

Scope
    Has files: File
    Has blocks: Block

File
    Has lines: Line
    Has blocks: Block,BlockExtractor
    Parses safely: 
    Checks if test file: 
    Parses Python file: 
    Checks file naming: FileNamingChecker 

Line
    Belongs to file: File
    Has number: 
    Has content: 
    Extracts from AST node: 
    Extracts from position: 

Block
    Has content: 
    Has subblocks: Block
    Has similarity: Block,SimilarityCalculator
    Has violations: Violation,ViolationReporter
    References file: File
    Normalizes content: 
    Analyzes structure: CodeStructureAnalyzer
    Calculates complexity: ComplexityMetrics
    Checks class naming: ClassNamingChecker
    Checks method naming: MethodNamingChecker

Walk
    Has lines: Line
    Has similarity: Block 

Violation
    References rule: Rule
    References block: Block
    References scan: Scan
    Creates from rule and context: Rule

Rule
    Defines validation: 
    Validates content: Scan,Scope
    May be violated : Scan, Violations

ScannerRegistry
    Finds scanner by rule: Rule
    Loads scanner class: 
    Registers helper: Scanner

PatternCollection
    Contains pattern: 
    Matches text: 

ComplexityMetrics
    Calculates cognitive complexity: 
    Calculates cyclomatic complexity: 
    Calculates max nesting depth: 
    Calculates LCOM: 
    Detects function responsibilities: 
    Detects class responsibilities: 

BlockExtractor
    Extracts blocks from file: File,Block
    Identifies code blocks: File,Block

SimilarityCalculator
    Calculates block similarity: Block
    Groups similar blocks: Block
    Compares block content: Block

GivenWhenThenHelpersScanner : Scanner
    Scans helper functions: Block,PatternCollection
    Validates GWT structure: Block,PatternCollection

ImportPlacementScanner : Scanner
    Scans import placement: Block
    Validates import order: Block

IntentionRevealingNamesScanner : Scanner
    Scans variable names: Block,PatternCollection
    Scans function names: Block,PatternCollection
    Validates naming clarity: Block,PatternCollection

RealImplementationsScanner : Scanner
    Scans implementation details: Block
    Validates real implementations: Block

SpecificationMatchScanner : Scanner
    Scans test specifications: Block
    Validates spec matching: Block

VerbNounScanner : Scanner
    Scans verb noun format: Block,PatternCollection
    Validates naming format: Block,PatternCollection

BadCommentsScanner : Scanner
    Scans comments: Block
    Detects bad comments: Block

ExcessiveGuardsScanner : Scanner
    Scans guard clauses: Block
    Detects excessive guards: Block

FunctionSizeScanner : Scanner
    Scans function size: Block,ComplexityMetrics
    Detects large functions: Block,ComplexityMetrics

ClassBasedOrganizationScanner : Scanner
    Scans file organization: File,Block
    Coordinates naming checks: File,Block

FileNamingChecker
    Checks file name matches sub epic: File
    Validates file naming conventions: File

ClassNamingChecker
    Checks class name matches story: Block
    Validates class naming conventions: Block

MethodNamingChecker
    Checks method name matches scenario: Block
    Validates method naming conventions: Block

CodeStructureAnalyzer
    Analyzes code structure: Block
    Examines AST for violations: Block
    Identifies code patterns: Block,PatternCollection

ViolationReporter
    Creates violation from block: Violation,Block
    Formats violation message: Violation
    Reports duplicate blocks: Violation,Block

ScannerRegistry
    Finds scanner helper by rule: Rule
    Loads scanner helper class: 
    Registers scanner helper:
```

---

## Key Design Principles Established

1. **Resource-Oriented**: Domain objects own their helpers, not separate manager/doer classes
2. **Self-Creating Violations**: Violation knows how to create itself from rule and context
3. **Violation Placement**: Violations only on Block (lowest level) and Scan (unique instance)
4. **Factory Pattern**: Scanner uses ScannerRegistry factory to select appropriate scanner helpers
5. **Base Scanner**: All scanners extend base Scanner with common responsibilities
6. **Helper Ownership**: Helpers are properties of owning resources (File owns BlockExtractor, Block owns SimilarityCalculator, etc.)
7. **Avoid Over-Encapsulation**: Parent navigates to child to sub-child rather than wrapping everything

---

## Order of Operations (Final Flow)

1. **Scanner Orchestrator** (entry point)
   - Receives a Scope and Rule(s) to validate
   - Calls "Performs scan on scope: Scan,Scope,Rule,Scanner"

2. **Scanner Orchestrator** selects scanner helpers
   - Uses ScannerRegistry to "Finds scanner by rule: Rule"
   - Gets the appropriate Scanner helper (e.g., ImportPlacementScanner, BadCommentsScanner)

3. **Scanner** (specific helper, e.g., ImportPlacementScanner)
   - "Performs scan for one rule: Scan,Scope,Rule"
   - Works with the Scope to analyze files/blocks

4. **Scope** provides resources
   - "Has files: File" and "Has blocks: Block"
   - Files are parsed and blocks are extracted

5. **File** processing
   - "Parses safely" and "Parses Python file" to parse the file
   - "Has blocks: Block,BlockExtractor" — uses BlockExtractor to extract code blocks
   - "Checks file naming: FileNamingChecker" if needed

6. **BlockExtractor** extracts blocks
   - "Extracts blocks from file: File,Block"
   - Creates Block objects from the file content

7. **Block** analysis (where violations are found)
   - Scanners analyze blocks using helpers:
     - "Analyzes structure: CodeStructureAnalyzer"
     - "Calculates complexity: ComplexityMetrics"
     - "Checks class naming: ClassNamingChecker"
     - "Checks method naming: MethodNamingChecker"
     - "Has similarity: Block,SimilarityCalculator" (for duplication)
   - PatternCollection is used for pattern matching

8. **Violation** creation
   - "Has violations: Violation,ViolationReporter" on Block
   - ViolationReporter "Creates violation from block: Violation,Block"
   - Violation "Creates from rule and context: Rule"
   - Violation references: Rule (what was violated), Block (where), Scan (which scan found it)

9. **Scan** collects violations
   - "Has violations: Violation"
   - Aggregates all violations from blocks

10. **Scanner Orchestrator** returns the Scan
    - "Returns scan: Scan" with all violations

**Summary flow**: Orchestrator → Registry finds Scanner → Scanner scans Scope → Files parsed → Blocks extracted → Blocks analyzed → Violations created on Blocks → Scan collects violations → Returns Scan

