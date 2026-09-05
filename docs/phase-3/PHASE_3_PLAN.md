# Phase 3 Plan

## 1. Purpose

Phase 3 defines implementation readiness for the deterministic conformance
kernel established by canonical Phase 1 and Phase 2 planning.

This phase is documentation-only. It translates canonical concepts into
bounded implementation requirements without creating executable artifacts or
activating implementation authority.

## 2. Authority

The active planning authority is:

`BOUNDED_KERNEL_IMPLEMENTATION_READINESS_PLANNING_ONLY`

Phase 3 implementation authority remains `NONE`.

Phase 4 authority remains `NONE`.

## 3. Canonical Inputs

Phase 3 planning is subordinate to:

- AFR product doctrine;
- the AFR system boundary;
- the NEXUS authoritative-truth boundary;
- the canonical AFR information model;
- canonical evaluation semantics;
- Phase 1 trust invariants;
- the deterministic kernel architecture;
- the kernel execution contract;
- the Phase 2 kernel trust boundary.

Phase 3 cannot weaken, replace, or reinterpret these records.

## 4. Exact Planning Package

The authorized planning package contains exactly:

1. `docs/SOT.md`
2. `docs/phase-3/PHASE_3_PLAN.md`
3. `docs/phase-3/PHASE_3_ACCEPTANCE_CRITERIA.md`
4. `docs/architecture/AFR_KERNEL_IMPLEMENTATION_BLUEPRINT.md`
5. `docs/contracts/AFR_EXECUTABLE_CONTRACT_MAPPING.md`
6. `docs/security/AFR_PHASE_3_IMPLEMENTATION_SAFETY_PLAN.md`

No other file is within Phase 3 planning authority.

## 5. Objectives

Phase 3 must define:

- bounded kernel module responsibilities;
- deterministic stage boundaries;
- allowed dependency direction;
- conceptual-to-future-typed-contract mappings;
- canonical representation requirements;
- deterministic fingerprint construction requirements;
- invalid-state and failure representation;
- semantic-preservation verification requirements;
- tenant-isolation and authority-preservation controls;
- supply-chain and dependency constraints;
- a proposed minimum first implementation slice;
- a separate implementation-activation effective point.

## 6. Planned Kernel Modules

The implementation blueprint must define, without implementing:

1. invocation validation;
2. truth-authority validation;
3. tenant, subject, environment, and release binding;
4. evidence eligibility;
5. evaluation-definition and version selection;
6. deterministic claim evaluation;
7. aggregate outcome construction;
8. limitation and validity construction;
9. canonical fingerprint construction;
10. authoritative result assembly;
11. non-authoritative explanation projection.

Each module must have one bounded responsibility.

## 7. Dependency Direction

The blueprint must define a dependency structure in which:

- authoritative domain semantics do not depend on providers;
- evaluation logic does not depend on presentation;
- explanation cannot mutate authoritative results;
- provider representations cannot become canonical records directly;
- persistence cannot define semantic identity;
- transport cannot define domain validity;
- models cannot select authoritative outcomes;
- enforcement remains outside the kernel.

Circular semantic dependencies are prohibited.

## 8. Contract Mapping

The executable-contract mapping remains conceptual and non-executable.

It must map canonical concepts to future typed representations, including:

- architecture-truth snapshot references;
- architecture claims;
- observations;
- evidence-eligibility decisions;
- evaluation definitions;
- evaluation context;
- claim-level results;
- aggregate results;
- limitations;
- validity windows;
- fingerprints;
- invalid-state failures.

The mapping must preserve required, optional, prohibited, and derived fields
without selecting a programming language or serialization framework.

## 9. Canonicalization Requirements

Planning must define requirements for:

- stable field inclusion;
- explicit null and absence treatment;
- deterministic collection ordering;
- canonical identifier representation;
- canonical timestamp representation;
- canonical version representation;
- duplicate rejection;
- unsupported-value rejection;
- Unicode and text normalization boundaries;
- numeric representation boundaries;
- canonical byte construction;
- algorithm and version identification.

Canonicalization ambiguity must fail closed.

## 10. Fingerprint Requirements

A future fingerprint must bind every material deterministic input, including:

- tenant and subject context;
- environment and release context;
- architecture-truth identity and version;
- evaluated claims;
- eligible evidence and eligibility decisions;
- evaluation definitions and rule versions;
- policy and evaluator versions;
- time and freshness boundaries;
- canonicalization version;
- material limitations.

A fingerprint is evidence of input identity, not execution or deployment
authority.

## 11. Failure and Invalid-State Requirements

Planning must distinguish:

- domain outcomes;
- input-validation failures;
- authority-validation failures;
- tenant or scope failures;
- unsupported-version failures;
- canonicalization failures;
- integrity failures;
- internal processing failures.

Failures cannot be silently converted into `CONFORMANT`, `NON_CONFORMANT`,
`INCONCLUSIVE`, or `STALE`.

## 12. Verification Design

Phase 3 may define future tests but cannot create or execute them.

The verification design must cover:

- deterministic replay;
- canonicalization equivalence;
- order independence where ordering is semantically irrelevant;
- order sensitivity where ordering is material;
- tenant-isolation failures;
- truth-authority failures;
- evidence-eligibility failures;
- contradictory evidence;
- stale evidence;
- missing required evidence;
- unsupported versions;
- fingerprint sensitivity;
- aggregate-outcome precedence;
- explanation non-authority;
- cross-environment reproducibility.

## 13. Security and Supply-Chain Planning

The safety plan must define future requirements for:

- dependency minimization;
- version pinning;
- provenance verification;
- integrity verification;
- software-bill-of-materials generation;
- vulnerability review;
- deterministic build expectations;
- secret exclusion;
- tenant-isolation validation;
- untrusted-input handling;
- resource-boundary enforcement;
- audit evidence;
- rollback and abandonment.

These requirements do not authorize dependencies, builds, or controls.

## 14. Proposed First Implementation Slice

Phase 3 may propose a future minimum implementation slice limited to pure,
side-effect-free deterministic domain behavior.

The proposal must identify:

- exact future source files;
- exact future test files;
- approved contract versions;
- permitted behavior;
- prohibited behavior;
- dependency constraints;
- deterministic acceptance vectors;
- security assertions;
- validation commands;
- rollback or abandonment conditions.

The proposed slice cannot include:

- provider adapters;
- live evidence ingestion;
- NEXUS integration;
- persistence;
- queues or streams;
- network services;
- runtime enforcement;
- certificate issuance;
- deployment;
- production access.

The first implementation slice remains unauthorized until a separate authority
proposal is independently reviewed, merged, and verified.

## 15. Review Workstreams

The complete package requires independent review for:

- architecture consistency;
- Phase 1 semantic preservation;
- Phase 2 kernel-contract preservation;
- deterministic behavior;
- canonicalization and fingerprint completeness;
- security and tenant isolation;
- NEXUS non-duplication;
- ATA authority preservation;
- implementation-authority leakage;
- Phase 4 authority leakage.

## 16. Exit Evidence

Phase 3 planning acceptance requires:

- exact six-file boundary verification;
- content-hash freezing;
- Markdown and whitespace validation;
- cross-document terminology convergence;
- semantic-preservation review;
- deterministic-contract review;
- security and tenant-boundary review;
- first-slice boundary review;
- clean staged-object verification;
- independent pull-request acceptance review;
- explicit merge authorization;
- canonical merge and post-merge verification;
- separately governed closure reconciliation.

## 17. Non-Authorization

Phase 3 does not authorize:

- source code;
- executable schemas;
- tests or fixtures;
- dependencies or build files;
- APIs, services, or command-line interfaces;
- provider collection;
- live evidence ingestion;
- NEXUS, ATA, PAA, or Humanize integration;
- persistence, queues, streams, or replay execution;
- runtime conformance evaluation;
- certificate generation or signing;
- deployment or production access;
- enforcement or remediation;
- Phase 4.

Completing Phase 3 planning does not activate implementation.
