/**
 * HTML Renderer
 * 
 * Generates HTML/CSS for webview display of status data.
 * Uses VS Code theme-aware CSS variables for styling.
 */

class HtmlRenderer {
  constructor() {
    this.escapeHtml = this.escapeHtml.bind(this);
  }

  /**
   * Render complete HTML document for webview
   * @param {object} statusData - Parsed status data
   * @returns {string} Complete HTML document
   */
  render(statusData) {
    return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bot Status Dashboard</title>
    <style>
        ${this.getStyles()}
    </style>
</head>
<body>
    ${this.renderBotSelector(statusData.availableBots || [], statusData.currentBot || 'story_bot')}
    ${this.renderHeader(statusData.bot, statusData.session)}
    ${this.renderBehaviors(statusData.behaviors)}
    ${this.renderScope(statusData.scope)}
    ${this.renderParameters(statusData.parameters)}
    ${this.renderRunExamples(statusData.runExamples)}
    ${this.renderHeadless(statusData.headless)}
    ${this.renderCommands(statusData.commands)}
    ${this.renderScripts()}
</body>
</html>`;
  }

  /**
   * Get CSS styles
   */
  getStyles() {
    return `
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding: 10px;
            color: var(--vscode-foreground);
            background-color: var(--vscode-editor-background);
            line-height: 1.5;
            margin: 0;
            font-size: 12px;
        }
        .header {
            border-bottom: 1px solid var(--vscode-panel-border);
            padding-bottom: 6px;
            margin-bottom: 10px;
        }
        .header h1 {
            margin: 0 0 4px 0;
            font-size: 15px;
            color: var(--vscode-foreground);
            font-weight: 600;
        }
        .header-info {
            font-size: 12px;
            color: var(--vscode-descriptionForeground);
            margin: 3px 0;
        }
        .controls {
            margin-bottom: 10px;
            display: flex;
            gap: 6px;
        }
        button {
            background-color: var(--vscode-button-background);
            color: var(--vscode-button-foreground);
            border: none;
            padding: 4px 10px;
            cursor: pointer;
            border-radius: 2px;
            font-size: 12px;
            font-family: inherit;
        }
        button:hover {
            background-color: var(--vscode-button-hoverBackground);
        }
        button:active {
            background-color: var(--vscode-button-background);
            opacity: 0.8;
        }
        .section {
            margin-bottom: 14px;
        }
        .section-title {
            font-weight: 600;
            margin-bottom: 6px;
            font-size: 12px;
            color: var(--vscode-foreground);
        }
        .behavior-item, .action-item, .operation-item {
            margin: 3px 0;
            padding: 4px 8px;
            border-radius: 2px;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .collapsible-header {
            margin: 3px 0;
            padding: 4px 8px;
            border-radius: 2px;
            display: flex;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            background-color: var(--vscode-list-hoverBackground);
            font-weight: 500;
            font-size: 12px;
        }
        .collapsible-header:hover {
            background-color: var(--vscode-list-activeSelectionBackground);
        }
        .collapsible-header.action-item {
            margin-left: 18px;
            background-color: var(--vscode-editor-lineHighlightBackground);
            font-weight: normal;
        }
        .collapsible-header.action-item:hover {
            background-color: var(--vscode-list-hoverBackground);
        }
        .operation-item {
            margin-left: 54px;
            font-size: 12px;
            color: var(--vscode-descriptionForeground);
        }
        .status-marker {
            font-family: 'Courier New', monospace;
            font-weight: bold;
            min-width: 24px;
            font-size: 12px;
        }
        .marker-current {
        }
        .marker-completed {
        }
        .marker-pending {
        }
        .scope-section {
            background-color: var(--vscode-editor-lineHighlightBackground);
            padding: 10px;
            border-radius: 2px;
            border-left: 2px solid var(--vscode-focusBorder);
        }
        .scope-filter {
            font-family: 'Courier New', monospace;
            font-size: 12px;
            margin-top: 5px;
        }
        .scope-links {
            margin-top: 5px;
        }
        .scope-links a {
            color: var(--vscode-textLink-foreground);
            text-decoration: none;
            margin-right: 10px;
            font-size: 12px;
        }
        .scope-links a:hover {
            text-decoration: underline;
            color: var(--vscode-textLink-activeForeground);
        }
        .headless-info {
            background-color: var(--vscode-editor-lineHighlightBackground);
            padding: 10px;
            border-radius: 2px;
            font-size: 12px;
        }
        .headless-info .section-title {
            margin-bottom: 4px;
        }
        .commands-footer {
            border-top: 1px solid var(--vscode-panel-border);
            padding-top: 8px;
            margin-top: 10px;
            font-size: 12px;
            color: var(--vscode-descriptionForeground);
        }
        .icon {
            font-size: 13px;
            margin-right: 3px;
        }
        .empty-state {
            color: var(--vscode-descriptionForeground);
            font-style: italic;
            padding: 8px;
        }
        .collapsible-content {
            overflow: hidden;
            transition: max-height 0.2s ease-out;
            display: block;
        }
        .expand-icon {
            display: inline-block;
            font-size: 10px;
            min-width: 12px;
        }
        /* Style tree icons */
        .tree-icon {
            color: #6B9BD1;
            font-weight: bold;
            margin-right: 4px;
        }
        /* Bot selector styles */
        .bot-selector {
            padding: 6px 0;
            margin-bottom: 10px;
            border-bottom: 1px solid var(--vscode-panel-border);
        }
        .bot-selector-title {
            font-size: 12px;
            color: var(--vscode-descriptionForeground);
            margin-bottom: 6px;
            font-weight: 500;
        }
        .bot-selector-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .bot-links {
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            align-items: center;
        }
        .refresh-button {
            background: none;
            border: none;
            color: var(--vscode-foreground);
            cursor: pointer;
            font-size: 14px;
            padding: 2px 6px;
            opacity: 0.7;
        }
        .refresh-button:hover {
            opacity: 1;
            background-color: var(--vscode-toolbar-hoverBackground);
        }
        .bot-link {
            font-size: 12px;
            cursor: pointer;
            text-decoration: underline;
            color: var(--vscode-descriptionForeground);
            opacity: 0.6;
        }
        .bot-link.active {
            color: var(--vscode-foreground);
            font-weight: 600;
            text-decoration: none;
            cursor: default;
            opacity: 1;
        }
        .bot-link:not(.active):hover {
            opacity: 0.8;
        }
    `;
  }

  /**
   * Render bot selector section
   * Displays available bots and allows switching between them
   */
  renderBotSelector(availableBots, currentBot) {
    if (!availableBots || availableBots.length === 0) {
      return '';
    }

    const botLinks = availableBots.map(botName => {
      const isActive = botName === currentBot;
      const activeClass = isActive ? ' active' : '';
      return `<a href="javascript:void(0)" class="bot-link${activeClass}" onclick="switchBot('${botName}')">${this.escapeHtml(botName)}</a>`;
    }).join('\n        ');

    return `
    <div class="bot-selector">
        <div class="bot-selector-title">Available Bots:</div>
        <div class="bot-selector-row">
            <div class="bot-links">
            ${botLinks}
            </div>
            <button class="refresh-button" onclick="refreshStatus()" title="Refresh">🔄</button>
        </div>
    </div>`;
  }

  /**
   * Render header section
   * AC: WHEN bot paths contain special characters THEN panel escapes HTML entities
   * AC: WHEN workspace directory is very long THEN panel truncates with ellipsis
   */
  renderHeader(bot, session) {
    const maxPathLength = 80;
    
    // AC: Escape HTML entities for all paths
    const safeBotName = this.escapeHtml(bot.name);
    const safeBotDir = this.escapeHtml(bot.botDirectory);
    const safeWorkspaceName = this.escapeHtml(bot.workspaceName);
    const safeWorkspaceDir = this.escapeHtml(bot.workspaceDirectory);
    
    // AC: Truncate very long directory paths
    const displayBotDir = this.truncatePath(safeBotDir, maxPathLength);
    const displayWorkspaceDir = this.truncatePath(safeWorkspaceDir, maxPathLength);
    
    return `
    <div class="header">
        <h1>🤖 ${safeBotName}</h1>
        <div class="header-info"><strong>Bot Path:</strong> <span title="${safeBotDir}">${displayBotDir}</span></div>
        <div class="header-info" style="display: flex; align-items: center; gap: 6px;">
            <strong>Workspace:</strong>
            <input type="text" id="workspacePathInput" 
                   value="${safeWorkspaceDir}" 
                   placeholder="Path to workspace"
                   onchange="updateWorkspace(this.value)"
                   onkeydown="if(event.key === 'Enter') { event.preventDefault(); updateWorkspace(this.value); }"
                   title="${safeWorkspaceDir}"
                   style="flex: 1; padding: 2px 6px; font-family: 'Courier New', monospace; font-size: 11px; background-color: var(--vscode-input-background); color: var(--vscode-input-foreground); border: 1px solid var(--vscode-input-border); border-radius: 2px;" />
        </div>
    </div>`;
  }

  /**
   * Truncate path with ellipsis if too long
   */
  truncatePath(path, maxLength) {
    if (!path || path.length <= maxLength) return path;
    const ellipsis = '...';
    const prefixLength = Math.floor((maxLength - ellipsis.length) / 2);
    const suffixLength = maxLength - ellipsis.length - prefixLength;
    return path.substring(0, prefixLength) + ellipsis + path.substring(path.length - suffixLength);
  }

  /**
   * Render control buttons
   */
  renderControls() {
    return `
    <div class="controls">
        <button onclick="refreshStatus()">🔄 Refresh</button>
        <button onclick="openScope()">🎯 View Scope</button>
    </div>`;
  }

  /**
   * Render behaviors hierarchy
   */
  renderBehaviors(behaviors) {
    if (!behaviors || behaviors.length === 0) {
      return `
    <div class="section">
        <div class="section-title">Workflow Status</div>
        <div class="empty-state">No behaviors available</div>
    </div>`;
    }

    const behaviorsHtml = behaviors.map((behavior, bIdx) => {
      const behaviorMarker = behavior.isCurrent 
        ? '<span class="status-marker marker-current">➤</span>'
        : behavior.isCompleted
        ? '<span class="status-marker marker-completed">☑</span>'
        : '<span class="status-marker marker-pending">☐</span>';
      
      const behaviorTooltip = behavior.description ? this.escapeHtml(behavior.description) : '';
      const behaviorId = `behavior-${bIdx}`;
      
      // Collapse non-current behaviors by default
      const behaviorExpanded = behavior.isCurrent;
      const behaviorIcon = behaviorExpanded ? '➖' : '➕';
      const behaviorIconClass = behaviorExpanded ? 'expanded' : '';
      const behaviorDisplay = behaviorExpanded ? 'block' : 'none';
      
      let html = `<div class="collapsible-header" onclick="toggleCollapse('${behaviorId}')" style="cursor: pointer;" title="${behaviorTooltip}"><span id="${behaviorId}-icon" class="${behaviorIconClass}" style="display: inline-block; font-size: 10px; min-width: 12px;">${behaviorIcon}</span> ${behaviorMarker}${this.escapeHtml(behavior.name)}</div>`;
      
      // Always create collapsible content, even if empty
      const hasActions = behavior.actions && behavior.actions.length > 0;
      const actionsHtml = hasActions ? behavior.actions.map((action, aIdx) => {
          const actionMarker = action.isCurrent
          ? '<span class="status-marker marker-current">➤</span>'
            : action.isCompleted
          ? '<span class="status-marker marker-completed">☑</span>'
          : '<span class="status-marker marker-pending">☐</span>';
          
        const actionTooltip = action.description ? this.escapeHtml(action.description) : '';
        const actionId = `action-${bIdx}-${aIdx}`;
        
        // Collapse non-current actions by default
        const actionExpanded = action.isCurrent;
        const actionIcon = actionExpanded ? '➖' : '➕';
        const actionIconClass = actionExpanded ? 'expanded' : '';
        const actionDisplay = actionExpanded ? 'block' : 'none';
        
        let actionHtml = `<div class="collapsible-header action-item" onclick="toggleCollapse('${actionId}')" style="cursor: pointer;" title="${actionTooltip}"><span id="${actionId}-icon" class="${actionIconClass}" style="display: inline-block; font-size: 10px; min-width: 12px;">${actionIcon}</span> ${actionMarker}${this.escapeHtml(action.name)}</div>`;
          
        // Always create collapsible content, even if empty
        const hasOperations = action.operations && action.operations.length > 0;
        const operationsHtml = hasOperations ? action.operations.map(op => {
              const opMarker = op.isCurrent
            ? '<span class="status-marker marker-current">➤</span>'
                : op.isCompleted
            ? '<span class="status-marker marker-completed">☑</span>'
            : '<span class="status-marker marker-pending">☐</span>';
          const opTooltip = op.description ? this.escapeHtml(op.description) : '';
          return `<div class="operation-item" title="${opTooltip}">${opMarker}${this.escapeHtml(op.name)}</div>`;
        }).join('') : '';
        
        actionHtml += `<div id="${actionId}" class="collapsible-content" style="display: ${actionDisplay};">${operationsHtml}</div>`;
          
          return actionHtml;
      }).join('') : '';
      
      html += `<div id="${behaviorId}" class="collapsible-content" style="display: ${behaviorDisplay};">${actionsHtml}</div>`;
      
      return html;
    }).join('');

    return `
    <div class="section">
        <div class="section-title">Workflow Status</div>
        ${behaviorsHtml}
    </div>`;
  }

  /**
   * Render scope section (polymorphic: story tree, file list, or "all")
   */
  renderScope(scope) {
    const linksHtml = scope.graphLinks && scope.graphLinks.length > 0
      ? scope.graphLinks.map(link => 
          `<a href="javascript:void(0)" onclick="openFile('${this.escapeForJs(link.url)}')">${this.escapeHtml(link.text)}</a>`
        ).join(' ')
      : '';

    let contentHtml = '';
    if (scope.type === 'story' && scope.content) {
      contentHtml = this.renderStoryTree(scope.content);
    } else if (scope.type === 'files' && scope.content) {
      contentHtml = this.renderFileList(scope.content);
    } else {
      contentHtml = '<div class="empty-state">All files in workspace</div>';
    }

    return `
    <div class="section scope-section">
        <div class="section-title">🎯 Scope</div>
        <div class="scope-filter">
            <strong>Filter:</strong> 
            <input type="text" id="scopeFilterInput" class="filter-input" 
                   value="${this.escapeHtml(scope.filter || '')}" 
                   placeholder="Epic or Story name"
                   onchange="updateFilter(this.value)"
                   onkeydown="if(event.key === 'Enter') { event.preventDefault(); updateFilter(this.value); }"
                   style="margin-left: 6px; padding: 2px 6px; width: calc(100% - 70px); font-family: 'Courier New', monospace; font-size: 12px; background-color: var(--vscode-input-background); color: var(--vscode-input-foreground); border: 1px solid var(--vscode-input-border); border-radius: 2px;" />
        </div>
        ${linksHtml ? `<div class="scope-links">${linksHtml}</div>` : ''}
        ${contentHtml}
    </div>`;
  }

  renderStoryTree(epics) {
    return epics.map((epic, epicIndex) => {
      const epicId = `epic-${epicIndex}`;
      const epicIcon = '🎯 ';
      let html = `<div style="margin-top: 8px; font-size: 12px;">
        <span class="collapsible-header" onclick="toggleCollapse('${epicId}')" style="cursor: pointer; user-select: none;">
          <span id="${epicId}-icon" style="display: inline-block; font-size: 10px; min-width: 12px;">➕</span> <strong>${epicIcon}${this.escapeHtml(epic.name)}</strong>
        </span>
      </div>`;
      
      html += `<div id="${epicId}" class="collapsible-content" style="display: none;">`;
      epic.features.forEach((feature, featureIndex) => {
        const featureId = `feature-${epicIndex}-${featureIndex}`;
        const featureIcon = '⚙️ ';
        html += `<div style="margin-left: 14px; margin-top: 4px; font-size: 12px;">
          <span class="collapsible-header" onclick="toggleCollapse('${featureId}')" style="cursor: pointer; user-select: none;">
            <span id="${featureId}-icon" style="display: inline-block; font-size: 10px; min-width: 12px;">➕</span> ${featureIcon}${this.escapeHtml(feature.name)}
          </span>`;
        
        if (feature.links && feature.links.length > 0) {
          html += ' ' + feature.links.map(link => 
            `<a href="javascript:void(0)" onclick="openFile('${this.escapeForJs(link.url)}')">[${this.escapeHtml(link.text)}]</a>`
          ).join(' ');
        }
        html += '</div>';
        
        html += `<div id="${featureId}" class="collapsible-content" style="display: none;">`;
        feature.stories.forEach(story => {
          const storyIcon = '📝 ';
          html += `<div style="margin-left: 28px; margin-top: 2px; font-size: 12px;">`;
          if (story.links && story.links.length > 0) {
            // First link is the story file itself
            const storyLink = story.links[0];
            html += `<a href="javascript:void(0)" onclick="openFile('${this.escapeForJs(storyLink.url)}')">${storyIcon}${this.escapeHtml(story.name)}</a>`;
            // Remaining links are test files, etc.
            if (story.links.length > 1) {
              html += ' ' + story.links.slice(1).map(link => 
                `<a href="javascript:void(0)" onclick="openFile('${this.escapeForJs(link.url)}')">[${this.escapeHtml(link.text)}]</a>`
              ).join(' ');
            }
          } else {
            html += `${storyIcon}${this.escapeHtml(story.name)}`;
          }
          html += '</div>';
        });
        html += '</div>'; // Close feature collapsible-content
      });
      html += '</div>'; // Close epic collapsible-content
      
      return html;
    }).join('');
  }

  renderFileList(files) {
    return '<div style="margin-top: 5px;">' + files.map(file => 
      `<div style="margin-left: 10px; font-family: monospace; font-size: 12px; margin-top: 2px;">- ${this.escapeHtml(file.path)}</div>`
    ).join('') + '</div>';
  }

  /**
   * Render parameters table
   */
  renderParameters(parameters) {
    if (!parameters || parameters.length === 0) return '';
    
    const rows = parameters.map(param => `
      <tr>
        <td style="padding: 3px 6px; font-family: monospace;">${this.escapeHtml(param.flag)}</td>
        <td style="padding: 3px 6px; font-family: monospace;">${this.escapeHtml(param.syntax)}</td>
        <td style="padding: 3px 6px;">${this.escapeHtml(param.description)}</td>
      </tr>
    `).join('');

    return `
    <div class="section">
        <div class="section-title">Parameters</div>
        <table style="width: 100%; border-collapse: collapse; font-size: 12px;">
          <thead>
            <tr style="border-bottom: 1px solid var(--vscode-panel-border);">
              <th style="padding: 3px 6px; text-align: left;">Flag</th>
              <th style="padding: 3px 6px; text-align: left;">Syntax</th>
              <th style="padding: 3px 6px; text-align: left;">Description</th>
            </tr>
          </thead>
          <tbody>${rows}</tbody>
        </table>
    </div>`;
  }

  /**
   * Render run examples
   */
  renderRunExamples(examples) {
    if (!examples || examples.length === 0) return '';
    
    const examplesHtml = examples.map(ex => `
      <div style="margin: 6px 0; padding: 6px; background-color: var(--vscode-textCodeBlock-background); border-radius: 2px; font-family: monospace; font-size: 12px;">
        ${this.escapeHtml(ex.command)}
        ${ex.description ? `<div style="color: var(--vscode-descriptionForeground); margin-top: 3px;"># ${this.escapeHtml(ex.description)}</div>` : ''}
      </div>
    `).join('');

    return `
    <div class="section">
        <div class="section-title">Run Examples</div>
        ${examplesHtml}
    </div>`;
  }

  /**
   * Render headless mode section
   */
  renderHeadless(headless) {
    let activeSessionHtml = '';
    if (headless.activeSession) {
      activeSessionHtml = `
        <div style="margin-top: 5px;"><strong>Active Session:</strong></div>
        <div style="margin-left: 10px; margin-top: 3px;">Session ID: ${this.escapeHtml(headless.activeSession.sessionId)}</div>
        <div style="margin-left: 10px; margin-top: 2px;">Log: ${this.escapeHtml(headless.activeSession.logPath)}</div>
      `;
    }

    return `
    <div class="section">
        <div class="headless-info">
            <div class="section-title">Headless Mode</div>
            <div><strong>Status:</strong> ${this.escapeHtml(headless.status || 'Unknown')}</div>
            ${headless.apiKey ? `<div><strong>API Key:</strong> ${this.escapeHtml(headless.apiKey)}</div>` : ''}
            ${activeSessionHtml}
        </div>
    </div>`;
  }

  /**
   * Render commands footer
   */
  renderCommands(commands) {
    const commandsText = commands && commands.text ? commands.text : 'N/A';
    return `
    <div class="commands-footer">
        <strong>💻 Commands:</strong> ${this.escapeHtml(commandsText)}
    </div>`;
  }

  /**
   * Render JavaScript for webview interaction
   */
  renderScripts() {
    return `
    <script>
        const vscode = acquireVsCodeApi();

        function refreshStatus() {
            vscode.postMessage({ command: 'refresh' });
        }

        function openScope() {
            vscode.postMessage({ 
                command: 'openScope',
                filePath: 'docs/stories/story-graph.json'
            });
        }

        function openFile(filePath) {
            vscode.postMessage({ 
                command: 'openScope',
                filePath: filePath
            });
        }

        function toggleCollapse(elementId) {
            const content = document.getElementById(elementId);
            const icon = document.getElementById(elementId + '-icon');
            
            if (content && content.style.display === 'none') {
                content.style.display = 'block';
                if (icon) {
                    icon.textContent = '➖';
                    icon.classList.add('expanded');
                }
            } else if (content) {
                content.style.display = 'none';
                if (icon) {
                    icon.textContent = '➕';
                    icon.classList.remove('expanded');
                }
            }
        }

        function updateFilter(filterValue) {
            console.log('[FILTER] updateFilter called with:', filterValue);
            vscode.postMessage({ 
                command: 'updateFilter',
                filter: filterValue
            });
        }

        function updateWorkspace(workspacePath) {
            vscode.postMessage({ 
                command: 'updateWorkspace',
                workspacePath: workspacePath
            });
        }

        function switchBot(botName) {
            vscode.postMessage({ 
                command: 'switchBot',
                botName: botName
            });
        }
    </script>`;
  }

  /**
   * Escape HTML special characters
   */
  escapeHtml(text) {
    if (!text) return '';
    const map = {
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&#039;'
    };
    return String(text).replace(/[&<>"']/g, m => map[m]);
  }

  /**
   * Escape string for JavaScript context (inside single quotes)
   * Only escapes single quotes and backslashes
   */
  escapeForJs(text) {
    if (!text) return '';
    return String(text).replace(/\\/g, '\\\\').replace(/'/g, "\\'");
  }

  /**
   * Render error page
   */
  renderError(errorMessage) {
    return `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding: 20px;
            color: var(--vscode-errorForeground);
            background-color: var(--vscode-editor-background);
        }
        .error {
            background-color: var(--vscode-inputValidation-errorBackground);
            border: 1px solid var(--vscode-inputValidation-errorBorder);
            padding: 16px;
            border-radius: 4px;
        }
        .error h2 {
            margin-top: 0;
        }
        button {
            background-color: var(--vscode-button-background);
            color: var(--vscode-button-foreground);
            border: none;
            padding: 8px 16px;
            cursor: pointer;
            margin-top: 12px;
            border-radius: 2px;
        }
    </style>
</head>
<body>
    <div class="error">
        <h2>Error Loading Status</h2>
        <p>${this.escapeHtml(errorMessage)}</p>
        <button onclick="retry()">Retry</button>
    </div>
    <script>
        const vscode = acquireVsCodeApi();
        function retry() {
            vscode.postMessage({ command: 'refresh' });
        }
    </script>
</body>
</html>`;
  }
}

module.exports = HtmlRenderer;
