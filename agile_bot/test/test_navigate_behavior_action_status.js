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

test('TestDisplayBotHierarchyTree', { concurrency: false }, async (t) => {
    
    await t.test('test_user_views_bot_hierarchy_with_status_command', async () => {
        /**
         * SCENARIO: Panel displays bot hierarchy
         * GIVEN: Bot is at exploration.validate
         * WHEN: Panel refreshes and receives status JSON from CLI
         * THEN: StatusView renders bot hierarchy information
         */
        const tmpPath = path.join(__dirname, '../../demo/mob_minion');
        const botDir = path.join(__dirname, '../bots/story_bot');
        
        const pythonProcess = spawnCLI(tmpPath, botDir);
        
        try {
            const statusJSON = await sendCommand(pythonProcess, 'status');
            
            const statusView = new StatusView(statusJSON, null);
            const html = statusView.render();
            
            assert(statusJSON.progress_path);
            assert(statusJSON.stage_name);
            assert(html.includes(statusJSON.progress_path));
            assert(html.includes(statusJSON.stage_name));
        } finally {
            pythonProcess.kill();
        }
    });
});

test('TestDisplayCurrentPosition', { concurrency: false }, async (t) => {
    
    await t.test('test_user_views_current_position_in_status', async () => {
        /**
         * SCENARIO: Panel displays current position
         * GIVEN: Bot is at shape.clarify
         * WHEN: Panel refreshes and receives status JSON from CLI
         * THEN: StatusView renders current position information
         */
        const tmpPath = path.join(__dirname, '../../demo/mob_minion');
        const botDir = path.join(__dirname, '../bots/story_bot');
        
        const pythonProcess = spawnCLI(tmpPath, botDir);
        
        try {
            const statusJSON = await sendCommand(pythonProcess, 'status');
            
            const statusView = new StatusView(statusJSON, null);
            const html = statusView.render();
            
            assert(statusJSON.progress_path);
            assert(html.includes(statusJSON.progress_path));
            if (statusJSON.current_behavior) {
                assert(html.includes(statusJSON.current_behavior));
            }
        } finally {
            pythonProcess.kill();
        }
    });
    
    await t.test('test_status_contains_progress_section_with_current_position', async () => {
        /**
         * SCENARIO: Panel displays Progress section with current position
         * GIVEN: Bot is at exploration.validate
         * WHEN: Panel refreshes and receives status JSON from CLI
         * THEN: StatusView renders Progress section with current position
         */
        const tmpPath = path.join(__dirname, '../../demo/mob_minion');
        const botDir = path.join(__dirname, '../bots/story_bot');
        
        const pythonProcess = spawnCLI(tmpPath, botDir);
        
        try {
            const statusJSON = await sendCommand(pythonProcess, 'status');
            
            assert('progress_path' in statusJSON);
            assert('stage_name' in statusJSON);
            assert('current_behavior' in statusJSON);
            assert('current_action' in statusJSON);
            
            const statusView = new StatusView(statusJSON, null);
            const html = statusView.render();
            
            assert(html.includes(statusJSON.progress_path));
        } finally {
            pythonProcess.kill();
        }
    });
    
    await t.test('test_status_contains_behavior_in_progress_section', async () => {
        /**
         * SCENARIO: Panel displays behavior in Progress section
         * GIVEN: Bot is at shape.validate
         * WHEN: Panel refreshes and receives status JSON from CLI
         * THEN: StatusView renders current behavior in Progress section
         */
        const tmpPath = path.join(__dirname, '../../demo/mob_minion');
        const botDir = path.join(__dirname, '../bots/story_bot');
        
        const pythonProcess = spawnCLI(tmpPath, botDir);
        
        try {
            const statusJSON = await sendCommand(pythonProcess, 'status');
            
            assert('current_behavior' in statusJSON);
            assert('current_action' in statusJSON);
            
            const statusView = new StatusView(statusJSON, null);
            const html = statusView.render();
            
            if (statusJSON.current_behavior) {
                assert(html.includes(statusJSON.current_behavior));
            }
        } finally {
            pythonProcess.kill();
        }
    });
});
