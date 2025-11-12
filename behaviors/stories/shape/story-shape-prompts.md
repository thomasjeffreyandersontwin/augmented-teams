# Story Shape Prompts

## Generate Action Prompts

**AI should infer from user request** - only ask if critical information is genuinely missing.

**CRITICAL - Location Inference Strategy:**
1. **Check open/recently viewed files** - If user has files open in a subdirectory (e.g., `demo/mm3e/`), use that as base
2. **Check current working directory** - Use pwd/cwd if available
3. **Check project context** - Look for project indicators (package.json, requirements.txt, etc.)
4. **Default to workspace root** - Only if no other context available

**Location Examples:**
- User viewing `demo/mm3e/HeroesHandbook.pdf` → Create in `demo/mm3e/docs/stories/map/`
- User viewing `demo/project-x/src/index.js` → Create in `demo/project-x/docs/stories/map/`
- No files open, at workspace root → Create in `docs/stories/map/`

Optional context to consider (don't prompt unless needed):
- Product vision, scope, users
- Business priorities
- Relative sizing reference (previous work)

---

## Validate Action Prompts

These checks should be performed AFTER generating the story map:

### Structure
- Are TWO files created:
  - `[inferred-location]/docs/stories/map/[product-name]-story-map.md` (hierarchical decomposition)
  - `[inferred-location]/docs/stories/increments/[product-name]-story-map-increments.md` (value increments organized)
- Does `[inferred-location]/docs/stories/increments/` folder exist?
- Is the 🎯 Epic → 📂 Sub-Epic → ⚙️ Feature → 📝 Story hierarchy present in documents?
- Are tree characters (│ ├─ └─) used correctly?
- Is the Legend at the top of the file?
- Are NO epic/feature documents created (those are created in Discovery/Exploration)?
- Are NO epic/feature folders created (those are created by `/story-arrange`)?

### Content Quality
- Are user AND system activities both present?
- Is business language used (verb/noun, not tasks)?
- Are ALL levels using [Verb] [Noun] *[optional clarifier]* format (including Sub-Epics)?
- Are stories action-oriented (not capabilities or implementation)?
- Are emojis used correctly (🎯 📂 ⚙️ 📝)?
- Are NO "Epic:", "Feature:", "Story:" prefixes anywhere (just emoji + name)?

### Sizing
- Are stories sized in 3-12d range (where detailed)?
- Are hierarchy levels within 7±2 thresholds?
  - Epics: 4-9 features (use Sub-Epics if > 9)
  - Features: 4-9 stories (split if > 9)
  - Stories: 2-9 AC (split if > 9)

### Scope and Counting
- Are only 10-20% of stories fully identified?
- Are story counts (~X stories) used for unexplored areas?
- Are areas marked as IDENTIFIED vs (~X stories)?
- When showing example features within epic/sub-epic, is remaining count displayed as "└─ ⚙️ ~X more features"?
- When showing example stories within feature, is remaining count displayed as "└─ 📝 ~X more stories"?

### Increments
- Are potential increments organized in `increments/[product-name]-story-map-increments.md`?
- Are increments using NOW/NEXT/LATER priorities?
- Does `docs/stories/increments/` folder exist (contains story-map-increments.md, individual increment docs added in Discovery)?

---

## Common Issues to Check

### Anti-Patterns
- Stories that are tasks (implement, develop, configure, build, set up)
- Stories without system activities (only user activities)
- Over-identification during shaping (> 20% identified)
- Missing story counts for unexplored areas
- Missing "~X more features" line when showing example features within epic/sub-epic
- Missing "~X more stories" line when showing example stories within feature
- Using "MVI" instead of "Value Increment"
- Increments using High/Medium/Low instead of NOW/NEXT/LATER
- Using "Epic:", "Feature:", "Story:" prefixes anywhere
- Sub-Epics not using verb/noun format
- Missing tree characters or emojis
- Epics with > 9 features (should use Sub-Epics 📂)
- Features with > 9 stories (should split)
- Creating epic/feature documents during Shape (should be created in Discovery/Exploration)

### Missing Elements
- Missing `[inferred-location]/docs/stories/map/` folder structure
- Missing `[inferred-location]/docs/stories/increments/` folder
- Missing `[product-name]-story-map.md` file in map/
- Missing `[product-name]-story-map-increments.md` file in increments/
- No story counting for unexplored areas
- Missing user OR system activities
- Missing Legend at top
- Missing tree characters (│ ├─ └─)
- Missing emojis (🎯 📂 ⚙️ 📝)

Note: Epic/feature folder structure (`epic-[name]/feature-[name]/`) is NOT created during Shape - it's created by `/story-arrange` command

---

## Notes
- Prompts ensure all context is gathered before generation
- Validation prompts ensure quality and completeness
- Common issues help identify and prevent anti-patterns

