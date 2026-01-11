/**
 * ScopeSection - Renders scope section with filter and story tree or file list.
 * 
 * Epic: Invoke Bot Through Panel
 * Sub-Epic: Manage Scope Through Panel
 * Story: Display Story Scope Hierarchy, Filter Story Scope
 */

const PanelView = require('./panel_view');

class ScopeSection extends PanelView {
    /**
     * Scope section view.
     * 
     * @param {Object} scopeJSON - Scope JSON from bot (contains type, filter, content, graphLinks)
     * @param {Object} cli - CLI instance (can be null)
     * @param {string} workspaceDirectory - Workspace directory path
     */
    constructor(scopeJSON, cli, workspaceDirectory, webview, extensionUri) {
        super(cli, workspaceDirectory);
        this.scopeData = scopeJSON || { type: 'all', filter: '', content: null, graphLinks: [] };
        this.webview = webview;
        this.extensionUri = extensionUri;
    }
    
    /**
     * Update scope data.
     * 
     * @param {Object} scopeJSON - Updated scope JSON
     */
    update(scopeJSON) {
        this.scopeData = scopeJSON || { type: 'all', filter: '', content: null, graphLinks: [] };
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
     * Escape for JavaScript string.
     * 
     * @param {string} text - Text to escape
     * @returns {string} Escaped text
     */
    escapeForJs(text) {
        if (typeof text !== 'string') {
            text = String(text);
        }
        return text.replace(/\\/g, '\\\\').replace(/'/g, "\\'").replace(/"/g, '\\"').replace(/\n/g, '\\n').replace(/\r/g, '\\r');
    }
    
    /**
     * Render scope section HTML.
     * 
     * @returns {string} HTML string
     */
    render() {
        const linksHtml = this.scopeData.graphLinks && this.scopeData.graphLinks.length > 0
            ? this.scopeData.graphLinks.map(link => 
                `<a href="javascript:void(0)" onclick="openFile('${this.escapeForJs(link.url)}')" style="color: var(--vscode-foreground); text-decoration: none; margin-left: 6px; font-size: 12px;">${this.escapeHtml(link.text).toLowerCase()}</a>`
            ).join('')
            : '';
        
        let contentHtml = '';
        let contentSummary = '';
        if ((this.scopeData.type === 'story' || this.scopeData.type === 'showAll') && this.scopeData.content) {
            contentHtml = this.renderStoryTree(this.scopeData.content);
            contentSummary = `${this.scopeData.content.length} epic${this.scopeData.content.length !== 1 ? 's' : ''}`;
        } else if (this.scopeData.type === 'files' && this.scopeData.content) {
            contentHtml = this.renderFileList(this.scopeData.content);
            contentSummary = `${this.scopeData.content.length} file${this.scopeData.content.length !== 1 ? 's' : ''}`;
        } else {
            contentHtml = '<div class="empty-state">All files in workspace</div>';
            contentSummary = 'all files';
        }
        
        const filterValue = this.escapeHtml(this.scopeData.filter || '');
        const hasFilter = filterValue.length > 0;
        
        return `
    <div class="section scope-section card-primary">
        <div class="collapsible-section expanded">
            <div class="collapsible-header" onclick="toggleSection('scope-content')" style="
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
                    <span style="margin-right: 8px; font-size: 20px;">🔍</span>
                    <span style="font-weight: 600; font-size: 20px;">Scope</span>
                    ${hasFilter ? `<button onclick="event.stopPropagation(); clearScopeFilter();" style="
                        background: transparent;
                        border: none;
                        padding: 4px 8px;
                        margin-left: 6px;
                        cursor: pointer;
                        display: flex;
                        align-items: center;
                        transition: opacity 0.15s ease;
                    " 
                    onmouseover="this.style.opacity='0.7'" 
                    onmouseout="this.style.opacity='1'"
                    title="Clear scope filter (show all)">
                        ✕
                    </button>` : ''}
                </div>
                ${linksHtml ? `<div onclick="event.stopPropagation();" style="display: flex; align-items: center;">${linksHtml}</div>` : ''}
            </div>
            <div id="scope-content" class="collapsible-content" style="max-height: 2000px; overflow: hidden; transition: max-height 0.3s ease;">
                <div class="card-secondary" style="padding: 5px;">
                    <div class="input-container" style="margin-bottom: 6px;">
                        <div class="input-header">Filter</div>
                        <input type="text" id="scopeFilterInput" 
                               value="${filterValue}" 
                               placeholder="Epic or Story name"
                               onchange="updateFilter(this.value)"
                               onkeydown="if(event.key === 'Enter') { event.preventDefault(); updateFilter(this.value); }" />
                    </div>
                    ${contentHtml}
                </div>
            </div>
        </div>
    </div>`;
    }
    
    /**
     * Render story tree (epics -> features -> stories -> scenarios).
     * 
     * @param {Array} epics - Epics array
     * @returns {string} HTML string
     */
    renderStoryTree(epics) {
        return epics.map((epic, epicIndex) => {
            const epicId = `epic-${epicIndex}`;
            const epicIcon = '💡 ';
            let html = `<div style="margin-top: 8px; font-size: 12px;">
        <span class="collapsible-header" onclick="toggleCollapse('${epicId}')" style="cursor: pointer; user-select: none;">
          <span id="${epicId}-icon" style="display: inline-block; min-width: 9px;">➕</span> ${epicIcon}${this.escapeHtml(epic.name)}
        </span>
      </div>`;
            
            html += `<div id="${epicId}" class="collapsible-content" style="display: none;">`;
            
            // Helper function to recursively render features
            const renderFeature = (feature, featureIndex, parentPath, depth = 0) => {
                const featureId = `${parentPath}-${featureIndex}`;
                const featureIcon = '⚙️ ';
                const featureLinks = (feature.links && feature.links.length > 0) 
                    ? ' ' + feature.links.map(link => 
                        `<a href="javascript:void(0)" onclick="event.stopPropagation(); openFile('${this.escapeForJs(link.url)}')">[${this.escapeHtml(link.text)}]</a>`
                    ).join(' ')
                    : '';
                
                const marginLeft = 7 + (depth * 7);
                
                html += `<div style="margin-left: ${marginLeft}px; margin-top: 4px; font-size: 12px;"><span class="collapsible-header" onclick="toggleCollapse('${featureId}')" style="cursor: pointer; user-select: none;"><span id="${featureId}-icon" style="display: inline-block; min-width: 9px;">➕</span> ${featureIcon}${this.escapeHtml(feature.name)}${featureLinks}</span></div>`;
                
                html += `<div id="${featureId}" class="collapsible-content" style="display: none;">`;
                
                // Render nested features
                if (feature.features && feature.features.length > 0) {
                    feature.features.forEach((nestedFeature, nestedIndex) => {
                        renderFeature(nestedFeature, nestedIndex, featureId, depth + 1);
                    });
                }
                
                // Render stories
                if (feature.stories && feature.stories.length > 0) {
                    feature.stories.forEach((story, storyIndex) => {
                        const storyId = `${featureId}-story-${storyIndex}`;
                        const storyIcon = '📝 ';
                        const hasScenarios = story.scenarios && story.scenarios.length > 0;
                        
                        html += `<div style="margin-left: ${marginLeft + 7}px; margin-top: 2px; font-size: 12px;">`;
                        
                        if (hasScenarios) {
                            html += `<span class="collapsible-header" onclick="toggleCollapse('${storyId}')" style="cursor: pointer; user-select: none;">`;
                            html += `<span id="${storyId}-icon" style="display: inline-block; min-width: 9px;">➕</span> `;
                        }
                        
                        if (story.links && story.links.length > 0) {
                            const storyLink = story.links[0];
                            html += `<a href="javascript:void(0)" onclick="event.stopPropagation(); openFile('${this.escapeForJs(storyLink.url)}')">${storyIcon}${this.escapeHtml(story.name)}</a>`;
                            if (story.links.length > 1) {
                                html += ' ' + story.links.slice(1).map(link => 
                                    `<a href="javascript:void(0)" onclick="event.stopPropagation(); openFile('${this.escapeForJs(link.url)}')">[${this.escapeHtml(link.text)}]</a>`
                                ).join(' ');
                            }
                        } else {
                            html += `${storyIcon}${this.escapeHtml(story.name)}`;
                        }
                        
                        if (hasScenarios) {
                            html += `</span>`;
                        }
                        
                        html += '</div>';
                        
                        // Render scenarios
                        if (hasScenarios) {
                            html += `<div id="${storyId}" class="collapsible-content" style="display: none;">`;
                            story.scenarios.forEach((scenario) => {
                                const testTubeIcon = '🧪 ';
                                html += `<div style="margin-left: ${marginLeft + 21}px; margin-top: 2px; font-size: 12px;">`;
                                
                                if (scenario.test_file) {
                                    html += `<a href="javascript:void(0)" onclick="event.stopPropagation(); openFile('${this.escapeForJs(scenario.test_file)}')">${testTubeIcon}${this.escapeHtml(scenario.name)}</a>`;
                                } else {
                                    html += `${testTubeIcon}${this.escapeHtml(scenario.name)}`;
                                }
                                
                                html += '</div>';
                            });
                            html += '</div>';
                        }
                    });
                }
                
                html += '</div>';
            };
            
            if (epic.features && epic.features.length > 0) {
                epic.features.forEach((feature, featureIndex) => {
                    renderFeature(feature, featureIndex, `epic-${epicIndex}`, 0);
                });
            }
            
            html += '</div>';
            return html;
        }).join('');
    }
    
    /**
     * Render file list.
     * 
     * @param {Array} files - Files array
     * @returns {string} HTML string
     */
    renderFileList(files) {
        return '<div style="margin-top: 5px;">' + files.map(file => 
            `<div style="margin-left: 5px; font-family: monospace; font-size: 12px; margin-top: 2px;">- ${this.escapeHtml(file.path)}</div>`
        ).join('') + '</div>';
    }
    
    /**
     * Handle events.
     * 
     * @param {string} eventType - Event type
     * @param {Object} eventData - Event data
     * @returns {Promise<Object>} Result
     */
    async handleEvent(eventType, eventData) {
        if (eventType === 'updateFilter') {
            // Update filter logic would go here
            return { success: true, filter: eventData.filter };
        }
        throw new Error(`Unknown event type: ${eventType}`);
    }
}

module.exports = ScopeSection;
