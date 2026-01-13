/**
 * Test InstructionsView
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
const { InstructionsViewTestHelper } = require('./helpers');

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

class TestInstructionsView {
    constructor(workspaceDir) {
        this.helper = new InstructionsViewTestHelper(workspaceDir, 'story_bot');
    }

    async testMarkdownFormatInstructions() {
        /**
         * GIVEN: Instructions in markdown format
         * WHEN: View renders instructions
         * THEN: HTML shows formatted markdown
         */
        const instructions = this.helper.create_markdown_instructions('# Bot Instructions\n\n## Getting Started\n\nFollow these steps...');
        const html = this.helper.render_html(instructions);
        
        this.helper.assert_format(html, 'markdown');
        assert.ok(html.includes('Bot Instructions'), 'Should contain heading');
        assert.ok(html.includes('Getting Started'), 'Should contain subheading');
    }

    async testPlainTextInstructions() {
        /**
         * GIVEN: Instructions in plain text
         * WHEN: View renders instructions
         * THEN: HTML shows plain text
         */
        const instructions = this.helper.create_plain_text_instructions('Bot is ready. Type help for commands.');
        const html = this.helper.render_html(instructions);
        
        assert.ok(html.includes('Bot is ready'), 'Should contain text');
        assert.ok(html.includes('help for commands'), 'Should contain instructions');
    }

    async testEmptyInstructions() {
        /**
         * GIVEN: No instructions
         * WHEN: View renders
         * THEN: HTML shows empty state
         */
        const instructions = this.helper.create_empty_instructions();
        const html = this.helper.render_html(instructions);
        
        assert.ok(typeof html === 'string', 'Should return string');
        assert.ok(html.length > 0, 'Should render HTML');
    }

    async testInstructionsWithCommandList() {
        /**
         * GIVEN: Instructions with command list
         * WHEN: View renders instructions
         * THEN: HTML shows all commands
         */
        const commands = ['status', 'shape', 'discovery', 'help'];
        const instructions = this.helper.create_instructions_with_commands(commands);
        const html = this.helper.render_html(instructions);
        
        for (const command of commands) {
            assert.ok(html.includes(command), `Should contain command "${command}"`);
        }
    }

    async testInstructionsWithCodeBlocks() {
        /**
         * GIVEN: Instructions with code examples
         * WHEN: View renders instructions
         * THEN: HTML shows formatted code blocks
         */
        const instructions = this.helper.create_instructions_with_code('```python\nprint("Hello")\n```');
        const html = this.helper.render_html(instructions);
        
        assert.ok(html.includes('print'), 'Should contain code');
        assert.ok(html.includes('Hello'), 'Should contain code content');
    }

    async testInstructionsWithLinks() {
        /**
         * GIVEN: Instructions with hyperlinks
         * WHEN: View renders instructions
         * THEN: HTML shows clickable links
         */
        const instructions = this.helper.create_instructions_with_links('[Documentation](https://example.com/docs)');
        const html = this.helper.render_html(instructions);
        
        assert.ok(html.includes('Documentation'), 'Should contain link text');
    }

    async testMultilineInstructions() {
        /**
         * GIVEN: Multi-paragraph instructions
         * WHEN: View renders instructions
         * THEN: HTML preserves paragraph structure
         */
        const instructions = this.helper.create_multiline_instructions([
            'First paragraph with setup instructions.',
            'Second paragraph with usage examples.',
            'Third paragraph with troubleshooting.'
        ]);
        const html = this.helper.render_html(instructions);
        
        assert.ok(html.includes('First paragraph'), 'Should contain first paragraph');
        assert.ok(html.includes('Second paragraph'), 'Should contain second paragraph');
        assert.ok(html.includes('Third paragraph'), 'Should contain third paragraph');
    }

    async testInstructionsWithBulletList() {
        /**
         * GIVEN: Instructions with bullet points
         * WHEN: View renders instructions
         * THEN: HTML shows formatted list
         */
        const instructions = this.helper.create_instructions_with_bullets([
            'Navigate to behavior',
            'Execute action',
            'Review results'
        ]);
        const html = this.helper.render_html(instructions);
        
        assert.ok(html.includes('Navigate to behavior'), 'Should contain first item');
        assert.ok(html.includes('Execute action'), 'Should contain second item');
        assert.ok(html.includes('Review results'), 'Should contain third item');
    }

    async testInstructionsUpdate() {
        /**
         * GIVEN: Initial instructions displayed
         * WHEN: Instructions change
         * THEN: HTML updates to show new content
         */
        const initial = this.helper.create_plain_text_instructions('Initial instructions');
        const initialHtml = this.helper.render_html(initial);
        assert.ok(initialHtml.includes('Initial'), 'Should show initial');
        
        const updated = this.helper.create_plain_text_instructions('Updated instructions');
        const updatedHtml = this.helper.render_html(updated);
        assert.ok(updatedHtml.includes('Updated'), 'Should show updated');
    }

    async testLongInstructions() {
        /**
         * GIVEN: Very long instruction text
         * WHEN: View renders instructions
         * THEN: HTML handles long content without truncation
         */
        const longText = 'A'.repeat(5000);
        const instructions = this.helper.create_plain_text_instructions(longText);
        const html = this.helper.render_html(instructions);
        
        assert.ok(html.length > 4000, 'Should contain full text');
    }
}

test('TestInstructionsView', { concurrency: false, timeout: 30000 }, async (t) => {
    const suite = new TestInstructionsView(workspaceDir);
    
    await t.test('testMarkdownFormatInstructions', async () => {
        await suite.testMarkdownFormatInstructions();
    });
    
    await t.test('testPlainTextInstructions', async () => {
        await suite.testPlainTextInstructions();
    });
    
    await t.test('testEmptyInstructions', async () => {
        await suite.testEmptyInstructions();
    });
    
    await t.test('testInstructionsWithCommandList', async () => {
        await suite.testInstructionsWithCommandList();
    });
    
    await t.test('testInstructionsWithCodeBlocks', async () => {
        await suite.testInstructionsWithCodeBlocks();
    });
    
    await t.test('testInstructionsWithLinks', async () => {
        await suite.testInstructionsWithLinks();
    });
    
    await t.test('testMultilineInstructions', async () => {
        await suite.testMultilineInstructions();
    });
    
    await t.test('testInstructionsWithBulletList', async () => {
        await suite.testInstructionsWithBulletList();
    });
    
    await t.test('testInstructionsUpdate', async () => {
        await suite.testInstructionsUpdate();
    });
    
    await t.test('testLongInstructions', async () => {
        await suite.testLongInstructions();
    });
});
