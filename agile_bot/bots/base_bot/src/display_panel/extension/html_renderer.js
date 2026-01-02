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
    ${this.renderHeader(statusData.bot, statusData.session)}
    ${this.renderControls()}
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
            padding: 16px;
            color: var(--vscode-foreground);
            background-color: var(--vscode-editor-background);
            line-height: 1.6;
            margin: 0;
        }
        .header {
            border-bottom: 2px solid var(--vscode-panel-border);
            padding-bottom: 12px;
            margin-bottom: 20px;
        }
        .header h1 {
            margin: 0 0 8px 0;
            font-size: 20px;
            color: var(--vscode-foreground);
            font-weight: 600;
        }
        .header-info {
            font-size: 13px;
            color: var(--vscode-descriptionForeground);
            margin: 4px 0;
        }
        .controls {
            margin-bottom: 16px;
            display: flex;
            gap: 8px;
        }
        button {
            background-color: var(--vscode-button-background);
            color: var(--vscode-button-foreground);
            border: none;
            padding: 6px 14px;
            cursor: pointer;
            border-radius: 2px;
            font-size: 13px;
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
            margin-bottom: 24px;
        }
        .section-title {
            font-weight: 600;
            margin-bottom: 12px;
            font-size: 15px;
            color: var(--vscode-foreground);
        }
        .behavior-item, .action-item, .operation-item {
            margin: 6px 0;
            padding: 6px 12px;
            border-radius: 3px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .behavior-item {
            background-color: var(--vscode-list-hoverBackground);
            font-weight: 500;
            font-size: 14px;
        }
        .action-item {
            margin-left: 24px;
            background-color: var(--vscode-editor-lineHighlightBackground);
            font-size: 13px;
        }
        .operation-item {
            margin-left: 48px;
            font-size: 12px;
            color: var(--vscode-descriptionForeground);
        }
        .status-marker {
            font-family: 'Courier New', monospace;
            font-weight: bold;
            min-width: 30px;
            font-size: 14px;
        }
        .marker-current {
            color: var(--vscode-terminal-ansiYellow);
        }
        .marker-completed {
            color: var(--vscode-terminal-ansiGreen);
        }
        .marker-pending {
            color: var(--vscode-descriptionForeground);
        }
        .scope-section {
            background-color: var(--vscode-editor-lineHighlightBackground);
            padding: 12px;
            border-radius: 4px;
            border-left: 3px solid var(--vscode-focusBorder);
        }
        .scope-filter {
            font-family: 'Courier New', monospace;
            font-size: 13px;
            margin-top: 8px;
        }
        .scope-links {
            margin-top: 8px;
        }
        .scope-links a {
            color: var(--vscode-textLink-foreground);
            text-decoration: none;
            margin-right: 12px;
            font-size: 13px;
        }
        .scope-links a:hover {
            text-decoration: underline;
            color: var(--vscode-textLink-activeForeground);
        }
        .headless-info {
            background-color: var(--vscode-editor-lineHighlightBackground);
            padding: 12px;
            border-radius: 4px;
            font-size: 13px;
        }
        .headless-info .section-title {
            margin-bottom: 8px;
        }
        .commands-footer {
            border-top: 1px solid var(--vscode-panel-border);
            padding-top: 12px;
            margin-top: 20px;
            font-size: 13px;
            color: var(--vscode-descriptionForeground);
        }
        .icon {
            font-size: 16px;
            margin-right: 4px;
        }
        .empty-state {
            color: var(--vscode-descriptionForeground);
            font-style: italic;
            padding: 12px;
        }
    `;
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
        <div class="header-info"><strong>Workspace:</strong> ${safeWorkspaceName} <span title="${safeWorkspaceDir}">(${displayWorkspaceDir})</span></div>
        <div class="header-info"><strong>Current Position:</strong> ${this.escapeHtml(session.currentPosition)}</div>
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

    const behaviorsHtml = behaviors.map(behavior => {
      const behaviorMarker = behavior.isCurrent 
        ? '<span class="status-marker marker-current">[➤]</span>'
        : behavior.isCompleted
        ? '<span class="status-marker marker-completed">[☑]</span>'
        : '<span class="status-marker marker-pending">[☐]</span>';
      
      const behaviorDesc = behavior.description ? ` - ${this.escapeHtml(behavior.description)}` : '';
      let html = `<div class="behavior-item">${behaviorMarker}${this.escapeHtml(behavior.name)}${behaviorDesc}</div>`;
      
      if (behavior.actions && behavior.actions.length > 0) {
        html += behavior.actions.map(action => {
          const actionMarker = action.isCurrent
            ? '<span class="status-marker marker-current">[➤]</span>'
            : action.isCompleted
            ? '<span class="status-marker marker-completed">[☑]</span>'
            : '<span class="status-marker marker-pending">[☐]</span>';
          
          const actionDesc = action.description ? ` - ${this.escapeHtml(action.description)}` : '';
          let actionHtml = `<div class="action-item">${actionMarker}${this.escapeHtml(action.name)}${actionDesc}</div>`;
          
          if (action.operations && action.operations.length > 0) {
            actionHtml += action.operations.map(op => {
              const opMarker = op.isCurrent
                ? '<span class="status-marker marker-current">[➤]</span>'
                : op.isCompleted
                ? '<span class="status-marker marker-completed">[☑]</span>'
                : '<span class="status-marker marker-pending">[☐]</span>';
              return `<div class="operation-item">${opMarker}${this.escapeHtml(op.name)}</div>`;
            }).join('');
          }
          
          return actionHtml;
        }).join('');
      }
      
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
          `<a href="#" onclick="return openFile('${this.escapeForJs(link.url)}')">${this.escapeHtml(link.text)}</a>`
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
        <div class="scope-filter"><strong>Filter:</strong> ${this.escapeHtml(scope.filter || 'None')}</div>
        ${linksHtml ? `<div class="scope-links">${linksHtml}</div>` : ''}
        ${contentHtml}
    </div>`;
  }

  renderStoryTree(epics) {
    return epics.map(epic => {
      let html = `<div style="margin-top: 12px;"><strong>${epic.icon} ${this.escapeHtml(epic.name)}</strong></div>`;
      epic.features.forEach(feature => {
        html += `<div style="margin-left: 20px; margin-top: 4px;">${feature.icon} ${this.escapeHtml(feature.name)}`;
        if (feature.links && feature.links.length > 0) {
          html += ' ' + feature.links.map(link => 
            `<a href="#" onclick="return openFile('${this.escapeForJs(link.url)}')">[${this.escapeHtml(link.text)}]</a>`
          ).join(' ');
        }
        html += '</div>';
        feature.stories.forEach(story => {
          html += `<div style="margin-left: 40px; margin-top: 2px;">`;
          if (story.links && story.links.length > 0) {
            // First link is the story file itself
            const storyLink = story.links[0];
            html += `<a href="#" onclick="return openFile('${this.escapeForJs(storyLink.url)}')">${story.icon} ${this.escapeHtml(story.name)}</a>`;
            // Remaining links are test files, etc.
            if (story.links.length > 1) {
              html += ' ' + story.links.slice(1).map(link => 
                `<a href="#" onclick="return openFile('${this.escapeForJs(link.url)}')">[${this.escapeHtml(link.text)}]</a>`
              ).join(' ');
            }
          } else {
            html += `${story.icon} ${this.escapeHtml(story.name)}`;
          }
          html += '</div>';
        });
      });
      return html;
    }).join('');
  }

  renderFileList(files) {
    return '<div style="margin-top: 8px;">' + files.map(file => 
      `<div style="margin-left: 12px; font-family: monospace; font-size: 12px;">- ${this.escapeHtml(file.path)}</div>`
    ).join('') + '</div>';
  }

  /**
   * Render parameters table
   */
  renderParameters(parameters) {
    if (!parameters || parameters.length === 0) return '';
    
    const rows = parameters.map(param => `
      <tr>
        <td style="padding: 4px 8px; font-family: monospace;">${this.escapeHtml(param.flag)}</td>
        <td style="padding: 4px 8px; font-family: monospace;">${this.escapeHtml(param.syntax)}</td>
        <td style="padding: 4px 8px;">${this.escapeHtml(param.description)}</td>
      </tr>
    `).join('');

    return `
    <div class="section">
        <div class="section-title">Parameters</div>
        <table style="width: 100%; border-collapse: collapse; font-size: 13px;">
          <thead>
            <tr style="border-bottom: 1px solid var(--vscode-panel-border);">
              <th style="padding: 4px 8px; text-align: left;">Flag</th>
              <th style="padding: 4px 8px; text-align: left;">Syntax</th>
              <th style="padding: 4px 8px; text-align: left;">Description</th>
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
      <div style="margin: 8px 0; padding: 8px; background-color: var(--vscode-textCodeBlock-background); border-radius: 3px; font-family: monospace; font-size: 12px;">
        ${this.escapeHtml(ex.command)}
        ${ex.description ? `<div style="color: var(--vscode-descriptionForeground); margin-top: 4px;"># ${this.escapeHtml(ex.description)}</div>` : ''}
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
        <div style="margin-top: 8px;"><strong>Active Session:</strong></div>
        <div style="margin-left: 12px;">Session ID: ${this.escapeHtml(headless.activeSession.sessionId)}</div>
        <div style="margin-left: 12px;">Log: ${this.escapeHtml(headless.activeSession.logPath)}</div>
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
            return false;
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
