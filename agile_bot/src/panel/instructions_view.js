/**
 * InstructionsSection - Renders action instructions with action-specific subsections.
 * 
 * Epic: Invoke Bot Through Panel
 * Sub-Epic: Display Action Instructions Through Panel
 * Story: Display Base Instructions, Display Clarify Instructions, Display Strategy Instructions, etc.
 */

const PanelView = require('./panel_view');

class InstructionsSection extends PanelView {
    /**
     * Instructions section view.
     * 
     * @param {Object} instructionsJSON - Instructions JSON from bot
     * @param {Object} currentAction - Current action object (optional)
     * @param {Object} cli - CLI instance (can be null)
     * @param {string} workspaceDirectory - Workspace directory path
     */
    constructor(instructionsJSON, currentAction, cli, workspaceDirectory, webview, extensionUri) {
        super(cli, workspaceDirectory);
        this.instructionsData = instructionsJSON || {};
        this.currentAction = currentAction || null;
        this.promptContent = '';
        this.webview = webview;
        this.extensionUri = extensionUri;
    }
    
    /**
     * Update instructions data.
     * 
     * @param {Object} instructionsJSON - Updated instructions JSON
     * @param {Object} currentAction - Updated current action (optional)
     */
    update(instructionsJSON, currentAction) {
        this.instructionsData = instructionsJSON || {};
        this.currentAction = currentAction || null;
    }
    
    /**
     * Escape HTML entities.
     * 
     * @param {string} text - Text to escape
     * @returns {string} Escaped text
     */
    escapeHtml(text) {
        if (typeof text !== 'string') {
            text = String(text);
        }
        const map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        };
        return text.replace(/[&<>"']/g, m => map[m]);
    }
    
    /**
     * Render instructions section HTML.
     * Always renders the section structure, even if empty (for consistent UI).
     * 
     * @returns {string} HTML string
     */
    render() {
        // Always render section structure, even if no instructions data
        const hasInstructions = this.instructionsData && Object.keys(this.instructionsData).length > 0;
        
        // Restructure instructions into sections
        const restructured = hasInstructions ? this.restructureInstructions() : {};
        
        // Generate sections HTML
        let sections = hasInstructions ? this.renderSections(restructured) : null;
        
        if (!sections) {
            sections = '<div class="empty-state">No instructions available. Run an action to see instructions.</div>';
        }
        
        // Escape prompt content for JavaScript
        const promptContentStr = typeof this.promptContent === 'string' ? this.promptContent : (this.promptContent ? String(this.promptContent) : '');
        const escapedPromptContent = promptContentStr.replace(/\\/g, '\\\\').replace(/'/g, "\\'").replace(/"/g, '\\"').replace(/\n/g, '\\n').replace(/\r/g, '\\r');
        
        return `
    <div class="section card-primary">
        <div class="collapsible-section expanded">
            <div class="collapsible-header" onclick="toggleSection('instructions-content')" style="
                cursor: pointer;
                padding: 4px 5px;
                background-color: transparent;
                border-left: none;
                border-radius: 2px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                user-select: none;
            ">
                <div style="display: flex; align-items: center;">
                    <span class="expand-icon" style="margin-right: 8px; font-size: 28px; transition: transform 0.15s;">▸</span>
                    <span style="margin-right: 8px; font-size: 20px;">📋</span>
                    <span style="font-weight: 600; font-size: 20px;">Instructions</span>
                </div>
                <button id="submit-to-chat-btn" onclick="sendInstructionsToChat(event)" style="
                    background: rgba(255, 140, 0, 0.15);
                    border: none;
                    border-radius: 8px;
                    padding: 6px;
                    cursor: pointer;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    transition: all 0.15s ease;
                    width: 48px;
                    height: 48px;
                    ${!promptContentStr ? 'opacity: 0.5; cursor: not-allowed;' : ''}
                " 
                onmouseover="this.style.backgroundColor='rgba(255, 140, 0, 0.3)'" 
                onmouseout="this.style.backgroundColor='rgba(255, 140, 0, 0.15)'"
                title="${promptContentStr ? 'Submit instructions to chat' : 'Run instructions command first'}">
                    🤖
                </button>
                <script>
                    window._promptContent = ${JSON.stringify(promptContentStr)};
                </script>
            </div>
            <div id="instructions-content" class="collapsible-content" style="max-height: 600px; overflow-y: auto; overflow-x: hidden; transition: max-height 0.3s ease;">
                <div class="card-secondary" style="padding: 5px 10px;">
                    ${sections}
                    
                    <!-- Raw Instructions Subsection -->
                    <div style="margin-top: 8px; padding-top: 8px; border-top: 1px solid rgba(255,255,255,0.1);">
                        <div class="collapsible-section">
                            <div class="collapsible-header" style="
                                cursor: pointer;
                                padding: 8px 0;
                                display: flex;
                                align-items: center;
                                user-select: none;
                            " onclick="toggleSection('raw-instructions-content')">
                                <span class="expand-icon" style="margin-right: 8px; font-size: 20px; transition: transform 0.15s;">▸</span>
                                <span style="margin-right: 8px; font-size: 14px;">📄</span>
                                <span style="font-weight: 600; font-size: 14px;">Raw Instructions (Test)</span>
                            </div>
                            <div id="raw-instructions-content" class="collapsible-content" style="max-height: 0; overflow: hidden; transition: max-height 0.3s ease;">
                                <div style="padding: 5px 0; margin-top: 8px;">
                                    <pre style="
                                        white-space: pre-wrap;
                                        word-wrap: break-word;
                                        font-family: 'Courier New', monospace;
                                        font-size: 11px;
                                        line-height: 1.4;
                                        color: rgba(255,255,255,0.8);
                                        background: rgba(0,0,0,0.3);
                                        padding: 6px;
                                        border-radius: 4px;
                                        margin: 0;
                                        max-height: 400px;
                                        overflow-y: auto;
                                    ">${promptContentStr ? this.escapeHtml(promptContentStr) : 'Click 🤖 Submit button or run an instructions command to populate'}</pre>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>`;
    }
    
    /**
     * Restructure instructions into sections.
     * 
     * @returns {Object} Restructured instructions
     */
    restructureInstructions() {
        const restructured = {};
        const instructions = this.instructionsData;
        const currentActionName = this.currentAction?.name || instructions.action_instructions?.name || '';
        
        // 1. BASE INSTRUCTIONS
        if (instructions.behavior_instructions || instructions.action_instructions || instructions.base_instructions) {
            let baseContent = '';
            
            if (instructions.behavior_instructions) {
                baseContent += '**Behavior Instructions**\n\n';
                if (typeof instructions.behavior_instructions === 'string') {
                    baseContent += instructions.behavior_instructions;
                }
                baseContent += '\n\n';
            }
            
            if (instructions.action_instructions) {
                baseContent += '**Action Instructions**\n\n';
                if (typeof instructions.action_instructions === 'string') {
                    baseContent += instructions.action_instructions;
                }
                baseContent += '\n\n';
            }
            
            if (instructions.base_instructions) {
                if (Array.isArray(instructions.base_instructions)) {
                    baseContent += instructions.base_instructions.map(i => `- ${i}`).join('\n');
                } else if (typeof instructions.base_instructions === 'string') {
                    baseContent += instructions.base_instructions;
                }
            }
            
            restructured.base_instructions = baseContent.trim();
        }
        
        // 2. CLARIFY - Only show when action is 'clarify'
        const hasClarificationData = instructions.clarify_instructions?.clarification_data || 
                                    instructions.clarification ||
                                    (instructions.guardrails?.required_context?.key_questions);
        
        if (hasClarificationData && currentActionName === 'clarify') {
            // Extract key_questions from guardrails if not already in clarify_instructions
            let clarificationData = instructions.clarify_instructions?.clarification_data || instructions.clarification || {};
            if (!clarificationData.key_questions && instructions.guardrails?.required_context?.key_questions) {
                clarificationData = {
                    ...clarificationData,
                    key_questions: instructions.guardrails.required_context.key_questions
                };
            }
            
            restructured.clarify_instructions = {
                clarification_data: clarificationData,
                evidence: instructions.clarify_instructions?.evidence || instructions.guardrails?.required_context?.evidence || [],
                guardrails: instructions.guardrails || instructions.clarify_instructions?.guardrails
            };
        }
        
        // 3. STRATEGY - Only show during strategy action
        const hasStrategyData = currentActionName === 'strategy' || 
                            instructions.strategy_instructions?.strategy_data || 
                            instructions.strategy;
        if (hasStrategyData) {
            restructured.strategy_instructions = {
                strategy_data: instructions.strategy_instructions?.strategy_data || instructions.strategy,
                strategy_criteria: instructions.strategy_instructions?.strategy_criteria || 
                              instructions.strategy_criteria ||
                              instructions.guardrails?.decision_criteria,
                assumptions: instructions.strategy_instructions?.assumptions || instructions.assumptions
            };
        }
        
        // 4. BUILD - Only show during build action
        const buildRelatedKeys = ['schema', 'story_graph_template', 'story_graph_config', 'rules', 'build_instructions'];
        const hasBuildData = buildRelatedKeys.some(key => instructions[key]);
        if (hasBuildData && currentActionName === 'build') {
            let schemaData = instructions.schema || instructions.build_instructions?.schema || {};
            if (instructions.story_graph_template) {
                schemaData = { ...schemaData, ...instructions.story_graph_template };
            }
            if (instructions.story_graph_config) {
                schemaData = { ...schemaData, ...instructions.story_graph_config };
            }
            restructured.build_instructions = {
                schema: Object.keys(schemaData).length > 0 ? schemaData : null,
                rules: instructions.rules || instructions.build_instructions?.rules || []
            };
        }
        
        // 5. RENDER - Only show during render action
        if (currentActionName === 'render') {
            restructured.render_instructions = {
                render_config: instructions.render_config || null,
                render_config_paths: instructions.render_config_paths || [],
                render_template_paths: instructions.render_template_paths || [],
                render_output_paths: instructions.render_output_paths || []
            };
        }
        
        // 6. VALIDATE - Only show during validate action
        if (currentActionName === 'validate' && instructions.rules) {
            restructured.validate_instructions = {
                rules: instructions.rules
            };
        }
        
        return restructured;
    }
    
    /**
     * Render instruction sections.
     * 
     * @param {Object} restructured - Restructured instructions
     * @returns {string} HTML string
     */
    renderSections(restructured) {
        const propertyConfig = {
            'base_instructions': { name: 'Base Instructions', color: '#ff8c00', icon: '📝', defaultExpanded: true },
            'clarify_instructions': { name: 'Clarify', color: '#569cd6', icon: '❓', defaultExpanded: false },
            'strategy_instructions': { name: 'Strategy', color: '#c586c0', icon: '💡', defaultExpanded: false },
            'build_instructions': { name: 'Build', color: '#4ec9b0', icon: '🔨', defaultExpanded: false },
            'render_instructions': { name: 'Render', color: '#ce9178', icon: '🎨', defaultExpanded: false },
            'validate_instructions': { name: 'Validate', color: '#dcdcaa', icon: '✓', defaultExpanded: false }
        };
        
        const validKeys = Object.keys(propertyConfig).filter(key => {
            const value = restructured[key];
            if (value === null || value === undefined) return false;
            if (typeof value === 'string' && value.trim() === '') return false;
            if (Array.isArray(value) && value.length === 0) return false;
            if (typeof value === 'object' && Object.keys(value).length === 0) return false;
            return true;
        });
        
        if (validKeys.length === 0) {
            return null;
        }
        
        return validKeys.map((key, index) => {
            const value = restructured[key];
            const config = propertyConfig[key] || { 
                name: this.formatPropertyName(key), 
                color: '#4ec9b0', 
                icon: '📄',
                defaultExpanded: false 
            };
            
            const sectionId = `instr-section-${index}`;
            const expandedClass = config.defaultExpanded ? 'expanded' : '';
            
            let contentHtml;
            if (key === 'clarify_instructions') {
                contentHtml = this.formatClarifyInstructions(value);
            } else if (key === 'strategy_instructions') {
                contentHtml = this.formatStrategyInstructions(value);
            } else if (key === 'build_instructions') {
                contentHtml = this.formatBuildInstructions(value);
            } else if (key === 'render_instructions') {
                contentHtml = this.formatRenderInstructions(value);
            } else if (key === 'validate_instructions') {
                contentHtml = this.formatValidateInstructions(value);
            } else {
                contentHtml = this.formatInstructionValue(value, config.color);
            }
            
            return `
        <div class="collapsible-section ${expandedClass}" style="margin-bottom: 8px;">
          <div class="collapsible-header" onclick="toggleSection('${sectionId}')" style="
            cursor: pointer;
            padding: 4px 5px;
            background-color: transparent;
            border-left: none;
            border-radius: 2px;
            display: flex;
            align-items: center;
            user-select: none;
          ">
            <span class="expand-icon" style="margin-right: 8px; font-size: 28px; transition: transform 0.15s;">▸</span>
            <span style="margin-right: 8px; font-size: 16px;">${config.icon}</span>
            <span style="font-weight: 600; color: var(--vscode-foreground); font-size: 14px;">${config.name}</span>
          </div>
          <div id="${sectionId}" class="collapsible-content" style="
            max-height: ${config.defaultExpanded ? 'none' : '0'};
            overflow: ${config.defaultExpanded ? 'visible' : 'hidden'};
            transition: max-height 0.3s ease;
          ">
            <div style="padding: 5px; background-color: transparent; margin-top: 2px;">
              ${contentHtml}
            </div>
          </div>
        </div>`;
        }).join('');
    }
    
    /**
     * Format property name.
     * 
     * @param {string} key - Property key
     * @returns {string} Formatted name
     */
    formatPropertyName(key) {
        return key
            .replace(/_/g, ' ')
            .replace(/([A-Z])/g, ' $1')
            .split(' ')
            .map(word => word.charAt(0).toUpperCase() + word.slice(1))
            .join(' ')
            .trim();
    }
    
    /**
     * Format instruction value.
     * 
     * @param {*} value - Instruction value
     * @param {string} color - Color
     * @returns {string} HTML string
     */
    formatInstructionValue(value, color) {
        if (typeof value === 'string') {
            return `<div style="white-space: pre-wrap; word-wrap: break-word; color: ${color};">${this.escapeHtml(value)}</div>`;
        } else if (Array.isArray(value)) {
            return '<ul>' + value.map(item => `<li>${this.escapeHtml(String(item))}</li>`).join('') + '</ul>';
        } else if (typeof value === 'object' && value !== null) {
            return '<pre>' + this.escapeHtml(JSON.stringify(value, null, 2)) + '</pre>';
        }
        return '';
    }
    
    /**
     * Format clarify instructions.
     * 
     * @param {Object} value - Clarify instructions object
     * @returns {string} HTML string
     */
    formatClarifyInstructions(value) {
        if (typeof value !== 'object' || !value) {
            return '';
        }
        
        let html = '';
        
        // Key questions
        if (value.clarification_data && value.clarification_data.key_questions) {
            html += '<h3>Key Questions</h3>';
            html += '<div class="key-questions">';
            const questions = Array.isArray(value.clarification_data.key_questions) 
                ? value.clarification_data.key_questions 
                : (value.clarification_data.key_questions.questions || []);
            questions.forEach((question, idx) => {
                const questionText = typeof question === 'string' ? question : (question.question || question.text || '');
                const answer = typeof question === 'object' && question.answer ? question.answer : '';
                html += `<div class="question" style="margin-bottom: 8px;">
                    <label style="display: block; margin-bottom: 4px;">${this.escapeHtml(questionText)}</label>
                    <textarea id="answer-${idx}" style="width: 100%; min-height: 60px; padding: 4px;" onchange="updateAnswer(${idx}, this.value)">${this.escapeHtml(answer)}</textarea>
                </div>`;
            });
            html += '</div>';
        }
        
        // Evidence
        if (value.evidence && value.evidence.length > 0) {
            html += '<h3>Evidence Requirements</h3>';
            html += '<div class="evidence-section">';
            html += '<ul>';
            value.evidence.forEach(evidence => {
                const evidenceText = typeof evidence === 'string' ? evidence : (evidence.text || evidence.requirement || '');
                html += `<li>${this.escapeHtml(evidenceText)}</li>`;
            });
            html += '</ul>';
            html += '</div>';
        }
        
        return html || '<div class="empty-state">No clarify instructions available</div>';
    }
    
    /**
     * Format strategy instructions.
     * 
     * @param {Object} value - Strategy instructions object
     * @returns {string} HTML string
     */
    formatStrategyInstructions(value) {
        if (typeof value !== 'object' || !value) {
            return '';
        }
        
        let html = '';
        
        // Decision criteria
        if (value.strategy_criteria) {
            html += '<h3>Decision Criteria</h3>';
            html += '<ul>';
            const criteria = Array.isArray(value.strategy_criteria) ? value.strategy_criteria : Object.values(value.strategy_criteria);
            criteria.forEach(criterion => {
                const criterionText = typeof criterion === 'string' ? criterion : (criterion.question || criterion.text || '');
                html += `<li>${this.escapeHtml(criterionText)}</li>`;
            });
            html += '</ul>';
        }
        
        // Assumptions
        if (value.assumptions) {
            html += '<h3>Assumptions</h3>';
            const assumptionsText = typeof value.assumptions === 'string' ? value.assumptions : JSON.stringify(value.assumptions);
            html += `<div style="white-space: pre-wrap;">${this.escapeHtml(assumptionsText)}</div>`;
        }
        
        return html || '<div class="empty-state">No strategy instructions available</div>';
    }
    
    /**
     * Format build instructions.
     * 
     * @param {Object} value - Build instructions object
     * @returns {string} HTML string
     */
    formatBuildInstructions(value) {
        if (typeof value !== 'object' || !value) {
            return '';
        }
        
        let html = '';
        
        // Schema
        if (value.schema) {
            html += '<h3>Story Graph Schema</h3>';
            html += '<pre>' + this.escapeHtml(JSON.stringify(value.schema, null, 2)) + '</pre>';
        }
        
        // Rules
        if (value.rules && value.rules.length > 0) {
            html += '<h3>Rules</h3>';
            html += '<ul>';
            value.rules.forEach(rule => {
                const ruleText = typeof rule === 'string' ? rule : (rule.name || rule.description || JSON.stringify(rule));
                html += `<li>${this.escapeHtml(ruleText)}</li>`;
            });
            html += '</ul>';
        }
        
        return html || '<div class="empty-state">No build instructions available</div>';
    }
    
    /**
     * Format render instructions.
     * 
     * @param {Object} value - Render instructions object
     * @returns {string} HTML string
     */
    formatRenderInstructions(value) {
        if (typeof value !== 'object' || !value) {
            return '';
        }
        
        let html = '';
        
        if (value.render_config) {
            html += '<h3>Render Configuration</h3>';
            html += '<pre>' + this.escapeHtml(JSON.stringify(value.render_config, null, 2)) + '</pre>';
        }
        
        if (value.render_template_paths && value.render_template_paths.length > 0) {
            html += '<h3>Template Paths</h3>';
            html += '<ul>';
            value.render_template_paths.forEach(path => {
                html += `<li>${this.escapeHtml(path)}</li>`;
            });
            html += '</ul>';
        }
        
        return html || '<div class="empty-state">No render instructions available</div>';
    }
    
    /**
     * Format validate instructions.
     * 
     * @param {Object} value - Validate instructions object
     * @returns {string} HTML string
     */
    formatValidateInstructions(value) {
        if (typeof value !== 'object' || !value) {
            return '';
        }
        
        let html = '';
        
        if (value.rules && value.rules.length > 0) {
            html += '<h3>Validation Rules</h3>';
            html += '<ul>';
            value.rules.forEach(rule => {
                const ruleText = typeof rule === 'string' ? rule : (rule.name || rule.description || JSON.stringify(rule));
                html += `<li>${this.escapeHtml(ruleText)}</li>`;
            });
            html += '</ul>';
        }
        
        return html || '<div class="empty-state">No validate instructions available</div>';
    }
}

module.exports = InstructionsSection;
