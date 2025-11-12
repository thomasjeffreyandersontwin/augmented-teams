# 📝 User saves character to cloud storage

**Epic:** Persist Character Data
**Feature:** Save Character

## Story Description

User saves character to cloud storage - and system validates data completeness and creates or updates record

## Acceptance Criteria

**AC are located in feature document, NOT in story document**

See feature document for acceptance criteria: `⚙️ Save Character - Feature Overview.md`

## Notes

**Consolidation Applied**:
- Combined create/update into single story (same save API logic)
- Validation errors WARN but do NOT prevent save (user control philosophy)
- Error handling specific to manual save (user-initiated, requires user action)

---

## Source Material

**Inherited From**: Story Map (Discovery Refinements)
- Primary Source: Mutants & Masterminds 3rd Edition - Hero's Handbook
- Chapter 1: Character Creation (pages 16-28) - Save/load patterns
- Discovery Refinements: Save operations use single API with create/update modes, validation warns but never prevents

