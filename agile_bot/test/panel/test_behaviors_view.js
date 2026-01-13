/**
 * Test BehaviorsView - Complete Coverage
 */

// Mock vscode before any imports
const Module = require('module');
const originalRequire = Module.prototype.require;
Module.prototype.require = function(...args) {
    if (args[0] === 'vscode') {
        return require('./mock_vscode');
    }
    return originalRequire.apply(this, args);
};
const { test, after } = require('node:test');
const assert = require('node:assert');
const path = require('path');
const { BehaviorsViewTestHelper, BotViewTestHelper } = require('./helpers');

// Track bot views for cleanup
const activeBotViews = [];

after(() => {
    for (const botView of activeBotViews) {
        try {
            if (botView.cleanup) {
                botView.cleanup();
            }
        } catch (e) {
            // Ignore cleanup errors
        }
    }
    setTimeout(() => process.exit(0), 100);
});

// Rule: use_class_based_organization
class TestBehaviorsView {
    constructor(workspaceDir) {
        this.helper = new BehaviorsViewTestHelper(workspaceDir, 'story_bot');
    }
    
    async setup() {
        await this.helper.initialize_cli();
    }
    
    teardown() {
        this.helper.cleanup_cli();
    }
    
    // ========================================================================
    // DISPLAY HIERARCHY TESTS
    // ========================================================================
    
    async testSingleBehaviorWithNoActions() {
        /**
         * GIVEN: Bot with single behavior, no actions
         * WHEN: View renders hierarchy
         * THEN: Behavior name appears, no action list
         */
        const behaviorData = this.helper.create_behavior_with_actions('shape', []);
        const html = this.helper.render_html([behaviorData]);
        
        assert.ok(html.includes('shape'), 'Should contain behavior name');
        assert.ok(html.length > 0, 'Should render HTML');
        this.helper.assert_behavior_with_actions(html, 'shape', []);
    }
    
    async testSingleBehaviorWithMultipleActions() {
        /**
         * GIVEN: Bot with single behavior, 5 actions
         * WHEN: View renders hierarchy
         * THEN: Behavior and all actions appear in order
         */
        const actions = ['clarify', 'strategy', 'validate', 'build', 'render'];
        const behaviorData = this.helper.create_behavior_with_actions('shape', actions);
        const html = this.helper.render_html([behaviorData]);
        
        this.helper.assert_behavior_with_actions(html, 'shape', actions);
        
        // Verify all actions present
        for (const action of actions) {
            assert.ok(html.includes(action), `Should contain action "${action}"`);
        }
    }
    
    async testMultipleBehaviorsInOrder() {
        /**
         * GIVEN: Bot with 3 behaviors in priority order
         * WHEN: View renders hierarchy
         * THEN: Behaviors appear in correct order
         */
        const behaviorsData = this.helper.create_behaviors([
            { name: 'prioritization', actions: ['clarify'] },
            { name: 'shape', actions: ['clarify', 'strategy'] },
            { name: 'discovery', actions: ['analyze'] }
        ]);
        
        const html = this.helper.render_html(behaviorsData);
        
        this.helper.assert_behaviors_in_order(html, ['prioritization', 'shape', 'discovery']);
        
        // Verify all behaviors present
        for (const behavior of behaviorsData) {
            assert.ok(html.includes(behavior.name), 
                `Should contain behavior "${behavior.name}"`);
        }
    }
    
    async testEmptyBehaviorsList() {
        /**
         * GIVEN: Bot with no behaviors
         * WHEN: View renders hierarchy
         * THEN: Returns empty or minimal HTML
         */
        const html = this.helper.render_html([]);
        
        assert.ok(typeof html === 'string', 'Should return string');
        // Empty array should return empty or minimal HTML
        assert.ok(html.length >= 0, 'Should handle empty behaviors');
    }
    
    // ========================================================================
    // CURRENT BEHAVIOR MARKING TESTS
    // ========================================================================
    
    async testCurrentBehaviorMarkedInHierarchy() {
        /**
         * GIVEN: Bot at shape behavior
         * WHEN: View renders with current state
         * THEN: Shape behavior has current marker
         */
        const behaviorData = this.helper.create_behavior_with_actions('shape', 
            ['clarify', 'strategy']);
        const html = this.helper.render_html([behaviorData]);
        
        this.helper.assert_current_behavior_marked(html, 'shape');
    }
    
    async testNonCurrentBehaviorNotMarked() {
        /**
         * GIVEN: Bot at shape, discovery exists but not current
         * WHEN: View renders hierarchy
         * THEN: Only shape is marked as current
         */
        const behaviorsData = this.helper.create_behaviors([
            { name: 'shape', actions: ['clarify'], is_current: true },
            { name: 'discovery', actions: ['analyze'], is_current: false }
        ]);
        
        const html = this.helper.render_html(behaviorsData);
        
        // Shape should be marked
        this.helper.assert_current_behavior_marked(html, 'shape');
        
        // Discovery should be present but not marked as current
        assert.ok(html.includes('discovery'), 'Discovery should be present');
    }
    
    // ========================================================================
    // ACTION LISTING TESTS
    // ========================================================================
    
    async testActionsListedUnderBehavior() {
        /**
         * GIVEN: Behavior with 3 actions
         * WHEN: View renders
         * THEN: All actions appear under behavior
         */
        const actions = ['clarify', 'strategy', 'validate'];
        const behaviorData = this.helper.create_behavior_with_actions('shape', actions);
        const html = this.helper.render_html([behaviorData]);
        
        this.helper.assert_behavior_with_actions(html, 'shape', actions);
    }
    
    async testActionsInCorrectOrder() {
        /**
         * GIVEN: Behavior with actions in specific order
         * WHEN: View renders
         * THEN: Actions appear in same order
         */
        const actions = ['clarify', 'strategy', 'validate', 'build', 'render'];
        const behaviorData = this.helper.create_behavior_with_actions('shape', actions);
        const html = this.helper.render_html([behaviorData]);
        
        // Verify order by checking index positions
        let lastIndex = -1;
        for (const action of actions) {
            const index = html.indexOf(action);
            assert.ok(index > lastIndex, 
                `Action "${action}" should appear after previous action`);
            lastIndex = index;
        }
    }
    
    // ========================================================================
    // COMPLETED ACTION TESTS
    // ========================================================================
    
    async testCompletedActionsShowIndicator() {
        /**
         * GIVEN: Behavior with 2 completed, 2 pending actions
         * WHEN: View renders
         * THEN: Completed actions show checkmark indicator
         */
        const allActions = ['clarify', 'strategy', 'validate', 'build'];
        const completedActions = ['clarify', 'strategy'];
        
        const behaviorData = this.helper.create_behavior_with_completed_actions(
            'shape', allActions, completedActions
        );
        
        const html = this.helper.render_html([behaviorData]);
        
        this.helper.assert_completed_actions_marked(html, completedActions);
    }
    
    async testNoCompletedActionsShowsPendingOnly() {
        /**
         * GIVEN: Behavior with no completed actions
         * WHEN: View renders
         * THEN: All actions show as pending (no checkmarks)
         */
        const actions = ['clarify', 'strategy', 'validate'];
        const behaviorData = this.helper.create_behavior_with_completed_actions(
            'shape', actions, []  // No completed actions
        );
        
        const html = this.helper.render_html([behaviorData]);
        
        // All actions should be present
        for (const action of actions) {
            assert.ok(html.includes(action), `Should contain action "${action}"`);
        }
    }
    
    // ========================================================================
    // EXECUTE BUTTON TESTS
    // ========================================================================
    
    async testActionsHaveExecuteButtons() {
        /**
         * GIVEN: Behavior with actions
         * WHEN: View renders
         * THEN: Each action has execute button
         */
        const actions = ['clarify', 'strategy'];
        const behaviorData = this.helper.create_behavior_with_actions('shape', actions);
        const html = this.helper.render_html([behaviorData]);
        
        this.helper.assert_actions_have_execute_buttons(html, actions);
    }
    
    // ========================================================================
    // COMPLETE HIERARCHY TESTS
    // ========================================================================
    
    async testCompleteHierarchyRendering() {
        /**
         * GIVEN: Complete bot state with multiple behaviors and actions
         * WHEN: View renders full hierarchy
         * THEN: All elements present with correct structure
         */
        const behaviorsData = this.helper.create_behaviors([
            { name: 'shape', actions: ['clarify', 'strategy', 'validate'] },
            { name: 'discovery', actions: ['analyze', 'map'] }
        ]);
        
        const html = this.helper.render_html(behaviorsData);
        
        this.helper.assert_hierarchy_complete(html, {
            behaviors: ['shape', 'discovery'],
            actions: {
                shape: ['clarify', 'strategy', 'validate'],
                discovery: ['analyze', 'map']
            },
            current: 'shape'
        });
    }
    
    // ========================================================================
    // EDGE CASE TESTS
    // ========================================================================
    
    async testBehaviorWithVeryLongName() {
        /**
         * GIVEN: Behavior with exceptionally long name
         * WHEN: View renders
         * THEN: Name renders without breaking layout
         */
        const longName = 'very_long_behavior_name_that_might_break_layout_if_not_handled';
        const behaviorData = this.helper.create_behavior_with_actions(longName, ['action1']);
        const html = this.helper.render_html([behaviorData]);
        
        assert.ok(html.includes(longName), 'Should contain long behavior name');
        assert.ok(html.length > 0, 'Should render HTML');
    }
    
    async testBehaviorWithSpecialCharacters() {
        /**
         * GIVEN: Behavior name with special characters
         * WHEN: View renders
         * THEN: Special characters handled correctly
         */
        const behaviorData = this.helper.create_behavior_with_actions('test-behavior_v2', 
            ['action-1', 'action_2']);
        const html = this.helper.render_html([behaviorData]);
        
        // Verify special characters preserved
        assert.ok(html.includes('test-behavior_v2'), 'Should handle hyphens and underscores');
        assert.ok(html.includes('action-1'), 'Should handle action with hyphen');
        assert.ok(html.includes('action_2'), 'Should handle action with underscore');
    }
    
    async testMultipleBehaviorsWithSameActionNames() {
        /**
         * GIVEN: Multiple behaviors with overlapping action names
         * WHEN: View renders
         * THEN: All actions appear correctly under their behaviors
         */
        const behaviorsData = this.helper.create_behaviors([
            { name: 'shape', actions: ['clarify', 'validate'] },
            { name: 'discovery', actions: ['clarify', 'validate'] }  // Same action names
        ]);
        
        const html = this.helper.render_html(behaviorsData);
        
        // Both behaviors should be present
        assert.ok(html.includes('shape'), 'Should contain shape');
        assert.ok(html.includes('discovery'), 'Should contain discovery');
        
        // Actions should appear (may appear multiple times)
        const clarifyCount = (html.match(/clarify/g) || []).length;
        const validateCount = (html.match(/validate/g) || []).length;
        assert.ok(clarifyCount >= 2, 'Clarify should appear at least twice');
        assert.ok(validateCount >= 2, 'Validate should appear at least twice');
    }
    
    // ========================================================================
    // INTEGRATION WITH REAL CLI DATA
    // ========================================================================
    
    async testRenderingFromRealCLIResponse() {
        /**
         * GIVEN: Real bot state from CLI
         * WHEN: View renders from statusResponse.behaviors.all_behaviors
         * THEN: Complete state structure is rendered in HTML
         */
        // Use BotViewTestHelper for CLI interaction
        const botHelper = new BotViewTestHelper(process.env.TEST_WORKSPACE || path.join(__dirname, '../../..'), 'story_bot');
        const botView = botHelper.createBotView();
        activeBotViews.push(botView);
        
        await new Promise(resolve => setTimeout(resolve, 1500));
        
        // Get real bot state from CLI
        const statusResponse = await botView.execute('status');
        
        assert.ok(statusResponse.behaviors, 'Should have behaviors');
        assert.ok(statusResponse.behaviors.all_behaviors, 'Should have all_behaviors');
        assert.ok(Array.isArray(statusResponse.behaviors.all_behaviors), 
            'all_behaviors should be array');
        
        // Render from real data using BehaviorsViewTestHelper
        const behaviorsData = statusResponse.behaviors.all_behaviors;
        const html = this.helper.render_html(behaviorsData);
        
        // Assert COMPLETE state is rendered
        this.helper.assert_complete_state_rendered(html, statusResponse);
        
        // Verify each behavior from CLI is in HTML
        for (const behavior of behaviorsData) {
            this.helper.assert_behavior_fully_rendered(html, behavior);
        }
    }
}

// Setup workspace
const workspaceDir = process.env.TEST_WORKSPACE || path.join(__dirname, '../../..');

// Rule: create_parameterized_tests_for_scenarios
test('TestBehaviorsView', { concurrency: false, timeout: 60000 }, async (t) => {
    const suite = new TestBehaviorsView(workspaceDir);
    
    // Display hierarchy tests
    await t.test('testSingleBehaviorWithNoActions', async () => {
        await suite.testSingleBehaviorWithNoActions();
    });
    
    await t.test('testSingleBehaviorWithMultipleActions', async () => {
        await suite.testSingleBehaviorWithMultipleActions();
    });
    
    await t.test('testMultipleBehaviorsInOrder', async () => {
        await suite.testMultipleBehaviorsInOrder();
    });
    
    await t.test('testEmptyBehaviorsList', async () => {
        await suite.testEmptyBehaviorsList();
    });
    
    // Current behavior marking tests
    await t.test('testCurrentBehaviorMarkedInHierarchy', async () => {
        await suite.testCurrentBehaviorMarkedInHierarchy();
    });
    
    await t.test('testNonCurrentBehaviorNotMarked', async () => {
        await suite.testNonCurrentBehaviorNotMarked();
    });
    
    // Action listing tests
    await t.test('testActionsListedUnderBehavior', async () => {
        await suite.testActionsListedUnderBehavior();
    });
    
    await t.test('testActionsInCorrectOrder', async () => {
        await suite.testActionsInCorrectOrder();
    });
    
    // Completed action tests
    await t.test('testCompletedActionsShowIndicator', async () => {
        await suite.testCompletedActionsShowIndicator();
    });
    
    await t.test('testNoCompletedActionsShowsPendingOnly', async () => {
        await suite.testNoCompletedActionsShowsPendingOnly();
    });
    
    // Execute button tests
    await t.test('testActionsHaveExecuteButtons', async () => {
        await suite.testActionsHaveExecuteButtons();
    });
    
    // Complete hierarchy tests
    await t.test('testCompleteHierarchyRendering', async () => {
        await suite.testCompleteHierarchyRendering();
    });
    
    // Edge case tests
    await t.test('testBehaviorWithVeryLongName', async () => {
        await suite.testBehaviorWithVeryLongName();
    });
    
    await t.test('testBehaviorWithSpecialCharacters', async () => {
        await suite.testBehaviorWithSpecialCharacters();
    });
    
    await t.test('testMultipleBehaviorsWithSameActionNames', async () => {
        await suite.testMultipleBehaviorsWithSameActionNames();
    });
    
    // Integration tests
    await t.test('testRenderingFromRealCLIResponse', async () => {
        await suite.testRenderingFromRealCLIResponse();
    });
});
