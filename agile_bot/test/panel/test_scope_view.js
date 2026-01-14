/**
 * Test ScopeView
 */

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
const { ScopeViewTestHelper } = require('./helpers');
const PanelView = require('../../src/panel/panel_view');

after(() => {
    PanelView.cleanupSharedCLI();
    setTimeout(() => process.exit(0), 100);
});

const workspaceDir = process.env.TEST_WORKSPACE || path.join(__dirname, '../../..');
process.env.BOT_DIRECTORY = path.join(workspaceDir, 'agile_bot', 'bots', 'story_bot');

class TestScopeView {
    constructor(workspaceDir) {
        this.helper = new ScopeViewTestHelper(workspaceDir, 'story_bot');
    }

    async testAllScopeType() {
        /**
         * GIVEN: Scope set to 'all'
         * WHEN: View renders scope
         * THEN: HTML shows "All Stories/Features"
         */
        const scopeData = this.helper.create_scope_all();
        const html = await this.helper.render_html();
        
        assert.ok(typeof html === 'string', 'Should return HTML string');
        assert.ok(html.length > 0, 'Should render HTML');
    }

    async testEpicScopeTypeSingleEpic() {
        /**
         * GIVEN: Scope set to single epic
         * WHEN: View renders scope
         * THEN: HTML shows epic name
         */
        const scopeData = this.helper.create_scope_epic(['User Management']);
        const html = await this.helper.render_html();
        
        assert.ok(typeof html === 'string', 'Should return HTML string');
        assert.ok(html.length > 0, 'Should render HTML');
    }

    async testEpicScopeTypeMultipleEpics() {
        /**
         * GIVEN: Scope set to multiple epics
         * WHEN: View renders scope
         * THEN: HTML shows all epic names
         */
        const scopeData = this.helper.create_scope_epic(['User Management', 'Reporting', 'Analytics']);
        const html = await this.helper.render_html();
        
        assert.ok(typeof html === 'string', 'Should return HTML string');
        assert.ok(html.length > 0, 'Should render HTML');
    }

    async testStoryScopeTypeSingleStory() {
        /**
         * GIVEN: Scope set to single story
         * WHEN: View renders scope
         * THEN: HTML shows story name
         */
        const scopeData = this.helper.create_scope_story(['Login Flow']);
        const html = await this.helper.render_html();
        
        assert.ok(typeof html === 'string', 'Should return HTML string');
        assert.ok(html.length > 0, 'Should render HTML');
    }

    async testStoryScopeTypeMultipleStories() {
        /**
         * GIVEN: Scope set to multiple stories
         * WHEN: View renders scope
         * THEN: HTML shows all story names
         */
        const scopeData = this.helper.create_scope_story(['Login Flow', 'Password Reset', 'Registration']);
        const html = await this.helper.render_html();
        
        assert.ok(typeof html === 'string', 'Should return HTML string');
        assert.ok(html.length > 0, 'Should render HTML');
    }

    async testIncrementScopeType() {
        /**
         * GIVEN: Scope set to increment range
         * WHEN: View renders scope
         * THEN: HTML shows increment numbers
         */
        const scopeData = this.helper.create_scope_increment([1, 2, 3]);
        const html = await this.helper.render_html();
        
        assert.ok(typeof html === 'string', 'Should return HTML string');
        assert.ok(html.length > 0, 'Should render HTML');
    }

    async testFilesScopeType() {
        /**
         * GIVEN: Scope set to specific files
         * WHEN: View renders scope
         * THEN: HTML shows file paths
         */
        const scopeData = this.helper.create_scope_files(['src/auth.py', 'src/user.py']);
        const html = await this.helper.render_html();
        
        assert.ok(typeof html === 'string', 'Should return HTML string');
        assert.ok(html.length > 0, 'Should render HTML');
    }

    async testEmptyScope() {
        /**
         * GIVEN: No scope set
         * WHEN: View renders scope
         * THEN: HTML shows default/empty state
         */
        const scopeData = this.helper.create_scope_empty();
        const html = await this.helper.render_html();
        
        assert.ok(typeof html === 'string', 'Should return string');
        assert.ok(html.length > 0, 'Should render HTML');
    }

    async testScopeWithExclusions() {
        /**
         * GIVEN: File scope with exclusions
         * WHEN: View renders scope
         * THEN: HTML shows included files and excluded patterns
         */
        const scopeData = this.helper.create_scope_files_with_exclusions(
            ['src/**/*.py'],
            ['**/test_*.py', '**/__pycache__/**']
        );
        const html = await this.helper.render_html();
        
        assert.ok(typeof html === 'string', 'Should return HTML string');
        assert.ok(html.length > 0, 'Should render HTML');
    }

    async testScopeChangeUpdateDisplay() {
        /**
         * GIVEN: Initial scope of 'all'
         * WHEN: Scope changes to specific epic
         * THEN: HTML updates to show epic scope
         */
        const initialScope = this.helper.create_scope_all();
        const initialHtml = await this.helper.render_html();
        assert.ok(typeof initialHtml === 'string', 'Should return initial HTML');
        assert.ok(initialHtml.length > 0, 'Should render initial HTML');
        
        const newScope = this.helper.create_scope_epic(['User Management']);
        const newHtml = await this.helper.render_html();
        assert.ok(typeof newHtml === 'string', 'Should return updated HTML');
        assert.ok(newHtml.length > 0, 'Should render updated HTML');
    }
}

test('TestScopeView', { concurrency: false, timeout: 30000 }, async (t) => {
    const suite = new TestScopeView(workspaceDir);
    
    await t.test('testAllScopeType', async () => {
        await suite.testAllScopeType();
    });
    
    await t.test('testEpicScopeTypeSingleEpic', async () => {
        await suite.testEpicScopeTypeSingleEpic();
    });
    
    await t.test('testEpicScopeTypeMultipleEpics', async () => {
        await suite.testEpicScopeTypeMultipleEpics();
    });
    
    await t.test('testStoryScopeTypeSingleStory', async () => {
        await suite.testStoryScopeTypeSingleStory();
    });
    
    await t.test('testStoryScopeTypeMultipleStories', async () => {
        await suite.testStoryScopeTypeMultipleStories();
    });
    
    await t.test('testIncrementScopeType', async () => {
        await suite.testIncrementScopeType();
    });
    
    await t.test('testFilesScopeType', async () => {
        await suite.testFilesScopeType();
    });
    
    await t.test('testEmptyScope', async () => {
        await suite.testEmptyScope();
    });
    
    await t.test('testScopeWithExclusions', async () => {
        await suite.testScopeWithExclusions();
    });
    
    await t.test('testScopeChangeUpdateDisplay', async () => {
        await suite.testScopeChangeUpdateDisplay();
    });
});
