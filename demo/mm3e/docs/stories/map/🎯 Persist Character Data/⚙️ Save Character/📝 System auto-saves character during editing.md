# 📝 System auto-saves character during editing

**Epic:** Persist Character Data
**Feature:** Save Character

## Story Description

System auto-saves character during editing - Saves draft every 2 minutes without user action

## Acceptance Criteria

**AC are located in feature document, NOT in story document**

See feature document for acceptance criteria: `⚙️ Save Character - Feature Overview.md`

## Notes

**Consolidation Applied**:
- Uses same save API as manual save (Story 1)
- Validation errors do NOT prevent auto-save (warn philosophy applies)
- Error handling differs from manual save: silent retry vs user-visible errors

---

## Source Material

**Inherited From**: Story Map (Discovery Refinements)
- Primary Source: Mutants & Masterminds 3rd Edition - Hero's Handbook
- Discovery Refinements: Auto-save interval is 2 minutes, uses same save API, silent error recovery for better UX

