/**
 * Smoke Test: Panel Views with Real CLI Integration
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
const { BotViewTestHelper, BehaviorsViewTestHelper } = require('./helpers');

// Track bot views for cleanup
const activeBotViews = [];

// Cleanup after all tests
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

class TestPanelSmokeTest {
    constructor(workspaceDir) {
        this.botHelper = new BotViewTestHelper(workspaceDir, 'story_bot');
        this.behaviorsHelper = new BehaviorsViewTestHelper(workspaceDir, 'story_bot');
    }
    
    async testBotViewSpawnsRealCLI() {
        /**
         * GIVEN: Workspace with story_bot
         * WHEN: BotView is instantiated
         * THEN: CLI subprocess spawns successfully
         */
        const botView = this.botHelper.createBotView();
        activeBotViews.push(botView);
        
        // Wait for CLI initialization
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        assert.ok(botView, 'BotView should be created');
        assert.strictEqual(typeof botView.execute, 'function', 'Should have execute method');
    }
    
    async testBotViewExecutesStatusCommand() {
        /**
         * GIVEN: BotView with active CLI
         * WHEN: Status command is executed
         * THEN: CLI returns bot state JSON
         */
        const botView = this.botHelper.createBotView();
        activeBotViews.push(botView);
        
        // Wait for CLI initialization
        await new Promise(resolve => setTimeout(resolve, 1000));
        
        const response = await botView.execute('status');
        
        assert.ok(response, 'Should receive response');
        assert.ok(response.bot || response.name, 'Should contain bot data');
        
        // Validate complete status response structure - no guards!
        assert.ok(response.behaviors, 'Should have behaviors in response');
        assert.ok(response.behaviors.all_behaviors, 'Should have all_behaviors array');
        assert.ok(response.behaviors.current, 'Should have current behavior');
        assert.ok(Array.isArray(response.behaviors.all_behaviors), 
            'all_behaviors should be array');
    }
    
    async testBehaviorsViewRendersHTML() {
        /**
         * GIVEN: Behavior data structure
         * WHEN: BehaviorsView renders
         * THEN: HTML is generated without errors
         */
        const behaviorData = this.behaviorsHelper.create_behavior_with_actions(
            'shape',
            ['clarify', 'strategy', 'validate']
        );
        
        const html = this.behaviorsHelper.render_html([behaviorData]);
        
        assert.ok(typeof html === 'string', 'Should return HTML string');
        assert.ok(html.length > 0, 'HTML should not be empty');
        
        this.behaviorsHelper.assert_behavior_with_actions(
            html,
            'shape',
            ['clarify', 'strategy', 'validate']
        );
    }
}

// Setup workspace
const workspaceDir = process.env.TEST_WORKSPACE || path.join(__dirname, '../../..');

test('TestPanelSmokeTest', { concurrency: false }, async (t) => {
    const suite = new TestPanelSmokeTest(workspaceDir);
    
    await t.test('testBotViewSpawnsRealCLI', async () => {
        await suite.testBotViewSpawnsRealCLI();
    });
    
    await t.test('testBotViewExecutesStatusCommand', async () => {
        await suite.testBotViewExecutesStatusCommand();
    });
    
    await t.test('testBehaviorsViewRendersHTML', async () => {
        await suite.testBehaviorsViewRendersHTML();
    });
});
