# 📝 User saves character revision with version note

**Epic:** Persist Character Data
**Feature:** Save Character

## Story Description

User saves character revision with version note - and system creates version history entry with timestamp and note

## Acceptance Criteria

**AC are located in feature document, NOT in story document**

See feature document for acceptance criteria: `⚙️ Save Character - Feature Overview.md`

## Notes

**Consolidation Applied**:
- Uses same save API as manual save (Story 1) with "save as" pattern
- Validation errors WARN but do NOT prevent revision save
- Revision creates separate version history entry, does not replace main character record

---

## Source Material

**Inherited From**: Story Map (Discovery Refinements)
- Primary Source: Mutants & Masterminds 3rd Edition - Hero's Handbook
- Discovery Refinements: "Save As" pattern for version history, maintains active version, uses same save API

