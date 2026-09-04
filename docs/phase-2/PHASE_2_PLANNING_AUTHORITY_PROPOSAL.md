# Phase 2 Planning-Authority Proposal

## 1. Purpose

This document proposes bounded planning authority for Architecture Flight
Recorder Phase 2.

It does not activate planning authority before canonical merge and required
post-merge verification.

It does not authorize implementation.

## 2. Proposed Phase Identity

- Phase: `2`
- Phase name: `DETERMINISTIC_CONFORMANCE_KERNEL`
- Proposed planning authority:
  `BOUNDED_DETERMINISTIC_CONFORMANCE_KERNEL_PLANNING_ONLY`
- Implementation authority: `NONE`
- Runtime authority: `NONE`
- Phase 3 authority: `NONE`

## 3. Objective

Phase 2 planning will define how the canonical Phase 1 information model and
evaluation semantics can be realized as a deterministic conformance kernel
without changing their approved meanings.

The planned kernel must preserve:

- deterministic evaluation for identical eligible inputs;
- fail-closed truth and evidence eligibility;
- explicit `CONFORMANT`, `NON_CONFORMANT`, `INCONCLUSIVE`, and `STALE`
  outcomes;
- tenant, subject, environment, release, and time boundaries;
- evidence provenance, integrity, freshness, and contradiction handling;
- evaluation fingerprint reproducibility;
- NEXUS authority over approved architecture truth;
- ATA authority over consequential runtime commits;
- separation of evaluation from enforcement and remediation.

## 4. Proposed Planning Scope

The proposed planning authority is limited to defining:

- deterministic kernel components and responsibilities;
- input-validation and eligibility gates;
- claim-level evaluation sequencing;
- aggregate-outcome constraints;
- invalid-state and failure behavior;
- evaluation fingerprint construction requirements;
- reproducibility and audit requirements;
- technology-neutral component boundaries;
- security and tenant-isolation controls;
- an implementation-readiness acceptance gate.

All outputs remain documentation-only.

## 5. Proposed Planning Artifact Boundary

If this proposal reaches its effective point, Phase 2 planning is limited to
exactly these six artifacts:

1. `docs/SOT.md`
2. `docs/phase-2/PHASE_2_PLAN.md`
3. `docs/phase-2/PHASE_2_ACCEPTANCE_CRITERIA.md`
4. `docs/architecture/AFR_DETERMINISTIC_KERNEL_ARCHITECTURE.md`
5. `docs/contracts/AFR_KERNEL_EXECUTION_CONTRACT.md`
6. `docs/security/AFR_PHASE_2_KERNEL_TRUST_BOUNDARY.md`

No additional artifact is implied or authorized.

## 6. Required Planning Questions

Phase 2 planning must resolve:

1. How are Phase 1 semantic records validated without redefining them?
2. Which gates must pass before claim evaluation can begin?
3. How are missing, stale, contradictory, or ineligible inputs represented?
4. How is deterministic rule selection constrained?
5. How are claim-level outcomes aggregated without masking weaker outcomes?
6. Which inputs bind the evaluation fingerprint?
7. How are evaluation replay and historical reproducibility preserved?
8. How are tenant and subject boundaries enforced between kernel stages?
9. How are model-assisted explanations excluded from authoritative decisions?
10. Which failures block evaluation rather than manufacture certainty?
11. What evidence is required before implementation may be proposed?
12. How will future implementations prove conformance to the planning package?

## 7. NEXUS Boundary

NEXUS remains authoritative for approved architecture truth.

Phase 2 planning may define validation of a conceptual immutable truth input,
but it cannot:

- define or implement a NEXUS export;
- read mutable NEXUS persistence;
- modify NEXUS objects or lifecycle state;
- create missing architecture meaning;
- infer approval;
- introduce NEXUS credentials or connectivity.

A separately governed integration contract and authority activation would be
required for any future NEXUS integration.

## 8. Evidence Boundary

Phase 2 planning may define conceptual eligible-evidence inputs to the kernel.

It cannot authorize:

- provider adapters;
- collectors;
- live evidence ingestion;
- normalization services;
- queues or event streams;
- provider credentials;
- cloud access;
- evidence persistence.

Observed state remains distinct from approved architecture truth.

## 9. Evaluation Boundary

Phase 2 planning may define deterministic evaluation mechanics at an
architecture and contract level.

It cannot authorize:

- executable evaluators;
- policy-engine code;
- executable rules;
- model-based authoritative decisions;
- production evaluation;
- certificate generation;
- enforcement;
- remediation.

Planning must not weaken or reinterpret the Phase 1 outcome semantics.

## 10. Security Boundary

Planning must preserve:

- tenant isolation;
- resolved source and collector identity;
- provenance and integrity validation;
- trusted-time and freshness controls;
- immutable evaluation inputs;
- deterministic version selection;
- replay and substitution resistance;
- fail-closed unsupported-version handling;
- non-authoritative model containment;
- downstream immutability of authoritative findings.

This proposal does not authorize implementation of those controls.

## 11. Explicit Exclusions

This proposal does not authorize:

- source code;
- executable schemas;
- tests or fixtures;
- dependency selection or installation;
- application or package scaffolding;
- APIs or services;
- provider or cloud adapters;
- NEXUS integration;
- ATA integration;
- PAA integration;
- Humanize integration;
- live evidence collection;
- evaluation execution;
- policy-engine execution;
- persistence or databases;
- queues, streams, or caches;
- certificate issuance or signing;
- deployment;
- production access;
- runtime mutation;
- remediation;
- Phase 3 planning or implementation.

## 12. Review Requirements

The proposal must receive independent review for:

- consistency with Phase 0 doctrine;
- consistency with Phase 1 contracts and semantics;
- deterministic-kernel scope;
- NEXUS non-duplication;
- ATA authority preservation;
- security and tenant isolation;
- implementation-authority leakage;
- Phase 3 authority leakage;
- exact two-file proposal boundary.

All findings must be resolved before merge authorization.

## 13. Effective Point

Before the effective point:

- Phase 2 planning authority: `NONE`;
- Phase 2 implementation authority: `NONE`;
- Phase 3 authority: `NONE`.

The proposal becomes effective only when:

1. it remains limited to `docs/SOT.md` and this proposal;
2. its content is frozen and independently reviewed;
3. all review findings are resolved;
4. the exact candidate is committed and pushed;
5. its draft pull request is verified;
6. explicit ready-transition authorization is granted;
7. explicit merge authorization is granted;
8. it is merged to canonical `main`;
9. post-merge identity, parentage, tree, and content verification passes;
10. local and remote canonical `main` converge cleanly.

After and only after that effective point:

- Phase 2 planning authority:
  `BOUNDED_DETERMINISTIC_CONFORMANCE_KERNEL_PLANNING_ONLY`;
- Phase 2 implementation authority: `NONE`;
- Phase 3 authority: `NONE`.

## 14. Non-Activation Statement

Creating, committing, pushing, reviewing, approving, or marking a pull request
ready does not activate Phase 2 planning authority.

Canonical merge without successful post-merge verification also does not
complete the effective point.

Implementation and Phase 3 require separately defined, reviewed, merged, and
verified authority activations.
