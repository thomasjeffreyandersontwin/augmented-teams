/**
 * BehaviorsView - Renders behavior hierarchy with actions and operations.
 * 
 * Epic: Invoke Bot Through Panel
 * Sub-Epic: Navigate And Execute Behaviors Through Panel
 * Story: Display Hierarchy, Navigate Behavior Action, Execute Behavior Action
 */

const PanelView = require('./panel_view');
const vscode = require('vscode');

class BehaviorsView extends PanelView {
    /**
     * Behaviors view.
     * 
     * @param {Array} behaviorsJSON - Behaviors array from bot JSON
     * @param {Object} cli - CLI instance (can be null)
     * @param {string} workspaceDirectory - Workspace directory path
     * @param {Object} webview - VS Code webview instance (required for image URIs)
     * @param {Object} extensionUri - VS Code extension URI (required for image URIs)
     */
    constructor(behaviorsJSON, cli, workspaceDirectory, webview, extensionUri) {
        try {
            console.log(`[BehaviorsView] Constructor called - webview: ${!!webview}, extensionUri: ${!!extensionUri}`);
            super(cli, workspaceDirectory);
            this.behaviorsData = behaviorsJSON || [];
            this.expansionState = {};
            this.webview = webview;
            this.extensionUri = extensionUri;
            console.log("[BehaviorsView] Constructor completed successfully");
        } catch (error) {
            console.error(`[BehaviorsView] ERROR in constructor: ${error.message}`);
            console.error(`[BehaviorsView] ERROR stack: ${error.stack}`);
            throw error;
        }
    }
    
    /**
     * Update behaviors data.
     * 
     * @param {Array} behaviorsJSON - Updated behaviors array
     */
    update(behaviorsJSON) {
        this.behaviorsData = behaviorsJSON || [];
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
     * @param {string} filename - Image filename (e.g., 'gear.png')
     * @returns {string} Image URI string or empty string if webview/extensionUri not available
     */
    getImageUri(filename) {
        try {
            if (!this.webview || !this.extensionUri) {
                console.warn(`[BehaviorsView] getImageUri(${filename}) - webview or extensionUri not available`);
                return '';
            }
            const uri = this.webview.asWebviewUri(vscode.Uri.joinPath(this.extensionUri, 'img', filename));
            const uriString = uri.toString();
            console.log(`[BehaviorsView] getImageUri(${filename}) - returning URI string: ${uriString}`);
            return uriString;
        } catch (error) {
            console.error(`[BehaviorsView] ERROR in getImageUri(${filename}): ${error.message}`);
            console.error(`[BehaviorsView] ERROR stack: ${error.stack}`);
            return '';
        }
    }
    
    /**
     * Get status marker for behavior/action/operation.
     * 
     * @param {boolean} isCurrent - Is current item
     * @param {boolean} isCompleted - Is completed item
     * @returns {string} Marker HTML
     */
    getStatusMarker(isCurrent, isCompleted) {
        if (!this.webview || !this.extensionUri) {
            return '<span class="status-marker"></span>';
        }
        if (isCurrent) {
            const arrowUri = this.getImageUri('right.png');
            return `<img src="${arrowUri}" class="status-marker marker-current" style="width: 16px; height: 16px;" />`;
        } else if (isCompleted) {
            const tickUri = this.getImageUri('tick.png');
            return `<img src="${tickUri}" class="status-marker marker-completed" style="width: 16px; height: 16px;" />`;
        } else {
            const notTickedUri = this.getImageUri('not_ticked.png');
            return `<img src="${notTickedUri}" class="status-marker marker-pending" style="width: 16px; height: 16px;" />`;
        }
    }
    
    /**
     * Render behaviors hierarchy HTML.
     * 
     * @returns {string} HTML string
     */
    render() {
        if (!this.behaviorsData || this.behaviorsData.length === 0) {
            return this.renderEmpty();
        }
        
        const behaviorsHtml = this.behaviorsData.map((behavior, bIdx) => {
            return this.renderBehavior(behavior, bIdx);
        }).join('');
        
        const gearUri = this.getImageUri('gear.png');
        const leftUri = this.getImageUri('left.png');
        const rightUri = this.getImageUri('right.png');
        const bullseyeUri = this.getImageUri('bullseye.png');
        
        return `
    <div class="section card-primary">
        <div class="collapsible-section expanded">
            <div class="collapsible-header" onclick="toggleSection('behaviors-content')" style="
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
                ${gearUri ? `<img src="${gearUri}" style="margin-right: 8px; width: 20px; height: 20px;" />` : ''}
                <span style="font-weight: 600; font-size: 20px;">Behavior Action Status</span>
            </div>
            <div id="behaviors-content" class="collapsible-content" style="max-height: 2000px; overflow: hidden; transition: max-height 0.3s ease;">
                <div class="card-secondary" style="padding: 5px;">
                    ${behaviorsHtml}
                    <div style="margin-top: 8px; padding-top: 5px; border-top: none; display: flex; gap: 4px; flex-wrap: wrap;">
                        <button onclick="executeNavigationCommand('back')" title="Back - Go to previous action" style="
                            background-color: var(--vscode-button-secondaryBackground);
                            color: var(--vscode-button-secondaryForeground);
                            border: none;
                            padding: 4px 6px;
                            cursor: pointer;
                            border-radius: 2px;
                            font-size: 16px;
                            font-family: inherit;
                            line-height: 1;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                        ">${leftUri ? `<img src="${leftUri}" style="width: 16px; height: 16px;" />` : ''}</button>
                        <button onclick="executeNavigationCommand('current')" title="Current - Show current action details" style="
                            background-color: var(--vscode-button-secondaryBackground);
                            color: var(--vscode-button-secondaryForeground);
                            border: none;
                            padding: 4px 6px;
                            cursor: pointer;
                            border-radius: 2px;
                            font-size: 16px;
                            font-family: inherit;
                            line-height: 1;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                        ">${bullseyeUri ? `<img src="${bullseyeUri}" style="width: 16px; height: 16px;" />` : ''}</button>
                        <button onclick="executeNavigationCommand('next')" title="Next - Advance to next action" style="
                            background-color: var(--vscode-button-secondaryBackground);
                            color: var(--vscode-button-secondaryForeground);
                            border: none;
                            padding: 4px 6px;
                            cursor: pointer;
                            border-radius: 2px;
                            font-size: 16px;
                            font-family: inherit;
                            line-height: 1;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                        ">${rightUri ? `<img src="${rightUri}" style="width: 16px; height: 16px;" />` : ''}</button>
                    </div>
                </div>
            </div>
        </div>
    </div>`;
    }
    
    /**
     * Render empty state.
     * 
     * @returns {string} HTML string
     */
    renderEmpty() {
        const gearUri = this.getImageUri('gear.png');
        const leftUri = this.getImageUri('left.png');
        const rightUri = this.getImageUri('right.png');
        const bullseyeUri = this.getImageUri('bullseye.png');
        
        return `
    <div class="section card-primary">
        <div class="collapsible-section expanded">
            <div class="collapsible-header" onclick="toggleSection('behaviors-content')" style="
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
                ${gearUri ? `<img src="${gearUri}" style="margin-right: 8px; width: 20px; height: 20px;" />` : ''}
                <span style="font-weight: 600; font-size: 20px;">Behavior Action Status</span>
            </div>
            <div id="behaviors-content" class="collapsible-content" style="max-height: 2000px; overflow: hidden; transition: max-height 0.3s ease;">
                <div class="card-secondary" style="padding: 5px;">
                    <div class="empty-state">No behaviors available</div>
                    <div style="margin-top: 8px; padding-top: 5px; border-top: none; display: flex; gap: 4px; flex-wrap: wrap;">
                        <button onclick="executeNavigationCommand('back')" title="Back - Go to previous action" style="
                            background-color: var(--vscode-button-secondaryBackground);
                            color: var(--vscode-button-secondaryForeground);
                            border: none;
                            padding: 4px 6px;
                            cursor: pointer;
                            border-radius: 2px;
                            font-size: 16px;
                            font-family: inherit;
                            line-height: 1;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                        ">${leftUri ? `<img src="${leftUri}" style="width: 16px; height: 16px;" />` : ''}</button>
                        <button onclick="executeNavigationCommand('current')" title="Current - Show current action details" style="
                            background-color: var(--vscode-button-secondaryBackground);
                            color: var(--vscode-button-secondaryForeground);
                            border: none;
                            padding: 4px 6px;
                            cursor: pointer;
                            border-radius: 2px;
                            font-size: 16px;
                            font-family: inherit;
                            line-height: 1;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                        ">${bullseyeUri ? `<img src="${bullseyeUri}" style="width: 16px; height: 16px;" />` : ''}</button>
                        <button onclick="executeNavigationCommand('next')" title="Next - Advance to next action" style="
                            background-color: var(--vscode-button-secondaryBackground);
                            color: var(--vscode-button-secondaryForeground);
                            border: none;
                            padding: 4px 6px;
                            cursor: pointer;
                            border-radius: 2px;
                            font-size: 16px;
                            font-family: inherit;
                            line-height: 1;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                        ">${rightUri ? `<img src="${rightUri}" style="width: 16px; height: 16px;" />` : ''}</button>
                    </div>
                </div>
            </div>
        </div>
    </div>`;
    }
    
    /**
     * Render a single behavior.
     * 
     * @param {Object} behavior - Behavior object
     * @param {number} bIdx - Behavior index
     * @returns {string} HTML string
     */
    renderBehavior(behavior, bIdx) {
        const isCurrent = behavior.is_current || false;
        const isCompleted = behavior.is_completed || false;
        const behaviorMarker = this.getStatusMarker(isCurrent, isCompleted);
        const behaviorTooltip = behavior.description ? this.escapeHtml(behavior.description) : '';
        const behaviorId = `behavior-${bIdx}`;
        const behaviorName = this.escapeHtml(behavior.name || '');
        
        // Get plus/subtract icon paths
        const plusIconPath = this.getImageUri('plus.png');
        const subtractIconPath = this.getImageUri('subtract.png');
        
        // Expansion logic: expand if current or completed
        const hasExpansionState = this.expansionState && (behaviorId in this.expansionState);
        const behaviorExpanded = hasExpansionState ? this.expansionState[behaviorId] : (isCurrent || isCompleted);
        const behaviorDisplay = behaviorExpanded ? 'block' : 'none';
        const behaviorIconSrc = behaviorExpanded ? subtractIconPath : plusIconPath;
        const behaviorIconAlt = behaviorExpanded ? 'Collapse' : 'Expand';
        const behaviorIconClass = behaviorExpanded ? 'expanded' : '';
        
        const behaviorActiveClass = isCurrent ? ' active' : '';
        let html = `<div class="collapsible-header card-item${behaviorActiveClass}" title="${behaviorTooltip}"><span id="${behaviorId}-icon" class="${behaviorIconClass}" style="display: inline-block; min-width: 12px; cursor: pointer;" onclick="toggleCollapse('${behaviorId}')" data-plus="${plusIconPath}" data-subtract="${subtractIconPath}">${plusIconPath && subtractIconPath ? `<img src="${behaviorIconSrc}" alt="${behaviorIconAlt}" style="width: 12px; height: 12px; vertical-align: middle;" />` : ''}</span> <span style="cursor: pointer; text-decoration: underline;" onclick="navigateToBehavior('${behaviorName}')">${behaviorMarker}${behaviorName}</span></div>`;
        
        // Render actions - check both array format and {all_actions: [...]} format
        // Old renderer uses: behavior.actions directly (assumes it's an array)
        let actionsArray = [];
        if (behavior.actions) {
            if (Array.isArray(behavior.actions)) {
                actionsArray = behavior.actions;
            } else if (behavior.actions.all_actions && Array.isArray(behavior.actions.all_actions)) {
                actionsArray = behavior.actions.all_actions;
            }
        }
        const hasActions = actionsArray.length > 0;
        const actionsHtml = hasActions ? actionsArray.map((action, aIdx) => {
            return this.renderAction(action, bIdx, aIdx, behaviorName);
        }).join('') : '';
        
        html += `<div id="${behaviorId}" class="collapsible-content" style="display: ${behaviorDisplay};">${actionsHtml}</div>`;
        
        return html;
    }
    
    /**
     * Render a single action.
     * 
     * @param {Object} action - Action object
     * @param {number} bIdx - Behavior index
     * @param {number} aIdx - Action index
     * @param {string} behaviorName - Behavior name (escaped)
     * @returns {string} HTML string
     */
    renderAction(action, bIdx, aIdx, behaviorName) {
        const isCurrent = action.is_current || false;
        const isCompleted = action.is_completed || false;
        const actionMarker = this.getStatusMarker(isCurrent, isCompleted);
        const actionTooltip = action.description ? this.escapeHtml(action.description) : '';
        const actionId = `action-${bIdx}-${aIdx}`;
        const actionName = this.escapeHtml(action.name || '');
        
        // Get plus/subtract icon paths
        const plusIconPath = this.getImageUri('plus.png');
        const subtractIconPath = this.getImageUri('subtract.png');
        
        // Expansion logic: expand if current or completed
        const hasActionExpansionState = this.expansionState && (actionId in this.expansionState);
        const actionExpanded = hasActionExpansionState ? this.expansionState[actionId] : (isCurrent || isCompleted);
        const actionDisplay = actionExpanded ? 'block' : 'none';
        const actionIconSrc = actionExpanded ? subtractIconPath : plusIconPath;
        const actionIconAlt = actionExpanded ? 'Collapse' : 'Expand';
        const actionIconClass = actionExpanded ? 'expanded' : '';
        
        const actionActiveClass = isCurrent ? ' active' : '';
        let actionHtml = `<div class="collapsible-header action-item card-item${actionActiveClass}" title="${actionTooltip}"><span id="${actionId}-icon" class="${actionIconClass}" style="display: inline-block; min-width: 9px; cursor: pointer;" onclick="toggleCollapse('${actionId}')" data-plus="${plusIconPath}" data-subtract="${subtractIconPath}">${plusIconPath && subtractIconPath ? `<img src="${actionIconSrc}" alt="${actionIconAlt}" style="width: 9px; height: 9px; vertical-align: middle;" />` : ''}</span> <span style="cursor: pointer; text-decoration: underline;" onclick="navigateToAction('${behaviorName}', '${actionName}')">${actionMarker}${actionName}</span></div>`;
        
        // Render operations - handle both array format and {all_operations: [...]} format
        const operationsArray = action.operations?.all_operations || (Array.isArray(action.operations) ? action.operations : []);
        const hasOperations = operationsArray.length > 0;
        const operationsHtml = hasOperations ? operationsArray.map(op => {
            return this.renderOperation(op, behaviorName, actionName);
        }).join('') : '';
        
        actionHtml += `<div id="${actionId}" class="collapsible-content" style="display: ${actionDisplay};">${operationsHtml}</div>`;
        
        return actionHtml;
    }
    
    /**
     * Render a single operation.
     * 
     * @param {Object} op - Operation object
     * @param {string} behaviorName - Behavior name (escaped)
     * @param {string} actionName - Action name (escaped)
     * @returns {string} HTML string
     */
    renderOperation(op, behaviorName, actionName) {
        const isCurrent = op.is_current || false;
        const isCompleted = op.is_completed || false;
        const opMarker = this.getStatusMarker(isCurrent, isCompleted);
        const opTooltip = op.description ? this.escapeHtml(op.description) : '';
        const opName = this.escapeHtml(op.name || '');
        const opClasses = ['operation-item', 'card-item'];
        if (isCurrent) {
            opClasses.push('active');
        }
        
        return `<div class="${opClasses.join(' ')}" title="${opTooltip}" onclick="navigateAndExecute('${behaviorName}', '${actionName}', '${opName}')" style="cursor: pointer; text-decoration: underline;">${opMarker}${opName}</div>`;
    }
    
    /**
     * Handle events.
     * 
     * @param {string} eventType - Event type
     * @param {Object} eventData - Event data
     * @returns {Promise<Object>} Result
     */
    async handleEvent(eventType, eventData) {
        if (eventType === 'execute') {
            // Execute behavior/action logic would go here
            return { success: true };
        }
        throw new Error(`Unknown event type: ${eventType}`);
    }
}

module.exports = BehaviorsView;
