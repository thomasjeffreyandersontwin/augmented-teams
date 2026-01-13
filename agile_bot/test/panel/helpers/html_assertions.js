/**
 * HTML Assertion Helpers
 * 
 * Provides HTML parsing and assertion utilities for panel view tests.
 * Rule: object_oriented_test_helpers - Helper class with domain methods
 * Rule: use_domain_language - Methods named after domain concepts
 */

const assert = require('node:assert');
const { JSDOM } = require('jsdom');

/**
 * Parse HTML string into DOM document
 * Rule: production_code_clean_functions - Small focused function
 */
function parseHTML(htmlString) {
    const dom = new JSDOM(htmlString);
    return dom.window.document;
}

/**
 * HTML Assertion Helpers
 * Rule: object_oriented_test_helpers - Class-based helper
 * Rule: consistent_vocabulary - Use same verbs throughout
 */
class HTMLAssertions {
    /**
     * Assert element is present in HTML
     * Rule: use_domain_language - assertElementPresent is domain vocabulary
     */
    static assertElementPresent(html, selector) {
        const doc = parseHTML(html);
        const element = doc.querySelector(selector);
        assert.ok(element, `Element not found: ${selector}`);
        return element;
    }
    
    /**
     * Assert element has specific class
     * Rule: assert_full_results - Assert complete class structure
     */
    static assertElementHasClass(html, selector, className) {
        const element = this.assertElementPresent(html, selector);
        assert.ok(element.classList.contains(className), 
            `Element ${selector} should have class "${className}"`);
    }
    
    /**
     * Assert element contains text
     * Rule: use_exact_variable_names - expectedText matches spec
     */
    static assertElementHasText(html, selector, expectedText) {
        const element = this.assertElementPresent(html, selector);
        assert.ok(element.textContent.includes(expectedText), 
            `Element ${selector} should contain text "${expectedText}"`);
    }
    
    /**
     * Assert element has attribute with optional value check
     * Rule: production_code_clean_functions - One thing, clear name
     */
    static assertElementHasAttribute(html, selector, attributeName, expectedValue) {
        const element = this.assertElementPresent(html, selector);
        if (expectedValue !== undefined) {
            assert.strictEqual(element.getAttribute(attributeName), expectedValue,
                `Element ${selector} attribute "${attributeName}" should be "${expectedValue}"`);
        } else {
            assert.ok(element.hasAttribute(attributeName),
                `Element ${selector} should have attribute "${attributeName}"`);
        }
    }
    
    /**
     * Assert count of elements matching selector
     * Rule: use_exact_variable_names - expectedCount matches spec
     */
    static assertElementCount(html, selector, expectedCount) {
        const doc = parseHTML(html);
        const elements = doc.querySelectorAll(selector);
        assert.strictEqual(elements.length, expectedCount,
            `Expected ${expectedCount} elements matching "${selector}", found ${elements.length}`);
    }
    
    /**
     * Assert behavior is present in HTML
     * Rule: use_domain_language - behaviorName is domain term
     */
    static assertBehaviorPresent(html, behaviorName) {
        assert.ok(html.includes(behaviorName), 
            `Expected HTML to contain behavior name "${behaviorName}"`);
    }
    
    /**
     * Assert action is present in HTML
     * Rule: use_domain_language - actionName is domain term
     */
    static assertActionPresent(html, behaviorName, actionName) {
        const doc = parseHTML(html);
        const actionElement = doc.querySelector(
            `[data-behavior="${behaviorName}"] [data-action="${actionName}"]`
        );
        assert.ok(actionElement, 
            `Action "${actionName}" not found in behavior "${behaviorName}"`);
    }
    
    /**
     * Assert current behavior is marked
     * Rule: test_observable_behavior - Tests visible HTML structure
     */
    static assertCurrentBehaviorMarked(html, behaviorName) {
        const doc = parseHTML(html);
        const behaviorElement = doc.querySelector(`[data-behavior="${behaviorName}"]`);
        assert.ok(behaviorElement, `Behavior element "${behaviorName}" not found`);
        assert.ok(behaviorElement.classList.contains('current') || 
                  behaviorElement.classList.contains('active'), 
            `Behavior "${behaviorName}" should have "current" or "active" class`);
    }
    
    /**
     * Assert multiple actions are present
     * Rule: assert_full_results - Assert complete list
     */
    static assertActionsPresent(html, behaviorName, actionNames) {
        for (const actionName of actionNames) {
            assert.ok(html.includes(actionName), 
                `Expected action "${actionName}" in behavior "${behaviorName}"`);
        }
    }
    
    /**
     * Assert behaviors appear in order
     * Rule: assert_full_results - Assert complete ordering
     */
    static assertBehaviorsInOrder(html, behaviorNames) {
        let lastIndex = -1;
        for (const behaviorName of behaviorNames) {
            const index = html.indexOf(behaviorName);
            assert.ok(index > lastIndex, 
                `Behaviors should appear in order. "${behaviorName}" not in correct position`);
            lastIndex = index;
        }
    }
}

module.exports = { parseHTML, HTMLAssertions };
