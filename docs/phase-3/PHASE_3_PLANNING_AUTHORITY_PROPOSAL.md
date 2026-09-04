# Phase 3 Planning-Authority Proposal

## 1. Purpose

This document proposes bounded planning authority for Architecture Flight
Recorder Phase 3.

Phase 3 would define implementation readiness for the deterministic
conformance kernel established by canonical Phase 1 and Phase 2 planning.

This proposal does not activate planning authority before canonical merge and
required post-merge verification.

It does not authorize implementation.

## 2. Proposed Phase Identity

- Phase: `3`
- Phase name: `DETERMINISTIC_KERNEL_IMPLEMENTATION_READINESS`
- Proposed planning authority:
  `BOUNDED_KERNEL_IMPLEMENTATION_READINESS_PLANNING_ONLY`
- Implementation authority: `NONE`
- Phase 4 authority: `NONE`

## 3. Objective

The proposed phase would translate the canonical conceptual kernel into a
technology-neutral implementation-readiness package without creating
executable artifacts.

The package would define:

- bounded module responsibilities;
- deterministic stage interfaces;
- conceptual-to-executable contract mapping;
- canonicalization and fingerprint implementation requirements;
- error and invalid-state handling requirements;
- verification and test-design requirements;
- dependency and supply-chain constraints;
- security controls for a future implementation;
- explicit first-slice implementation boundaries;
- implementation activation prerequisites.

## 4. Governing Canonical Inputs

Phase 3 planning would remain subordinate to:

- AFR product doctrine;
- the NEXUS authoritative-truth boundary;
- the canonical AFR information model;
- canonical evaluation semantics;
- Phase 1 trust invariants;
- the deterministic kernel architecture;
- the kernel execution contract;
- the Phase 2 kernel trust boundary.

Phase 3 cannot weaken, reinterpret, or replace those records.

## 5. Proposed Planning Questions

The planning package may answer:

1. What modules are required to implement the deterministic kernel?
2. Which responsibilities must remain isolated?
3. How are conceptual records mapped into future typed representations?
4. How is canonical serialization specified without ambiguity?
5. How are gate inputs, outputs, and failures represented?
6. How is deterministic rule selection constrained?
7. How are fingerprints reproduced across environments?
8. What tests would prove semantic preservation?
9. What dependency and supply-chain controls are required?
10. What is the smallest safe first implementation slice?
11. What evidence would be required to activate that slice?
12. Which capabilities must remain deferred?

These are planning questions only.

## 6. Exact Future Planning Package

If activated, Phase 3 planning would be limited to exactly:

1. `docs/SOT.md`
2. `docs/phase-3/PHASE_3_PLAN.md`
3. `docs/phase-3/PHASE_3_ACCEPTANCE_CRITERIA.md`
4. `docs/architecture/AFR_KERNEL_IMPLEMENTATION_BLUEPRINT.md`
5. `docs/contracts/AFR_EXECUTABLE_CONTRACT_MAPPING.md`
6. `docs/security/AFR_PHASE_3_IMPLEMENTATION_SAFETY_PLAN.md`

The proposal file is the authority-activation record and is not an additional
file in the future six-file planning package.

## 7. Required Planning Boundaries

Phase 3 planning must preserve:

- NEXUS as the authority for approved architecture truth;
- observations as non-authoritative descriptions of operational state;
- explicit evidence-eligibility decisions;
- deterministic and fail-closed gate ordering;
- canonical outcome meanings;
- claim-level and aggregate-result separation;
- complete material-input fingerprinting;
- tenant and subject isolation;
- source and collector identity separation;
- trusted-time and freshness requirements;
- model exclusion from authoritative decisions;
- ATA consequential runtime commit authority;
- PAA and Humanize as non-authoritative consumers.

## 8. Explicit Exclusions

This proposal does not authorize:

- source code;
- executable schemas;
- tests or fixtures;
- build files or dependencies;
- packages or services;
- APIs or command-line interfaces;
- provider adapters or collectors;
- live evidence ingestion;
- NEXUS, ATA, PAA, or Humanize integration;
- database or object-store persistence;
- queues, streams, or replay execution;
- runtime conformance evaluation;
- certificate generation or signing;
- deployment artifacts;
- production access;
- runtime enforcement;
- autonomous remediation;
- Phase 4 planning or implementation.

## 9. First-Slice Constraint

Phase 3 planning may recommend a future first implementation slice.

It cannot activate that slice.

Any future implementation authority must identify:

- an exact source and test file boundary;
- approved typed contract versions;
- deterministic behavior to be implemented;
- prohibited behavior;
- dependency constraints;
- security and tenant-isolation controls;
- required validation commands;
- acceptance evidence;
- rollback or abandonment conditions;
- a separately governed effective point.

## 10. Review Requirements

This proposal requires independent review for:

- Phase 0 doctrine consistency;
- Phase 1 semantic preservation;
- Phase 2 kernel-contract preservation;
- deterministic-boundary preservation;
- NEXUS non-duplication;
- ATA authority preservation;
- security and tenant isolation;
- implementation-authority leakage;
- Phase 4 authority leakage;
- effective-point completeness.

## 11. Activation Effective Point

Before the effective point:

- Phase 3 planning authority: `NONE`;
- Phase 3 implementation authority: `NONE`;
- runtime evaluation authority: `NONE`;
- integration authority: `NONE`;
- persistence authority: `NONE`;
- deployment authority: `NONE`;
- production authority: `NONE`;
- Phase 4 authority: `NONE`.

Phase 3 planning authority becomes active if and only if:

1. this proposal remains limited to `docs/SOT.md` and this file;
2. the proposal is independently reviewed;
3. all review findings are resolved;
4. the frozen proposal is committed and pushed;
5. its pull request is created as a draft;
6. the pull request receives independent acceptance review;
7. the pull request is explicitly authorized for merge;
8. the proposal is merged to canonical `main`;
9. post-merge identity, parentage, tree, and content verification passes;
10. local and remote canonical `main` converge cleanly.

After and only after that effective point:

- Phase 3 planning authority:
  `BOUNDED_KERNEL_IMPLEMENTATION_READINESS_PLANNING_ONLY`;
- Phase 3 implementation authority: `NONE`;
- runtime evaluation authority: `NONE`;
- integration authority: `NONE`;
- persistence authority: `NONE`;
- deployment authority: `NONE`;
- production authority: `NONE`;
- Phase 4 authority: `NONE`.

## 12. Non-Automatic Transition

Activation of Phase 3 planning authority authorizes only the exact six-file
planning package.

Completing or accepting that planning package will not automatically authorize
implementation or Phase 4.

Implementation requires a separate authority proposal, independent review,
canonical merge, and post-merge verification.
