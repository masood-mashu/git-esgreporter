# Explainability, Auditability & Decision Logic: GitEsgReporter

This document details the transparent decision architecture, algorithmic criteria, data provenance, and operational boundaries of **GitEsgReporter**, ensuring complete compliance with OpenGAP standards and Checkpoint 02 requirements.

---

## 1. Input Data and Data Sources Used

**GitEsgReporter** ingests structured, machine-verifiable data artifacts from well-defined sources to ensure total repeatability:
- **Corporate**: Corporate facility natural gas, diesel, and fleet fuel purchase manifests.
- **Regional**: Regional electricity utility billing kWh statements.
- **EPA**: EPA GHG Emission Factors Hub and IEA national grid emission datasets.
- **OpenGAP Specification Manifests**: Ingests `agent.yaml`, `RULES.md`, and local state from `memory/MEMORY.md`.

All data sources are parsed deterministically without dynamic external unverified calls, ensuring that evaluations reflect the exact state of the repository at the moment of inspection.

---

## 2. How It Decides and Reasoning Process

The decision pipeline operates through a multi-stage validation sequence designed to eliminate subjective ambiguity:

1. **Syntax & Schema Verification**: Ingested inputs are first validated against strict JSON and YAML schemas defined in `tools/`. Any malformed payloads are immediately rejected.
2. **Deterministic Metric Extraction**:
   - **calculate_scope1_emissions**: Uses `scope1-emission-calculator` to calculate computes metric tonnes co2e from natural gas and diesel fuel consumption.
   - **calculate_scope2_emissions**: Uses `scope2-market-grid-factor` to calculate applies egrid regional carbon factor to purchased electricity kilowatt-hours.
   - **certify_ghg_report**: Uses `ghg-protocol-certifier` to calculate validates total carbon footprint report against ghg protocol corporate standard.
3. **Policy Boundary Checks**: Extracted metrics are evaluated against the non-negotiable rules defined in `RULES.md`.
4. **Verdict Synthesis**:
   - **`APPROVED`**: Issued when all criteria strictly pass thresholds, zero compliance violations are detected, and data integrity is certified.
   - **`NEEDS_REVIEW`**: Issued when borderline metrics or ambiguous edge cases require human supervisor assessment.
   - **`BLOCKED`**: Issued immediately upon detecting any violation of zero-tolerance rules, severe risk factors, or non-compliant parameters.

When utility and fuel activity data is ingested, the agent executes scope1_emission_calculator, scope2_market_grid_factor, and ghg_protocol_certifier. If all factors are certified and documentation is complete, it issues APPROVED. If missing sub-meter data requires estimation, it issues NEEDS_REVIEW. If unverified emission factors or negative fuel metrics are detected, it issues BLOCKED.

---

## 3. Constraints, Limitations, and Known Issues

To ensure reliable and safe operation, the following constraints and operational boundaries apply:
- **Operates**: Operates deterministically (temperature = 0.1) based on standard EPA greenhouse mathematical models.
- **Assumes**: Assumes utility meter telemetry is calibrated and verified by utility providers.
- **Scope**: Scope 3 supply chain estimates require supplier primary activity questionnaires.
- **Deterministic Execution Constraint**: All model prompts and evaluations must run with low temperature (`0.1`) to ensure predictable, reproducible scoring and eliminate hallucinated findings.
- **Human Authority**: The agent cannot self-execute irreversible external mutations; final approval is reserved strictly for human authorities as specified in `DUTIES.md`.
