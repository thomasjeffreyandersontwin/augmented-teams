/**
 * Base class for all panel views.
 * Provides singleton CLI access - views don't need parameters passed around.
 */

const { spawn } = require('child_process');
const path = require('path');

class PanelView {
    // Singleton CLI instance shared by all views
    static _sharedCLI = null;
    static _workspaceDir = null;
    static _botDir = null;
    static _commandQueue = [];
    static _processingCommand = false;
    static _firstCommandSent = false;
    
    /**
     * Base class for all panel views.
     * Views access singleton CLI - no parameters needed.
     */
    constructor() {
        // Views just inherit from base
    }
    
    /**
     * Initialize singleton CLI (call once at startup)
     * @param {string} workspaceDirectory - Workspace root path
     * @param {string} botDirectory - Bot directory path
     */
    static initializeCLI(workspaceDirectory, botDirectory) {
        if (!PanelView._sharedCLI) {
            PanelView._workspaceDir = workspaceDirectory;
            PanelView._botDir = botDirectory || process.env.BOT_DIRECTORY;
            
            if (!PanelView._botDir) {
            throw new Error('BOT_DIRECTORY environment variable must be set or botDirectory must be provided');
        }
        
            PanelView._spawnCLI();
        }
        return PanelView._sharedCLI;
    }
    
    /**
     * Get singleton CLI instance
     */
    static getCLI() {
        return PanelView._sharedCLI;
    }
    
    /**
     * Get workspace directory
     */
    static getWorkspaceDir() {
        return PanelView._workspaceDir;
    }
    
    /**
     * Get bot directory
     */
    static getBotDir() {
        return PanelView._botDir;
    }
    
    /**
     * Execute command on singleton CLI
     */
    async execute(command) {
        const cli = PanelView.getCLI();
        if (!cli) {
            // Auto-initialize if not done yet
            if (PanelView._workspaceDir || process.env.WORKING_AREA) {
                PanelView.initializeCLI(
                    PanelView._workspaceDir || process.env.WORKING_AREA || process.cwd(),
                    process.env.BOT_DIRECTORY
                );
            } else {
                throw new Error('CLI not initialized. Call PanelView.initializeCLI() first.');
            }
        }
        return await PanelView._sendCommand(command);
    }
    
    /**
     * Cleanup shared CLI instance (for tests).
     */
    static cleanupSharedCLI() {
        if (PanelView._sharedCLI) {
            try {
                const proc = PanelView._sharedCLI;
                proc.stdout.removeAllListeners();
                proc.stderr.removeAllListeners();
                proc.removeAllListeners();
                proc.kill('SIGKILL');
            } catch (e) {
                // Ignore errors
            }
            PanelView._sharedCLI = null;
            PanelView._workspaceDir = null;
            PanelView._botDir = null;
            PanelView._commandQueue = [];
            PanelView._processingCommand = false;
            PanelView._firstCommandSent = false;
        }
    }
    
    /**
     * Spawn Python CLI subprocess (static singleton).
     */
    static _spawnCLI() {
        const workspaceRoot = PanelView._workspaceDir || process.env.WORKING_AREA || process.cwd();
        const cliPath = path.join(workspaceRoot, 'agile_bot', 'src', 'cli', 'cli_main.py');
        
        console.log('[PanelView] _spawnCLI called with:', {
            _workspaceDir: PanelView._workspaceDir,
            _botDir: PanelView._botDir,
            workspaceRoot: workspaceRoot,
            cliPath: cliPath
        });
        
        // Verify CLI path exists
        try {
            const fs = require('fs');
            if (!fs.existsSync(cliPath)) {
                console.error(`[PanelView] CLI script NOT found at: ${cliPath}`);
                throw new Error(`CLI script not found at: ${cliPath}`);
            }
            console.log(`[PanelView] CLI script verified at: ${cliPath}`);
        } catch (err) {
            console.error('[PanelView] CLI path check error:', err);
            throw new Error(`Cannot find CLI script: ${cliPath}. Please ensure you're in the correct workspace.`);
        }
        
        const env = {
            ...process.env,
            PYTHONPATH: workspaceRoot,
            BOT_DIRECTORY: PanelView._botDir,
            WORKING_AREA: workspaceRoot,
            CLI_MODE: 'json'
        };
        
        console.log('[PanelView] Spawning CLI with env:', {
            python: 'python',
            cliPath: cliPath,
            workspaceRoot: workspaceRoot,
            botDirectory: PanelView._botDir,
            cwd: workspaceRoot,
            CLI_MODE: 'json'
        });
        
        PanelView._sharedCLI = spawn('python', [cliPath], {
            cwd: workspaceRoot,
            env: env,
            stdio: ['pipe', 'pipe', 'pipe']
        });
        
        console.log('[PanelView] CLI spawn initiated, PID:', PanelView._sharedCLI.pid);
        
        PanelView._sharedCLI.on('error', (err) => {
            console.error('[PanelView] Python process spawn error:', err);
            throw new Error(`Failed to spawn Python process: ${err.message}`);
        });
        
        PanelView._sharedCLI.stderr.on('data', (data) => {
            const errorText = data.toString();
            console.error('[PanelView] Python stderr:', errorText);
            if (errorText.includes('Traceback')) {
                console.error('[PanelView] Python process crashed!');
            }
        });
        
        PanelView._sharedCLI.stdout.on('data', (data) => {
            console.log('[PanelView] Python stdout (raw):', data.toString().substring(0, 200));
        });
        
        PanelView._sharedCLI.on('exit', (code, signal) => {
            console.log(`[PanelView] Python process exited with code ${code}, signal ${signal}`);
        });
        
        console.log('[PanelView] CLI spawn complete');
        return PanelView._sharedCLI;
    }
    
    /**
     * Send command to singleton CLI
     */
    static async _sendCommand(command) {
        const cli = PanelView._sharedCLI;
        if (!cli || cli.killed || cli.exitCode !== null) {
            throw new Error('CLI process not available');
        }
        
        // Queue command
        return new Promise((resolve, reject) => {
            PanelView._commandQueue.push({ command, resolve, reject });
            PanelView._processNextCommand();
        });
    }
    
    /**
     * Process command queue (static)
     */
    static async _processNextCommand() {
        if (PanelView._processingCommand || PanelView._commandQueue.length === 0) {
            return;
        }
        
        PanelView._processingCommand = true;
        const { command, resolve, reject } = PanelView._commandQueue.shift();
        const cli = PanelView._sharedCLI;
        
        try {
            // Wait for process to be ready (first command)
            if (!PanelView._firstCommandSent) {
                await new Promise(r => setTimeout(r, 500));
                PanelView._firstCommandSent = true;
            }
            
            let buffer = '';
            let dataTimeout = null;
            
            const timeout = setTimeout(() => {
                if (dataTimeout) clearTimeout(dataTimeout);
                cli.stdout.removeListener('data', stdoutHandler);
                cli.stderr.removeListener('data', stderrHandler);
                PanelView._processingCommand = false;
                console.error('[PanelView] Command timeout:', { command, buffer, processAlive: !cli.killed });
                reject(new Error(`Timeout waiting for JSON response. Buffer: ${buffer}`));
                PanelView._processNextCommand();
            }, 10000);
            
            const stdoutHandler = (data) => {
                buffer += data.toString();
                console.log(`[PanelView] Command "${command}" - stdout chunk:`, data.toString().substring(0, 100));
                console.log(`[PanelView] Buffer length: ${buffer.length}`);
                if (dataTimeout) clearTimeout(dataTimeout);
                
                // Find complete JSON object
                let depth = 0, start = -1;
                for (let i = 0; i < buffer.length; i++) {
                    if (buffer[i] === '{') {
                        if (depth === 0) start = i;
                        depth++;
                    } else if (buffer[i] === '}') {
                        depth--;
                        if (depth === 0 && start !== -1) {
                            try {
                                const jsonData = JSON.parse(buffer.substring(start, i + 1));
                                console.log(`[PanelView] Command "${command}" - JSON parsed successfully`);
                                console.log(`[PanelView] JSON keys:`, Object.keys(jsonData));
                                if (jsonData.bot) {
                                    console.log(`[PanelView] Bot data keys:`, Object.keys(jsonData.bot));
                                }
                                dataTimeout = setTimeout(() => {
                                    clearTimeout(timeout);
                                    cli.stdout.removeListener('data', stdoutHandler);
                                    cli.stderr.removeListener('data', stderrHandler);
                                    PanelView._processingCommand = false;
                                    console.log(`[PanelView] Resolving command "${command}" with data`);
                                    resolve(jsonData);
                                    PanelView._processNextCommand();
                                }, 200);
                                return;
                            } catch (e) {
                                console.error(`[PanelView] JSON parse error:`, e.message);
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
                    cli.stdout.removeListener('data', stdoutHandler);
                    cli.stderr.removeListener('data', stderrHandler);
                    PanelView._processingCommand = false;
                    reject(new Error(`Python error: ${errorText}`));
                    PanelView._processNextCommand();
                }
            };
            
            cli.stdout.on('data', stdoutHandler);
            cli.stderr.on('data', stderrHandler);
            
            console.log(`[PanelView] Sending command to CLI: "${command}"`);
            cli.stdin.write(command.trim() + '\n');
            if (cli.stdin.flush) cli.stdin.flush();
            console.log(`[PanelView] Command written to stdin`);
        } catch (error) {
            PanelView._processingCommand = false;
            reject(error);
            PanelView._processNextCommand();
        }
    }
    
    /**
     * Get unique element ID
     */
    getElementId() {
        return `view-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
    }
    
    /**
     * Render to HTML. Override in subclasses.
     */
    render(jsonData) {
        throw new Error('render() must be implemented by subclass');
    }
}

module.exports = PanelView;
