# Clean Code Violations Report

**File:** {{file}}  
**Language:** {{language}}  
**Generated:** {{generated_date}}

## Summary

- **Critical Violations:** {{summary.critical}}
- **Important Violations:** {{summary.important}}
- **Suggested Improvements:** {{summary.suggested}}
- **Total Violations:** {{summary.total}}

## Code Structure

- **Total Lines:** {{code_structure.total_lines}}
- **Functions:** {{code_structure.functions}}
- **Classes:** {{code_structure.classes}}

## Violations by Severity

### Critical Violations

{{#each violations}}
{{#if severity == "critical"}}
- **Line {{line}}** ({{function}}{{#if class}} in {{class}}{{/if}}): {{issue}}
  - **Principle:** {{principle}}
  - **Suggestion:** {{suggestion}}
  ```{{language}}
  {{code_snippet}}
  ```

{{/if}}
{{/each}}

### Important Violations

{{#each violations}}
{{#if severity == "important"}}
- **Line {{line}}** ({{function}}{{#if class}} in {{class}}{{/if}}): {{issue}}
  - **Principle:** {{principle}}
  - **Suggestion:** {{suggestion}}
  ```{{language}}
  {{code_snippet}}
  ```

{{/if}}
{{/each}}

### Suggested Improvements

{{#each violations}}
{{#if severity == "suggested"}}
- **Line {{line}}** ({{function}}{{#if class}} in {{class}}{{/if}}): {{issue}}
  - **Principle:** {{principle}}
  - **Suggestion:** {{suggestion}}

{{/if}}
{{/each}}

## Violations by Principle

{{#group violations by principle}}
### {{principle}}

{{#each items}}
- **Line {{line}}** ({{function}}{{#if class}} in {{class}}{{/if}}): {{issue}}
  - **Severity:** {{severity}}
  - **Suggestion:** {{suggestion}}

{{/each}}
{{/group}}

## Code Quality Score

**Score:** {{quality_score}}/100

**Breakdown:**
- Structure: {{structure_score}}/25
- Naming: {{naming_score}}/25
- Functions: {{functions_score}}/25
- Classes: {{classes_score}}/25

## Recommendations

{{recommendations}}

## Heuristics Summary

{{#if heuristics.deep_nesting.length}}
### Deep Nesting
{{heuristics.deep_nesting.length}} instances found

{{/if}}
{{#if heuristics.magic_numbers.length}}
### Magic Numbers
{{heuristics.magic_numbers.length}} instances found

{{/if}}
{{#if heuristics.large_functions.length}}
### Large Functions
{{heuristics.large_functions.length}} instances found

{{/if}}
{{#if heuristics.large_classes.length}}
### Large Classes
{{heuristics.large_classes.length}} instances found

{{/if}}

## AI Analysis

{{ai_analysis}}


