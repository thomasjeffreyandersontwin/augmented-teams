### Command: /story-explore-generate

**[Purpose]:**
Generate acceptance criteria for stories with exhaustive AC decomposition and consolidation review.

**[Rule]:**
`behaviors/stories/stories-rule.mdc` - Section 3: Story Exploration Principles

**Runner:**
```bash
python behaviors/stories/stories_runner.py story-explore --action generate
```

---

## Delegate to Main Command

This command delegates to **Action 1: GENERATE** in the main `/story-explore` command.

See: `behaviors/stories/exploration/story-explore-cmd.md` - Action 1: GENERATE

---

## Summary

This command:
1. Reads source material from story map (Discovery Refinements)
2. Enumerates ALL acceptance criteria permutations for stories/features
3. Presents CONSOLIDATION REVIEW to user (identifies similar ACs, asks questions)
4. Waits for user confirmation on consolidation decisions
5. Generates final Domain AC (feature level) and Behavioral AC (story level)
6. Updates feature documents with AC (NOT story documents)
7. Uses When/Then format (NO "Given" clauses at AC level)

**Output**: Feature documents with Domain AC and Behavioral AC for all stories

