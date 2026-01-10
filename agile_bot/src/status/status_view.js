/**
 * StatusView - Renders Status domain object as HTML.
 * 
 * Epic: Invoke Bot Through Panel
 * Sub-Epic: Manage Bot Information
 * Story: Open Panel, Refresh Panel
 */

const PanelView = require('../panel/panel_view');

class StatusView extends PanelView {
    /**
     * Renders Status domain object as HTML.
     * 
     * @param {Object} statusJSON - Status JSON from CLI
     * @param {Object} cli - CLI instance for subprocess communication
     */
    constructor(statusJSON, cli) {
        super(cli);
        this.statusData = statusJSON;
    }
    
    /**
     * Render Status JSON to HTML.
     * 
     * @returns {string} HTML string
     */
    render() {
        const {
            progress_path,
            stage_name,
            current_behavior,
            current_action,
            has_current_behavior,
            has_current_action
        } = this.statusData;
        
        let currentHTML = '';
        if (has_current_behavior) {
            let current = current_behavior;
            if (has_current_action) {
                current += ` > ${current_action}`;
            }
            currentHTML = `<div class="status-current">
                <span class="label">Current:</span>
                <span class="value">${current}</span>
            </div>`;
        }
        
        return `
            <div class="status-view">
                <div class="status-progress">
                    <span class="label">Progress:</span>
                    <span class="value">${progress_path}</span>
                </div>
                <div class="status-stage">
                    <span class="label">Stage:</span>
                    <span class="value">${stage_name}</span>
                </div>
                ${currentHTML}
            </div>
        `;
    }
}

module.exports = StatusView;
