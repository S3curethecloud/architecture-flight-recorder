# Phase 1 Planning-Authority Proposal

## 1. Purpose

This document proposes bounded planning authority for Architecture Flight
Recorder Phase 1.

It does not itself activate that authority before canonical merge and required
post-merge verification.

It does not authorize implementation.

## 2. Proposed Phase Identity

- Phase: `1`
- Phase name: `CANONICAL_CONTRACTS_AND_EVALUATION_SEMANTICS`
- Proposed authority:
  `BOUNDED_CONTRACT_AND_EVALUATION_SEMANTICS_PLANNING_ONLY`
- Implementation authority: `NONE`

## 3. Planning Objective

Phase 1 planning will define the normative semantic contracts required for AFR
to evaluate approved architecture truth against eligible operational evidence
without changing the authority boundaries established by Phase 0.

The planning package must make explicit:

- architecture-claim identity and scope;
- immutable truth-snapshot references;
- observation and evidence distinctions;
- evidence-eligibility semantics;
- tenant, subject, environment, and release binding;
- provenance, integrity, freshness, and time semantics;
- evaluation-definition semantics;
- deterministic claim-level outcomes;
- aggregate-result constraints;
- evaluation fingerprints and reproducibility;
- evidence gaps and contradiction handling;
- fail-closed behavior;
- compatibility and versioning requirements;
- Phase 1 exit and acceptance criteria.

## 4. Authorized Future Planning Package

If this proposal reaches its activation effective point, Phase 1 planning is
limited to these files:

1. `docs/SOT.md`
2. `docs/phase-1/PHASE_1_PLAN.md`
3. `docs/phase-1/PHASE_1_ACCEPTANCE_CRITERIA.md`
4. `docs/contracts/AFR_CANONICAL_INFORMATION_MODEL.md`
5. `docs/contracts/AFR_EVALUATION_SEMANTICS.md`
6. `docs/security/AFR_PHASE_1_TRUST_INVARIANTS.md`

No additional file is authorized without a separately reviewed authority
amendment.

## 5. Required Planning Boundaries

The Phase 1 planning package must preserve all Phase 0 doctrine and system
boundaries.

In particular:

- NEXUS remains authoritative for approved architecture truth;
- provider and enterprise observations do not become architecture truth;
- evidence eligibility does not elevate evidence authority;
- AFR owns only bounded conformance-evaluation results;
- ATA retains consequential runtime commit authority;
- PAA cannot rewrite AFR findings or NEXUS truth;
- Humanize remains a downstream presentation consumer;
- model inference cannot select authoritative outcomes;
- missing or invalid required inputs cannot produce `CONFORMANT`;
- cross-tenant evidence use remains prohibited;
- certificates cannot grant execution or deployment authority.

## 6. Explicitly Excluded Authority

This proposal does not authorize:

- source code;
- executable schemas or generated models;
- tests representing implementation behavior;
- persistence or database design implementation;
- provider or enterprise adapters;
- live evidence collection;
- NEXUS export or integration implementation;
- ATA integration;
- PAA integration;
- Humanize integration;
- evaluation execution;
- certificate generation, signing, or issuance;
- model integration;
- credentials or secrets;
- external-system mutation;
- deployment;
- production access;
- Phase 2 planning or implementation.

## 7. Planning Deliverable Requirements

The future planning package must:

- use provider-neutral and technology-neutral semantics;
- distinguish normative concepts from implementation choices;
- define deterministic behavior without implementing it;
- preserve stable identifiers and version relationships;
- define invalid, incomplete, contradictory, and stale conditions;
- define how weaker claim outcomes constrain aggregate outcomes;
- make every authoritative output traceable to its bounded inputs;
- identify unresolved decisions rather than silently resolving them;
- include an independently reviewable acceptance gate.

## 8. Proposal Effective Point

Before the effective point:

- Phase 1 planning authority: `NONE`;
- Phase 1 implementation authority: `NONE`.

The proposal becomes effective only when:

1. its change set remains limited to this proposal and `docs/SOT.md`;
2. the proposal receives independent architecture and acceptance review;
3. all review findings are resolved;
4. the proposal is merged to canonical `main`;
5. post-merge identity, parentage, tree, and content are verified;
6. the local canonical `main` checkout is synchronized and clean.

After that effective point:

- Phase 1 planning authority:
  `BOUNDED_CONTRACT_AND_EVALUATION_SEMANTICS_PLANNING_ONLY`;
- Phase 1 implementation authority: `NONE`;
- runtime authority: `NONE`;
- integration authority: `NONE`;
- persistence authority: `NONE`;
- deployment authority: `NONE`;
- Phase 2 authority: `NONE`.

Opening, approving, or marking the proposal PR ready does not activate Phase 1
planning authority.

## 9. Proposed Acceptance Statement

The proposal may be accepted only if reviewers can support this statement:

> Phase 1 may plan AFR's canonical information contracts and deterministic
> evaluation semantics, but it may not implement, integrate, execute, persist,
> issue certificates, deploy, or activate Phase 2.
