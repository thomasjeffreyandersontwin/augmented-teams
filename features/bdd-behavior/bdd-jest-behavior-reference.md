# BDD Jest Behavior Reference

Comprehensive examples and patterns for BDD testing with Jest/JavaScript.

See `bdd-jest-behavior-rule.mdc` for the concise rule file and `bdd-behavior-rule.mdc` for framework-agnostic principles.

---

## 1. Business Readable Language

### Use Nouns for Describe, Connect with Linking Words, Nest Broad→Specific

**✅ Excellent Example:**

```javascript
describe('a ranged damage power', () => {
  let helper, standardPowerActor, rangedPower;
  
  beforeEach(() => {
    helper = new StandardTestHelper();
    standardPowerActor = helper.actor;
    const rangedPouvoir = helper.createPouvoirWithDeltas({
      name: "Ranged " + helper.pouvoir.name,
      portee: "distance",
      effetsprincipaux: "Damage 10",
      rang: 10
    });
    rangedPower = new Power(rangedPouvoir, standardPowerActor);
  });
  
  describe('that has targeted and resulted in a successful attack', () => {
    let attackResults;
    
    beforeEach(async () => {
      rangedPower.attack.targets.add(testTarget);
      global.Roll = function() { return mockFactory.createRoll({ total: 20, diceTotal: 12 }); };
      attackResults = await rangedPower.attack.rollToHit();
    });
    
    it('should have attack DC equal to target actor\'s dodge ability', () => {
      expect(attackResults[0].DC).toBe(testTarget.actor.system.defense.esquive.total + 10);
    });
    
    describe('that the target has rolled a resistance save against', () => {
      let resistanceResult;
      
      beforeEach(async () => {
        global.Roll = function() { return mockFactory.createRoll({ total: 10, diceTotal: 2 }); };
        resistanceResult = await attackResults[0].effect.rollResistance();
      });
      
      it('should apply damage based on degrees of failure', () => {
        expect(resistanceResult.degreesOfFailure).toBe(2);
        expect(resistanceResult.outcome.injuries).toBe(2);
        expect(testTarget.actor.system.blessure).toBe(2);
      });
      
      it('should apply conditions based on degree (Dazed, Staggered, Incapacitated)', () => {
        expect(resistanceResult.outcome.condition).toEqual(['staggered']);
      });
    });
  });
});
```

**❌ Bad Example:**

```javascript
describe('when attacking Target', () => {  // Missing article, action verb, class name
  describe('Power.execute() results', () => {  // Method name, not business concept
    describe('retrieved attack', () => {  // Breaks natural connection
      it('sets isSubmitting flag', () => {  // Missing "should", technical jargon
        expect(result.isSubmitting).toBe(true);
      });
    });
  });
});
```

---

## 2. Comprehensive and Brief

### Test Observable Behavior, Cover All Paths, Keep Tests Short & Fast

**✅ Excellent Example:**

```javascript
describe('a damage power', () => {
  let damagePower, testTarget;
  
  beforeEach(() => {
    const damagePouvoir = helper.createPouvoirWithDeltas({
      name: "Damage Power",
      effetsprincipaux: "Damage 5",
      notes: "<p>DC 26; Smash [5 extra ranks]<br>(Standard - Close - Instant)</p>",
      rang: 5
    });
    damagePower = new Power(damagePouvoir, standardPowerActor);
    testTarget = mockFactory.createTarget({ dodge: 15, injury: 0 });
    testTarget.actor.system.blessure = 0;
    testTarget.actor.effects = [];
  });
  
  // Cover STATE
  it('should be a ranged attack', () => {
    expect(damagePower.isRanged).toBe(true);
  });
  
  it('should have default resistance of toughness', () => {
    expect(damagePower.effect.resistance).toBe("toughness");
  });
  
  // Cover CALCULATIONS
  it('should calculate DC from targets dodge', () => {
    damagePower.attack.targets.add(testTarget);
    global.Roll = function() { return mockFactory.createRoll(); };
    const result = damagePower.attack.rollToHitTarget(testTarget);
    expect(result.DC).toBe(20);  // 10 + dodge (10)
  });
  
  // Cover INTERACTIONS
  it('should apply injury to target', async () => {
    global.Roll = function() { return mockFactory.createRoll({ total: 10 }); };
    const resistanceResult = await damagePower.effect.rollResistance(testTarget);
    expect(testTarget.actor.system.blessure).toBe(2);
  });
  
  // Cover NORMAL PATH
  describe('whose roll exceeds the DC', () => {
    let result;
    
    beforeEach(async () => {
      global.Roll = function() { return mockFactory.createRoll({ total: 20, diceTotal: 12 }); };
      result = await damagePower.attack.rollToHitTarget(testTarget);
    });
    
    it('should indicate a hit', () => {
      expect(result.hit).toBe(true);
    });
    
    it('should calculate degrees of success', () => {
      expect(result.degreesOfSuccess).toBe(1);
    });
    
    it('should store result on attack', () => {
      expect(damagePower.attack.rollResult).toBe(result);
    });
  });
  
  // Cover FAILURE PATH
  describe('whose roll does not exceed the DC', () => {
    let result;
    
    beforeEach(async () => {
      global.Roll = function() { return mockFactory.createRoll({ total: 7, diceTotal: -1 }); };
      result = await damagePower.attack.rollToHitTarget(testTarget);
    });
    
    it('should indicate a miss', () => {
      expect(result.hit).toBe(false);
    });
    
    it('should have zero degrees of success', () => {
      expect(result.degreesOfSuccess).toBe(0);
    });
  });
});
```

**❌ Bad Example:**

```javascript
it('calls _validateCredentials()', () => {  // Tests internal/private methods
  expect(form._internal_flag).toBe(true);  // Tests private state
  expect(form._validateCredentials).toHaveBeenCalled();  // Asserts internal calls
});

it('handles attack', () => {  // Skips validations (no assertions!)
  // 50 lines of procedural setup...
  await new Promise(r => setTimeout(r, 2000));  // Arbitrary sleep
  expect(database.records).toHaveLength(5);  // Depends on external state
});
```

---

## 3. Balance Context Sharing with Localization

### Nest Parent Context, Use Helper Factories, Reset Between Runs

**✅ Excellent Example:**

```javascript
// Helper factory defined once, reused everywhere
const createPower = (overrides = {}) => ({
  name: 'Test Power',
  rank: 10,
  ...overrides
});

// More complex factory from attack.test.mjs
function makeRangedPouvoir(helper) {
  return helper.createPouvoirWithDeltas({
    name: "Ranged " + helper.pouvoir.name,
    portee: "distance",
    effetsprincipaux: "Base Effect 10",
    rang: 10
  });
}

describe('a Power', () => {
  let helper, standardPowerActor, standardPower, mockFactory;
  
  // Setup at correct scope - shared by all children
  beforeEach(() => {
    helper = new StandardTestHelper();
    standardPowerActor = helper.actor;
    standardPower = new Power(helper.pouvoir, standardPowerActor);
    mockFactory = new MockFoundryFactory();
    mockFactory.reset();  // Clear state between runs
    mockTargets.clear();
  });

  it('should have a reference to owning actor and the original pouvoir', () => {
    expect(standardPower.actor).toBe(standardPowerActor);
    expect(standardPower.pouvoir).toStrictEqual(helper.pouvoir);
  });

  it('should default to an instant duration', () => {
    expect(standardPower.duration).toBe(DURATIONS.INSTANT);
  });
  
  // Nested context extends parent, doesn't repeat
  describe('that is a ranged power', () => {
    let rangedPower;
    
    // Decorate parent setup
    beforeEach(() => {
      const rangedPouvoir = makeRangedPouvoir(helper);  // Reuse helper
      rangedPower = new Power(rangedPouvoir, standardPowerActor);
    });
    
    it('should create a power with range', () => {
      expect(rangedPower.isRanged).toBe(true);
      expect(rangedPower.range).toBe('ranged');
    });
    
    it('should have distance calculated from power level', () => {
      expect(rangedPower.attack.distance).toBe(40);
    });
    
    it('should have bonus to hit equal to attacking actor\'s dexterity', () => {
      expect(rangedPower.attack.bonus).toBe(standardPowerActor.system.caracteristique.dexterite.total);
    });
  });
});
```

**❌ Bad Example:**

```javascript
describe('Power', () => {  // Missing article
  // Duplicated setup in each child context
  describe('created from actor', () => {
    beforeEach(() => {
      this.actor = { id: '123', name: 'Test' };  // Duplicated
      this.power = new Power({});
    });
  });
  
  describe('that is ranged', () => {
    beforeEach(() => {
      this.actor = { id: '123', name: 'Test' };  // Duplicated - should be in parent
      this.power = new Power({});  // Scattered setup logic
    });
  });
});

it('has tokens', () => {
  const tokens = getTokens();  // Helper created per test, not reused
  this.dirtyState = 'leaked';  // Side effects between tests
});
```

---

## 4. Cover All Layers of the System

### Include Separate Tests for Each Layer, Isolate with Mocks, Organize to Tell a Story

**✅ Excellent Example:**

```javascript
describe('an Attack Power', () => {
  let standardPowerActor, damagePower, mockFactory;
  
  beforeEach(() => {
    helper = new StandardTestHelper();
    standardPowerActor = helper.actor;
    const damagePouvoir = makeDamagePouvoir(helper);
    damagePower = new Power(damagePouvoir, standardPowerActor);
    mockFactory = new MockFoundryFactory();
    mockFactory.reset();
  });
  
  // Front-end layer - UI/presentation
  describe('whose actor data is being displayed on a character sheet', () => {
    let context, html;
    
    beforeEach(async () => {
      ({ context, html } = await mockFactory.prepareAttackSheetAndRenderHtml(standardPowerActor, damagePower));
    });
    
    // Test data structure passed to template
    it('should include attack bonus in context', () => {
      expect(context.attackPowers[0].name).toBe(damagePower.name);
      expect(context.attackPowers[0].pouvoir._id).toBe(damagePower.pouvoir._id);
      expect(context.attackPowers[0].attack).toBeDefined();
      expect(context.attackPowers[0].effect).toBeDefined();
    });
    
    // Test rendered HTML output
    it('should render attack bonus in HTML', () => {
      expect(html).toContain(damagePower.effect.name);
      expect(html).toContain(damagePower.effect.rank.toString());
      expect(html).toContain('value="8"');
    });
    
    it('should render attack button with power id', () => {
      expect(html).toContain('class="attack-roll"');
      expect(html).toContain(`data-power-id="${damagePower.pouvoir._id}"`);
    });
  });
  
  // Domain/business logic layer - core behavior
  describe('that is a damage power', () => {
    it('should calculate damage from rank', () => {
      expect(damagePower.effect).toBeDefined();
      expect(damagePower.effect.name).toBe("Damage");
      expect(damagePower.effect.rank).toBe(13);  // 5 base + 8 strength
    });
    
    it('should have default resistance of toughness', () => {
      expect(damagePower.effect.resistance).toBe("toughness");
    });
    
    it('should have DC based on effect rank (15 + rank)', () => {
      expect(damagePower.effect.DC).toBe(20);  // 15 + 5
    });
  });
  
  // Data access/integration layer - persistence (conceptual example)
  describe('that has been saved to the repository', () => {
    let mockDb, repo, savedAttack;
    
    beforeEach(() => {
      mockDb = jest.fn();
      repo = new AttackRepository(mockDb);
      savedAttack = repo.saveAttack(damagePower.attack);
    });
    
    describe('that is retrieved at a later time', () => {
      it('should return the saved attack with all properties', () => {
        const retrieved = repo.getAttack(savedAttack.id);
        expect(retrieved.bonus).toBe(damagePower.attack.bonus);
        expect(retrieved.range).toBe(damagePower.attack.range);
        expect(retrieved.effect.rank).toBe(damagePower.effect.rank);
      });
    });
  });
});
```

**❌ Bad Example:**

```javascript
describe('when attacking Target', () => {  // Action verb, class name
  describe('Power.execute() results', () => {  // Method name
    describe('retrieved attack', () => {  // Breaks natural connection
      it('sets isSubmitting flag', () => {  // Missing "should", jargon
        expect(result.isSubmitting).toBe(true);
      });
    });
  });
});
```

---

## 2. Comprehensive and Brief

### Test Observable Behavior, Cover All Paths, Keep Tests Short & Fast

**✅ Excellent Example:**

```javascript
describe('a damage power', () => {
  let damagePower, damageEffect, testTarget;
  
  beforeEach(() => {
    const damagePouvoir = helper.createPouvoirWithDeltas({
      name: "Damage Power",
      effetsprincipaux: "Damage 5",
      notes: "<p>DC 20; Smash [5 extra ranks]</p>",
      rang: 5
    });
    damagePower = new Power(damagePouvoir, standardPowerActor);
    damageEffect = damagePower.effect;
    testTarget = mockFactory.createTarget({ dodge: 15, injury: 0 });
    testTarget.actor.system.blessure = 0;
    testTarget.actor.effects = [];
  });
  
  // Cover STATE
  it('should be a ranged attack', () => {
    expect(damagePower.isRanged).toBe(true);
  });
  
  it('should have default resistance of toughness', () => {
    expect(damageEffect.resistance).toBe("toughness");
  });
  
  // Cover CALCULATIONS
  it('should calculate DC from targets dodge', () => {
    damagePower.attack.targets.add(testTarget);
    global.Roll = function() { return mockFactory.createRoll({ total: 20 }); };
    
    const result = damagePower.attack.rollToHitTarget(testTarget);
    expect(result.DC).toBe(18);  // target parade (8) + 10
  });
  
  // Cover BUSINESS RULES
  it('should have resistance formula that includes resistance bonus', () => {
    const formula = damageEffect.resistanceFormula;
    expect(formula).toContain('1d20 + 8');  // testTarget toughness = 8
  });
  
  // Cover INTERACTIONS
  describe('that has executed an attack that has hit the target', () => {
    beforeEach(() => {
      damagePower.attack.targets.add(testTarget);
    });
    
    it('should trigger damage resistance save (toughness)', async () => {
      const mockRoll = {
        formula: '1d20 + 8',
        total: 25,
        dice: [{ total: 17 }],
        evaluate: async () => undefined,
        getTooltip: async () => '<div>Roll</div>'
      };
      global.Roll = function() { return mockRoll; };
      
      const resistanceResult = await damageEffect.rollResistance();
      expect(resistanceResult).toBeDefined();
      expect(resistanceResult.success).toBe(true);
    });
  });
  
  // Cover NORMAL PATH
  describe('whose roll exceeds the DC', () => {
    let result;
    
    beforeEach(async () => {
      global.Roll = function() { return mockFactory.createRoll({ total: 26, diceTotal: 18 }); };
      result = await damageEffect.rollResistance();
    });
    
    it('should indicate a hit', () => {
      expect(result.success).toBe(true);
    });
    
    it('should have zero degrees of failure', () => {
      expect(result.degreesOfFailure).toBe(0);
    });
    
    it('should not apply injuries', () => {
      expect(result.injuries).toBeUndefined();
    });
  });
  
  // Cover FAILURE PATH
  describe('whose roll does not exceed the DC', () => {
    let result;
    
    beforeEach(async () => {
      global.Roll = function() { return mockFactory.createRoll({ total: 10, diceTotal: 2 }); };
      result = await damageEffect.rollResistance();
    });
    
    it('should indicate a miss', () => {
      expect(result.success).toBe(false);
    });
    
    it('should calculate degrees of failure', () => {
      expect(result.degreesOfFailure).toBe(2);  // DC 20 - total 10 = 10 / 5 = 2
    });
    
    it('should apply 1 injury per degree of failure', () => {
      const outcome = result.outcome;
      expect(outcome.injuries).toBe(2);
      expect(testTarget.actor.system.blessure).toBe(2);
    });
    
    it('should apply conditions based on degree (Dazed, Staggered, Incapacitated)', () => {
      expect(result.outcome.condition).toEqual(['staggered']);
      expect(testTarget.actor.effects.length).toBeGreaterThan(0);
    });
  });
});
```

**❌ Bad Example:**

```javascript
it('calls _validateCredentials()', () => {
  expect(form._internal_flag).toBe(true);
  expect(form._validateCredentials).toHaveBeenCalled();
});

it('handles attack', () => {
  // 50 lines of procedural code...
  await new Promise(r => setTimeout(r, 2000));
  expect(database.records).toHaveLength(5);
});
```

---

## 3. Balance Context Sharing with Localization

### Nest Parent Context, Use Helper Factories, Reset Between Runs

**✅ Excellent Example:**

```javascript
// Helper factory - from attack.test.mjs
const createPower = (overrides = {}) => ({
  name: 'Test Power',
  rank: 10,
  ...overrides
});

// Real factory from attack.test.mjs
class StandardTestHelper {
  get actor() {
    return {
      _id: "Ub42p1BuHTw2J7mT",
      name: "A Standard Power",
      system: {
        caracteristique: this.abilities,
        defense: this.defenses,
      },
      pouvoirs: [this.pouvoir],
      items: [this.pouvoir]
    };
  }
  
  createPouvoirWithDeltas(deltas) {
    const pouvoir = { ...this.pouvoir };
    pouvoir.system = { ...pouvoir.system };
    
    if (deltas.name) pouvoir.name = deltas.name;
    if (deltas.portee) pouvoir.system.portee = deltas.portee;
    if (deltas.rang !== undefined) pouvoir.system.cout.rang = deltas.rang;
    
    return pouvoir;
  }
}

// Single factory instance with reset - from attack.test.mjs
const mockFactory = new MockFoundryFactory();

describe('a Power', () => {
  let helper, standardPowerActor, standardPower;
  
  // Base setup - reused by all children
  beforeEach(() => {
    helper = new StandardTestHelper();
    standardPowerActor = helper.actor;
    standardPower = new Power(helper.pouvoir, standardPowerActor);
    mockTargets.clear();
    mockFactory.reset();  // Reset between runs - crucial!
  });

  describe('created from an actor that has a pouvoir', () => {
    it('should have a reference to owning actor', () => {
      expect(standardPower.actor).toBe(standardPowerActor);
    });
    
    it('should take power name and descriptor from pouvoir', () => {
      expect(standardPower.name).toBe(helper.pouvoir.name);
      expect(standardPower.descriptors[1]).toBe(helper.pouvoir.system.descripteurs[1]);
    });
  });
  
  // Extends parent, doesn't repeat
  describe('that is a ranged power', () => {
    let rangedPower;
    
    // Further decoration of setup
    beforeEach(() => {
      rangedPower = createPower({ range: 'ranged' });  // Keeps helper code close
    });
    
    it('should have distance calculated from power level', () => {
      expect(rangedPower.attack.distance).toBe(40);
    });
    
    // Even deeper nesting
    describe('whose actor data is being shown on a character sheet', () => {
      let context, html;
      
      beforeEach(async () => {
        ({ context, html } = await mockFactory.prepareAttackSheetAndRenderHtml(standardPowerActor, rangedPower));
      });
      
      it('should include ranged attack data in context', () => {
        expect(context.attackPowers[0].attack.range).toBe(RANGES.RANGED);
        expect(context.attackPowers[0].attack.bonus).toBe(standardPowerActor.system.caracteristique.dexterite.total);
      });
    });
  });
});
```

**❌ Bad Example:**

```javascript
describe('Power', () => {
  describe('created from actor', () => {
    beforeEach(() => {
      this.actor = { id: '123' };  // Duplicated init
    });
  });
  
  describe('that is ranged', () => {
    beforeEach(() => {
      this.actor = { id: '123' };  // Should be in parent - scattered setup
    });
  });
});

it('has tokens', () => {
  const t = getTokens();  // Helper created per test
  this.state = 'dirty';  // Side effects between tests
});
```

---

## 4. Cover All Layers of the System

### Include Separate Tests for Each Layer, Isolate with Mocks, Organize to Tell a Story

**✅ Excellent Example:**

```javascript
describe('an Attack Power', () => {
  let standardPowerActor, damagePower;
  
  beforeEach(() => {
    helper = new StandardTestHelper();
    standardPowerActor = helper.actor;
    const damagePouvoir = makeDamagePouvoir(helper);
    damagePower = new Power(damagePouvoir, standardPowerActor);
  });
  
  // FRONT-END LAYER - UI/Presentation
  describe('whose actor data is being displayed on a character sheet', () => {
    let context, html;
    
    beforeEach(async () => {
      ({ context, html } = await mockFactory.prepareAttackSheetAndRenderHtml(standardPowerActor, damagePower));
    });
    
    it('should include attack bonus in context', () => {
      expect(context.attackPowers[0].effectFragment).toBe('damage');
      expect(context.attackPowers[0].effect.name).toBe("Damage");
      expect(context.attackPowers[0].effect.resistance).toBe("toughness");
    });
    
    it('should render attack bonus in HTML', () => {
      expect(html).toContain("Damage");
      expect(html).toContain(damagePower.effect.rank.toString());
      expect(html).toContain("Toughness");
    });
  });
  
  // DOMAIN LAYER - Business Logic
  describe('that is a damage power', () => {
    it('should calculate damage from rank', () => {
      expect(damagePower.effect).toBeDefined();
      expect(damagePower.effect.name).toBe("Damage");
      expect(damagePower.effect.rank).toBe(13);
    });
    
    it('should have default resistance of toughness', () => {
      expect(damagePower.effect.resistance).toBe("toughness");
    });
    
    describe('that has executed an attack that has hit the target', () => {
      beforeEach(() => {
        damagePower.attack.targets.add(testTarget);
      });
      
      it('should trigger damage resistance save (toughness)', async () => {
        const mockRoll = mockFactory.createRoll({ total: 25 });
        global.Roll = function() { return mockRoll; };
        
        const resistanceResult = await damagePower.effect.rollResistance();
        expect(resistanceResult).toBeDefined();
        expect(resistanceResult.success).toBe(true);
      });
    });
  });
  
  // DATA ACCESS LAYER - Persistence (conceptual)
  describe('that has been saved to the repository', () => {
    let mockDb, repo;
    
    beforeEach(() => {
      mockDb = jest.fn();
      repo = new AttackRepository(mockDb);
      repo.saveAttack(damagePower.attack);
    });
    
    describe('that is retrieved at a later time', () => {
      it('should return the saved attack with all properties', () => {
        const retrieved = repo.getAttack(damagePower.attack.id);
        expect(retrieved.bonus).toBe(damagePower.attack.bonus);
        expect(retrieved.range).toBe(damagePower.attack.range);
        expect(retrieved.effect).toBeDefined();
      });
    });
  });
});
```

**❌ Bad Example:**

```javascript
describe('damage', () => {  // Stops at happy path
  it('works', () => {
    expect(axios.get(url)).toBe(ok);  // Tests 3rd party lib
  });
});

it('passes if repo ready', () => {  // Relies on dependent code, mixes types
  renderPage();
  expect(database.hasRecord()).toBe(true);
});
```

---

## 5. Unit Tests the Front-End

### Mock Services, Test Both Data and Rendering, Validate Conditional Paths

**✅ Excellent Example:**

```javascript
jest.mock('../services/api');

describe('an attack power display', () => {
  let mockService, context, html, standardPowerActor, standardPower;
  
  beforeEach(async () => {
    mockService = jest.fn();
    helper = new StandardTestHelper();
    standardPowerActor = helper.actor;
    standardPower = new Power(helper.pouvoir, standardPowerActor);
    
    ({ context, html } = await mockFactory.prepareAttackSheetAndRenderHtml(standardPowerActor, standardPower));
  });
  
  // Test data structure
  it('should include attack bonus in context', () => {
    expect(context.attackPowers[0].name).toBe(standardPower.name);
    expect(context.attackPowers[0].pouvoir._id).toBe(standardPower.pouvoir._id);
    expect(context.attackPowers[0].attack).toBeDefined();
    expect(context.attackPowers[0].effect).toBeDefined();
  });
  
  // Test rendered output
  it('should render attack bonus in HTML', () => {
    const html = renderTemplate(context);
    expect(html).toContain(standardPower.effect.name);
    expect(html).toContain(standardPower.effect.rank.toString());
    expect(html).toContain(standardPower.effect.DC.toString());
  });
  
  it('should render attack button with power id', () => {
    expect(html).toContain(standardPower.name);
    expect(html).toContain('class="attack-roll"');
    expect(html).toContain(`data-power-id="${standardPower.pouvoir._id}"`);
  });
  
  // Validate conditional render paths
  describe('that is loading', () => {
    beforeEach(() => {
      context.isLoading = true;
      html = renderTemplate(context);
    });
    
    it('should show spinner', () => {
      expect(html).toContain('loading-spinner');
    });
    
    it('should not show attack list', () => {
      expect(html).not.toContain('attack-list');
    });
  });
  
  describe('that has an error', () => {
    beforeEach(() => {
      context.error = 'Failed to load';
      html = renderTemplate(context);
    });
    
    it('should display error message', () => {
      expect(html).toContain('Failed to load');
    });
  });
  
  // Test button handlers
  describe('whose attack button is clicked', () => {
    let targets;
    
    beforeEach(() => {
      targets = [testTarget];
    });
    
    it('should execute attack when targets exist', async () => {
      await BetterAttackSheetHelper.handleAttackButtonClick(
        { powerId: standardPower.pouvoir._id, attackPowers: [standardPower], targets },
        { ui: mockFactory.ui, console: mockFactory.console, Hooks: mockFactory.hooks }
      );
      
      expect(mockFactory.hooks.call).toHaveBeenCalledWith('betterAttacks.createAttackChatCard', expect.anything(), standardPower);
    });
    
    it('should show error when no targets selected', async () => {
      await BetterAttackSheetHelper.handleAttackButtonClick(
        { powerId: standardPower.pouvoir._id, attackPowers: [standardPower], targets: [] },
        { ui: mockFactory.ui, console: mockFactory.console, Hooks: mockFactory.hooks }
      );
      
      expect(mockFactory.ui.notifications.warn).toHaveBeenCalledWith('Please select at least one target');
      expect(mockFactory.hooks.call).not.toHaveBeenCalled();
    });
  });
});
```

**❌ Bad Example:**

```javascript
it('renders bonus', () => {  // Tests only HTML, not data
  expect(html).toContain('value="8"');
  expect(html).toContain('color: blue');  // Tests styling
  await fetch('http://api.com');  // Hits live API
});

it('calls _onMount()', () => {  // Tests lifecycle internals
  expect(component._onMount).toHaveBeenCalled();
});
```

---

## Common Jest Patterns

**Single factory instance with reset:**
```javascript
const mockFactory = new MockFoundryFactory();

beforeEach(() => {
  mockFactory.reset();  // Runs before ALL tests
});
```

**Helper factories:**
```javascript
function makeRangedPouvoir(helper) {
  return helper.createPouvoirWithDeltas({
    name: "Ranged " + helper.pouvoir.name,
    portee: "distance",
    effetsprincipaux: "Base Effect 10",
    rang: 10
  });
}
```

**Async tests:**
```javascript
it('should fetch data', async () => {
  const data = await fetchData();
  expect(data).toBeDefined();
});
```

**Mocking modules:**
```javascript
jest.mock('../services/api');

global.Roll = function() { 
  return mockFactory.createRoll({ total: 20 }); 
};
```

