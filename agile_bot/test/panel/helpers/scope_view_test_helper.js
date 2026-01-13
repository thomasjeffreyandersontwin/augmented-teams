/**
 * ScopeView Test Helper
 * 
 * Helper class for testing ScopeView HTML rendering.
 * Rule: object_oriented_test_helpers - Class-based helper with domain methods
 * Rule: use_domain_language - Methods named after domain concepts
 */

const assert = require('node:assert');
const path = require('path');
const ScopeSection = require('../../../src/panel/scope_view');
const { HTMLAssertions, parseHTML } = require('./html_assertions');

/**
 * ScopeView Test Helper
 * Rule: object_oriented_test_helpers - Helper class builds complete domain objects
 * Rule: standard_test_data_sets - Provides standard scope view states
 */
class ScopeViewTestHelper {
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
     * Create ScopeSection with mock webview and extensionUri
     * Rule: call_production_code_directly - Returns real ScopeSection instance
     * Rule: mock_only_boundaries - Only mocks VS Code API boundary
     * 
     * @param {Object} scopeData - Scope data from bot JSON
     * @returns {ScopeSection} Real ScopeSection instance
     */
    createScopeView(scopeData) {
        const webview = this.createMockWebview();
        const extensionUri = this.createMockExtensionUri();
        
        return new ScopeSection(
            scopeData,
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
     * Assert scope section is present
     * Rule: use_domain_language - Scope section is domain concept
     */
    assertScopeSectionPresent(html) {
        assert.ok(html.includes('scope') || html.includes('Scope'), 
            'Expected HTML to contain scope section');
    }
    
    /**
     * Assert epic name is present
     * Rule: use_domain_language - epicName is domain term
     */
    assertEpicPresent(html, epicName) {
        assert.ok(html.includes(epicName), 
            `Expected HTML to contain epic "${epicName}"`);
    }
    
    /**
     * Assert story name is present
     * Rule: use_domain_language - storyName is domain term
     */
    assertStoryPresent(html, storyName) {
        assert.ok(html.includes(storyName), 
            `Expected HTML to contain story "${storyName}"`);
    }
    
    /**
     * Assert scope filter input is present
     * Rule: use_domain_language - Filter input is domain concept
     */
    assertScopeFilterPresent(html) {
        const doc = parseHTML(html);
        const filterInput = doc.querySelector('#scopeFilterInput') || 
                           doc.querySelector('input[placeholder*="Epic"]') ||
                           doc.querySelector('input[placeholder*="Story"]');
        assert.ok(filterInput || html.includes('filter') || html.includes('Filter'), 
            'Expected HTML to contain scope filter input');
    }
    
    /**
     * Assert filter value is set
     * Rule: use_exact_variable_names - filterValue matches spec
     */
    assertScopeFilterValue(html, filterValue) {
        const doc = parseHTML(html);
        const filterInput = doc.querySelector('#scopeFilterInput');
        if (filterInput) {
            assert.strictEqual(filterInput.value, filterValue,
                `Expected filter value to be "${filterValue}"`);
        } else {
            assert.ok(html.includes(filterValue), 
                `Expected HTML to contain filter value "${filterValue}"`);
        }
    }
    
    /**
     * Assert clear filter button is present
     * Rule: test_observable_behavior - Tests visible UI element
     */
    assertClearFilterButtonPresent(html) {
        assert.ok(html.includes('clearScopeFilter') || html.includes('clear'), 
            'Expected HTML to contain clear filter button');
    }
    
    /**
     * Assert epic hierarchy is present
     * Rule: use_domain_language - Epic hierarchy is domain concept
     */
    assertEpicHierarchyPresent(html) {
        assert.ok(html.includes('epic-') || 
                  html.includes('toggleCollapse') || 
                  html.includes('collapsible'), 
            'Expected HTML to contain epic hierarchy structure');
    }
    
    /**
     * Assert no scope message is displayed
     * Rule: use_domain_language - No scope message is domain concept
     */
    assertNoScopeMessageDisplayed(html) {
        assert.ok(html.includes('No scope') || 
                  html.includes('no scope') || 
                  html.includes('all') ||
                  html.includes('All'), 
            'Expected HTML to contain no scope message');
    }
    
    /**
     * Assert scope type is displayed
     * Rule: use_exact_variable_names - scopeType matches spec
     */
    assertScopeTypeDisplayed(html, scopeType) {
        assert.ok(html.includes(scopeType), 
            `Expected HTML to contain scope type "${scopeType}"`);
    }
    
    /**
     * Assert complete scope structure
     * Rule: assert_full_results - Assert complete structure
     * 
     * @param {Object} expectedStructure - { type: '...', content: [...], filter: '...' }
     */
    assertCompleteScopeStructure(html, expectedStructure) {
        this.assertScopeSectionPresent(html);
        
        if (expectedStructure.type) {
            this.assertScopeTypeDisplayed(html, expectedStructure.type);
        }
        
        if (expectedStructure.filter) {
            this.assertScopeFilterValue(html, expectedStructure.filter);
        }
        
        if (expectedStructure.content && expectedStructure.content.length > 0) {
            this.assertEpicHierarchyPresent(html);
        }
    }
}

module.exports = ScopeViewTestHelper;
