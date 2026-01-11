# CLI Test Helpers Plan (Markdown / Piped / JsonPy)

This plan complements `REFACTOR_TEST_BOT_SETUP_PLAN.md` by defining CLI-focused test helpers and retrofit steps. The goal is to keep the domain refactor plan lean while outlining how to test CLI outputs across formats.

## Scope and Principles
- Three helpers, one per format: `MarkdownCliTestHelper`, `PipedCliTestHelper`, `JsonPyCliTestHelper`.
- Thin wrappers over `BotTestHelper`: reuse bot init, workspace paths, state/scope/navigation helpers; keep CLI command construction and output assertions format-specific and hard-coded.
- No polymorphic “one helper for all.” Each helper is single-purpose.
- Full-output assertions only (entire sections/panels/objects), no substring/partial checks.
- Defer capturing expected outputs until the CLI is run during implementation; plug in real outputs afterward.
- Prefer upgrading existing CLI/instructions tests to use these helpers; add smoke tests only if a format currently has zero coverage.

## Tasks
1) Survey current CLI/instructions tests to find where CLI output is asserted (Markdown/Piped/JsonPy) and note current assertion styles (partial vs full).
2) Add helper scaffolds (new helper module): constructors accept `tmp_path`, create/hold `BotTestHelper`; expose pass-throughs for state/scope/navigation.
3) Implement fixed command runners:
   - `run_markdown(...)`: calls CLI with Markdown flags/env; captures stdout/stderr.
   - `run_piped(...)`: calls CLI with piped/pipe-delimited flags; captures stdout/stderr.
   - `run_jsonpy(...)`: calls CLI with JSON/JsonPy flags; captures stdout/stderr and parses JSON where appropriate.
4) Implement format-specific assertion helpers:
   - Markdown: assert whole sections/panels as full blocks.
   - Piped: assert exact pipe-delimited lines/segments in order.
   - JsonPy: assert full JSON objects/arrays (structure and values).
5) Retrofit existing tests (incremental):
   - Replace ad-hoc CLI invocations with the format helper runners.
   - Replace partial/substr assertions with full-output assertions using the captured payloads.
6) Only if a format lacks any coverage, add one minimal smoke test per format using its helper to exercise a simple CLI action, marking it as the place to plug real expected output after first run.
7) During implementation, for each test touched: run the CLI once, capture actual full output, update the expected block/fixture, and assert exact match.
8) Keep safety guards: ensure helpers write only to workspace (`tmp_path`); never production bot paths.
9) Validation: run targeted pytest nodes for updated tests; run lints on touched files.

## Expected Outcomes
- Consistent, hard-coded CLI invocations per format with no conditional logic.
- Tests assert full CLI outputs (sections/panels/objects) rather than fragments.
- Reuse of `BotTestHelper` for all bot setup/state/navigation to avoid duplication.
- Minimal churn to existing tests; new tests only to cover missing format gaps.

