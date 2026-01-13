/**
 * BotView Test Helper
 * 
 * Helper class for testing BotView HTML rendering.
 * Rule: object_oriented_test_helpers - Class-based helper with domain methods
 * Rule: use_domain_language - Methods named after domain concepts
 */

const assert = require('node:assert');
const path = require('path');
const BotView = require('../../../src/panel/bot/bot_view');
const { HTMLAssertions } = require('./html_assertions');

/**
 * BotView Test Helper
 * Rule: object_oriented_test_helpers - Helper class builds complete domain objects
 * Rule: standard_test_data_sets - Provides standard bot view states
 */
class BotViewTestHelper {
    /**
     * Create helper with workspace context
     * Rule: production_code_explicit_dependencies - All dependencies through constructor
     * 
     * @param {string} workspaceDir - Workspace directory path
     * @param {string} botName - Bot name (defaults to story_bot)
     */
    constructor(workspaceDir, botName = 'story_bot') {
        this.workspaceDir = workspaceDir;
        this.botDir = path.join(workspaceDir, 'agile_bot', 'bots', botName);
        this.activeBotViews = [];
    }
    
    /**
     * Create BotView with mock webview and extensionUri
     * Rule: call_production_code_directly - Returns real BotView instance
     * Rule: mock_only_boundaries - Only mocks VS Code API boundary
     * 
     * @param {Object} botJSON - Bot JSON data (optional, will execute status if not provided)
     * @returns {BotView} Real BotView instance
     */
    createBotView(botJSON = {}) {
        const webview = this.createMockWebview();
        const extensionUri = this.createMockExtensionUri();
        
        const botView = new BotView(
            botJSON,
            null,  // cli - BotView will spawn its own
            this.workspaceDir,
            this.botDir,
            '0.1.0',  // panelVersion
            webview,
            extensionUri
        );
        
        this.activeBotViews.push(botView);
        return botView;
    }
    
    /**
     * Clean up all active bot views
     * Rule: production_code_clean_functions - Small focused cleanup
     */
    cleanup() {
        for (const botView of this.activeBotViews) {
            try {
                botView.cleanup();
            } catch (e) {
                // Ignore cleanup errors
            }
        }
        this.activeBotViews = [];
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
        HTMLAssertions.assertCurrentBehaviorMarked(html, behaviorName);
    }
    
    /**
     * Assert action is present in behavior
     * Rule: use_domain_language - behaviorName, actionName are domain terms
     */
    assertActionPresent(html, behaviorName, actionName) {
        HTMLAssertions.assertActionPresent(html, behaviorName, actionName);
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
     * Assert bot header is present
     * Rule: use_domain_language - Bot header is domain concept
     */
    assertBotHeaderPresent(html) {
        assert.ok(html.includes('bot-view') || html.includes('Bot'), 
            'Expected HTML to contain bot header');
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
     * Assert instructions section is present
     * Rule: use_domain_language - Instructions section is domain concept
     */
    assertInstructionsSectionPresent(html) {
        assert.ok(html.includes('instructions') || html.includes('Instructions'), 
            'Expected HTML to contain instructions section');
    }
    
    /**
     * Assert complete bot view structure
     * Rule: assert_full_results - Assert complete structure
     * Rule: test_observable_behavior - Tests visible HTML sections
     */
    assertCompleteBotViewStructure(html) {
        this.assertBotHeaderPresent(html);
        assert.ok(html.includes('behaviors') || html.includes('Behavior'), 
            'Expected HTML to contain behaviors section');
        this.assertScopeSectionPresent(html);
        this.assertInstructionsSectionPresent(html);
    }
}

module.exports = BotViewTestHelper;
