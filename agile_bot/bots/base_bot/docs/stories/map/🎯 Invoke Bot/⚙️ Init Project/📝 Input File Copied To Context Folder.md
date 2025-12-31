# 📝 Input File Copied To Context Folder

**Navigation:** [📋 Story Map](../../../../story-map.drawio)

**User:** Bot Behavior
**Path:** [🎯 Invoke Bot](../..) / [⚙️ Init Project](.)  
**Sequential Order:** 1.6
**Story Type:** user

## Story Description

Input File Copied To Context Folder functionality for the mob minion system.

## Acceptance Criteria

### Behavioral Acceptance Criteria

  **and** : input file exists at original location

- **When** : initialize_project action executes

  **then** : initialize_project copies input file to {project_area}/docs/context/input.txt

  **and** : original input file remains at original location (copy, not move)

  **and** : {project_area}/docs/context/input.txt exists and contains original content

## Scenarios

### Scenario: Initialize project copies input file to context folder (happy_path)

**Steps:**
```gherkin
GIVEN: User provides input file via @input.txt command
AND: input file exists at original location
WHEN: initialize_project action executes
THEN: initialize_project copies input file to {project_area}/docs/context/input.txt
AND: original input file remains at original location (copy, not move)
AND: {project_area}/docs/context/input.txt exists and contains original content
```

