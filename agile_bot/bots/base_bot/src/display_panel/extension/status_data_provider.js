/**
 * Status Data Provider
 * 
 * Interfaces with Python REPL CLI to retrieve status information.
 * Spawns Python subprocess and sends 'status' command via stdin.
 */

const cp = require("child_process");
const path = require("path");
const Logger = require("./logger.js");

class StatusDataProvider {
  constructor(workspaceRoot) {
    this.workspaceRoot = workspaceRoot;
    this.timeout = 10000; // 10 second timeout
    
    // Setup logger
    const logPath = path.join(workspaceRoot, "agile_bot", "bots", "base_bot", "logs", "panel-debug.log");
    this.logger = new Logger(logPath);
    this.logger.log("StatusDataProvider initialized", { workspaceRoot });
  }

  /**
   * Get status data by calling REPL CLI
   * @returns {Promise<string>} Raw status text output from CLI
   */
  async getStatus() {
    this.logger.log("getStatus() called");
    
    return new Promise((resolve, reject) => {
      const replMainPath = path.join(
        this.workspaceRoot,
        "agile_bot",
        "bots",
        "base_bot",
        "src",
        "repl_cli",
        "repl_main.py"
      );

      // Set up environment variables for CLI
      const env = Object.assign({}, process.env, {
        PYTHONPATH: this.workspaceRoot,
        BOT_DIRECTORY: path.join(this.workspaceRoot, "agile_bot", "bots", "story_bot"),
        WORKING_AREA: path.join(this.workspaceRoot, "agile_bot", "bots", "base_bot")
      });

      this.logger.log("Spawning Python process", {
        replMainPath,
        cwd: this.workspaceRoot,
        env: {
          PYTHONPATH: env.PYTHONPATH,
          BOT_DIRECTORY: env.BOT_DIRECTORY,
          WORKING_AREA: env.WORKING_AREA
        }
      });

      // Spawn Python process with environment
      const pythonProcess = cp.spawn("python", [replMainPath], {
        cwd: this.workspaceRoot,
        timeout: this.timeout,
        env: env
      });

      let stdout = "";
      let stderr = "";
      let timedOut = false;

      // Set timeout
      const timeoutId = setTimeout(() => {
        timedOut = true;
        pythonProcess.kill();
        reject(new Error("Python process timed out after 10 seconds"));
      }, this.timeout);

      // Send 'status --format json' command via stdin
      try {
        pythonProcess.stdin.write("status --format json\n");
        pythonProcess.stdin.end();
      } catch (err) {
        clearTimeout(timeoutId);
        this.logger.error("Failed to write to Python stdin", err);
        reject(new Error(`Failed to communicate with Python process: ${err.message}`));
        return;
      }

      // Collect stdout
      pythonProcess.stdout.on("data", (data) => {
        stdout += data.toString();
      });

      // Collect stderr
      pythonProcess.stderr.on("data", (data) => {
        stderr += data.toString();
      });

      // Handle process error
      pythonProcess.on("error", (err) => {
        clearTimeout(timeoutId);
        this.logger.error("Python process error", err);
        reject(new Error(`Python process error: ${err.message}`));
      });

      // Handle process completion
      pythonProcess.on("close", (code) => {
        clearTimeout(timeoutId);
        
        if (timedOut) {
          return; // Already rejected
        }

        this.logger.log("Python process closed", {
          exitCode: code,
          stdoutLength: stdout.length,
          stderrLength: stderr.length
        });

        if (stderr) {
          this.logger.log("STDERR output:", stderr);
        }

        if (code !== 0 && stderr) {
          this.logger.error("Python CLI failed", new Error(`Exit ${code}: ${stderr}`));
          reject(new Error(`Python CLI failed (exit ${code}): ${stderr}`));
          return;
        }

        if (!stdout || stdout.trim().length === 0) {
          this.logger.log("ERROR: No output from Python CLI");
          reject(new Error("No output from Python CLI"));
          return;
        }

        this.logger.log("Raw CLI output received (first 500 chars):", stdout.substring(0, 500));
        this.logger.log("Raw CLI output received (FULL OUTPUT):", stdout);
        resolve(stdout);
      });
    });
  }

  /**
   * Check if Python and REPL CLI are available
   * @returns {Promise<boolean>} True if available
   */
  async checkAvailability() {
    return new Promise((resolve) => {
      try {
        const pythonCheck = cp.spawn("python", ["--version"]);
        pythonCheck.on("close", (code) => {
          this.logger.log("Python availability check", { exitCode: code });
          resolve(code === 0);
        });
        pythonCheck.on("error", () => {
          this.logger.log("Python not found");
          resolve(false);
        });
      } catch (err) {
        this.logger.error("Availability check error", err);
        resolve(false);
      }
    });
  }
}

module.exports = StatusDataProvider;
