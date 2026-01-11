/**
 * BotView - Main panel orchestrator that wraps bot JSON and displays all domain views.
 * 
 * Epic: Invoke Bot Through Panel
 * Sub-Epic: Manage Panel Session
 * Story: Open Panel, Display Session Status
 */

const PanelView = require('../panel_view');
const BotHeaderView = require('./bot_header_view');
const BehaviorsView = require('../behaviors_view');
const ScopeSection = require('../scope_view');
const InstructionsSection = require('../instructions_view');

class BotView extends PanelView {
    /**
     * Main panel orchestrator.
     * 
     * @param {Object} botJSON - Bot JSON from CLI (status command returns Bot object)
     * @param {Object} cli - CLI instance for subprocess communication (can be null)
     * @param {string} workspaceDirectory - Workspace directory path
     * @param {string} botDirectory - Bot directory path (optional)
     * @param {string} panelVersion - Panel version string (optional)
     * @param {Object} webview - VS Code webview instance (required for image URIs)
     * @param {Object} extensionUri - VS Code extension URI (required for image URIs)
     */
    constructor(botJSON, cli, workspaceDirectory, botDirectory, panelVersion, webview, extensionUri) {
        try {
            console.log(`[BotView] Constructor called - workspaceDirectory: ${workspaceDirectory}, webview: ${!!webview}, extensionUri: ${!!extensionUri}`);
        super(cli, workspaceDirectory, botDirectory);
        this.botData = botJSON;
        this.panelVersion = panelVersion || null;
            this.webview = webview;
            this.extensionUri = extensionUri;
        
        // Initialize domain views
            console.log("[BotView] Creating BotHeaderView");
            this.headerView = new BotHeaderView(botJSON, cli, workspaceDirectory, this.panelVersion, webview, extensionUri);
        // Behaviors JSON structure: { current: string, names: string[], all_behaviors: array }
        const behaviorsData = botJSON.behaviors?.all_behaviors || [];
            console.log("[BotView] Creating BehaviorsView");
            this.behaviorsView = new BehaviorsView(behaviorsData, cli, workspaceDirectory, webview, extensionUri);
            console.log("[BotView] Creating ScopeSection");
            this.scopeSection = new ScopeSection(botJSON.scope || {}, cli, workspaceDirectory, webview, extensionUri);
            console.log("[BotView] Creating InstructionsSection");
        this.instructionsSection = new InstructionsSection(
            botJSON.instructions || {}, 
            botJSON.current_action || null,
            cli, 
                workspaceDirectory,
                webview,
                extensionUri
            );
            console.log("[BotView] Constructor completed successfully");
        } catch (error) {
            console.error(`[BotView] ERROR in constructor: ${error.message}`);
            console.error(`[BotView] ERROR stack: ${error.stack}`);
            throw error;
        }
    }
    
    /**
     * Render complete bot view HTML.
     * 
     * @returns {string} Complete HTML string
     */
    render() {
        return `
            <div class="bot-view">
                ${this.headerView.render()}
                ${this.behaviorsView.render()}
                ${this.scopeSection.render()}
                ${this.instructionsSection.render()}
            </div>
        `;
    }
    
    /**
     * Update bot data and refresh all domain views.
     * 
     * @param {Object} botJSON - Updated bot JSON
     */
    update(botJSON) {
        this.botData = botJSON;
        this.headerView.update(botJSON);
        // Behaviors JSON structure: { current: string, names: string[], all_behaviors: array }
        const behaviorsData = botJSON.behaviors?.all_behaviors || [];
        this.behaviorsView.update(behaviorsData);
        this.scopeSection.update(botJSON.scope || {});
        this.instructionsSection.update(botJSON.instructions || {}, botJSON.current_action || null);
    }
    
    /**
     * Execute command and return appropriate data.
     * Overrides PanelView.execute() to extract data from unified JSON response.
     * 
     * @param {string} command - Command to execute
     * @returns {Promise<Object>} Extracted data (bot JSON for status, unified response for actions)
     */
    async execute(command) {
        const response = await super.execute(command);
        
        // In JSON mode, CLI returns unified structure: { execution?, instructions?, bot, scope? }
        // For "status" command, return bot data (response is already { bot: ... })
        if (command === 'status' && response.bot) {
            return response.bot;
        }
        
        // For "scope" command, return scope data with bot
        if (command === 'scope' && response.scope) {
            // Update botData with the bot portion
            if (response.bot) {
                this.update(response.bot);
            }
            return response;
        }
        
        // For action commands, return unified response (contains execution, instructions, bot)
        // Update botData with the bot portion
        if (response.bot) {
            this.update(response.bot);
        }
        
        return response;
    }
    
    /**
     * Refresh data from CLI.
     * 
     * @returns {Promise<Object>} Updated bot JSON
     */
    async refresh() {
        if (!this.cli) {
            throw new Error('CLI instance required for refresh');
        }
        // "status" command returns the Bot object itself
        const botJSON = await this.execute('status');
        this.update(botJSON);
        return botJSON;
    }
    
    /**
     * Handle user events.
     * 
     * @param {string} eventType - Type of event
     * @param {Object} eventData - Event data
     * @returns {Promise<Object>} Updated data or result
     */
    async handleEvent(eventType, eventData) {
        switch (eventType) {
            case 'refresh':
                return await this.refresh();
            case 'executeBehavior':
                return await this.behaviorsView.handleEvent('execute', eventData);
            case 'updateScope':
                return await this.scopeSection.handleEvent('updateFilter', eventData);
            case 'updateWorkspace':
                return await this.pathsSection.handleEvent('updateWorkspace', eventData);
            case 'switchBot':
                return await this.headerView.handleEvent('switchBot', eventData);
            default:
                throw new Error(`Unknown event type: ${eventType}`);
        }
    }
}

module.exports = BotView;
