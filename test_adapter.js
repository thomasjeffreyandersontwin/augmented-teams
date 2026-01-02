const fs = require('fs');

// Read the test output
const rawOutput = fs.readFileSync('test_raw.txt', 'utf8');

// Test bot name extraction
const botMatch = /##[^B]*Bot:\s*(.+)/m.exec(rawOutput);
console.log('Bot Match:', botMatch ? botMatch[1].trim() : 'NO MATCH');

// Test bot path extraction
const botPathMatch = /\*\*Bot Path:\*\*[^\n]*\n\s*```\s*\n\s*(.+?)\s*\n\s*```/s.exec(rawOutput);
console.log('Bot Path Match:', botPathMatch ? botPathMatch[1].trim() : 'NO MATCH');

// Test workspace extraction - try different patterns
console.log('\n--- Testing Workspace Patterns ---');
const ws1 = /📂\s*\*\*Workspace:\*\*\s*(.+?)\s*\n\s*```\s*\n\s*(.+?)\s*\n\s*```/s.exec(rawOutput);
console.log('Pattern 1:', ws1 ? {name: ws1[1].trim(), path: ws1[2].trim()} : 'NO MATCH');

const ws2 = /📂\s*\*\*Workspace:\*\*\s*(.+)\n```\n(.+?)\n```/s.exec(rawOutput);
console.log('Pattern 2:', ws2 ? {name: ws2[1].trim(), path: ws2[2].trim()} : 'NO MATCH');

const ws3 = /Workspace:\*\*\s+(.+?)\s*\n\s*```\s*(.+?)```/s.exec(rawOutput);
console.log('Pattern 3:', ws3 ? {name: ws3[1].trim(), path: ws3[2].trim()} : 'NO MATCH');

// Test behaviors extraction
const progressSection = rawOutput.match(/Progress[\s\S]*?────/);
console.log('Progress Section Found:', progressSection ? 'YES' : 'NO');
if (progressSection) {
    const behaviorMatches = progressSection[0].match(/^- [➤☑☐] \w+/gm);
    console.log('Behaviors Found:', behaviorMatches ? behaviorMatches.length : 0);
}
