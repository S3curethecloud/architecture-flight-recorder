# AFR Kernel Implementation Blueprint

## 1. Purpose

This document defines the technology-neutral implementation blueprint for the
Architecture Flight Recorder deterministic conformance kernel.

It translates canonical architecture and evaluation semantics into bounded
module responsibilities, dependency rules, conceptual interfaces, state
transitions, failure boundaries, and implementation-readiness requirements.

It is not source code, an executable schema, a test suite, an API, a runtime
service, or implementation authorization.

## 2. Governing Authority

This blueprint is subordinate to:

- AFR product doctrine;
- the AFR system boundary;
- the NEXUS authoritative-truth boundary;
- the AFR canonical information model;
- AFR evaluation semantics;
- Phase 1 trust invariants;
- the deterministic kernel architecture;
- the kernel execution contract;
- the Phase 2 kernel trust boundary.

If this blueprint conflicts with a governing canonical record, the governing
record prevails and the conflict must fail closed.

## 3. Architectural Objective

A future kernel implementation must transform validated, immutable,
tenant-bound inputs into deterministic conformance results without:

- creating architecture truth;
- elevating observation authority;
- bypassing evidence eligibility;
- using model inference to select an outcome;
- mutating provider or NEXUS state;
- granting execution, deployment, or remediation authority;
- hiding failures inside domain outcomes.

The same canonical inputs and semantic versions must produce the same
authoritative result and fingerprint.

## 4. Design Principles

The future kernel must be:

- deterministic;
- fail-closed;
- side-effect-free within its evaluation boundary;
- tenant-bound;
- subject-bound;
- version-explicit;
- time-bound;
- reproducible;
- dependency-minimal;
- auditable;
- provider-neutral;
- transport-neutral;
- persistence-neutral;
- model-independent for authoritative decisions.

## 5. Logical Architecture

The future kernel is divided into four logical layers:

1. canonical domain records;
2. deterministic validation and evaluation;
3. authoritative result construction;
4. non-authoritative projections.

The authoritative dependency direction is:

`canonical records -> validation -> evaluation -> result construction`

Non-authoritative projections may consume completed results but cannot
participate in authoritative outcome selection.

## 6. Module Boundary: Invocation Validation

The invocation-validation module establishes whether a requested evaluation
has a complete and internally coherent invocation identity.

Conceptual inputs include:

- invocation identity;
- tenant identity;
- subject identity;
- environment identity;
- release identity;
- requested claim identities;
- evaluation-definition identity;
- policy version;
- evaluator version;
- canonicalization version;
- evaluation time boundary.

Conceptual output is either:

- a validated immutable invocation context; or
- a typed invocation failure.

This module cannot:

- resolve missing authority through inference;
- substitute default tenant or subject identities;
- retrieve additional data;
- mutate any input;
- produce a conformance outcome.

## 7. Module Boundary: Truth-Authority Validation

The truth-authority module validates that the architecture-truth snapshot is
eligible to act as the approved expectation.

It must validate:

- source authority;
- tenant and subject scope;
- approval state;
- immutability;
- snapshot identity;
- version identity;
- integrity;
- supersession state;
- referenced-claim resolvability;
- supported contract version.

Conceptual output is either:

- validated architecture truth and claims; or
- a typed truth-authority failure.

Syntactic validity alone cannot establish truth authority.

NEXUS remains authoritative for approved architecture truth in
NEXUS-governed systems.

## 8. Module Boundary: Scope Binding

The scope-binding module proves that invocation, truth, claims, observations,
and evaluation context refer to the same authorized boundary.

It must evaluate:

- tenant equality;
- subject equality;
- environment compatibility;
- release compatibility;
- claim applicability;
- time-window compatibility.

Cross-tenant substitution must fail before evidence or claim evaluation.

Unresolved or ambiguous scope cannot produce `CONFORMANT`.

## 9. Module Boundary: Evidence Eligibility

The evidence-eligibility module determines whether an observation may
participate in an evaluation.

Eligibility evaluation must consider:

- source identity;
- collector identity;
- tenant and subject scope;
- provenance;
- integrity;
- observation time;
- collection time;
- freshness;
- normalization history;
- contract version;
- applicability to a claim;
- duplication or supersession;
- contradictions.

Conceptual output is an immutable eligibility decision for every candidate
observation.

An observation cannot become eligible merely because it is present,
well-formed, normalized, aggregated, or model-classified.

## 10. Module Boundary: Evaluation Selection

The evaluation-selection module chooses only explicitly approved,
version-compatible evaluation definitions and deterministic rules.

Selection must be based on canonical identifiers and versions.

It cannot:

- generate rules dynamically;
- accept an unsupported version;
- select rules based on model output;
- infer an unapproved fallback;
- weaken a required condition;
- substitute provider state for architecture truth.

Selection ambiguity must fail closed.

## 11. Module Boundary: Claim Evaluation

The claim-evaluation module evaluates one approved claim against its applicable
eligible evidence and identified deterministic rule.

Each claim evaluation must preserve:

- claim identity;
- truth-snapshot identity;
- applicable evidence identities;
- eligibility-decision identities;
- evaluation-definition identity;
- policy and evaluator versions;
- time and freshness boundaries;
- contradictions;
- limitations;
- derived outcome;
- trace information.

Claim evaluation cannot aggregate unrelated claims or alter an eligibility
decision.

## 12. Canonical Claim Outcomes

The authoritative claim outcomes remain:

- `CONFORMANT`;
- `NON_CONFORMANT`;
- `INCONCLUSIVE`;
- `STALE`.

A future implementation must preserve their canonical meanings.

`CONFORMANT` requires complete eligible support for the evaluated claim and no
unresolved eligible contradiction.

`NON_CONFORMANT` requires eligible evidence demonstrating contradiction or
failure of a required condition.

`INCONCLUSIVE` represents insufficient, ambiguous, conflicting, or unresolved
inputs where neither conformance nor non-conformance is supportable.

`STALE` represents evidence or a prior result that has exceeded its authorized
freshness boundary.

Failures are not additional conformance outcomes.

## 13. Module Boundary: Aggregate Construction

The aggregate-construction module combines completed claim results without
masking weaker material outcomes.

It must preserve:

- every included claim result;
- materiality;
- outcome precedence;
- unresolved limitations;
- excluded or failed claims;
- scope and time boundaries.

Aggregation cannot:

- convert a weaker material result into `CONFORMANT`;
- omit a contradictory material claim;
- treat a processing failure as successful evidence;
- widen evaluated scope;
- infer unevaluated architecture correctness.

## 14. Module Boundary: Result Construction

The result-construction module assembles the authoritative evaluation result.

The result must identify:

- invocation;
- tenant and subject;
- environment and release;
- architecture-truth snapshot;
- evaluated claims;
- evidence and eligibility decisions;
- evaluation definitions;
- policy, evaluator, and canonicalization versions;
- claim-level outcomes;
- aggregate outcome;
- limitations;
- evaluation time;
- validity window;
- fingerprint.

The constructed result must be immutable within the kernel boundary.

## 15. Module Boundary: Canonicalization

The canonicalization module produces the stable representation used for
fingerprinting and reproducibility.

A future implementation must define:

- field inclusion;
- field ordering;
- collection ordering;
- null and absence handling;
- duplicate handling;
- identifier representation;
- enumeration representation;
- timestamp representation;
- text normalization;
- numeric representation;
- binary representation;
- version markers;
- canonical byte encoding.

Canonicalization must not depend on:

- map iteration order;
- locale;
- host timezone;
- operating system;
- process identity;
- memory address;
- nondeterministic serialization;
- external network state;
- model output.

Canonicalization uncertainty must fail closed.

## 16. Module Boundary: Fingerprint Construction

The fingerprint module binds the canonical representation of every material
deterministic input and result field.

The fingerprint envelope must identify:

- fingerprint version;
- canonicalization version;
- digest algorithm;
- domain-separation label;
- canonical payload digest;
- result digest where separately required.

Fingerprint construction cannot establish truth authority, evidence
eligibility, execution authority, or certificate validity.

## 17. Module Boundary: Explanation Projection

Explanation is a non-authoritative projection of an already completed
authoritative result.

It may present:

- evaluated claims;
- supporting evidence references;
- contradictions;
- limitations;
- outcome reasons;
- remediation suggestions clearly marked as proposals.

It cannot:

- change an outcome;
- change a fingerprint;
- suppress a limitation;
- add eligible evidence;
- rewrite architecture truth;
- grant execution authority;
- issue remediation commands.

Failure to create an explanation cannot invalidate or mutate the authoritative
result.

## 18. Conceptual Interface Discipline

Every future module interface must define:

- accepted input type;
- returned output type;
- typed failures;
- required invariants;
- prohibited side effects;
- deterministic ordering;
- supported versions;
- ownership of validation;
- audit-relevant trace information.

Interfaces must not rely on undocumented dictionaries, implicit defaults,
ambient tenant context, global mutable state, or exception text as a stable
contract.

## 19. Immutability Boundary

Authoritative inputs must be immutable before entering claim evaluation.

Each stage must consume the output of the preceding validated stage.

A later stage cannot:

- mutate an earlier stage output;
- replace a canonical identity;
- reclassify evidence eligibility;
- weaken an authority decision;
- alter the invocation boundary;
- silently discard a contradiction.

Any detected mutation or identity mismatch must fail closed.

## 20. Dependency Rules

Allowed dependency direction:

1. canonical value concepts;
2. canonical domain records;
3. validation contracts;
4. deterministic evaluation rules;
5. aggregation;
6. canonicalization and fingerprinting;
7. result assembly;
8. non-authoritative presentation.

Prohibited dependencies include:

- domain records depending on providers;
- domain semantics depending on persistence;
- evaluation depending on presentation;
- authoritative outcomes depending on models;
- canonicalization depending on transport formatting;
- truth validation depending on observed provider state;
- kernel modules invoking remediation or enforcement;
- kernel modules mutating NEXUS or provider systems.

## 21. Side-Effect Boundary

The deterministic kernel must be conceptually pure.

During one evaluation it must not:

- perform network access;
- read environment-dependent configuration implicitly;
- query databases;
- write persistence;
- publish events;
- call providers;
- call NEXUS;
- call models;
- issue certificates;
- execute tools;
- trigger deployment;
- execute remediation.

External systems may prepare inputs or consume completed results only through
separately governed boundaries.

## 22. Failure Model

The future implementation must distinguish at least:

- `INVOCATION_INVALID`;
- `TRUTH_AUTHORITY_INVALID`;
- `SCOPE_BINDING_INVALID`;
- `EVIDENCE_ELIGIBILITY_INVALID`;
- `EVALUATION_DEFINITION_UNSUPPORTED`;
- `POLICY_VERSION_UNSUPPORTED`;
- `EVALUATOR_VERSION_UNSUPPORTED`;
- `CANONICALIZATION_FAILED`;
- `INTEGRITY_VALIDATION_FAILED`;
- `DETERMINISM_VIOLATION`;
- `INTERNAL_PROCESSING_FAILED`.

Failure records must include stable codes and bounded diagnostic context.

They must not include secrets, cross-tenant data, unstable exception text as
identity, or fabricated conformance outcomes.

## 23. Determinism Requirements

A future implementation must demonstrate:

- identical canonical inputs produce identical results;
- identical canonical inputs produce identical fingerprints;
- irrelevant input ordering does not affect results;
- materially relevant ordering remains preserved;
- host timezone does not affect results;
- locale does not affect results;
- repeated execution does not depend on process state;
- unsupported versions fail consistently;
- error classification is stable;
- explanation generation cannot affect authority.

## 24. Resource Boundaries

Implementation planning must define bounded limits for:

- claim count;
- observation count;
- evidence size;
- identifier length;
- text length;
- nesting depth;
- collection size;
- evaluation duration;
- canonical payload size;
- diagnostic detail.

Exceeding an authorized limit must produce a typed failure and cannot produce
`CONFORMANT`.

## 25. Audit Boundary

A future kernel result must expose sufficient trace information to reproduce:

- validation decisions;
- eligibility decisions;
- rule selection;
- claim outcomes;
- aggregate construction;
- canonicalization;
- fingerprinting;
- limitations.

Audit information cannot become an alternate mutable source of truth.

## 26. Proposed First Implementation Slice

The recommended future first implementation slice is limited to deterministic
canonicalization and fingerprint construction over a minimal, explicitly
versioned invocation envelope.

The slice should prove:

- stable canonical field inclusion;
- deterministic ordering;
- explicit null and absence handling;
- stable timestamp and identifier representation;
- domain-separated fingerprint construction;
- repeatability across executions;
- sensitivity to every material input;
- rejection of unsupported versions;
- rejection of duplicates and malformed values;
- absence of network, persistence, provider, model, and runtime side effects.

The slice must not implement:

- NEXUS ingestion;
- provider collection;
- evidence eligibility;
- claim evaluation;
- aggregate outcomes;
- runtime services;
- persistence;
- certificate issuance;
- enforcement;
- remediation;
- deployment.

### Proposed Future File Boundary

Subject to a separate implementation-authority proposal, the proposed first
implementation slice may be limited to exactly:

1. `src/afr/kernel/contracts.py`
2. `src/afr/kernel/canonicalization.py`
3. `src/afr/kernel/fingerprints.py`
4. `tests/unit/kernel/test_canonicalization.py`
5. `tests/unit/kernel/test_fingerprints.py`
6. `tests/vectors/kernel/canonicalization-v1.json`

These paths are planning candidates only. They are not created, activated, or
authorized by this blueprint.

The exact future source and test files must converge across the Phase 3
blueprint, contract mapping, safety plan, and any later
implementation-authority proposal.

This blueprint does not activate the proposed slice.

## 27. Future Implementation Layers

A later implementation may be decomposed into:

### Layer A: Canonical primitives

Stable identifiers, versions, timestamps, enumerations, immutable collections,
and bounded scalar values.

### Layer B: Canonical records

Invocation, truth references, claims, observations, eligibility decisions,
evaluation contexts, results, limitations, and failures.

### Layer C: Deterministic kernel

Validation, selection, claim evaluation, aggregation, canonicalization,
fingerprinting, and result construction.

### Layer D: Boundary adapters

Future provider, NEXUS, persistence, transport, certificate, and presentation
adapters.

Layer D remains outside the kernel and is not authorized by Phase 3.

## 28. Implementation-Readiness Evidence

A future implementation-authority proposal must identify:

- exact source and test file boundaries;
- exact contract versions;
- approved language and runtime;
- dependency policy;
- canonical test vectors;
- deterministic acceptance commands;
- security assertions;
- prohibited side effects;
- rollback or abandonment conditions;
- reviewed content hashes;
- an explicit activation effective point.

No implementation may begin without that separate authority.

## 29. Non-Authorization

This blueprint creates no authority for:

- source code;
- executable schemas;
- tests or fixtures;
- build files or dependencies;
- APIs or services;
- provider adapters;
- live evidence collection;
- NEXUS integration;
- persistence;
- runtime evaluation;
- certificate issuance;
- deployment;
- production access;
- enforcement;
- remediation;
- Phase 4.
