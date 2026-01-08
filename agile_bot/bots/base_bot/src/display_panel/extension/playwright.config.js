// @ts-check
const { defineConfig, devices } = require('@playwright/test');

/**
 * Playwright Configuration for VS Code Extension Testing
 * 
 * This configuration:
 * - Uses a single worker to avoid VS Code conflicts
 * - Captures screenshots and videos on failure
 * - Uses Chromium browser
 * - Sets generous timeouts for VS Code extension startup
 */
module.exports = defineConfig({
  testDir: './test',
  
  // Match test files using Python-style naming convention (test_*.js)
  testMatch: /test_.*\.js$/,
  
  // Run tests in files in parallel, but use single worker to avoid VS Code conflicts
  fullyParallel: false,
  workers: 1,
  
  // Fail the build on CI if you accidentally left test.only in the source code
  forbidOnly: !!process.env.CI,
  
  // Retry on CI only
  retries: process.env.CI ? 2 : 0,
  
  // Reporter to use
  reporter: [
    ['html'],
    ['list']
  ],
  
  // Shared settings for all the projects below
  use: {
    // Base URL to use in actions like `await page.goto('/')`
    baseURL: 'http://localhost:3000',
    
    // Collect trace when retrying the failed test
    trace: 'on-first-retry',
    
    // Screenshot on failure
    screenshot: 'only-on-failure',
    
    // Video on failure
    video: 'retain-on-failure',
    
    // Generous timeout for VS Code extension actions
    actionTimeout: 30000,
  },
  
  // Configure timeout for each test
  timeout: 60000,
  
  // Configure projects for major browsers
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
  ],
  
  // Start the panel server before running tests
  webServer: {
    command: 'node server.js',
    port: 3000,
    timeout: 120 * 1000,
    reuseExistingServer: !process.env.CI,
  },
});

