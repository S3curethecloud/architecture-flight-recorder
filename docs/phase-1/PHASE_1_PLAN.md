# Phase 1 Plan: Canonical Contracts and Evaluation Semantics

## 1. Purpose

Phase 1 defines the normative, provider-neutral information contracts and
deterministic evaluation semantics required by Architecture Flight Recorder.

This is a planning phase only.

## 2. Authority

Authorized planning authority:

`BOUNDED_CONTRACT_AND_EVALUATION_SEMANTICS_PLANNING_ONLY`

Implementation authority: `NONE`.

The controlling authority is the canonically merged and verified
`PHASE_1_PLANNING_AUTHORITY_PROPOSAL.md`.

## 3. Objective

Phase 1 must establish a precise semantic foundation for evaluating whether
eligible operational evidence supports approved architecture truth.

The result must be sufficiently explicit for a later implementation phase to
make technology choices without redefining product authority or inventing
missing semantics.

## 4. Planning Questions

Phase 1 must answer:

1. What uniquely identifies an architecture claim?
2. How is a claim bound to tenant, subject, environment, release, and scope?
3. How does AFR reference immutable approved truth without duplicating it?
4. What distinguishes an observation from eligible evidence?
5. Which provenance, identity, integrity, freshness, and scope properties are
   mandatory?
6. How are evidence gaps, contradictions, and stale evidence represented?
7. What constitutes `CONFORMANT`, `NON_CONFORMANT`, `INCONCLUSIVE`, and
   `STALE`?
8. How are claim-level outcomes aggregated without hiding weaker results?
9. Which inputs determine an evaluation fingerprint?
10. How are evaluator, policy, and contract compatibility represented?
11. Which conditions must fail closed?
12. Which semantics remain explicitly deferred?

## 5. Workstreams

### 5.1 Canonical Information Model

Define normative conceptual records for:

- authoritative truth references;
- architecture claims;
- evidence observations;
- evidence-eligibility decisions;
- evaluation definitions;
- evaluation contexts;
- claim-level results;
- aggregate results;
- evidence gaps;
- contradictions;
- drift findings;
- evaluation fingerprints;
- provenance events.

The model remains descriptive and technology-neutral. It must not become an
executable schema or persistence design.

### 5.2 Evaluation Semantics

Define deterministic semantics for:

- input validation;
- evidence eligibility;
- claim-to-evidence matching;
- support and contradiction;
- completeness;
- freshness;
- outcome selection;
- aggregation;
- reproducibility;
- compatibility;
- limitations and failure behavior.

### 5.3 Trust Invariants

Define cross-cutting invariants for:

- tenant isolation;
- identity;
- source authority;
- provenance;
- integrity;
- time;
- immutability;
- non-repudiation direction;
- model exclusion from authoritative decisions;
- downstream authority containment.

### 5.4 Acceptance and Traceability

Define reviewable criteria proving that:

- every required semantic concept is covered;
- every outcome is deterministic;
- every positive result is evidence-bound;
- every authority boundary remains intact;
- every unresolved implementation decision remains deferred.

## 6. Required Semantic Separations

Phase 1 must preserve these distinctions:

- architecture truth versus operational observation;
- observation versus eligible evidence;
- missing evidence versus negative evidence;
- contradiction versus insufficiency;
- claim-level outcome versus aggregate outcome;
- evaluation result versus architecture approval;
- conformance certificate versus execution authority;
- normative contract versus executable schema;
- evaluation semantics versus implementation algorithm;
- conformance verification versus remediation.

No document may collapse these concepts for convenience.

## 7. Determinism Boundary

The future authoritative evaluation must be reproducible from the same:

- truth snapshot;
- evaluated claims;
- eligible evidence set;
- evaluation definition;
- policy version;
- evaluator version;
- evaluation context;
- trusted time inputs.

Phase 1 defines this requirement but does not implement an evaluator.

## 8. Fail-Closed Boundary

Phase 1 must ensure that `CONFORMANT` is impossible when any required input has
unresolved:

- identity;
- authority;
- tenant or subject scope;
- approval state;
- provenance;
- integrity;
- freshness;
- compatibility;
- completeness;
- contradiction.

Incomplete information must become `INCONCLUSIVE`, `STALE`, or another
non-conformant condition permitted by the canonical semantics.

## 9. NEXUS Boundary

NEXUS remains authoritative for approved architecture truth.

Phase 1 may define only the AFR-side semantic requirements for referencing a
future immutable truth snapshot. It cannot define or implement the NEXUS export
contract, modify NEXUS objects, or infer missing NEXUS meaning.

## 10. Ecosystem Boundary

- ATA retains consequential runtime commit authority.
- PAA may eventually explain findings but cannot rewrite them.
- Humanize remains a downstream presentation consumer.
- Providers remain sources of bounded observations.
- AFR cannot perform remediation or grant authority.

## 11. Exact File Boundary

Phase 1 planning is limited to:

1. `docs/SOT.md`
2. `docs/phase-1/PHASE_1_PLAN.md`
3. `docs/phase-1/PHASE_1_ACCEPTANCE_CRITERIA.md`
4. `docs/contracts/AFR_CANONICAL_INFORMATION_MODEL.md`
5. `docs/contracts/AFR_EVALUATION_SEMANTICS.md`
6. `docs/security/AFR_PHASE_1_TRUST_INVARIANTS.md`

## 12. Explicit Non-Goals

Phase 1 does not authorize:

- source code;
- executable schemas;
- implementation tests;
- persistence models;
- APIs or events;
- provider adapters;
- credentials;
- live evidence collection;
- NEXUS integration;
- evaluator execution;
- certificate generation or signing;
- runtime enforcement;
- ATA, PAA, or Humanize integration;
- deployment or production access;
- Phase 2.

## 13. Review Sequence

1. Materialize the exact six-file planning package.
2. Validate file and terminology boundaries.
3. Validate cross-document semantic consistency.
4. Conduct independent architecture and security review.
5. Resolve all findings through bounded amendments.
6. Stage and verify the reviewed package.
7. Commit and push the exact candidate.
8. Create a draft pull request.
9. Conduct independent acceptance review.
10. Require explicit ready and merge transitions.
11. Verify canonical merge identity and content.
12. Close Phase 1 through a separately governed reconciliation.

## 14. Exit Constraint

Completing Phase 1 planning does not authorize implementation or Phase 2.

A separate implementation-authority proposal and effective point would be
required before any executable artifact is created.
