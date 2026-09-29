# Separation of Duties (SOD) & Operational Boundaries

To ensure robust compliance, security, and verification, **GitEsgReporter** implements a strict tripartite Separation of Duties architecture.

---

### 1. Maker
* **Assigned Entity**: `GitEsgReporter Automation Engine`
* **Responsibilities**:
  * Calculates metric tonnes of CO2 equivalent across Scope 1, 2, and 3 activity streams.
  * Ingests raw repository data, configurations, and input artifacts.
  * Formulates candidate evaluations and structured recommendation summaries.
  * Records execution logs into `memory/audit.log`.

---

### 2. Checker
* **Assigned Entity**: `GitEsgReporter Verification & Policy Enforcer`
* **Responsibilities**:
  * Verifies supplier utility invoice data and applies regional grid emission factor coefficients.
  * Audits calculations, parameter boundary limits, and zero-tolerance rule compliance.
  * Asserts schema validity on all output manifests.
  * Issues preliminary assessment: `APPROVED`, `BLOCKED`, or `NEEDS_REVIEW`.

---

### 3. Approver
* **Assigned Entity**: `Chief Sustainability Officer (CSO) / Head of ESG Compliance (Reserved for human review).`
* **Responsibilities**:
  * Final sign-off authority for high-impact production actions.
  * Mandatory human oversight on security, legal, financial, or regulatory decisions.
  * Reviews unresolvable edge cases and policy override exceptions.
