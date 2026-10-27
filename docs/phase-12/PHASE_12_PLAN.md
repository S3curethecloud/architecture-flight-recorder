# AFR Phase 12 - Drift, Findings, Conformance Certificates, and Command Center Plan

## 1. Status and authority

- Phase: 12 - Drift, Findings, and Conformance Certificates
- Command Center posture: bounded read-oriented product-surface planning
- Artifact posture: DETACHED PLANNING CANDIDATE - NONCANONICAL
- Authority: planning and contract preparation only
- Implementation authority: NONE
- Runtime authority: NONE
- Finding-issuance runtime authority: NONE
- Certificate-issuance runtime authority: NONE
- Command Center implementation authority: NONE
- Command Center runtime authority: NONE
- Command Center deployment authority: NONE
- Command Center production authority: NONE
- NEXUS mutation authority: NONE
- ATA commit authority: NONE
- Phase 13 entry authority: NONE
- Phase 14 entry authority: NONE

## 2. Frozen predecessor identity

Phase 12 planning is anchored to terminal Phase 11:

- canonical predecessor main OID: `6e3789ff6f972bfffb5ea04031b874b419730dc2`
- canonical predecessor tree: `8ca430c260f9171424d0329ed28ca128e76fbfc3`
- Phase 11 closure record SHA-256: `95ac664def50bb0e785ea7df7ddded1f6c91c28ec5f406fbb99ecdb7a667a3bb`
- Phase 11 closure PR: `42`
- Phase 11 evaluation result remains upstream and immutable.

Phase 12 does not reopen Phase 11.

## 3. Canonical roadmap position

The AFR V1 roadmap remains:

1. Phase 12 - drift, findings, and conformance certificates;
2. Phase 13 - operational delivery and downstream consumer integration;
3. Phase 14 - production hardening, E2E acceptance, and final NEXUS/ARCP compatibility certification.

`AFR_V1_COMPLETION_TARGET=PHASE_14`

Phase 13 is not the final AFR V1 phase.

## 4. Phase 12 objective

Define deterministic, technology-neutral semantics for:

1. deriving Phase 12 findings from accepted Phase 11 evaluation results;
2. identifying architecture drift without rewriting history;
3. composing time-bound conformance certificate representations from accepted
   finding state;
4. projecting those results through a durable provider-neutral AFR Command Center;
5. preserving evidence, provenance, authority, freshness, and uncertainty visibly;
6. freezing extension seams that permit Phase 13 and Phase 14 to extend the
   product without routine replacement of the Command Center shell.

This plan creates no implementation or runtime authority.

## 5. Finding semantics

The Phase 12 presentation finding-state domain is:

- `SUPPORTED`
- `CONTRADICTED`
- `STALE`
- `INCONCLUSIVE`
- `EVIDENCE_UNAVAILABLE`

These are Phase 12 finding states, not replacements for the canonical Phase 11
evaluation outcomes.

A future accepted derivation contract must deterministically bind each finding to
its exact source evaluation result, claim, truth identity, evidence identity,
policy/version set, tenant, subject, scope, and trusted-time context.

`EVIDENCE_UNAVAILABLE` must never render as `SUPPORTED`.

`INCONCLUSIVE` must never collapse into `SUPPORTED`.

## 6. Drift semantics

Architecture drift is a deterministic material change in accepted conformance state
or in a bound input identity that is relevant to current architectural support.

A drift record must identify:

- prior accepted finding identity;
- current accepted finding identity;
- affected architecture claim;
- exact material change class;
- prior and current truth/evidence/policy/version identities;
- trusted-time context;
- scope;
- deterministic rationale references.

Drift is not architecture redesign and does not modify NEXUS truth.

## 7. Certificate semantics

A Phase 12 conformance certificate representation is a bounded, time-qualified,
cryptographically bindable statement over an accepted conformance scope.

A certificate representation must bind at least:

- certificate contract version;
- tenant and subject scope;
- architecture-truth identity;
- finding-set identity;
- source evaluation-set identity;
- evidence-set identity;
- policy/evaluator/canonicalization/fingerprint versions;
- validity interval;
- limitations and unresolved conditions;
- certificate-content fingerprint.

Planning a certificate representation does not authorize signing, issuance,
publication, revocation, or external delivery.

## 8. Architecture Conformance Score

A Command Center may expose an Architecture Conformance Score only as a deterministic
traceable derived summary.

The score must:

- declare formula identity and version;
- declare denominator and exclusions;
- preserve counts for `STALE`, `INCONCLUSIVE`, and `EVIDENCE_UNAVAILABLE`;
- link to the underlying finding set;
- become unavailable rather than fabricate certainty when required state is unresolved.

The score is never source of truth and cannot replace finding states.

## 9. Durable AFR Command Center

The Command Center is the human-facing conformance operations and investigation
plane. It observes, explains, correlates, and presents accepted AFR state.

The durable semantic surfaces are:

1. Executive Status / Traceable Conformance Summary
2. Live Findings
3. Architecture Drift
4. Evidence Health
5. Evaluation Runs
6. Conformance Certificates / Attestations
7. System / Tenant / Architecture Scope
8. Critical Alerts
9. Flight Recorder Timeline
10. Governance / Audit

These are semantic surfaces, not a requirement for ten routes or ten pages.

## 10. Command Center authority boundary

The Command Center cannot:

- create or modify NEXUS architecture truth;
- rewrite Phase 11 evaluation results;
- waive evidence or freshness failures;
- convert unknown state into success;
- issue or sign a certificate merely because it can display one;
- mutate providers;
- perform remediation;
- grant ATA commit authority;
- create deployment or production authority.

`COMMAND_CENTER_PRESENTATION != EXECUTION_AUTHORITY`

## 11. Durable shell and read-model strategy

Phase 12 planning freezes a provider-neutral shell around versioned read models.

Every read model must carry:

- read-model contract version;
- tenant/workspace/subject scope where applicable;
- `as_of` and freshness state;
- source identity/fingerprint;
- authority state;
- limitations/warnings;
- deterministic data payload.

The shell consumes contracts, not provider-specific payload shapes.

## 12. Extension and capability strategy

The Command Center must expose a versioned capability registry and adapter boundary.

A capability registration must declare:

- capability ID;
- contract version;
- supported shell surface(s);
- source type;
- read/write posture;
- authority requirements;
- freshness semantics;
- failure semantics;
- compatibility range;
- provenance requirements.

Presence of a capability is not permission to invoke it.

## 13. Phase 13 extension seam

Phase 13 may add operational delivery and downstream consumer integration through
versioned adapters over the stable Phase 12 shell.

Expected extension classes may include:

- downstream read projections;
- notification/delivery projections;
- approved consumer adapters;
- external presentation feeds;
- integration health projections.

Phase 13 may not reinterpret Phase 12 findings or silently add provider mutation
authority.

## 14. Phase 14 hardening seam

Phase 14 may add:

- production security controls;
- SLOs and reliability evidence;
- performance and capacity qualification;
- observability and operational diagnostics;
- E2E acceptance;
- final NEXUS/ARCP compatibility certification;
- compatibility and upgrade evidence.

Phase 14 hardening may not redefine accepted Phase 12 semantics merely to satisfy
operational convenience.

## 15. Technology neutrality

This planning package selects no frontend framework, backend framework, database,
event bus, queue, cache, identity provider, cloud provider, observability vendor,
certificate-signing service, or deployment topology.

## 16. Planned validation campaign

Before implementation authority can be considered, the accepted package must support
future tests or fixtures covering at least:

- deterministic finding derivation;
- contradicted finding derivation;
- stale finding derivation;
- inconclusive finding derivation;
- evidence unavailable handling;
- cross-tenant and cross-subject rejection;
- drift from evidence change;
- drift from truth change;
- drift from policy/evaluator version change;
- no-drift duplicate cycle;
- finding immutability and supersession;
- certificate fingerprint reproducibility;
- certificate validity expiration;
- unresolved condition propagation;
- conformance-score traceability;
- score unavailable on unresolved mandatory state;
- Command Center unknown-state fail closed;
- read-model version compatibility;
- capability registration without authority inheritance;
- Phase 13 adapter addition without shell rebuild;
- Phase 14 hardening without semantic redefinition.

## 17. Sequencing

1. detached Phase 12 planning-package preparation;
2. independent whole-package read-only acceptance;
3. separately authorized repository materialization and publication lifecycle;
4. canonical Phase 12 planning effective point and terminal planning closure;
5. separately governed implementation-readiness review;
6. only then, if explicitly authorized, bounded implementation;
7. separately governed runtime qualification;
8. only then, if explicitly authorized, finding/certificate runtime effects;
9. Phase 13 remains independently gated;
10. Phase 14 remains independently gated.

No earlier step implies a later one.

## 18. Non-goals

This plan does not authorize source code, UI implementation, API implementation,
database schemas, provider reads, evidence ingestion, finding issuance, certificate
signing or issuance, external delivery, remediation, enforcement, NEXUS mutation,
ATA commit, deployment, production access, Phase 13, or Phase 14.
