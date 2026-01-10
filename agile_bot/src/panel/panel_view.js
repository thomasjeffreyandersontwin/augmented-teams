/**
 * Base class for all panel views.
 * Handles subprocess communication and JSON parsing.
 */

const { spawn } = require('child_process');

class PanelView {
    /**
     * Base class for all panel views.
     * Handles subprocess communication and JSON parsing.
     */
    constructor(cli) {
        this.cli = cli;
        this.pythonProcess = null;
    }
    
    /**
     * Spawn Python CLI subprocess.
     * 
     * @param {string} scriptPath - Path to Python CLI script
     * @returns {ChildProcess} Python subprocess
     */
    spawnCLI(scriptPath) {
        this.pythonProcess = spawn('python', [scriptPath]);
        return this.pythonProcess;
    }
    
    /**
     * Send command to CLI via stdin.
     * 
     * @param {string} command - Command to send
     */
    sendCommand(command) {
        if (!this.pythonProcess) {
            throw new Error('Python process not spawned');
        }
        const commandJSON = JSON.stringify({ command: command });
        this.pythonProcess.stdin.write(commandJSON + '\n');
    }
    
    /**
     * Receive and parse JSON from CLI stdout.
     * 
     * @returns {Promise<Object>} Parsed JSON data
     */
    async receiveJSON() {
        return new Promise((resolve, reject) => {
            let buffer = '';
            
            this.pythonProcess.stdout.on('data', (data) => {
                buffer += data.toString();
                
                // Try to parse complete JSON
                try {
                    const jsonData = JSON.parse(buffer);
                    resolve(jsonData);
                    buffer = ''; // Clear buffer after successful parse
                } catch (e) {
                    // Incomplete JSON, keep buffering
                }
            });
            
            this.pythonProcess.stderr.on('data', (data) => {
                reject(new Error(`Python error: ${data.toString()}`));
            });
            
            // Timeout after 5 seconds
            setTimeout(() => {
                if (buffer) {
                    reject(new Error('Timeout waiting for complete JSON response'));
                }
            }, 5000);
        });
    }
    
    /**
     * Execute command and return parsed JSON.
     * 
     * @param {string} command - Command to execute
     * @returns {Promise<Object>} Parsed JSON response
     */
    async execute(command) {
        this.sendCommand(command);
        return await this.receiveJSON();
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
