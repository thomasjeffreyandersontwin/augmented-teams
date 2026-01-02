/**
 * Status Panel Controller
 * 
 * Manages webview panel lifecycle and coordinates data fetching,
 * parsing, and rendering. Implements singleton pattern.
 */

const vscode = require("vscode");
const path = require("path");
const StatusDataProvider = require("./status_data_provider.js");
const CLIOutputAdapter = require("./cli_output_adapter.js");
const HtmlRenderer = require("./html_renderer.js");
const Logger = require("./logger.js");

class StatusPanel {
  static currentPanel = undefined;
  static viewType = "agilebot.statusPanel";

  constructor(panel, workspaceRoot, extensionUri) {
    this._panel = panel;
    this._workspaceRoot = workspaceRoot;
    this._extensionUri = extensionUri;
    this._disposables = [];
    
    // Initialize logger
    const logPath = path.join(workspaceRoot, "agile_bot", "bots", "base_bot", "logs", "panel-debug.log");
    this._logger = new Logger(logPath);
    this._logger.log("StatusPanel constructor called");
    
    // Initialize components
    this._dataProvider = new StatusDataProvider(workspaceRoot);
    this._adapter = new CLIOutputAdapter();
    this._renderer = new HtmlRenderer();

    // Set the webview's initial html content
    this._update();

    // Listen for when the panel is disposed
    this._panel.onDidDispose(() => this.dispose(), null, this._disposables);

    // Update the content when the webview becomes visible
    this._panel.onDidChangeViewState(
      (e) => {
        if (this._panel.visible) {
          this._update();
        }
      },
      null,
      this._disposables
    );

    // Handle messages from the webview
    this._panel.webview.onDidReceiveMessage(
      (message) => {
        this._logger.log('Received message from webview:', message);
        switch (message.command) {
          case "refresh":
            this._update();
            return;
          case "openScope":
            if (message.filePath) {
              // Strip line number fragment if present (e.g., #L233)
              const cleanPath = message.filePath.split('#')[0];
              const lineNumber = message.filePath.includes('#L') 
                ? parseInt(message.filePath.split('#L')[1]) 
                : null;
              
              // If path is already absolute, use it; otherwise resolve from workspace root
              const absolutePath = path.isAbsolute(cleanPath) 
                ? cleanPath 
                : path.join(this._workspaceRoot, cleanPath);
              const fileUri = vscode.Uri.file(absolutePath);
              
              vscode.workspace.openTextDocument(fileUri).then(
                (doc) => {
                  const options = lineNumber 
                    ? { 
                        selection: new vscode.Range(lineNumber - 1, 0, lineNumber - 1, 0),
                        viewColumn: vscode.ViewColumn.One
                      }
                    : { viewColumn: vscode.ViewColumn.One };
                  vscode.window.showTextDocument(doc, options);
                },
                (error) => {
                  vscode.window.showErrorMessage(`Failed to open file: ${message.filePath}\n${error.message}`);
                }
              );
            }
            return;
          case "updateFilter":
            if (message.filter) {
              this._logger.log(`Updating scope filter to: ${message.filter}`);
              // Execute scope command via CLI
              this._dataProvider.updateScope(message.filter)
                .then(() => {
                  // Refresh panel after scope change
                  this._update();
                })
                .catch((error) => {
                  this._logger.error('Failed to update scope filter', error);
                  vscode.window.showErrorMessage(`Failed to update scope: ${error.message}`);
                });
            }
            return;
          case "updateWorkspace":
            if (message.workspacePath) {
              this._logger.log(`Updating workspace path to: ${message.workspacePath}`);
              // Execute path command via CLI
              this._dataProvider.updateWorkspace(message.workspacePath)
                .then(() => {
                  // Update workspace root and refresh
                  this._workspaceRoot = message.workspacePath;
                  this._update();
                })
                .catch((error) => {
                  this._logger.error('Failed to update workspace path', error);
                  vscode.window.showErrorMessage(`Failed to update workspace: ${error.message}`);
                });
            }
            return;
          case "switchBot":
            if (message.botName) {
              this._logger.log(`Switching bot to: ${message.botName}`);
              this._dataProvider.currentBot = message.botName;
              this._update();
            }
            return;
          case "executeCommand":
            if (message.commandText) {
              this._logger.log(`Executing command: ${message.commandText}`);
              this._dataProvider.executeCommand(message.commandText)
                .then((result) => {
                  this._logger.log('Command executed successfully');
                  // Show result in output channel or notification
                  vscode.window.showInformationMessage(`Command executed: ${message.commandText}`);
                  // Refresh the panel to show any state changes
                  this._update();
                })
                .catch((error) => {
                  this._logger.error('Failed to execute command', error);
                  vscode.window.showErrorMessage(`Failed to execute command: ${error.message}`);
                });
            }
            return;
        }
      },
      null,
      this._disposables
    );
  }

  static createOrShow(workspaceRoot, extensionUri) {
    const column = vscode.ViewColumn.Two;

    // If we already have a panel, show it
    if (StatusPanel.currentPanel) {
      StatusPanel.currentPanel._panel.reveal(column);
      return;
    }

    // Otherwise, create a new panel
    const panel = vscode.window.createWebviewPanel(
      StatusPanel.viewType,
      "Bot Status Dashboard",
      column,
      {
        enableScripts: true,
        retainContextWhenHidden: true,
        localResourceRoots: [extensionUri],
      }
    );

    StatusPanel.currentPanel = new StatusPanel(panel, workspaceRoot, extensionUri);
  }

  dispose() {
    StatusPanel.currentPanel = undefined;

    // Clean up resources
    this._panel.dispose();

    while (this._disposables.length) {
      const disposable = this._disposables.pop();
      if (disposable) {
        disposable.dispose();
      }
    }
  }

  async _update() {
    const webview = this._panel.webview;
    this._panel.title = "Bot Status Dashboard";
    
    this._logger.log("_update() called");
    
    try {
      // Check availability first
      const isAvailable = await this._dataProvider.checkAvailability();
      this._logger.log("Availability check", { isAvailable });
      
      if (!isAvailable) {
        this._panel.webview.html = this._renderer.renderError(
          "REPL CLI not found or Python not available. Please ensure Python is installed and REPL CLI is in the expected location."
        );
        return;
      }

      // Fetch status data
      const rawStatus = await this._dataProvider.getStatus();
      this._logger.log("Got raw status, length:", rawStatus.length);
      
      // Adapt CLI output to structured JSON
      const structuredData = this._adapter.adapt(rawStatus);
      
      // Add bot selector data
      structuredData.availableBots = this._dataProvider.getAvailableBots();
      structuredData.currentBot = this._dataProvider.getCurrentBot();
      
      this._logger.log("Adapted data", structuredData);

      // Render HTML
      this._panel.webview.html = this._renderer.render(structuredData);
      this._logger.log("Rendered HTML to webview");
      
    } catch (err) {
      console.error("Status panel update error:", err);
      this._logger.error("Status panel update error", err);
      this._panel.webview.html = this._renderer.renderError(err.message);
    }
  }
}

module.exports = StatusPanel;
