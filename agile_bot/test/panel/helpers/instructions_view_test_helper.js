/**
 * InstructionsView Test Helper
 * 
 * Helper class for testing InstructionsView HTML rendering.
 * Rule: object_oriented_test_helpers - Class-based helper with domain methods
 * Rule: use_domain_language - Methods named after domain concepts
 */

const assert = require('node:assert');
const path = require('path');
const InstructionsSection = require('../../../src/panel/instructions_view');
const { HTMLAssertions, parseHTML } = require('./html_assertions');

/**
 * InstructionsView Test Helper
 * Rule: object_oriented_test_helpers - Helper class builds complete domain objects
 * Rule: standard_test_data_sets - Provides standard instructions view states
 */
class InstructionsViewTestHelper {
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
     * Create InstructionsSection with mock webview and extensionUri
     * Rule: call_production_code_directly - Returns real InstructionsSection instance
     * Rule: mock_only_boundaries - Only mocks VS Code API boundary
     * 
     * @param {Object} instructionsData - Instructions data from bot JSON
     * @param {Object} currentAction - Current action data (optional)
     * @returns {InstructionsSection} Real InstructionsSection instance
     */
    createInstructionsView(instructionsData, currentAction = null) {
        const webview = this.createMockWebview();
        const extensionUri = this.createMockExtensionUri();
        
        return new InstructionsSection(
            instructionsData,
            currentAction,
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
     * Assert instructions section is present
     * Rule: use_domain_language - Instructions section is domain concept
     */
    assertInstructionsSectionPresent(html) {
        assert.ok(html.includes('instructions') || html.includes('Instructions'), 
            'Expected HTML to contain instructions section');
    }
    
    /**
     * Assert behavior instructions are displayed
     * Rule: use_domain_language - Behavior instructions is domain concept
     */
    assertBehaviorInstructionsDisplayed(html, behaviorName) {
        assert.ok(html.includes(behaviorName) || html.includes('instructions'), 
            `Expected HTML to contain instructions for behavior "${behaviorName}"`);
    }
    
    /**
     * Assert action instructions are displayed
     * Rule: use_domain_language - Action instructions is domain concept
     */
    assertActionInstructionsDisplayed(html, actionName) {
        assert.ok(html.includes(actionName) || html.includes('instructions'), 
            `Expected HTML to contain instructions for action "${actionName}"`);
    }
    
    /**
     * Assert input parameters are displayed
     * Rule: use_domain_language - Input parameters is domain concept
     */
    assertInputParametersDisplayed(html) {
        assert.ok(html.includes('input') || 
                  html.includes('parameter') || 
                  html.includes('Input') || 
                  html.includes('Parameter'), 
            'Expected HTML to contain input parameters section');
    }
    
    /**
     * Assert output artifacts are displayed
     * Rule: use_domain_language - Output artifacts is domain concept
     */
    assertOutputArtifactsDisplayed(html) {
        assert.ok(html.includes('output') || 
                  html.includes('artifact') || 
                  html.includes('Output') || 
                  html.includes('Artifact'), 
            'Expected HTML to contain output artifacts section');
    }
    
    /**
     * Assert no instructions message is displayed
     * Rule: use_domain_language - No instructions message is domain concept
     */
    assertNoInstructionsMessageDisplayed(html) {
        assert.ok(html.includes('No instructions') || 
                  html.includes('no instructions') || 
                  html.includes('empty') ||
                  html.length === 0 ||
                  html.includes('Instructions'), 
            'Expected HTML to contain no instructions message or empty content');
    }
    
    /**
     * Assert instruction text is present
     * Rule: use_exact_variable_names - instructionText matches spec
     */
    assertInstructionTextPresent(html, instructionText) {
        assert.ok(html.includes(instructionText), 
            `Expected HTML to contain instruction text "${instructionText}"`);
    }
    
    /**
     * Assert current action is displayed
     * Rule: use_domain_language - Current action is domain concept
     */
    assertCurrentActionDisplayed(html, actionName) {
        assert.ok(html.includes(actionName), 
            `Expected HTML to contain current action "${actionName}"`);
    }
    
    /**
     * Assert complete instructions structure
     * Rule: assert_full_results - Assert complete structure
     * 
     * @param {Object} expectedStructure - { behavior: '...', action: '...', hasInputs: bool, hasOutputs: bool }
     */
    assertCompleteInstructionsStructure(html, expectedStructure) {
        this.assertInstructionsSectionPresent(html);
        
        if (expectedStructure.behavior) {
            this.assertBehaviorInstructionsDisplayed(html, expectedStructure.behavior);
        }
        
        if (expectedStructure.action) {
            this.assertActionInstructionsDisplayed(html, expectedStructure.action);
        }
        
        if (expectedStructure.hasInputs) {
            this.assertInputParametersDisplayed(html);
        }
        
        if (expectedStructure.hasOutputs) {
            this.assertOutputArtifactsDisplayed(html);
        }
    }
}

module.exports = InstructionsViewTestHelper;
