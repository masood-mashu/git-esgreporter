# Skill: Epa Emissions Factors

## Description
EPA eGRID regional subregion factor application and carbon metrics.

## Procedural Workflow
1. Ingest relevant parameters from repository state.
2. Execute deterministic analysis via `GitEsgReporter` registered tools.
3. Validate output against compliance rules in `RULES.md`.
4. Return structured status dictionary to calling runtime.
