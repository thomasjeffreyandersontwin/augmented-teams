/**
 * BotHeaderView - Renders bot header section with bot name, version, refresh button, and bot selector.
 * 
 * Epic: Invoke Bot Through Panel
 * Sub-Epic: Manage Panel Session
 * Story: Open Panel, Display Session Status, Switch Bot
 */

const PanelView = require('../panel_view');
const vscode = require('vscode');

class BotHeaderView extends PanelView {
    /**
     * Bot header view.
     * 
     * @param {Object} botJSON - Bot JSON from CLI
     * @param {Object} cli - CLI instance (can be null)
     * @param {string} workspaceDirectory - Workspace directory path
     * @param {string} panelVersion - Panel extension version (optional)
     */
    constructor(botJSON, cli, workspaceDirectory, panelVersion, webview, extensionUri) {
        super(cli, workspaceDirectory);
        this.botData = botJSON;
        this.availableBots = botJSON.available_bots || [];
        this.currentBot = botJSON.name || botJSON.bot_name || 'story_bot';
        this.panelVersion = panelVersion || null;
        this.webview = webview;
        this.extensionUri = extensionUri;
    }
    
    /**
     * Update bot data.
     * 
     * @param {Object} botJSON - Updated bot JSON
     */
    update(botJSON) {
        this.botData = botJSON;
        this.availableBots = botJSON.available_bots || [];
        this.currentBot = botJSON.name || botJSON.bot_name || 'story_bot';
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
     * Get image URI for a given image filename.
     * 
     * @param {string} filename - Image filename (e.g., 'company_icon.png')
     * @returns {string} Image URI string or empty string if webview/extensionUri not available
     */
    getImageUri(filename) {
        try {
            if (!this.webview || !this.extensionUri) {
                console.warn(`[BotHeaderView] getImageUri(${filename}) - webview or extensionUri not available`);
                return '';
            }
            const uri = this.webview.asWebviewUri(vscode.Uri.joinPath(this.extensionUri, 'img', filename)).toString();
            console.log(`[BotHeaderView] getImageUri(${filename}) - returning URI: ${uri}`);
            return uri;
        } catch (error) {
            console.error(`[BotHeaderView] ERROR in getImageUri(${filename}): ${error.message}`);
            console.error(`[BotHeaderView] ERROR stack: ${error.stack}`);
            return '';
        }
    }
    
    /**
     * Truncate path with ellipsis if too long.
     * 
     * @param {string} path - Path to truncate
     * @param {number} maxLength - Maximum length
     * @returns {string} Truncated path
     */
    truncatePath(path, maxLength) {
        if (!path || path.length <= maxLength) return path;
        const ellipsis = '...';
        const start = path.substring(0, Math.floor((maxLength - ellipsis.length) / 2));
        const end = path.substring(path.length - Math.ceil((maxLength - ellipsis.length) / 2));
        return start + ellipsis + end;
    }
    
    /**
     * Render bot header HTML.
     * 
     * @returns {string} HTML string
     */
    render() {
        const maxPathLength = 80;
        const safeBotName = this.escapeHtml(this.botData.name || this.currentBot);
        const safeBotDir = this.escapeHtml(this.botData.botDirectory || this.botData.bot_directory || '');
        const safeWorkspaceDir = this.escapeHtml(this.botData.workspaceDirectory || this.botData.workspace_directory || this.workspaceDirectory || '');
        const displayBotDir = this.truncatePath(safeBotDir, maxPathLength);
        const displayWorkspaceDir = this.truncatePath(safeWorkspaceDir, maxPathLength);

        // Build bot selector links
        let botLinksHtml = '';
        if (this.availableBots && this.availableBots.length > 0) {
            botLinksHtml = this.availableBots.map(botName => {
                const isActive = botName === this.currentBot;
                const activeClass = isActive ? ' active' : '';
                return `<a href="javascript:void(0)" class="bot-link${activeClass}" onclick="switchBot('${this.escapeHtml(botName)}')">${this.escapeHtml(botName)}</a>`;
            }).join('\n                ');
        }

        // Get image URIs
        const imagePath = this.getImageUri('company_icon.png');
        const refreshIconPath = this.getImageUri('refresh.png');
        const storyIconPath = this.getImageUri('story.png');
        const crcIconPath = this.getImageUri('crc.png');

        const versionHtml = this.panelVersion
            ? `<span style="font-size: 14px; opacity: 0.7; margin-left: 6px;">v${this.escapeHtml(this.panelVersion)}</span>`
            : '';

        return `
    <div class="section card-primary" style="border-top: none; padding-top: 0;">
        <div class="main-header">
            ${imagePath ? `<img src="${imagePath}" class="main-header-icon" alt="Company Icon" onerror="console.error('Failed to load icon:', this.src); this.style.border='1px solid red';" />` : ''}
            <span class="main-header-title">Agile Bots ${versionHtml}</span>
            <button class="main-header-refresh" onclick="refreshStatus()" title="Refresh">
                ${refreshIconPath ? `<img src="${refreshIconPath}" style="width: 36px; height: 36px; object-fit: contain; filter: saturate(1.3) brightness(0.95) hue-rotate(-5deg);" alt="Refresh" />` : ''}
            </button>
        </div>
        <div class="collapsible-section expanded">
            <div class="collapsible-header" onclick="toggleSection('header-content')" style="
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
                    ${this.currentBot === 'story_bot' && storyIconPath
                        ? `<img src="${storyIconPath}" style="margin-right: 8px; width: 36px; height: 36px; object-fit: contain;" alt="Story Bot Icon" />`
                        : this.currentBot === 'crc_bot' && crcIconPath
                        ? `<img src="${crcIconPath}" style="margin-right: 8px; width: 36px; height: 36px; object-fit: contain;" alt="CRC Bot Icon" />`
                        : ''}
                    <span style="font-weight: 600; font-size: 20px;">${safeBotName}</span>
                </div>
                <div class="bot-links" onclick="event.stopPropagation();" style="gap: 6px;">
                    ${botLinksHtml}
                </div>
            </div>
            <div id="header-content" class="collapsible-content" style="max-height: 2000px; overflow: hidden; transition: max-height 0.3s ease;">
                <div class="card-secondary" style="padding: 1px 5px 2px 5px;">
                    <div class="input-container" style="margin-top: 0;">
                        <div class="input-header">Workspace</div>
                        <input type="text" id="workspacePathInput"
                               value="${displayWorkspaceDir}"
                               placeholder="Path to workspace"
                               onchange="updateWorkspace(this.value)"
                               onkeydown="if(event.key === 'Enter') { event.preventDefault(); updateWorkspace(this.value); }"
                               title="${safeWorkspaceDir}" />
                    </div>
                    <div class="info-display" style="margin-top: 4px;" title="${safeBotDir}">
                        <span class="label">Bot Path:</span>
                        <span class="value">${displayBotDir}</span>
                    </div>
                </div>
            </div>
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
        if (eventType === 'switchBot') {
            // Switch bot logic would go here
            // For now, just return success
            return { success: true, bot: eventData.botName };
        }
        throw new Error(`Unknown event type: ${eventType}`);
    }
}

module.exports = BotHeaderView;
