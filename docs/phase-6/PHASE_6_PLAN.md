# AFR Phase 6 Plan

## 1. Purpose

Phase 6 defines planning semantics for immutable conformance findings and
future integrity-bound certificate representations derived from completed AFR
evaluations.

This phase is documentation and architecture planning only.

## 2. Canonical Baseline

The canonical Phase 6 planning baseline is:

- canonical `main`: `c0d79d54c4cc9582ab46afd430d62169e93d5d29`;
- canonical tree: `beaf1219710941476fbbeb518d20b1f30308d845`;
- Phase 6 capability:
  `CONFORMANCE_FINDINGS_AND_CERTIFICATE_BOUNDARY_PLANNING`;
- Phase 6 planning authority:
  `BOUNDED_CONFORMANCE_FINDINGS_AND_CERTIFICATE_BOUNDARY_PLANNING_ONLY`.

Accepted Phase 0 through Phase 5 semantics remain immutable predecessor
semantics.

## 3. Mission and Position

The Phase 6 mission is:

`DEFINE_IMMUTABLE_TIME_BOUND_CONFORMANCE_FINDING_AND_INTEGRITY_BOUND_CERTIFICATE_REPRESENTATION_SEMANTICS_FROM_COMPLETED_AFR_EVALUATIONS`

The architectural position is downstream of completed deterministic evaluation
and upstream of future Delivery and Integration.

## 4. Exact Planning Package

Phase 6 planning is limited exactly to six documentation paths:

1. `docs/SOT.md`
2. `docs/phase-6/PHASE_6_PLAN.md`
3. `docs/phase-6/PHASE_6_ACCEPTANCE_CRITERIA.md`
4. `docs/architecture/AFR_FINDINGS_AND_CERTIFICATE_ARCHITECTURE.md`
5. `docs/contracts/AFR_CONFORMANCE_FINDING_AND_CERTIFICATE_CONTRACT.md`
6. `docs/security/AFR_PHASE_6_FINDINGS_AND_CERTIFICATE_TRUST_BOUNDARY.md`

No seventh planning path is authorized.

## 5. Planning Outcomes

Phase 6 planning must converge on:

- immutable finding semantics;
- deterministic result-to-finding lineage;
- canonical outcome preservation;
- evidence-gap and contradiction preservation;
- limitation preservation;
- drift and staleness semantics;
- time and validity semantics;
- certificate eligibility boundaries;
- future certificate representation semantics;
- integrity and issuer-attribution boundaries;
- expiry, supersession, and future revocation relationships;
- tenant, subject, environment, release, deployment, and scope isolation;
- replay and cross-context reuse resistance;
- evaluator, issuer, verifier, consumer, and runtime-authority separation;
- model exclusion from authoritative decisions;
- explicit downstream and implementation boundaries.

## 6. Canonical Semantic Foundation

Phase 6 cannot reopen or weaken canonical semantics for:

- architecture truth;
- evidence eligibility;
- canonical evidence;
- completed evaluation identity;
- claim-level results;
- aggregate result;
- deterministic rationale;
- evidence gaps;
- contradictions;
- limitations;
- evaluation fingerprints;
- validity windows;
- supersession;
- provenance;
- tenant and subject isolation;
- model exclusion;
- ATA consequential runtime authority.

## 7. Completed-Evaluation Input Boundary

Phase 6 planning may consume only a completed bounded AFR evaluation.

The input model must preserve, as applicable:

- evaluation identity;
- evaluation context;
- tenant identity;
- subject identity;
- environment;
- release;
- deployment;
- evaluated scope;
- truth-snapshot reference;
- authoritative claim references;
- claim-level results;
- aggregate result;
- evidence-set reference;
- eligibility-decision references;
- supporting evidence references;
- contradicting evidence references;
- evidence gaps;
- deterministic rationale;
- limitations;
- evaluation-definition version;
- policy version;
- evaluator version;
- canonicalization version;
- fingerprint version;
- evaluation time;
- validity deadline;
- evaluation fingerprint;
- supersession state;
- provenance.

Missing mandatory input must fail closed.

## 8. Conformance Outcome Model

The canonical result vocabulary is:

- `CONFORMANT`;
- `NON_CONFORMANT`;
- `INCONCLUSIVE`;
- `STALE`.

Phase 6 cannot select a different authoritative outcome from the completed
evaluation.

A required-input failure cannot become `CONFORMANT`.

A stale result cannot become current conformance.

Processing or downstream-delivery failure must remain distinguishable from a
conformance outcome.

## 9. Finding Identity and Immutability

A finding must have an identity deterministically bound to its source
evaluation and bounded claim or aggregate-result context.

A finding must not mutate a historical evaluation.

Correction requires a new bounded object with explicit provenance,
supersession, or replacement semantics.

## 10. Claim Binding and Rationale

A claim-level finding must preserve the authoritative architecture-claim
reference and its deterministic rationale.

A finding cannot widen the claim set or infer approval from object presence.

## 11. Evidence, Contradictions, Gaps, and Limitations

Findings must preserve applicable:

- supporting evidence references;
- contradicting evidence references;
- evidence gaps;
- unresolved contradictions;
- source limitations;
- evaluation limitations.

Absence of required evidence cannot be silently converted into support.

## 12. Drift and Staleness

Planning must distinguish:

- bounded conformance finding;
- drift finding;
- stale result or staleness finding;
- evidence gap;
- contradiction;
- processing failure;
- downstream-delivery failure.

Drift remains bound to the authoritative claim and completed evaluation.

Neither drift nor staleness grants remediation authority.

## 13. Tenant, Subject, Environment, and Scope

Finding and certificate representation semantics must preserve exact:

- tenant;
- subject;
- environment;
- release;
- deployment;
- scope.

Cross-tenant, cross-subject, cross-environment, cross-release, and
out-of-scope reuse must fail closed.

## 14. Time and Validity

Planning must distinguish:

- evaluation time;
- finding-construction time;
- result validity deadline;
- certificate applicability interval;
- future preparation time;
- future issuance time;
- expiry;
- supersession effective time;
- future revocation effective time.

Expired or stale semantics cannot be presented as current conformance.

## 15. Certificate Eligibility

Certificate eligibility must be subordinate to approved deterministic policy.

Eligibility cannot exceed the underlying:

- evaluated claims;
- evidence;
- result;
- tenant;
- subject;
- environment;
- release;
- deployment;
- scope;
- validity;
- limitations.

A model cannot make the authoritative eligibility decision.

## 16. Certificate Representation

Planning may define a future certificate representation binding, where
applicable:

- certificate identity;
- representation version;
- completed evaluation identity;
- claim-level and aggregate-result references;
- tenant and subject;
- environment, release, deployment, and scope;
- truth-snapshot and architecture-claim references;
- evidence-set fingerprint;
- evaluation fingerprint;
- evaluation-definition version;
- policy version;
- evaluator version;
- canonicalization and fingerprint versions;
- evaluation time;
- applicability interval;
- validity deadline;
- limitations;
- supersession state;
- future issuer identity;
- future integrity or signature metadata;
- future expiry;
- future revocation relationship;
- verification version;
- provenance.

## 17. Integrity and Issuer Attribution

Integrity metadata may prove representation integrity and issuer attribution
only.

It cannot prove universal architecture correctness.

It cannot widen the underlying evaluation.

Phase 6 does not select a cryptographic algorithm, provider, PKI, KMS, HSM,
trust anchor, key hierarchy, or deployment topology.

## 18. Expiry, Supersession, and Future Revocation

Historical results remain immutable.

Supersession must preserve predecessor and successor identities.

Expiry does not delete historical truth.

Future revocation must not rewrite the completed evaluation.

## 19. Replay and Reuse Safety

Planning must define rejection semantics for reuse outside the bound:

- tenant;
- subject;
- environment;
- release;
- deployment;
- scope;
- validity interval;
- representation identity.

## 20. Model Exclusion

A model may assist with explanatory or non-authoritative drafting.

A model cannot:

- choose authoritative outcomes;
- choose authoritative certificate eligibility;
- fabricate evidence;
- suppress evidence;
- repair missing required evidence;
- widen scope;
- calculate substitute authoritative fingerprints outside an approved
  deterministic mechanism;
- grant architecture or execution authority.

## 21. Security, Privacy, and Audit Workstream

Planning must address:

- immutable lineage;
- tenant isolation;
- subject isolation;
- integrity continuity;
- limitation preservation;
- replay resistance;
- issuer attribution;
- future key-protection requirements without selecting keys or infrastructure;
- expiry;
- supersession;
- future revocation;
- verification semantics;
- audit-safe provenance;
- sensitive evidence reference handling;
- downstream authority non-expansion.

## 22. NEXUS and Cross-Program Boundary

NEXUS remains authoritative for approved architecture truth.

Phase 6 does not create NEXUS export or integration authority.

ARCP, ATA, PAA, Humanize, providers, CI/CD, and other systems remain outside
the Phase 6 integration boundary.

ATA consequential runtime authority remains preserved.

## 23. Downstream Delivery Boundary

Delivery and Integration remains deferred.

Phase 6 creates no:

- API;
- event;
- webhook;
- queue;
- feed;
- gateway;
- dashboard integration;
- CI/CD integration;
- audit-system integration;
- consumer mutation behavior.

## 24. Explicitly Prohibited Work

Phase 6 planning does not authorize:

- implementation;
- persistence;
- database schemas or migrations;
- executable schemas;
- source;
- tests;
- fixtures;
- dependencies;
- credentials;
- secrets;
- network activity;
- live evidence collection;
- provider integration;
- certificate generation;
- certificate signing;
- certificate issuance;
- certificate revocation execution;
- key generation;
- key custody;
- KMS or HSM selection or operation;
- deployment;
- runtime enforcement;
- remediation;
- production access.

## 25. Stop Conditions

Planning must stop and require new authority if:

- predecessor semantics require amendment;
- completed evaluation semantics must be recomputed or repaired;
- authoritative outcome semantics require amendment;
- evidence-eligibility semantics require amendment;
- architecture-truth semantics require amendment;
- NEXUS export or integration becomes necessary;
- live provider access becomes necessary;
- implementation or persistence becomes necessary;
- cryptographic selection or key operations become necessary;
- actual certificate generation, signing, issuance, or revocation becomes
  necessary;
- downstream delivery or integration design becomes necessary;
- the exact six-document package becomes insufficient.

## 26. Review Sequence

The planning package must receive independent review for:

1. package scope;
2. architecture consistency;
3. contract determinism;
4. outcome preservation;
5. certificate-boundary safety;
6. security and trust;
7. tenant and scope isolation;
8. model exclusion;
9. NEXUS non-duplication;
10. downstream non-drift;
11. authority leakage;
12. stop-condition completeness.

## 27. Completion Condition

Phase 6 planning is complete only when the exact six-document package:

- converges semantically;
- contains no unresolved blocking finding;
- is frozen by exact identity;
- completes its separately governed repository lifecycle;
- is merged and independently reconciled on canonical `main`.

Planning completion does not imply implementation authority.

## 28. Authority State

`AFR_PHASE_6_PLANNING_AUTHORITY =
BOUNDED_CONFORMANCE_FINDINGS_AND_CERTIFICATE_BOUNDARY_PLANNING_ONLY`

`AFR_PHASE_6_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_6_FINDING_PERSISTENCE_AUTHORITY = NONE`

`AFR_PHASE_6_CERTIFICATE_GENERATION_AUTHORITY = NONE`

`AFR_PHASE_6_CERTIFICATE_SIGNING_AUTHORITY = NONE`

`AFR_PHASE_6_CERTIFICATE_ISSUANCE_AUTHORITY = NONE`

`AFR_PHASE_6_CERTIFICATE_REVOCATION_AUTHORITY = NONE`

`AFR_PHASE_6_KEY_GENERATION_AUTHORITY = NONE`

`AFR_PHASE_6_KEY_CUSTODY_AUTHORITY = NONE`

`AFR_PHASE_6_KMS_HSM_AUTHORITY = NONE`

`AFR_PHASE_6_RUNTIME_AUTHORITY = NONE`

`AFR_PHASE_6_DEPLOYMENT_AUTHORITY = NONE`
