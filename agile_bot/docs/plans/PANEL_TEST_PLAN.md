# Panel Test Plan - JavaScript Testing with Given-When-Then

## Overview

This plan mirrors the successful CLI test migration approach, but for JavaScript panel code that renders HTML from JSON CLI responses.

**Goal:** Create comprehensive JavaScript tests for panel views using Given-When-Then format with class-based organization following ALL 25 test rules.

**Critical:** Every test file MUST be validated against all 25 test rules (see Validation Checklist section).

## Current Architecture

### Panel Domain Objects (JavaScript)

```
PanelView (base)
├── BotView (orchestrator)
│   ├── BotHeaderView
│   ├── BehaviorsView
│   ├── ScopeView
│   └── InstructionsView
```

### Data Flow

```
Python CLI (JSON mode) → JavaScript Panel Views → HTML Rendering → VS Code Webview
```

Each view:
1. Receives JSON from Python CLI subprocess
2. Transforms JSON → HTML
3. Handles user interactions (clicks, expansions)
4. Sends commands back to CLI

## Test Framework Selection

**Selected:** **Node.js Test Runner** (`node:test`) with Given-When-Then helpers

**Why Node Test Runner:**
- ✅ Built-in to Node.js (no external dependencies)
- ✅ Standard, traditional unit testing approach
- ✅ Simple, straightforward API
- ✅ Native `assert` module for assertions
- ✅ Consistent with Python's unittest/pytest patterns
- ✅ No framework lock-in or configuration overhead

**HTML Parsing:** Use `jsdom` (minimal dependency) or `happy-dom` (lighter alternative)

## Test Structure - Mirroring CLI Tests

### Directory Structure

```
agile_bot/src/panel/
├── test/
│   ├── helpers/
│   │   ├── bot_view_test_helper.js       # Creates views with real CLI
│   │   ├── behaviors_view_test_helper.js
│   │   ├── scope_view_test_helper.js
│   │   ├── instructions_view_test_helper.js
│   │   └── html_assertions.js
│   ├── bot_view.test.js
│   ├── behaviors_view.test.js
│   ├── scope_view.test.js
│   ├── instructions_view.test.js
│   └── panel_view.test.js
├── bot_view.js
├── behaviors_view.js
├── scope_view.js
├── instructions_view.js
└── panel_view.js                         # Base class with CLI integration
```

### Test Helper Pattern (Mirrors Python CLI Helpers)

```javascript
// test/helpers/bot_view_test_helper.js

const assert = require('node:assert');
const { parseHTML } = require('./html_assertions');
const PanelView = require('../../panel_view'); // Base class with CLI integration

class BotViewTestHelper {
    constructor(workspaceDir, botName = 'story_bot') {
        this.webview = this.createMockWebview();
        this.extensionUri = this.createMockExtensionUri();
        this.workspaceDir = workspaceDir;
        this.botDir = `${workspaceDir}/agile_bot/bots/${botName}`;
        this.cli = null; // Real CLI instance - persistent across tests
    }
    
    // Create persistent CLI session - called once in setup
    async initializeCLI() {
        // PanelView base class has CLI spawn logic
        this.cli = await PanelView.spawnCLI(this.workspaceDir, this.botDir);
        return this.cli;
    }
    
    // Cleanup CLI - called once in teardown
    cleanupCLI() {
        if (this.cli) {
            this.cli.kill();
            this.cli = null;
        }
    }
    
    // Factory method - creates view with REAL CLI
    createBotView() {
        return new BotView(
            this.cli,              // Real CLI instance
            this.workspaceDir,
            this.botDir,
            '0.1.0',              // panelVersion
            this.webview,
            this.extensionUri
        );
    }
    
    // Assertion helpers (similar to Python helper methods)
    assertBehaviorNamePresent(html, behaviorName) {
        assert.ok(html.includes(behaviorName), 
            `Expected HTML to contain behavior name "${behaviorName}"`);
    }
    
    assertCurrentBehaviorMarked(html, behaviorName) {
        const doc = parseHTML(html);
        const behaviorElement = doc.querySelector(`[data-behavior="${behaviorName}"]`);
        assert.ok(behaviorElement, `Behavior element "${behaviorName}" not found`);
        assert.ok(behaviorElement.classList.contains('current'), 
            `Behavior "${behaviorName}" should have "current" class`);
    }
    
    assertActionPresent(html, behaviorName, actionName) {
        const doc = parseHTML(html);
        const actionElement = doc.querySelector(
            `[data-behavior="${behaviorName}"] [data-action="${actionName}"]`
        );
        assert.ok(actionElement, 
            `Action "${actionName}" not found in behavior "${behaviorName}"`);
    }
    
    createMockWebview() {
        return { postMessage: () => {} };
    }
    
    createMockExtensionUri() {
        return { fsPath: this.workspaceDir };
    }
}

module.exports = BotViewTestHelper;
```

### Given-When-Then Test Format (Class-Based with Real CLI)

```javascript
// test/behaviors_view.test.js

const { test, before, after } = require('node:test');
const assert = require('node:assert');
const BehaviorsViewTestHelper = require('./helpers/behaviors_view_test_helper');
const { parseHTML } = require('./helpers/html_assertions');

class TestBehaviorsView {
    
    constructor(workspaceDir) {
        this.helper = new BehaviorsViewTestHelper(workspaceDir, 'story_bot');
    }
    
    async setup() {
        // Initialize persistent CLI session - views will use this
        await this.helper.initializeCLI();
    }
    
    teardown() {
        // Cleanup CLI after all tests
        this.helper.cleanupCLI();
    }
    
    // Story: Display Behavior Hierarchy
    async testSingleBehaviorWithActions() {
        // GIVEN: Create BotView with real CLI
        const view = this.helper.createBotView();
        
        // WHEN: Navigate to shape and refresh (view uses its CLI internally)
        await view.navigateToBehavior('shape');
        await view.refresh();  // View gets JSON from CLI
        const html = view.getBehaviorsHTML();  // View renders HTML
        
        // THEN: HTML contains behavior and actions from real CLI
        this.helper.assertBehaviorPresent(html, 'shape');
        ['clarify', 'strategy', 'validate', 'build', 'render'].forEach(action => {
            this.helper.assertActionPresent(html, 'shape', action);
        });
    }
    
    async testMultipleBehaviors() {
        // GIVEN: BotView with real CLI
        const view = this.helper.createBotView();
        
        // WHEN: Refresh view (gets current state from CLI)
        await view.refresh();
        const html = view.getBehaviorsHTML();
        
        // THEN: HTML contains all behaviors from CLI
        ['prioritization', 'shape', 'discovery', 'exploration'].forEach(behavior => {
            this.helper.assertBehaviorPresent(html, behavior);
        });
    }
    
    async testCurrentBehaviorMarked() {
        // GIVEN: BotView at specific behavior
        const view = this.helper.createBotView();
        await view.navigateToBehavior('shape');
        
        // WHEN: Refresh and render
        await view.refresh();
        const html = view.getBehaviorsHTML();
        
        // THEN: Current behavior has marker
        this.helper.assertCurrentBehaviorMarked(html, 'shape');
    }
    
    // Story: Navigate Behavior Action
    async testClickingBehaviorExpandsActions() {
        // GIVEN: BotView with behaviors
        const view = this.helper.createBotView();
        await view.refresh();
        
        // WHEN: User clicks behavior (simulate expansion)
        view.expandBehavior('shape');  // View's own method
        const html = view.getBehaviorsHTML();
        
        // THEN: Behavior is expanded, actions are visible
        this.helper.assertBehaviorExpanded(html, 'shape');
        this.helper.assertActionsVisible(html, 'shape');
    }
    
    // Story: Execute Behavior Action
    async testActionDisplaysExecuteButton() {
        // GIVEN: BotView with actions
        const view = this.helper.createBotView();
        await view.navigateToBehavior('shape');
        await view.refresh();
        
        // WHEN: View renders
        const html = view.getBehaviorsHTML();
        
        // THEN: Each action has execute button
        const doc = parseHTML(html);
        const actionElements = doc.querySelectorAll('[data-action]');
        actionElements.forEach(actionEl => {
            const executeBtn = actionEl.querySelector('.execute-btn, [data-command*="execute"]');
            assert.ok(executeBtn, 'Action should have execute button');
        });
    }
}

// Run tests - mirrors Python unittest pattern
const workspaceDir = process.env.TEST_WORKSPACE || process.cwd();
const testSuite = new TestBehaviorsView(workspaceDir);

before(async () => await testSuite.setup());
after(() => testSuite.teardown());

test('TestBehaviorsView.testSingleBehaviorWithActions', async () => {
    await testSuite.testSingleBehaviorWithActions();
});

test('TestBehaviorsView.testMultipleBehaviors', async () => {
    await testSuite.testMultipleBehaviors();
});

test('TestBehaviorsView.testCurrentBehaviorMarked', async () => {
    await testSuite.testCurrentBehaviorMarked();
});

test('TestBehaviorsView.testClickingBehaviorExpandsActions', async () => {
    await testSuite.testClickingBehaviorExpandsActions();
});

test('TestBehaviorsView.testActionDisplaysExecuteButton', async () => {
    await testSuite.testActionDisplaysExecuteButton();
});
```

## CLI Integration - Views Use Their Built-In CLI

**Panel views ALREADY have CLI integration.** Tests instantiate views with a real CLI instance - the views handle all CLI communication using their existing methods.

### Key Architecture Points

1. **PanelView base class** spawns and manages CLI subprocess
2. **Views use their existing methods** to get JSON from CLI
3. **Persistent CLI session** - spawn once, reuse across tests
4. **No separate CLI helper needed** - views already know how to talk to CLI

### Test Approach

```javascript
// Tests create views with real CLI - views handle everything

class TestDisplayBehaviorHierarchy {
    constructor(workspaceDir) {
        this.helper = new BehaviorsViewTestHelper(workspaceDir, 'story_bot');
    }
    
    async setup() {
        // Initialize persistent CLI session ONCE
        await this.helper.initializeCLI();
    }
    
    teardown() {
        // Cleanup CLI after all tests
        this.helper.cleanupCLI();
    }
    
    async testSingleBehaviorWithActions() {
        // GIVEN: Create view with real CLI
        const view = this.helper.createBotView();
        
        // WHEN: View uses its built-in methods to get data from CLI and render
        await view.navigateToBehavior('shape'); // View's own method
        await view.refresh();                    // View's own method to get JSON
        const html = view.render();             // View's own method to render HTML
        
        // THEN: HTML contains expected structure from REAL CLI
        this.helper.assertBehaviorPresent(html, 'shape');
        this.helper.assertActionsPresent(html, 'shape', 
            ['clarify', 'strategy', 'validate', 'build', 'render']);
    }
}
```

### Benefits

✅ **No separate CLI abstraction** - use views as designed  
✅ **Tests real integration** - exactly how views work in production  
✅ **Persistent session** - CLI spawned once, reused across tests  
✅ **Contract testing** - ensures CLI ↔ Panel integration works  
✅ **Follows rules:**
- `call_production_code_directly` - calling real view methods with real CLI
- `mock_only_boundaries` - not mocking internal system components  
- `test_observable_behavior` - testing public view API
- `standard_test_data_sets` - consistent CLI states via view methods

## HTML Assertion Helpers

```javascript
// test/helpers/html_assertions.js

const assert = require('node:assert');
const { JSDOM } = require('jsdom');

function parseHTML(htmlString) {
    const dom = new JSDOM(htmlString);
    return dom.window.document;
}

class HTMLAssertions {
    static assertElementPresent(html, selector) {
        const doc = parseHTML(html);
        const element = doc.querySelector(selector);
        assert.ok(element, `Element not found: ${selector}`);
        return element;
    }
    
    static assertElementHasClass(html, selector, className) {
        const element = this.assertElementPresent(html, selector);
        assert.ok(element.classList.contains(className), 
            `Element ${selector} should have class "${className}"`);
    }
    
    static assertElementHasText(html, selector, expectedText) {
        const element = this.assertElementPresent(html, selector);
        assert.ok(element.textContent.includes(expectedText), 
            `Element ${selector} should contain text "${expectedText}"`);
    }
    
    static assertElementHasAttribute(html, selector, attributeName, expectedValue) {
        const element = this.assertElementPresent(html, selector);
        if (expectedValue !== undefined) {
            assert.strictEqual(element.getAttribute(attributeName), expectedValue,
                `Element ${selector} attribute "${attributeName}" should be "${expectedValue}"`);
        } else {
            assert.ok(element.hasAttribute(attributeName),
                `Element ${selector} should have attribute "${attributeName}"`);
        }
    }
    
    static assertElementCount(html, selector, expectedCount) {
        const doc = parseHTML(html);
        const elements = doc.querySelectorAll(selector);
        assert.strictEqual(elements.length, expectedCount,
            `Expected ${expectedCount} elements matching "${selector}", found ${elements.length}`);
    }
}

module.exports = { parseHTML, HTMLAssertions };
```

## Test Files to Create

### 1. `test/bot_view.test.js` (Orchestrator Tests)

**Stories:**
- Display Bot Header (name, version, paths)
- Display All Domain Sections (behaviors, scope, instructions)
- Update Bot Data (refresh functionality)

**Test Count:** ~15 tests (5 scenarios × 3 parameterized variations)

### 2. `test/behaviors_view.test.js` (Behavior Hierarchy Tests)

**Stories:**
- Display Behavior Hierarchy
- Navigate Behavior Action (expand/collapse)
- Execute Behavior Action
- Display Current Position Marker
- Display Completed Actions

**Test Count:** ~25 tests (8-10 scenarios × 2-3 variations)

### 3. `test/scope_view.test.js` (Scope Display Tests)

**Stories:**
- Display Current Scope
- Display No Scope Message
- Display Scope Types (story, epic, increment, files)
- Render Scope Target Information

**Test Count:** ~12 tests (4 scenarios × 3 variations)

### 4. `test/instructions_view.test.js` (Instructions Tests)

**Stories:**
- Display Behavior Instructions
- Display Action Instructions
- Display Input Parameters
- Display Output Artifacts
- Display No Instructions Message

**Test Count:** ~15 tests (5 scenarios × 3 variations)

### 5. `test/panel_view.test.js` (Base Class Tests)

**Stories:**
- Spawn CLI Subprocess
- Execute Command via CLI
- Parse JSON Response
- Handle CLI Errors

**Test Count:** ~10 tests

## Setup and Configuration

### 1. Install Dependencies

```bash
cd agile_bot/src/panel

# Only need jsdom for HTML parsing - Node test runner is built-in
npm install --save-dev jsdom
```

### 2. Create Test Setup

Create `test/setup.js`:

```javascript
// test/setup.js
// Common setup for Node.js test runner

// Mock VS Code APIs
global.vscode = {
    Uri: {
        file: (path) => ({ fsPath: path, toString: () => `file://${path}` }),
        joinPath: (base, ...paths) => ({ 
            fsPath: `${base.fsPath}/${paths.join('/')}`,
            toString: () => `file://${base.fsPath}/${paths.join('/')}`
        })
    }
};

// Helper to run setup before all tests
module.exports = { vscode: global.vscode };
```

### 3. Add NPM Scripts

Update `package.json`:

```json
{
    "scripts": {
        "test": "node --test test/**/*.test.js",
        "test:watch": "node --test --watch test/**/*.test.js",
        "test:verbose": "node --test test/**/*.test.js --test-reporter=spec"
    }
}
```

### 4. Node Version Requirement

Node.js test runner requires **Node.js 18.0.0 or higher**. Check version:

```bash
node --version  # Should be >= 18.0.0
```

## Test Rules - ALL 25 Rules for Validation

**CRITICAL:** All tests created for panel code MUST follow these rules. Use this checklist to validate every test file.

### Core Language & Naming Rules

#### 1. **use_domain_language**
Use domain vocabulary from stories/scenarios in all code. Class names = domain nouns. Method names = domain verbs.

```javascript
// ✅ GOOD: Domain language
class BehaviorsView {
    renderHierarchy() { /* ... */ }
}
test('TestBehaviorsView.testRendersHierarchyWithActions', () => { /* ... */ });

// ❌ BAD: Technical/generic terms
class HTMLRenderer {
    doRender() { /* ... */ }
}
test('test_render', () => { /* ... */ });
```

#### 2. **consistent_vocabulary**
Use ONE word per concept throughout codebase. Pick: create (not build/make), verify (not check/validate), load (not fetch/get).

```javascript
// ✅ GOOD: Consistent verbs
createBotView(), createBehaviorsView(), createScopeView()

// ❌ BAD: Mixed synonyms
createBotView(), buildBehaviorsView(), makeScopeView()
```

#### 3. **use_exact_variable_names**
Use exact variable names from specifications/stories.

```javascript
// ✅ GOOD: Exact names from spec
const view = helper.createBotView();
await view.refresh();
const behaviorName = 'shape';
const actionName = 'clarify';

// ❌ BAD: Different names
const v = helper.createBotView();
await v.refresh();
const behavior = 'shape';  // spec says behaviorName
const action = 'clarify';   // spec says actionName
```

### Test Structure Rules

#### 4. **use_class_based_organization**
Test structure: file = feature area, class = story, method = scenario. Match domain hierarchy.

```javascript
// ✅ GOOD: Class-based, mirrors domain
// File: test/behaviors_view.test.js
class TestDisplayBehaviorHierarchy {
    testSingleBehaviorWithFiveActions() { /* ... */ }
    testMultipleBehaviorsInPriorityOrder() { /* ... */ }
}

// ❌ BAD: No classes, generic names
test('display test', () => { /* ... */ });
test('another test', () => { /* ... */ });
```

#### 5. **place_imports_at_top**
All imports at top of file. Group: stdlib, third-party, local.

```javascript
// ✅ GOOD: Imports at top, grouped
const { test } = require('node:test');
const assert = require('node:assert');
const { JSDOM } = require('jsdom');
const BehaviorsView = require('../behaviors_view');

// ❌ BAD: Imports scattered
const { test } = require('node:test');
class TestSomething {
    testMethod() {
        const assert = require('node:assert'); // WRONG
    }
}
```

#### 6. **create_parameterized_tests_for_scenarios**
Use explicit test methods with descriptive names. NO generic parameterized functions.

```javascript
// ✅ GOOD: Explicit test methods
class TestDisplayBehaviorHierarchy {
    testSingleBehaviorWithActions() { /* ... */ }
    testMultipleBehaviors() { /* ... */ }
    testCurrentBehaviorMarked() { /* ... */ }
}

// ❌ BAD: Generic parameterized method
class TestDisplay {
    testBehavior(fixture, expected) { /* ... */ }
}
```

### Test Content Rules

#### 7. **no_defensive_code_in_tests**
No guard clauses, if-checks, or fallback logic in tests. Tests control setup - let them fail if wrong.

```javascript
// ✅ GOOD: Direct calls, no guards
const view = helper.createBehaviorsView(data);
const html = view.render();
assert.ok(html.includes('shape'));

// ❌ BAD: Defensive checks
if (view) {  // WRONG - let test fail if view is null
    const html = view.render();
    if (html) {  // WRONG
        assert.ok(html.includes('shape'));
    }
}
```

#### 8. **call_production_code_directly**
Call real production code. Let tests fail naturally. Don't mock classes under test.

```javascript
// ✅ GOOD: Real code
const view = new BehaviorsView(botJSON);
const html = view.render();

// ❌ BAD: Mock class under test
const view = { render: () => '<html>' };  // WRONG
```

#### 9. **test_observable_behavior**
Test public API and observable results. Don't test private fields or implementation details.

```javascript
// ✅ GOOD: Test public behavior
const html = view.render();
assert.ok(html.includes('data-behavior="shape"'));

// ❌ BAD: Test private internals
assert.ok(view._internalCache);  // WRONG - private field
assert.ok(view._renderCount === 1);  // WRONG - implementation detail
```

#### 10. **design_api_through_failing_tests**
Write tests against real expected API BEFORE implementing. Tests MUST fail initially.

```javascript
// ✅ GOOD: Test real API that doesn't exist yet
const view = new BehaviorsView(botJSON);  // Will fail until implemented
const html = view.render();
assert.ok(html.includes('shape'));

// ❌ BAD: Placeholder or skip failing step
const view = null;  // TODO: implement  // WRONG
```

#### 11. **match_specification_scenarios**
Tests must match specification scenarios exactly. Use same terminology and assertions.

```javascript
// ✅ GOOD: Matches spec exactly
// Spec says: "behavior 'shape' with actions ['clarify', 'strategy']"
testSingleBehaviorWithActions() {
    const behaviorName = 'shape';
    const actionNames = ['clarify', 'strategy'];
    // ... test using exact spec terms
}

// ❌ BAD: Different terminology
testBehavior() {
    const behavior = 'shp';  // WRONG - not from spec
    const acts = ['clr', 'stg'];  // WRONG
}
```

### Test Helper Rules

#### 12. **object_oriented_test_helpers**
Use helper classes that build complete domain objects with standard data.

```javascript
// ✅ GOOD: Helper class with complete objects
class BehaviorsViewTestHelper {
    createBehaviorsView(behaviorsData) { /* ... */ }
    assertBehaviorPresent(html, behaviorName) { /* ... */ }
}

// ❌ BAD: Scattered primitive functions
function getBehavior(name) { /* ... */ }
function checkHTML(html, value) { /* ... */ }
```

#### 13. **helper_extraction_and_reuse**
Extract duplicate setup to reusable helpers. Keep test bodies focused.

```javascript
// ✅ GOOD: Extracted to helper
const view = helper.createBehaviorsView(data);

// ❌ BAD: Duplicate setup in every test
const webview = createMockWebview();
const uri = createMockUri();
const view = new BehaviorsView(data, null, '/workspace', '/bot', '0.1.0', webview, uri);
// ... repeated in every test method
```

#### 14. **use_given_when_then_helpers**
Use reusable Given/When/Then helper functions for setup, action, assertion.

```javascript
// ✅ GOOD: Given/When/Then helpers
class TestBehaviorsView {
    testSingleBehavior() {
        // Given
        const data = this.givenBotWithSingleBehavior();
        // When
        const html = this.whenViewRendersHTML(data);
        // Then
        this.thenHTMLContainsBehavior(html, 'shape');
    }
    
    givenBotWithSingleBehavior() { /* ... */ }
    whenViewRendersHTML(data) { /* ... */ }
    thenHTMLContainsBehavior(html, name) { /* ... */ }
}

// ❌ BAD: Inline 4+ line blocks
test('test', () => {
    const dir = '/workspace';
    mkdirSync(dir);
    writeFileSync(dir + '/config.json', '{}');
    const data = JSON.parse(readFileSync(dir + '/config.json'));
    // ... WRONG - extract to helper
});
```

### Test Data Rules

#### 15. **standard_test_data_sets**
Use standard view states via real CLI. Don't recreate ad-hoc mock data per test.

```javascript
// ✅ GOOD: Standard view states using real CLI
class TestBehaviorsView {
    async getViewAtShapeBehavior() {
        const view = this.helper.createBotView();
        await view.navigateToBehavior('shape');
        await view.refresh();
        return view;
    }
    
    async testSomething() {
        const view = await this.getViewAtShapeBehavior();
        const html = view.getBehaviorsHTML();
        // ... test with real CLI data via view
    }
}

// ❌ BAD: Ad-hoc mock values per test
const view = { render: () => '<html>' };  // WRONG - use real view with CLI
```

#### 16. **assert_full_results**
Assert complete domain objects, not single cherry-picked fields.

```javascript
// ✅ GOOD: Assert full structure
helper.assertBehaviorHierarchyComplete(html, {
    behaviors: ['shape', 'discovery'],
    actions: { shape: ['clarify', 'strategy'] },
    current: 'shape'
});

// ❌ BAD: Cherry-pick single field
assert.ok(html.includes('shape'));  // WRONG - too specific
```

### Coverage Rules

#### 17. **cover_all_behavior_paths**
Cover normal (happy path), edge cases, and failure scenarios. Each gets its own test.

```javascript
// ✅ GOOD: Separate tests for each path
testRendersSingleBehavior() { /* happy path */ }
testRendersEmptyBehaviors() { /* edge case */ }
testThrowsErrorWhenInvalidData() { /* failure */ }

// ❌ BAD: One test for everything
testAllCases() {
    // tests happy + edge + failure  // WRONG - split up
}
```

#### 18. **bug_fix_test_first**
When fixing bugs: write failing test, verify failure, fix code, verify success.

```javascript
// ✅ GOOD: RED-GREEN workflow
// 1. Write test that reproduces bug
testCurrentBehaviorNotMarked() {
    const html = view.render();
    assert.ok(html.includes('class="current"'));  // FAILS
}
// 2. Run test - verify RED
// 3. Fix code
// 4. Run test - verify GREEN

// ❌ BAD: Fix code without test
// Edit view.render() directly without test  // WRONG
```

### Mock & Dependency Rules

#### 19. **mock_only_boundaries**
Mock ONLY external boundaries (APIs, network). Don't mock business logic or file I/O.

```javascript
// ✅ GOOD: Mock external API
const mockFetch = { get: () => Promise.resolve({}) };

// ❌ BAD: Mock business logic or internal classes
const mockView = { render: () => '<html>' };  // WRONG - test real view
```

#### 20. **production_code_explicit_dependencies**
Production code: inject all dependencies through constructor. No hidden globals.

```javascript
// ✅ GOOD: Explicit dependencies
class BehaviorsView {
    constructor(data, cli, workspace, botDir, version, webview, uri) {
        this.data = data;
        this.cli = cli;
        // ...
    }
}

// ❌ BAD: Hidden dependencies
class BehaviorsView {
    constructor(data) {
        this.cli = global.CLI;  // WRONG - hidden global
    }
}
```

### Code Quality Rules

#### 21. **production_code_clean_functions**
Production functions: ONE thing, under 20 lines, one abstraction level. Name reveals behavior.

```javascript
// ✅ GOOD: Small focused functions
renderBehaviorList(behaviors) {
    const items = this.createBehaviorItems(behaviors);
    return this.wrapInList(items);
}

// ❌ BAD: Long multi-purpose function
render() {
    // 50 lines doing: parse, validate, transform, render  // WRONG - split up
}
```

#### 22. **self_documenting_tests**
Tests document through code structure. Don't add verbose comments.

```javascript
// ✅ GOOD: Self-documenting
testSingleBehaviorWithFiveActions() {
    const botJSON = loadJSONFixture('bot_with_shape_behavior');
    const view = helper.createBehaviorsView(botJSON.behaviors);
    const html = view.render();
    helper.assertActionsPresent(html, 'shape', ['clarify', 'strategy', 'validate', 'build', 'render']);
}

// ❌ BAD: Verbose unnecessary comments
testSingleBehavior() {
    // This test checks if the view renders correctly
    // First we load the fixture
    const botJSON = loadJSONFixture('bot.json');
    // Then we create the view
    const view = new BehaviorsView(botJSON);
    // ... WRONG - comments are noise
}
```

#### 23. **use_ascii_only**
Use ASCII-only characters. No Unicode, emojis, or special characters.

```javascript
// ✅ GOOD: ASCII only
console.log('[PASS] Test passed');
console.log('[ERROR] Test failed');

// ❌ BAD: Unicode/emojis
console.log('✓ Test passed');  // WRONG - Unicode checkmark
console.log('❌ Test failed');  // WRONG - Unicode X
```

### Fixture Rules

#### 24. **define_fixtures_in_test_file**
Define test-specific fixtures in the test file itself. Only truly reusable fixtures go in shared files.

```javascript
// ✅ GOOD: Fixtures in test file
// test/behaviors_view.test.js
const TEST_BOT_JSON = {
    behaviors: { /* ... */ }
};

class TestBehaviorsView {
    setup() {
        this.botJSON = TEST_BOT_JSON;
    }
}

// ❌ BAD: Test-specific fixtures in shared file
// test/fixtures/behaviors_view_fixtures.js  // WRONG - put in test file
```

#### 25. **orchestrator_pattern**
Test methods are orchestrators (under 20 lines) showing Given-When-Then flow by calling helpers.

```javascript
// ✅ GOOD: Orchestrator pattern
testSingleBehaviorWithActions() {
    // Given: Bot with single behavior
    const botJSON = this.givenBotWithSingleBehavior();
    
    // When: View renders HTML
    const view = helper.createBehaviorsView(botJSON.behaviors);
    const html = view.render();
    
    // Then: HTML contains behavior and actions
    helper.assertBehaviorPresent(html, 'shape');
    helper.assertActionsPresent(html, 'shape', ['clarify', 'strategy']);
}

// ❌ BAD: Inline complex logic
testSingleBehavior() {
    const dir = createTempDir();
    mkdirSync(dir);
    writeFileSync(dir + '/config.json', JSON.stringify({...}));
    const data = JSON.parse(readFileSync(dir + '/config.json'));
    const webview = { postMessage: () => {} };
    // ... 30 more lines  // WRONG - extract to helpers
}
```

---

## Validation Checklist

When creating or reviewing panel tests, validate against ALL 25 rules:

**Language & Naming:**
- [ ] use_domain_language
- [ ] consistent_vocabulary
- [ ] use_exact_variable_names

**Structure:**
- [ ] use_class_based_organization
- [ ] place_imports_at_top
- [ ] create_parameterized_tests_for_scenarios

**Content:**
- [ ] no_defensive_code_in_tests
- [ ] call_production_code_directly
- [ ] test_observable_behavior
- [ ] design_api_through_failing_tests
- [ ] match_specification_scenarios

**Helpers:**
- [ ] object_oriented_test_helpers
- [ ] helper_extraction_and_reuse
- [ ] use_given_when_then_helpers

**Data:**
- [ ] standard_test_data_sets
- [ ] assert_full_results

**Coverage:**
- [ ] cover_all_behavior_paths
- [ ] bug_fix_test_first

**Mocking:**
- [ ] mock_only_boundaries
- [ ] production_code_explicit_dependencies

**Quality:**
- [ ] production_code_clean_functions
- [ ] self_documenting_tests
- [ ] use_ascii_only

**Fixtures:**
- [ ] define_fixtures_in_test_file
- [ ] orchestrator_pattern

## Implementation Phases

### Phase 1: Setup Infrastructure (~2 hours)
1. Install jsdom (only external dependency needed)
2. Create test directory structure
3. Create base view helper classes that initialize persistent CLI (rule: object_oriented_test_helpers)
4. Create HTML assertion helpers (rule: assert_full_results)
5. Configure package.json test scripts
6. Write first test class - views use their built-in CLI integration (smoke test)
7. **Validate against all 25 rules using checklist**

### Phase 2: BehaviorsView Tests (~4 hours)
1. Create BehaviorsViewTestHelper (rule: object_oriented_test_helpers)
2. Create test class with ~25 explicit test methods (rule: use_class_based_organization)
3. Cover all scenarios (rule: cover_all_behavior_paths):
   - Display hierarchy (multiple test methods for different cases)
   - Current behavior marking
   - Action listing
   - Expansion/collapse
   - Execute buttons
4. **Validate each test against all 25 rules**

### Phase 3: Remaining Views (~6 hours)
1. Create TestScopeView class (~12 test methods)
2. Create TestInstructionsView class (~15 test methods)
3. Create TestBotView class (~15 test methods)
4. Create TestPanelView class (~10 test methods)
5. **Validate all tests against all 25 rules**

### Phase 4: Integration Tests (~2 hours)
1. End-to-end HTML rendering
2. CLI subprocess integration
3. Command execution flows
4. **Final validation against all 25 rules**

### Phase 5: Rule Validation (~1 hour)
1. Run through validation checklist for every test file
2. Document any rule violations and fix them
3. Ensure 100% compliance with all 25 rules

### Total Estimated Time: ~15 hours

## Success Criteria

### Test Count & Organization
- ✅ ~77 test methods created (mirroring CLI test count ratio)
- ✅ All tests use class-based structure (rule: use_class_based_organization)
- ✅ Each test method has explicit, descriptive domain name (rule: use_domain_language)
- ✅ Given-When-Then format in all test methods (rule: orchestrator_pattern)

### Code Quality
- ✅ Zero code duplication - use helper classes (rule: helper_extraction_and_reuse, object_oriented_test_helpers)
- ✅ All tests call production code directly (rule: call_production_code_directly)
- ✅ No defensive code in tests (rule: no_defensive_code_in_tests)
- ✅ Production code uses clean functions (rule: production_code_clean_functions)

### Assertions & Coverage
- ✅ HTML assertions are comprehensive (rule: assert_full_results)
- ✅ Cover happy path, edge cases, failures (rule: cover_all_behavior_paths)
- ✅ Test observable behavior only (rule: test_observable_behavior)
- ✅ Match specifications exactly (rule: match_specification_scenarios)

### Test Data
- ✅ Tests use real CLI in JSON mode (rule: standard_test_data_sets, call_production_code_directly)
- ✅ Standard CLI commands/states across tests (rule: standard_test_data_sets)
- ✅ Use exact variable names from specs (rule: use_exact_variable_names)
- ✅ No mocked JSON fixtures - real integration testing

### Validation
- ✅ ALL 25 test rules followed (see Validation Checklist)
- ✅ 100% test pass rate
- ✅ Coverage > 80% for panel code
- ✅ Tests mirror Python unittest patterns
- ✅ ASCII-only characters (rule: use_ascii_only)

## Benefits

### Mirrors CLI Success
- **Same class-based patterns** as Python CLI tests
- **Same test rules** applied
- **Same Given-When-Then** format
- **Same explicit test methods** approach (not parameterized DSL)

### Node Test Runner Advantages
- **Zero dependencies** - built into Node.js 18+
- **Standard, traditional** unit testing approach
- **JSDOM** for realistic HTML parsing
- **Fast execution** (no subprocess overhead)
- **Simple, straightforward** - no framework magic
- **Consistent** with Python unittest patterns

### Quality Improvements
- **Prevents regressions** in HTML rendering
- **Documents expected HTML structure**
- **Makes refactoring safe**
- **Enables confident changes**

## Next Steps

1. **Review this plan** - Confirm approach mirrors CLI tests
2. **Start Phase 1** - Set up infrastructure
3. **Write first test** - BehaviorsView smoke test
4. **Iterate** - Complete all views systematically

---

## Example: Complete Test File Following ALL Rules

```javascript
// test/behaviors_view.test.js
// Rule: place_imports_at_top - all imports at top, grouped

// Standard library
const { test, before, after } = require('node:test');
const assert = require('node:assert');

// Third-party
const { JSDOM } = require('jsdom');

// Local
const BehaviorsViewTestHelper = require('./helpers/behaviors_view_test_helper');

// Rule: use_class_based_organization - class = story
// Rule: use_domain_language - class name uses domain vocabulary
class TestDisplayBehaviorHierarchy {
    
    constructor(workspaceDir) {
        this.helper = new BehaviorsViewTestHelper(workspaceDir, 'story_bot');
    }
    
    // Rule: helper_extraction_and_reuse - setup extracted to method
    async setup() {
        // Initialize persistent CLI session ONCE - views will use it
        await this.helper.initializeCLI();
    }
    
    teardown() {
        // Cleanup CLI after all tests complete
        this.helper.cleanupCLI();
    }
    
    // Rule: use_exact_variable_names - names match spec
    // Rule: orchestrator_pattern - method under 20 lines, Given-When-Then flow
    // Rule: create_parameterized_tests_for_scenarios - explicit method name
    async testSingleBehaviorWithFiveActions() {
        // Rule: use_given_when_then_helpers - structured flow
        // GIVEN: BotView with real CLI at shape behavior
        const view = this.helper.createBotView(); // Rule: standard_test_data_sets
        await view.navigateToBehavior('shape');
        
        // Rule: call_production_code_directly - calling real view with real CLI
        // WHEN: View refreshes and renders HTML
        await view.refresh();  // View uses its CLI to get JSON
        const html = view.getBehaviorsHTML();
        
        // Rule: assert_full_results - asserting complete structure
        // Rule: test_observable_behavior - testing public API output
        // THEN: HTML contains expected structure from real CLI
        this.helper.assertBehaviorPresent(html, 'shape');
        this.helper.assertActionsPresent(html, 'shape', 
            ['clarify', 'strategy', 'validate', 'build', 'render']);
        this.helper.assertCurrentBehaviorMarked(html, 'shape');
    }
    
    // Rule: cover_all_behavior_paths - separate test for different scenario
    async testMultipleBehaviorsInPriorityOrder() {
        // GIVEN: BotView with multiple behaviors via real CLI
        const view = this.helper.createBotView();
        
        // WHEN: View refreshes and renders
        await view.refresh();
        const html = view.getBehaviorsHTML();
        
        // THEN: HTML contains behaviors in correct order from CLI
        this.helper.assertBehaviorsInOrder(html, 
            ['prioritization', 'shape', 'discovery', 'exploration']);
        this.helper.assertCurrentBehaviorMarked(html, 'shape');
    }
    
    // Rule: use_ascii_only - test name uses ASCII, not Unicode checkmark
    async testCompletedActionsMarked() {
        // GIVEN: BotView with completed actions
        const view = this.helper.createBotView();
        await view.navigateToBehavior('shape');
        await view.navigateToAction('strategy'); // Complete clarify, move to strategy
        
        // Rule: no_defensive_code_in_tests - no if-checks, direct calls
        // WHEN: View refreshes and renders
        await view.refresh();
        const html = view.getBehaviorsHTML();
        
        // THEN: Completed actions are marked
        this.helper.assertBehaviorPresent(html, 'shape');
        this.helper.assertActionsCompleted(html, 'shape', ['clarify']);
    }
    
    // Rule: cover_all_behavior_paths - failure scenario
    async testThrowsErrorWhenCLIUnavailable() {
        // GIVEN: Helper with no CLI initialized
        const newHelper = new BehaviorsViewTestHelper(process.cwd(), 'story_bot');
        
        // WHEN/THEN: Creating view without CLI throws error
        assert.throws(
            () => newHelper.createBotView(),
            { message: /CLI not initialized/ }
        );
    }
}

// Rule: self_documenting_tests - code structure shows what's tested
// Rule: match_specification_scenarios - test names match story scenarios
// Run all tests
const workspaceDir = process.env.TEST_WORKSPACE || process.cwd();
const suite = new TestDisplayBehaviorHierarchy(workspaceDir);

before(async () => await suite.setup());
after(() => suite.teardown());

test('TestDisplayBehaviorHierarchy.testSingleBehaviorWithFiveActions', async () => {
    await suite.testSingleBehaviorWithFiveActions();
});

test('TestDisplayBehaviorHierarchy.testMultipleBehaviorsInPriorityOrder', async () => {
    await suite.testMultipleBehaviorsInPriorityOrder();
});

test('TestDisplayBehaviorHierarchy.testCompletedActionsMarked', async () => {
    await suite.testCompletedActionsMarked();
});

test('TestDisplayBehaviorHierarchy.testThrowsErrorWhenCLIUnavailable', async () => {
    await suite.testThrowsErrorWhenCLIUnavailable();
});
```

**Rules Demonstrated:** 16 of 25 rules shown in this example. All 25 must be validated against every test file.

**Key Architecture:** 
- Views use their built-in CLI integration
- Persistent CLI session across all tests
- No separate CLI helper - views handle everything

This plan provides a complete, systematic approach to testing the panel code using class-based patterns with ALL 25 test rules explicitly defined for validation!

---

## Rule Validation Workflow

### When Creating New Tests

1. **Write test class** using class-based organization
2. **Write test methods** with explicit descriptive names
3. **Run validation** against all 25 rules using checklist
4. **Fix violations** immediately
5. **Document compliance** - note which rules each test follows

### When Reviewing Tests

Use this format for validation results:

```
Rule Name | PASS or FAIL | Explanation if FAIL

use_domain_language | PASS
consistent_vocabulary | PASS
use_class_based_organization | PASS
call_production_code_directly | FAIL | Line 45 mocks BehaviorsView instead of testing real code
assert_full_results | FAIL | Line 67 only asserts html.includes('shape') instead of full structure
```

### Quick Rule Reference

**Most Common Violations to Watch For:**

1. **assert_full_results** - Cherry-picking fields instead of asserting complete objects
2. **object_oriented_test_helpers** - Inline setup instead of using helper classes
3. **no_defensive_code_in_tests** - Adding if-checks or guards in tests
4. **call_production_code_directly** - Mocking classes under test
5. **use_domain_language** - Generic technical names instead of domain vocabulary

### Validation Report Template

```markdown
# Test Validation Report: [test_file_name.test.js]

## Summary
- Total Rules: 25
- Passing: X
- Failing: Y

## Failures
1. [rule_name] | Line [N] | [explanation]
2. [rule_name] | Line [N] | [explanation]

## Action Items
- [ ] Fix [rule_name] violation in [method_name]
- [ ] Refactor [method_name] to use helper class
```

---

## Final Checklist Before Implementation

- [ ] Review all 25 test rules
- [ ] Understand validation checklist
- [ ] Review example test file showing rule compliance
- [ ] Set up validation template for tracking
- [ ] Commit to validating EVERY test against ALL 25 rules
- [ ] Ready to begin Phase 1
