# AFR Phase 6 Acceptance Criteria

## 1. Purpose

These criteria define the conditions required to accept Phase 6
Conformance-Findings and Certificate-Boundary planning.

## 2. Canonical Baseline Acceptance

PASS requires the package to bind the accepted canonical baseline:

- `c0d79d54c4cc9582ab46afd430d62169e93d5d29`;
- tree `beaf1219710941476fbbeb518d20b1f30308d845`;
- effective Phase 6 planning authority.

## 3. Exact Planning-Package Boundary

PASS requires exactly six authorized planning documents and no seventh path.

## 4. Document Convergence

PASS requires all six documents to use compatible definitions, boundaries,
authority states, outcome vocabulary, failure semantics, and stop conditions.

## 5. Completed-Evaluation Input Acceptance

PASS requires findings to consume only already-completed bounded AFR evaluation
semantics.

Missing mandatory completed-evaluation identity or authority must fail closed.

## 6. Outcome Preservation Acceptance

PASS requires the canonical outcome vocabulary:

- `CONFORMANT`;
- `NON_CONFORMANT`;
- `INCONCLUSIVE`;
- `STALE`.

Phase 6 must not recompute or replace an authoritative outcome.

Required-input failure must not produce `CONFORMANT`.

## 7. Finding-Identity Acceptance

PASS requires explicit finding identity and deterministic binding to the
source evaluation and applicable claim or aggregate-result context.

## 8. Immutability Acceptance

PASS requires historical evaluation and finding records to remain immutable.

Correction, supersession, and replacement must produce new identities and
preserve provenance.

## 9. Claim-Binding Acceptance

PASS requires claim-level findings to preserve authoritative claim references
without widening evaluated architecture scope.

## 10. Evidence-Lineage Acceptance

PASS requires support, contradiction, evidence-gap, and limitation references
to remain traceable to the completed evaluation.

## 11. Evidence-Gap and Contradiction Acceptance

PASS requires unresolved gaps or contradictions to remain explicit.

They cannot be suppressed or converted into conformance.

## 12. Drift Acceptance

PASS requires drift semantics to remain bound to authoritative claims and the
completed evaluation.

Drift creates no remediation or execution authority.

## 13. Staleness Acceptance

PASS requires stale or expired semantics to remain distinguishable from current
conformance.

A stale result cannot be presented as `CONFORMANT` for a current context.

## 14. Tenant and Subject Acceptance

PASS requires exact tenant and subject binding and fail-closed rejection of
cross-tenant or cross-subject reuse.

## 15. Environment, Release, Deployment, and Scope Acceptance

PASS requires scope non-expansion across environment, release, deployment, and
evaluated scope.

## 16. Time and Validity Acceptance

PASS requires explicit distinction among evaluation time, finding time,
validity deadline, applicability interval, expiry, supersession, and future
revocation time.

## 17. Certificate-Eligibility Acceptance

PASS requires certificate eligibility to remain subordinate to approved
deterministic policy.

A model cannot make the authoritative eligibility decision.

Eligibility cannot exceed the underlying evaluation.

## 18. Certificate-Representation Acceptance

PASS requires a future certificate representation to preserve required
evaluation, claim, evidence, scope, time, limitation, version, integrity,
issuer, supersession, and provenance bindings.

## 19. Integrity Acceptance

PASS requires integrity metadata to mean only representation integrity and
issuer attribution.

It must not be interpreted as universal architecture correctness or execution
authority.

## 20. Evaluator-Issuer-Consumer Separation Acceptance

PASS requires explicit separation among:

- architecture authority;
- evaluator;
- finding constructor;
- future issuer;
- future verifier;
- human reviewer;
- downstream consumer;
- ATA runtime authority.

## 21. Expiry, Supersession, and Future Revocation Acceptance

PASS requires immutable history and explicit predecessor-successor
relationships.

Future revocation cannot rewrite evaluation truth.

## 22. Replay and Cross-Context Safety Acceptance

PASS requires replay and reuse rejection outside bound tenant, subject,
environment, release, deployment, scope, validity, and representation
identity.

## 23. Model-Exclusion Acceptance

PASS requires explicit prohibition on model authority for:

- conformance outcome selection;
- certificate eligibility;
- evidence fabrication or suppression;
- scope widening;
- authoritative fingerprint substitution;
- authority grants.

## 24. Security and Audit Acceptance

PASS requires planning for:

- integrity continuity;
- lineage;
- tenant isolation;
- limitation preservation;
- replay resistance;
- attribution;
- audit provenance;
- sensitive evidence-reference handling.

## 25. NEXUS and Cross-Program Non-Drift Acceptance

PASS requires NEXUS architecture-truth authority and ATA consequential runtime
authority to remain preserved.

Phase 6 must create no integration authority.

## 26. Prohibited-Scope Acceptance

PASS requires implementation, persistence, signing, issuance, key operations,
network, provider, integration, runtime, deployment, enforcement, remediation,
and production authority to remain `NONE`.

## 27. Stop-Condition Acceptance

PASS requires explicit stop conditions for every transition beyond the
six-document planning authority.

## 28. Review and Evidence Acceptance

PASS requires independent architecture, contract, semantic, security,
certificate-boundary, tenant-isolation, model-exclusion, NEXUS non-duplication,
downstream non-drift, and authority-leakage review.

## 29. Planning Completion Acceptance

PASS requires exact-content freeze, controlled repository lifecycle, merge,
and post-merge reconciliation of the exact six-document package.

## 30. Post-Planning Authority Acceptance

Planning completion does not establish implementation authority.

All runtime-adjacent authorities remain `NONE` until separately proposed and
accepted.
