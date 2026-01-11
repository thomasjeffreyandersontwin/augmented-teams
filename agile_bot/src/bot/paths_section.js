/**
 * PathsSection - Renders workspace path and bot directory paths.
 * 
 * Epic: Invoke Bot Through Panel
 * Sub-Epic: Manage Panel Session
 * Story: Change Workspace Path
 */

const PanelView = require('../panel/panel_view');

class PathsSection extends PanelView {
    /**
     * Paths section view.
     * 
     * @param {Object} botJSON - Bot JSON from CLI (contains bot_paths or workspace_directory, bot_directory)
     * @param {Object} cli - CLI instance (can be null)
     * @param {string} workspaceDirectory - Workspace directory path
     */
    constructor(botJSON, cli, workspaceDirectory) {
        super(cli, workspaceDirectory);
        this.botData = botJSON;
        this.workspaceDirectory = botJSON.workspace_directory || workspaceDirectory || '';
        this.botDirectory = botJSON.bot_directory || '';
    }
    
    /**
     * Update paths data.
     * 
     * @param {Object} botJSON - Updated bot JSON
     */
    update(botJSON) {
        this.botData = botJSON;
        this.workspaceDirectory = botJSON.workspace_directory || this.workspaceDirectory || '';
        this.botDirectory = botJSON.bot_directory || '';
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
     * Truncate path with ellipsis if too long.
     * 
     * @param {string} path - Path to truncate
     * @param {number} maxLength - Maximum length
     * @returns {string} Truncated path
     */
    truncatePath(path, maxLength) {
        if (!path || path.length <= maxLength) {
            return path;
        }
        const ellipsis = '...';
        const prefixLength = Math.floor((maxLength - ellipsis.length) / 2);
        const suffixLength = maxLength - ellipsis.length - prefixLength;
        return path.substring(0, prefixLength) + ellipsis + path.substring(path.length - suffixLength);
    }
    
    /**
     * Render paths section HTML.
     * 
     * @returns {string} HTML string
     */
    render() {
        const maxPathLength = 80;
        const safeWorkspaceDir = this.escapeHtml(this.workspaceDirectory);
        const safeBotDir = this.escapeHtml(this.botDirectory);
        const displayWorkspaceDir = this.truncatePath(safeWorkspaceDir, maxPathLength);
        const displayBotDir = this.truncatePath(safeBotDir, maxPathLength);
        
        return `
            <div class="card-secondary" style="padding: 1px 5px 2px 5px;">
                <div class="input-container" style="margin-top: 0;">
                    <div class="input-header">Workspace</div>
                    <input type="text" id="workspacePathInput" 
                           value="${safeWorkspaceDir}" 
                           placeholder="Path to workspace"
                           onchange="updateWorkspace(this.value)"
                           onkeydown="if(event.key === 'Enter') { event.preventDefault(); updateWorkspace(this.value); }"
                           title="${safeWorkspaceDir}" />
                </div>
                <div class="info-display" style="margin-top: 4px;" title="${safeBotDir}">
                    <span class="label">Bot Path:</span>
                    <span class="value">${displayBotDir}</span>
                </div>
            </div>`;
    }
    
    /**
     * Handle events.
     * 
     * @param {string} eventType - Event type
     * @param {Object} eventData - Event data
     * @returns {Promise<Object>} Result
     */
    async handleEvent(eventType, eventData) {
        if (eventType === 'updateWorkspace') {
            // Update workspace logic would go here
            // For now, just return success
            return { success: true, workspace: eventData.workspacePath };
        }
        throw new Error(`Unknown event type: ${eventType}`);
    }
}

module.exports = PathsSection;
