# Validation Report - Design

**Generated:** 2025-12-29 12:54:51
**Project:** base_bot
**Behavior:** design
**Action:** validate

## Summary

Validated content against **9 validation rules**.

## Content Validated

- **Clarification:** `clarification.json`
- **Rendered Outputs:**
  - `story-graph.json`

## Scanner Execution Status

### 🟩 Overall Status: ALL CLEAN

| Status | Count | Description |
|--------|-------|-------------|
| [i] No Scanner | 9 | Rule has no scanner configured |

**Total Rules:** 9
- **Rules with Scanners:** 0
  - 🟩 **Executed Successfully:** 0
- [i] **Rules without Scanners:** 9

### <span style="color: gray;">[i] Rules Without Scanners</span>

- <span style="color: gray;">[i]</span> **[Apply Exhaustive Decomposition](#apply-exhaustive-decomposition)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Preserve Module From Domain](#preserve-module-from-domain)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Assign Base Class Responsibilities](#assign-base-class-responsibilities)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Assign Helper Ownership](#assign-helper-ownership)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Place At Lowest Level](#place-at-lowest-level)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Encapsulate Through Properties](#encapsulate-through-properties)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Hide Calculation Timing](#hide-calculation-timing)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Object Creation And Selection](#object-creation-and-selection)** - No scanner configured
- <span style="color: gray;">[i]</span> **[Ensure Unidirectional Ownership](#ensure-unidirectional-ownership)** - No scanner configured

## Validation Rules Checked

### [i] Rule: <span id="apply-exhaustive-decomposition">Apply Exhaustive Decomposition</span> - NO SCANNER
**Description:** Apply exhaustive logic decomposition. Cover all validation paths, calculation branches, and edge cases explicitly. Use inheritance for variations, not enumeration. Example: Order -> Creates, Validates, Calculates total, Submits (complete flow); ShippingCalculator base, InternationalShippingCalculator : ShippingCalculator (inheritance for variations).
**Scanner:** Not configured

### [i] Rule: <span id="assign-base-class-responsibilities">Assign Base Class Responsibilities</span> - NO SCANNER
**Description:** When classes share responsibilities and collaborators, lift them into a base class. Use ': BaseClass' notation for inheritance. Reference base type in relationships instead of enumerating subtypes. Example: Scanner base with Scans/Reports; ImportPlacementScanner : Scanner adds Validates import ordering.
**Scanner:** Not configured

### [i] Rule: <span id="assign-helper-ownership">Assign Helper Ownership</span> - NO SCANNER
**Description:** Decompose large domain objects into focused assistants to maintain single responsibility and smaller surface area. Use Doer patterns (Helper, Calculator, Analyzer) when a concept has too many distinct responsibility areas. Assistants must be subordinate to and owned by the domain concept they serve. Example: Portfolio delegates to RiskAnalyzer, RebalanceCalculator, PerformanceAnalyzer.
**Scanner:** Not configured

### [i] Rule: <span id="encapsulate-through-properties">Encapsulate Through Properties</span> - NO SCANNER
**Description:** Objects internalize their own state and functionality, accessed through properties. Avoid methods that receive external state the object should already own. Example: LineItem owns Product/Quantity, so Calculates extended price: Money, Discount (not Money, Product, Quantity, Discount).
**Scanner:** Not configured

### [i] Rule: <span id="ensure-unidirectional-ownership">Ensure Unidirectional Ownership</span> - NO SCANNER
**Description:** Ownership relationships must be unidirectional. If A owns B, B should not own A. References can be bidirectional, but ownership is one-way. Example: File Has blocks: Block (ownership down); Block References file: File (reference up).
**Scanner:** Not configured

### [i] Rule: <span id="hide-calculation-timing">Hide Calculation Timing</span> - NO SCANNER
**Description:** Use properties where resource-oriented access makes more sense than explicit operations. Properties hide calculation timing. Explicit operations when action is meaningful. Example: Get total value: Money (property); Submits for fulfillment: FulfillmentRequest (operation).
**Scanner:** Not configured

### [i] Rule: <span id="object-creation-and-selection">Object Creation And Selection</span> - NO SCANNER
**Description:** Objects create themselves from their context. Factory/registry selects which implementation to use, but creation logic belongs to the object being created. Example: Order Creates from shopping cart: Order, Cart, Customer; ScannerRegistry Finds scanner for rule: Scanner, Rule.
**Scanner:** Not configured

### [i] Rule: <span id="place-at-lowest-level">Place At Lowest Level</span> - NO SCANNER
**Description:** Place state and responsibilities at the lowest-level object that owns them. Delegate to lowest-level objects, chain dependencies through hierarchy. Example: Holding owns Symbol/Quantity and Calculates market value; Portfolio Has holdings and delegates to them.
**Scanner:** Not configured

### [i] Rule: <span id="preserve-module-from-domain">Preserve Module From Domain</span> - NO SCANNER
**Description:** Preserve module field from domain phase and verify accuracy. Module MUST match source code folder structure using dot notation.
**Scanner:** Not configured

## Violations Found

🟩 **No violations found.** All rules passed validation.

## Validation Instructions

The following validation steps were performed:

1. ## Step 1: Scanner Violation Review
2. 
3. {{scanner_output}}
4. 
5. Carefully review all scanner-reported violations as follows:
6. 1. For each violation message, locate the corresponding element in the knowledge graph.
7. 2. Open the relevant rule file and read all DO and DON'T examples thoroughly.
8. 3. Decide if the violation is **Valid** (truly a rule breach per examples) or a **False Positive** (explain why if so).
9. 4. Determine the **Root Cause** (e.g., 'incorrect concept naming', 'missing actor', etc.).
10. 5. Assign a **Theme** grouping based on the type of issue (e.g., 'noun-only naming', 'incomplete acceptance criteria').
*... and 49 more instructions*

## Report Location

This report was automatically generated and saved to:
`C:\dev\augmented-teams\agile_bot\bots\base_bot\docs\stories\reports\design-validation-report-2025-12-29_12-54-51.md`

