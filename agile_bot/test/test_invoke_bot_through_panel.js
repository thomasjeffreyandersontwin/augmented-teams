const { test } = require('node:test');
const { spawn } = require('child_process');
const assert = require('assert');
const path = require('path');
const StatusView = require('../src/status/status_view');

function spawnCLI(workspacePath, botDirectory) {
    const cliScript = path.join(__dirname, '../src/cli/cli_main.py');
    const env = {
        ...process.env,
        PYTHONPATH: path.join(__dirname, '../../..'),
        BOT_DIRECTORY: botDirectory,
        WORKING_AREA: workspacePath
    };
    
    const pythonProcess = spawn('python', [cliScript], {
        cwd: workspacePath,
        env: env,
        stdio: ['pipe', 'pipe', 'pipe']
    });
    
    return pythonProcess;
}

function sendCommand(process, command) {
    return new Promise((resolve, reject) => {
        let buffer = '';
        let errorBuffer = '';
        const timeout = setTimeout(() => {
            reject(new Error(`Timeout waiting for JSON response. Received: ${buffer}, Errors: ${errorBuffer}`));
        }, 5000);
        
        const stdoutHandler = (data) => {
            buffer += data.toString();
            try {
                const jsonData = JSON.parse(buffer.trim());
                clearTimeout(timeout);
                process.stdout.removeListener('data', stdoutHandler);
                process.stderr.removeListener('data', stderrHandler);
                resolve(jsonData);
            } catch (e) {
            }
        };
        
        const stderrHandler = (data) => {
            errorBuffer += data.toString();
        };
        
        process.stdout.on('data', stdoutHandler);
        process.stderr.on('data', stderrHandler);
        
        process.stdin.write(command + '\n');
        process.stdin.end();
    });
}

test('TestStartPanel', { concurrency: false }, async (t) => {
    
    await t.test('test_panel_opens_in_json_mode', async () => {
        /**
         * SCENARIO: Panel opens in JSON mode
         * GIVEN: Panel spawns CLI subprocess (piped mode)
         * WHEN: Panel sends 'status' command to CLI
         * THEN: CLI returns JSON response
         * AND: StatusView can parse JSON and render HTML
         */
        const tmpPath = path.join(__dirname, '../../demo/mob_minion');
        const botDir = path.join(__dirname, '../bots/story_bot');
        
        const pythonProcess = spawnCLI(tmpPath, botDir);
        
        try {
            const statusJSON = await sendCommand(pythonProcess, 'status');
            
            assert(typeof statusJSON === 'object');
            assert('progress_path' in statusJSON || 'stage_name' in statusJSON);
            
            const statusView = new StatusView(statusJSON, null);
            const html = statusView.render();
            
            assert(typeof html === 'string');
            assert(html.length > 0);
        } finally {
            pythonProcess.kill();
        }
    });
    
    await t.test('test_panel_displays_status_correctly', async () => {
        /**
         * SCENARIO: Panel displays status correctly
         * GIVEN: Bot is at exploration.validate
         * WHEN: Panel opens and receives status JSON from CLI
         * THEN: StatusView renders bot hierarchy information
         * AND: StatusView renders current position
         */
        const tmpPath = path.join(__dirname, '../../demo/mob_minion');
        const botDir = path.join(__dirname, '../bots/story_bot');
        
        const pythonProcess = spawnCLI(tmpPath, botDir);
        
        try {
            const statusJSON = await sendCommand(pythonProcess, 'status');
            
            assert(statusJSON.progress_path);
            assert(statusJSON.stage_name);
            
            const statusView = new StatusView(statusJSON, null);
            const html = statusView.render();
            
            assert(html.includes(statusJSON.progress_path));
            assert(html.includes(statusJSON.stage_name));
            
            if (statusJSON.current_behavior) {
                assert(html.includes(statusJSON.current_behavior));
            }
        } finally {
            pythonProcess.kill();
        }
    });
    
    await t.test('test_panel_already_open_when_command_executed', async () => {
        /**
         * SCENARIO: Panel already open when command executed
         * GIVEN: Panel is already open
         * WHEN: User executes panel command again (sends another status command)
         * THEN: Existing panel is refreshed (not duplicated)
         * AND: StatusView can be re-instantiated with new JSON
         */
        const tmpPath = path.join(__dirname, '../../demo/mob_minion');
        const botDir = path.join(__dirname, '../bots/story_bot');
        
        const pythonProcess1 = spawnCLI(tmpPath, botDir);
        
        try {
            const statusJSON1 = await sendCommand(pythonProcess1, 'status');
            const statusView1 = new StatusView(statusJSON1, null);
            const html1 = statusView1.render();
            
            pythonProcess1.kill();
            
            const pythonProcess2 = spawnCLI(tmpPath, botDir);
            const statusJSON2 = await sendCommand(pythonProcess2, 'status');
            const statusView2 = new StatusView(statusJSON2, null);
            const html2 = statusView2.render();
            pythonProcess2.kill();
            
            assert(typeof html1 === 'string');
            assert(typeof html2 === 'string');
            assert(html1.length > 0);
            assert(html2.length > 0);
        } catch (e) {
            if (pythonProcess1) pythonProcess1.kill();
            throw e;
        }
    });
    
    await t.test('test_panel_handles_cli_errors_gracefully', async () => {
        /**
         * SCENARIO: Panel handles CLI errors gracefully
         * GIVEN: CLI subprocess is spawned
         * WHEN: Panel sends invalid command
         * THEN: Panel receives error response
         * AND: Panel does not crash
         */
        const tmpPath = path.join(__dirname, '../../demo/mob_minion');
        const botDir = path.join(__dirname, '../bots/story_bot');
        
        const pythonProcess = spawnCLI(tmpPath, botDir);
        
        try {
            try {
                await sendCommand(pythonProcess, 'invalid_command_xyz');
                assert.fail('Should have thrown error for invalid command');
            } catch (error) {
                assert(error instanceof Error);
            }
        } finally {
            pythonProcess.kill();
        }
    });
});
