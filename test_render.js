const path = require('path');
const PanelView = require('./agile_bot/src/panel/panel_view');
const BehaviorsView = require('./agile_bot/src/behaviors/behaviors_view');

async function test() {
    PanelView.initializeCLI(
        'C:\\dev\\augmented-teams',
        'C:\\dev\\augmented-teams\\agile_bot\\bots\\story_bot'
    );
    
    const view = new BehaviorsView();
    const html = await view.render();
    console.log('HTML length:', html.length);
    console.log('Contains clarify:', html.includes('clarify'));
    console.log('Contains prioritization:', html.includes('prioritization'));
    console.log('First 500 chars:', html.substring(0, 500));
    
    PanelView.cleanupSharedCLI();
}

test().catch(console.error);
