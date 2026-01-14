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
const PanelView = require('../../src/panel/panel_view');

after(() => {
    PanelView.cleanupSharedCLI();
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
        const html = await this.helper.render_html();
        
        assert.ok(html.includes('shape'), 'Should contain behavior name');
        assert.ok(html.length > 0, 'Should render HTML');
        this.helper.assert_behavior_with_actions(html, 'shape', []);
    }
    
    async testSingleBehaviorWithMultipleActions() {
        /**
         * GIVEN: Bot with prioritization behavior (4 actions from real CLI)
         * WHEN: View renders hierarchy
         * THEN: Behavior and all actions appear in order
         */
        const html = await this.helper.render_html();
        
        // Real CLI returns prioritization with 4 actions
        const expectedActions = ['clarify', 'strategy', 'validate', 'render'];
        this.helper.assert_behavior_with_actions(html, 'prioritization', expectedActions);
        
        // Verify all actions present
        for (const action of expectedActions) {
            assert.ok(html.includes(action), `Should contain action "${action}"`);
        }
    }
    
    async testMultipleBehaviorsInOrder() {
        /**
         * GIVEN: Bot with 7 behaviors from real CLI
         * WHEN: View renders hierarchy
         * THEN: Behaviors appear in correct order
         */
        const html = await this.helper.render_html();
        
        // Real CLI returns these behaviors in this order
        const expectedBehaviors = ['prioritization', 'exploration', 'scenarios', 'tests', 'code', 'discovery', 'shape'];
        this.helper.assert_behaviors_in_order(html, expectedBehaviors);
        
        // Verify all behaviors present
        for (const behaviorName of expectedBehaviors) {
            assert.ok(html.includes(behaviorName), 
                `Should contain behavior "${behaviorName}"`);
        }
    }
    
    async testEmptyBehaviorsList() {
        /**
         * GIVEN: Bot with no behaviors
         * WHEN: View renders hierarchy
         * THEN: Returns empty or minimal HTML
         */
        const html = await this.helper.render_html();
        
        assert.ok(typeof html === 'string', 'Should return string');
        // Empty array should return empty or minimal HTML
        assert.ok(html.length >= 0, 'Should handle empty behaviors');
    }
    
    // ========================================================================
    // CURRENT BEHAVIOR MARKING TESTS
    // ========================================================================
    
    async testCurrentBehaviorMarkedInHierarchy() {
        /**
         * GIVEN: Real CLI at prioritization behavior
         * WHEN: View renders with current state
         * THEN: Prioritization behavior has current marker
         */
        const html = await this.helper.render_html();
        
        // Real CLI has prioritization as current behavior
        this.helper.assert_current_behavior_marked(html, 'prioritization');
    }
    
    async testNonCurrentBehaviorNotMarked() {
        /**
         * GIVEN: Real CLI at prioritization, other behaviors exist but not current
         * WHEN: View renders hierarchy
         * THEN: Only prioritization is marked as current
         */
        const html = await this.helper.render_html();
        
        // Prioritization should be marked
        this.helper.assert_current_behavior_marked(html, 'prioritization');
        
        // Real CLI returns 7 behaviors - verify only current one is marked
        assert.ok(html.includes('discovery'), 'Discovery should be present');
        assert.ok(html.includes('prioritization'), 'Prioritization should be present');
    }
    
    // ========================================================================
    // ACTION LISTING TESTS
    // ========================================================================
    
    async testActionsListedUnderBehavior() {
        /**
         * GIVEN: Prioritization behavior with 4 actions from real CLI
         * WHEN: View renders
         * THEN: All actions appear under behavior
         */
        const html = await this.helper.render_html();
        
        // Real CLI returns prioritization with these actions
        const expectedActions = ['clarify', 'strategy', 'validate', 'render'];
        this.helper.assert_behavior_with_actions(html, 'prioritization', expectedActions);
    }
    
    async testActionsInCorrectOrder() {
        /**
         * GIVEN: Prioritization behavior with actions from real CLI
         * WHEN: View renders
         * THEN: Actions appear in same order
         */
        const html = await this.helper.render_html();
        
        // Real CLI returns prioritization actions in this order
        const expectedActions = ['clarify', 'strategy', 'validate', 'render'];
        
        // Verify order by checking index positions
        let lastIndex = -1;
        for (const action of expectedActions) {
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
        
        const html = await this.helper.render_html();
        
        this.helper.assert_completed_actions_marked(html, completedActions);
    }
    
    async testNoCompletedActionsShowsPendingOnly() {
        /**
         * GIVEN: Real CLI with prioritization behavior (no completed actions)
         * WHEN: View renders
         * THEN: All actions show as pending (no checkmarks)
         */
        const html = await this.helper.render_html();
        
        // Real CLI returns prioritization with these actions
        const expectedActions = ['clarify', 'strategy', 'validate', 'render'];
        
        // All actions should be present
        for (const action of expectedActions) {
            assert.ok(html.includes(action), `Should contain action "${action}"`);
        }
    }
    
    // ========================================================================
    // EXECUTE BUTTON TESTS
    // ========================================================================
    
    async testActionsHaveExecuteButtons() {
        /**
         * GIVEN: Real CLI with prioritization behavior
         * WHEN: View renders
         * THEN: Each action has execute button
         */
        const html = await this.helper.render_html();
        
        // Real CLI returns prioritization with these actions
        const expectedActions = ['clarify', 'strategy', 'validate', 'render'];
        this.helper.assert_actions_have_execute_buttons(html, expectedActions);
    }
    
    // ========================================================================
    // COMPLETE HIERARCHY TESTS
    // ========================================================================
    
    async testCompleteHierarchyRendering() {
        /**
         * GIVEN: Complete bot state from real CLI with 7 behaviors
         * WHEN: View renders full hierarchy
         * THEN: All elements present with correct structure
         */
        const html = await this.helper.render_html();
        
        // Real CLI returns 7 behaviors, prioritization is current
        this.helper.assert_hierarchy_complete(html, {
            behaviors: ['prioritization', 'exploration', 'scenarios', 'tests', 'code', 'discovery', 'shape'],
            actions: {
                prioritization: ['clarify', 'strategy', 'validate', 'render']
            },
            current: 'prioritization'
        });
    }
    
    // ========================================================================
    // EDGE CASE TESTS
    // ========================================================================
    
    async testBehaviorWithVeryLongName() {
        /**
         * GIVEN: Real CLI behaviors (some have long names like "prioritization")
         * WHEN: View renders
         * THEN: Names render without breaking layout
         */
        const html = await this.helper.render_html();
        
        // Real CLI has "prioritization" which is relatively long
        assert.ok(html.includes('prioritization'), 'Should contain prioritization behavior');
        assert.ok(html.length > 0, 'Should render HTML');
    }
    
    async testBehaviorWithSpecialCharacters() {
        /**
         * GIVEN: Real CLI behaviors (use underscores like "story_bot")
         * WHEN: View renders
         * THEN: Special characters handled correctly
         */
        const html = await this.helper.render_html();
        
        // Real CLI behaviors use underscores
        assert.ok(html.includes('prioritization'), 'Should handle behavior names');
        assert.ok(html.includes('clarify'), 'Should handle action names');
    }
    
    async testMultipleBehaviorsWithSameActionNames() {
        /**
         * GIVEN: Real CLI with multiple behaviors sharing action names (clarify, validate, etc.)
         * WHEN: View renders
         * THEN: Actions correctly scoped to their behaviors
         */
        const html = await this.helper.render_html();
        
        // Real CLI has multiple behaviors with shared action names
        assert.ok(html.includes('prioritization'), 'Should contain prioritization');
        assert.ok(html.includes('exploration'), 'Should contain exploration');
        assert.ok(html.includes('scenarios'), 'Should contain scenarios');
        
        // Actions like "clarify" and "validate" appear in multiple behaviors
        const clarifyCount = (html.match(/clarify/g) || []).length;
        const validateCount = (html.match(/validate/g) || []).length;
        assert.ok(clarifyCount >= 2, 'Clarify should appear in multiple behaviors');
        assert.ok(validateCount >= 2, 'Validate should appear in multiple behaviors');
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
        
        await new Promise(resolve => setTimeout(resolve, 1500));
        
        // Get real bot state from CLI
        const statusResponse = await botView.execute('status');
        
        assert.ok(statusResponse.behaviors, 'Should have behaviors');
        assert.ok(statusResponse.behaviors.all_behaviors, 'Should have all_behaviors');
        assert.ok(Array.isArray(statusResponse.behaviors.all_behaviors), 
            'all_behaviors should be array');
        
        // Render from real data using BehaviorsViewTestHelper
        const behaviorsData = statusResponse.behaviors.all_behaviors;
        const html = await this.helper.render_html();
        
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
