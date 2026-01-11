/**
 * Base class for all panel views.
 * Handles subprocess communication and JSON parsing.
 */

const { spawn } = require('child_process');
const path = require('path');

class PanelView {
    /**
     * Base class for all panel views.
     * Spawns and manages a persistent CLI subprocess.
     * 
     * @param {Object} cli - CLI instance for subprocess communication (can be null, will spawn if needed)
     * @param {string} workspaceDirectory - Workspace directory path
     * @param {string} botDirectory - Bot directory path (optional, defaults to story_bot)
     */
    constructor(cli, workspaceDirectory, botDirectory) {
        this.workspaceDirectory = workspaceDirectory;
        
        // Determine bot directory using same logic as CLI
        // 1. Use provided botDirectory if given
        // 2. Check BOT_DIRECTORY environment variable
        if (botDirectory) {
            this.botDirectory = botDirectory;
        } else if (process.env.BOT_DIRECTORY) {
            this.botDirectory = process.env.BOT_DIRECTORY;
        } else {
            throw new Error('BOT_DIRECTORY environment variable must be set or botDirectory must be provided');
        }
        
        this.cli = null;
        this._firstCommandSent = false;
        this._commandQueue = [];
        this._processingCommand = false;
        
        // Spawn CLI process immediately (cli parameter is ignored for now, kept for API compatibility)
        this.spawnCLI();
    }
    
    /**
     * Spawn Python CLI subprocess in JSON mode.
     * Creates a persistent REPL session that can handle multiple commands.
     * Stores the process in this.cli.
     * 
     * @returns {ChildProcess} CLI subprocess
     */
    spawnCLI() {
        // Find CLI script relative to workspace root (not extension directory)
        // The CLI is at: workspace_root/agile_bot/src/cli/cli_main.py
        const workspaceRoot = this.workspaceDirectory || process.env.WORKING_AREA || process.cwd();
        const cliPath = path.join(workspaceRoot, 'agile_bot', 'src', 'cli', 'cli_main.py');
        
        // Verify CLI path exists
        try {
            const fs = require('fs');
            if (!fs.existsSync(cliPath)) {
                throw new Error(`CLI script not found at: ${cliPath}`);
            }
        } catch (err) {
            console.error('CLI path check error:', err);
            throw new Error(`Cannot find CLI script: ${cliPath}. Please ensure you're in the correct workspace.`);
        }
        
        // PYTHONPATH should include the workspace root so Python can find agile_bot modules
        const pythonPath = workspaceRoot;
        
        const env = {
            ...process.env,
            PYTHONPATH: pythonPath,
            BOT_DIRECTORY: this.botDirectory,
            WORKING_AREA: workspaceRoot,
            CLI_MODE: 'json'  // Explicitly request JSON mode for panel views
        };
        
        console.log('[PanelView] Spawning CLI:', {
            python: 'python',
            cliPath: cliPath,
            workspaceRoot: workspaceRoot,
            botDirectory: this.botDirectory,
            cwd: this.workspaceDirectory || process.cwd()
        });
        
        this.cli = spawn('python', [cliPath], {
            cwd: this.workspaceDirectory || process.cwd(),
            env: env,
            stdio: ['pipe', 'pipe', 'pipe']
        });
        
        // Handle process errors
        this.cli.on('error', (err) => {
            console.error('[PanelView] Python process spawn error:', err);
            throw new Error(`Failed to spawn Python process: ${err.message}. Please ensure Python is installed and accessible.`);
        });
        
        // Track if process has started
        this._processReady = false;
        
        // Wait a short time for process to start, then mark as ready
        // This avoids needing a permanent listener that interferes with command processing
        setTimeout(() => {
            this._processReady = true;
        }, 500);
        
        // Log all stderr for debugging
        this.cli.stderr.on('data', (data) => {
            const errorText = data.toString();
            console.error('[PanelView] Python stderr:', errorText);
            // If we see a traceback, the process is likely dead
            if (errorText.includes('Traceback')) {
                console.error('[PanelView] Python process crashed!');
            }
        });
        
        // Log stdout for debugging
        this.cli.stdout.on('data', (data) => {
            const outputText = data.toString();
            console.log('[PanelView] Python stdout (initial):', outputText.substring(0, 200));
        });
        
        // Handle process exit
        this.cli.on('exit', (code, signal) => {
            console.error(`[PanelView] Python process exited with code ${code}, signal ${signal}`);
        });
        
        return this.cli;
    }
    
    /**
     * Clean up: kill the Python process and remove all listeners.
     */
    cleanup() {
        if (this.cli) {
            const proc = this.cli;
            
            // Remove all listeners first to prevent memory leaks
            proc.stdout.removeAllListeners();
            proc.stderr.removeAllListeners();
            proc.stdin.removeAllListeners();
            
            // Close stdin to signal EOF to Python process
            try {
                if (!proc.stdin.destroyed) {
                    proc.stdin.destroy();
                }
            } catch (e) {
                // Ignore errors
            }
            
            // Kill the process forcefully
            try {
                if (!proc.killed && proc.exitCode === null) {
                    proc.kill('SIGKILL');
                }
            } catch (e) {
                // Ignore errors if process is already dead
            }
            
            // Clear the reference
            this.cli = null;
        }
    }
    
    /**
     * Send command to CLI via stdin in JSON mode and return parsed JSON response.
     * Reuses the same Python process for multiple commands.
     * Commands are queued and processed sequentially to avoid interference.
     * 
     * @param {string} command - Command to send
     * @returns {Promise<Object>} Parsed JSON response
     */
    async sendCommand(command) {
        if (!this.cli) {
            throw new Error('CLI process not spawned');
        }
        
        // Check if process is still alive
        if (this.cli.killed || this.cli.exitCode !== null) {
            throw new Error(`CLI process has exited (exitCode: ${this.cli.exitCode})`);
        }
        
        // Queue command if another is being processed
        return new Promise((resolve, reject) => {
            this._commandQueue.push({ command, resolve, reject });
            this._processNextCommand();
        });
    }
    
    /**
     * Process the next command in the queue.
     * Ensures only one command is processed at a time.
     */
    async _processNextCommand() {
        // If already processing or queue is empty, return
        if (this._processingCommand || this._commandQueue.length === 0) {
            return;
        }
        
        this._processingCommand = true;
        const { command, resolve, reject } = this._commandQueue.shift();
        
        try {
            // Wait for process to be ready (if first command)
            if (!this._firstCommandSent) {
                // Wait for process to be ready (max 1000ms)
                let waited = 0;
                while (!this._processReady && waited < 1000) {
                    await new Promise(resolve => setTimeout(resolve, 50));
                    waited += 50;
                }
                // Additional small delay to ensure process is fully initialized
                await new Promise(resolve => setTimeout(resolve, 100));
                this._firstCommandSent = true;
            }
            
            let buffer = '';
            let lastCompleteJson = null;
            let dataReceivedTimeout = null;
            
            const timeout = setTimeout(() => {
                // Remove listeners to prevent memory leaks
                if (dataReceivedTimeout) clearTimeout(dataReceivedTimeout);
                this.cli.stdout.removeListener('data', stdoutHandler);
                this.cli.stderr.removeListener('data', stderrHandler);
                this._processingCommand = false;
                const errorMsg = `Timeout waiting for JSON response. Buffer: ${buffer.substring(0, 500)}${buffer.length > 500 ? '...' : ''}`;
                console.error('[PanelView] Command timeout:', {
                    command: command,
                    buffer: buffer,
                    processAlive: !this.cli.killed && this.cli.exitCode === null,
                    exitCode: this.cli.exitCode
                });
                reject(new Error(errorMsg));
                // Process next command in queue
                this._processNextCommand();
            }, 10000); // Increased timeout to 10 seconds
            
            const stdoutHandler = (data) => {
                buffer += data.toString();
                
                // Clear any pending timeout since we got new data
                if (dataReceivedTimeout) {
                    clearTimeout(dataReceivedTimeout);
                    dataReceivedTimeout = null;
                }
                
                // In JSON mode, CLI outputs a single unified JSON object
                // Find the complete JSON object by counting braces
                let depth = 0;
                let start = -1;
                
                for (let i = 0; i < buffer.length; i++) {
                    if (buffer[i] === '{') {
                        if (depth === 0) start = i;
                        depth++;
                    } else if (buffer[i] === '}') {
                        depth--;
                        if (depth === 0 && start !== -1) {
                            // Found a complete JSON object
                            try {
                                const jsonStr = buffer.substring(start, i + 1);
                                const jsonData = JSON.parse(jsonStr);
                                lastCompleteJson = jsonData;
                                // Wait a short time to ensure no more data arrives
                                dataReceivedTimeout = setTimeout(() => {
                                    clearTimeout(timeout);
                                    this.cli.stdout.removeListener('data', stdoutHandler);
                                    this.cli.stderr.removeListener('data', stderrHandler);
                                    this._processingCommand = false;
                                    resolve(lastCompleteJson);
                                    // Process next command in queue
                                    this._processNextCommand();
                                }, 200);
                                return;
                            } catch (e) {
                                // Not valid JSON, keep looking
                                start = -1;
                            }
                        }
                    }
                }
            };
            
            const stderrHandler = (data) => {
                const errorText = data.toString();
                if (errorText.includes('ERROR:') || errorText.includes('Traceback')) {
                    clearTimeout(timeout);
                    this.cli.stdout.removeListener('data', stdoutHandler);
                    this.cli.stderr.removeListener('data', stderrHandler);
                    this._processingCommand = false;
                    reject(new Error(`Python error: ${errorText}`));
                    // Process next command in queue
                    this._processNextCommand();
                }
            };
            
            this.cli.stdout.on('data', stdoutHandler);
            this.cli.stderr.on('data', stderrHandler);
            
            // Always request JSON format for panel views
            // DON'T close stdin - keep the REPL session alive
            // CLI_MODE=json is already set in env, so just send the command
            // The CLI will strip --format json if present, but it's not needed
            const jsonCommand = command.trim();
            this.cli.stdin.write(jsonCommand + '\n');
            // Flush stdin to ensure command is sent immediately
            if (this.cli.stdin.flush) {
                this.cli.stdin.flush();
            }
        } catch (error) {
            this._processingCommand = false;
            reject(error);
            // Process next command in queue
            this._processNextCommand();
        }
    }
    
    /**
     * Execute command and return parsed JSON.
     * Convenience method that calls sendCommand.
     * 
     * @param {string} command - Command to execute
     * @returns {Promise<Object>} Parsed JSON response
     */
    async execute(command) {
        return await this.sendCommand(command);
    }
    
    /**
     * Get unique element ID for this view.
     * 
     * @returns {string} Unique element ID
     */
    getElementId() {
        return `view-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
    }
    
    /**
     * Render to HTML. Override in subclasses.
     * 
     * @param {Object} jsonData - JSON data to render
     * @returns {string} HTML string
     */
    render(jsonData) {
        throw new Error('render() must be implemented by subclass');
    }
}

module.exports = PanelView;
