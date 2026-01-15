# 📝 Display Strategy Instructions

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** User
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Invoke Bot Through Panel](..) / [⚙️ Display Action Instructions Through Panel](.)  
**Sequential Order:** 3
**Story Type:** user

## Story Description

Display Strategy Instructions functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

- **When** Current action is strategy

  **then** System displays decision criteria with radio button options

  **and** System displays assumptions textarea

- **When** Saved strategy exists

  **then** System displays selected option for each decision criterion

- **When** User edits assumptions textarea

  **then** System updates assumptions

## Scenarios

<a id="scenario-unnamed-scenario"></a>
### Scenario: [Unnamed Scenario](#scenario-unnamed-scenario) (happy_path)

**Steps:**
```gherkin
Given Bot is at shape.strategy
When Panel displays instructions section
Then Panel displays decision criteria with radio options
And Panel displays assumptions textarea
And User can select option for each criterion
```


<a id="scenario-unnamed-scenario"></a>
### Scenario: [Unnamed Scenario](#scenario-unnamed-scenario) (happy_path)

**Steps:**
```gherkin
Given Panel displays strategy instructions
When User selects radio option for decision criterion
Then System saves selected option
And Selection persists across panel refreshes
```

