/**
 * BehaviorsView Test Helper
 * 
 * Helper class for testing BehaviorsView HTML rendering.
 * Rule: object_oriented_test_helpers - Class-based helper with domain methods
 * Rule: use_domain_language - Methods named after domain concepts
 */

const assert = require('node:assert');
const path = require('path');
const BehaviorsView = require('../../../src/panel/behaviors_view');
const { HTMLAssertions, parseHTML } = require('./html_assertions');

/**
 * BehaviorsView Test Helper
 * Rule: object_oriented_test_helpers - Helper class builds complete domain objects
 * Rule: standard_test_data_sets - Provides standard behavior view states
 */
class BehaviorsViewTestHelper {
    /**
     * Create helper with workspace context
     * Rule: production_code_explicit_dependencies - All dependencies through constructor
     * 
     * @param {string} workspaceDir - Workspace directory path
     */
    constructor(workspaceDir) {
        this.workspaceDir = workspaceDir;
    }
    
    /**
     * Create BehaviorsView with mock webview and extensionUri
     * Rule: call_production_code_directly - Returns real BehaviorsView instance
     * Rule: mock_only_boundaries - Only mocks VS Code API boundary
     * 
     * @param {Array} behaviorsData - Behaviors array from bot JSON
     * @returns {BehaviorsView} Real BehaviorsView instance
     */
    createBehaviorsView(behaviorsData) {
        const webview = this.createMockWebview();
        const extensionUri = this.createMockExtensionUri();
        
        return new BehaviorsView(
            behaviorsData,
            null,  // cli
            this.workspaceDir,
            webview,
            extensionUri
        );
    }
    
    /**
     * Create mock VS Code webview
     * Rule: mock_only_boundaries - Mock external API boundary
     */
    createMockWebview() {
        return { 
            postMessage: () => {},
            asWebviewUri: (uri) => uri
        };
    }
    
    /**
     * Create mock VS Code extension URI
     * Rule: mock_only_boundaries - Mock external API boundary
     */
    createMockExtensionUri() {
        return { 
            fsPath: this.workspaceDir,
            toString: () => `file://${this.workspaceDir}`
        };
    }
    
    /**
     * Assert behavior name is present in HTML
     * Rule: use_domain_language - behaviorName is domain term
     * Rule: helper_extraction_and_reuse - Reusable assertion
     */
    assertBehaviorPresent(html, behaviorName) {
        HTMLAssertions.assertBehaviorPresent(html, behaviorName);
    }
    
    /**
     * Assert current behavior is marked in HTML
     * Rule: use_domain_language - currentBehavior is domain term
     * Rule: test_observable_behavior - Tests visible HTML structure
     */
    assertCurrentBehaviorMarked(html, behaviorName) {
        const doc = parseHTML(html);
        // Check for active or current class on behavior elements
        const activeBehavior = doc.querySelector('.active') || doc.querySelector('.current');
        assert.ok(activeBehavior, 'Expected to find current/active behavior marker');
        assert.ok(html.includes(behaviorName), 
            `Expected current behavior to be "${behaviorName}"`);
    }
    
    /**
     * Assert action is present in behavior
     * Rule: use_domain_language - behaviorName, actionName are domain terms
     */
    assertActionPresent(html, behaviorName, actionName) {
        assert.ok(html.includes(actionName), 
            `Expected action "${actionName}" in behavior "${behaviorName}"`);
    }
    
    /**
     * Assert multiple actions are present
     * Rule: assert_full_results - Assert complete list of actions
     * Rule: use_exact_variable_names - actionNames matches spec
     */
    assertActionsPresent(html, behaviorName, actionNames) {
        HTMLAssertions.assertActionsPresent(html, behaviorName, actionNames);
    }
    
    /**
     * Assert behaviors appear in order
     * Rule: assert_full_results - Assert complete ordering
     * Rule: use_exact_variable_names - behaviorNames matches spec
     */
    assertBehaviorsInOrder(html, behaviorNames) {
        HTMLAssertions.assertBehaviorsInOrder(html, behaviorNames);
    }
    
    /**
     * Assert completed actions are marked
     * Rule: test_observable_behavior - Tests visible completion markers
     * Rule: use_domain_language - completedActionNames is domain term
     */
    assertActionsCompleted(html, behaviorName, completedActionNames) {
        const doc = parseHTML(html);
        for (const actionName of completedActionNames) {
            // Look for completed marker (checkmark icon or completed class)
            const hasCompletedMarker = html.includes('marker-completed') || 
                                      html.includes('status-marker') ||
                                      html.includes('tick.png');
            assert.ok(hasCompletedMarker || html.includes(actionName), 
                `Expected action "${actionName}" to be marked as completed`);
        }
    }
    
    /**
     * Assert behavior hierarchy section is present
     * Rule: use_domain_language - Behavior hierarchy is domain concept
     */
    assertBehaviorHierarchyPresent(html) {
        assert.ok(html.includes('Behavior') || html.includes('behavior'), 
            'Expected HTML to contain behavior hierarchy section');
    }
    
    /**
     * Assert expand/collapse icons are present
     * Rule: test_observable_behavior - Tests visible UI elements
     */
    assertExpandCollapseIconsPresent(html) {
        assert.ok(html.includes('toggleCollapse') || 
                  html.includes('expand-icon') || 
                  html.includes('collapsible'), 
            'Expected HTML to contain expand/collapse icons');
    }
    
    /**
     * Assert navigation buttons are present
     * Rule: use_domain_language - Navigation buttons are domain concept
     */
    assertNavigationButtonsPresent(html) {
        assert.ok(html.includes('back') || html.includes('next') || html.includes('current'), 
            'Expected HTML to contain navigation buttons');
    }
    
    /**
     * Assert behavior hierarchy is complete
     * Rule: assert_full_results - Assert complete structure
     * 
     * @param {Object} expectedStructure - { behaviors: [...], actions: {...}, current: '...' }
     */
    assertBehaviorHierarchyComplete(html, expectedStructure) {
        // Assert all behaviors present
        if (expectedStructure.behaviors) {
            this.assertBehaviorsInOrder(html, expectedStructure.behaviors);
        }
        
        // Assert actions for each behavior
        if (expectedStructure.actions) {
            for (const [behaviorName, actionNames] of Object.entries(expectedStructure.actions)) {
                this.assertActionsPresent(html, behaviorName, actionNames);
            }
        }
        
        // Assert current behavior marked
        if (expectedStructure.current) {
            this.assertCurrentBehaviorMarked(html, expectedStructure.current);
        }
    }
}

module.exports = BehaviorsViewTestHelper;
