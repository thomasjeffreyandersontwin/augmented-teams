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
        const html = this.helper.render_html(scopeData);
        
        this.helper.assert_scope_type(html, 'all');
        assert.ok(html.includes('All'), 'Should contain "All"');
    }

    async testEpicScopeTypeSingleEpic() {
        /**
         * GIVEN: Scope set to single epic
         * WHEN: View renders scope
         * THEN: HTML shows epic name
         */
        const scopeData = this.helper.create_scope_epic(['User Management']);
        const html = this.helper.render_html(scopeData);
        
        this.helper.assert_scope_type(html, 'epic');
        this.helper.assert_scope_value(html, 'User Management');
    }

    async testEpicScopeTypeMultipleEpics() {
        /**
         * GIVEN: Scope set to multiple epics
         * WHEN: View renders scope
         * THEN: HTML shows all epic names
         */
        const scopeData = this.helper.create_scope_epic(['User Management', 'Reporting', 'Analytics']);
        const html = this.helper.render_html(scopeData);
        
        this.helper.assert_scope_type(html, 'epic');
        this.helper.assert_scope_value(html, 'User Management');
        this.helper.assert_scope_value(html, 'Reporting');
        this.helper.assert_scope_value(html, 'Analytics');
    }

    async testStoryScopeTypeSingleStory() {
        /**
         * GIVEN: Scope set to single story
         * WHEN: View renders scope
         * THEN: HTML shows story name
         */
        const scopeData = this.helper.create_scope_story(['Login Flow']);
        const html = this.helper.render_html(scopeData);
        
        this.helper.assert_scope_type(html, 'story');
        this.helper.assert_scope_value(html, 'Login Flow');
    }

    async testStoryScopeTypeMultipleStories() {
        /**
         * GIVEN: Scope set to multiple stories
         * WHEN: View renders scope
         * THEN: HTML shows all story names
         */
        const scopeData = this.helper.create_scope_story(['Login Flow', 'Password Reset', 'Registration']);
        const html = this.helper.render_html(scopeData);
        
        this.helper.assert_scope_type(html, 'story');
        this.helper.assert_scope_value(html, 'Login Flow');
        this.helper.assert_scope_value(html, 'Password Reset');
        this.helper.assert_scope_value(html, 'Registration');
    }

    async testIncrementScopeType() {
        /**
         * GIVEN: Scope set to increment range
         * WHEN: View renders scope
         * THEN: HTML shows increment numbers
         */
        const scopeData = this.helper.create_scope_increment([1, 2, 3]);
        const html = this.helper.render_html(scopeData);
        
        this.helper.assert_scope_type(html, 'increment');
        assert.ok(html.includes('1'), 'Should contain increment 1');
        assert.ok(html.includes('2'), 'Should contain increment 2');
        assert.ok(html.includes('3'), 'Should contain increment 3');
    }

    async testFilesScopeType() {
        /**
         * GIVEN: Scope set to specific files
         * WHEN: View renders scope
         * THEN: HTML shows file paths
         */
        const scopeData = this.helper.create_scope_files(['src/auth.py', 'src/user.py']);
        const html = this.helper.render_html(scopeData);
        
        this.helper.assert_scope_type(html, 'files');
        this.helper.assert_scope_value(html, 'src/auth.py');
        this.helper.assert_scope_value(html, 'src/user.py');
    }

    async testEmptyScope() {
        /**
         * GIVEN: No scope set
         * WHEN: View renders scope
         * THEN: HTML shows default/empty state
         */
        const scopeData = this.helper.create_scope_empty();
        const html = this.helper.render_html(scopeData);
        
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
        const html = this.helper.render_html(scopeData);
        
        this.helper.assert_scope_type(html, 'files');
        assert.ok(html.includes('src/**/*.py'), 'Should show included pattern');
    }

    async testScopeChangeUpdateDisplay() {
        /**
         * GIVEN: Initial scope of 'all'
         * WHEN: Scope changes to specific epic
         * THEN: HTML updates to show epic scope
         */
        const initialScope = this.helper.create_scope_all();
        const initialHtml = this.helper.render_html(initialScope);
        this.helper.assert_scope_type(initialHtml, 'all');
        
        const newScope = this.helper.create_scope_epic(['User Management']);
        const newHtml = this.helper.render_html(newScope);
        this.helper.assert_scope_type(newHtml, 'epic');
        this.helper.assert_scope_value(newHtml, 'User Management');
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
