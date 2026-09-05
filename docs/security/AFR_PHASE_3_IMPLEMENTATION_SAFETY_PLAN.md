# AFR Phase 3 Implementation Safety Plan

## 1. Purpose

This document defines the security, trust, supply-chain, resource, validation,
failure-containment, and activation requirements for a possible future first
implementation slice of the AFR deterministic conformance kernel.

It is a planning document only.

It does not authorize source code, executable schemas, tests, fixtures,
dependencies, builds, integrations, persistence, runtime evaluation,
deployment, production access, remediation, Phase 4, or the proposed first
implementation slice.

## 2. Governing Security Position

Any future implementation must preserve:

- NEXUS authority over approved architecture truth;
- observations as non-authoritative operational descriptions;
- explicit evidence-eligibility decisions;
- deterministic and fail-closed evaluation;
- tenant and subject isolation;
- immutable authoritative inputs;
- complete material-input fingerprinting;
- separation of outcomes from processing failures;
- model exclusion from authoritative decisions;
- ATA authority over consequential runtime commits;
- enforcement and remediation outside the AFR kernel.

Security controls cannot create architecture truth or elevate evidence
authority.

## 3. Proposed First-Slice Boundary

Subject to a separate implementation-authority proposal, the proposed first
implementation slice may be limited to exactly:

1. `src/afr/kernel/contracts.py`
2. `src/afr/kernel/canonicalization.py`
3. `src/afr/kernel/fingerprints.py`
4. `tests/unit/kernel/test_canonicalization.py`
5. `tests/unit/kernel/test_fingerprints.py`
6. `tests/vectors/kernel/canonicalization-v1.json`

These paths are planning candidates only.

This document does not create, activate, or authorize them.

Any change to this proposed boundary requires renewed planning review before an
implementation-authority proposal may be accepted.

## 4. Proposed Slice Objective

The future slice would prove only:

- minimal immutable canonical scalar concepts;
- a versioned invocation envelope;
- canonical field inclusion and ordering;
- explicit null and absence handling;
- deterministic timestamp and identifier representation;
- deterministic canonical byte construction;
- domain-separated fingerprint construction;
- sensitivity to every material input;
- rejection of malformed or unsupported inputs;
- repeatability across executions.

It would not perform conformance evaluation.

## 5. Explicitly Excluded Capabilities

The proposed slice excludes:

- architecture-truth import;
- NEXUS integration;
- provider adapters;
- evidence collection;
- live evidence ingestion;
- evidence eligibility;
- rule selection;
- claim evaluation;
- aggregate outcome construction;
- certificate construction or signing;
- databases or object stores;
- queues or streams;
- network APIs;
- command-line execution;
- background workers;
- model calls;
- runtime enforcement;
- deployment;
- production access;
- autonomous remediation.

Excluded capabilities cannot be introduced as helpers, mocks, optional
features, or unused dependencies.

## 6. Core Safety Invariants

A future implementation must preserve these invariants:

1. one invocation is bound to exactly one tenant context;
2. tenant identity is explicit and never ambient;
3. canonicalization never grants authority;
4. fingerprinting never grants authority;
5. malformed input fails before fingerprint production;
6. unsupported versions fail closed;
7. duplicates are rejected where uniqueness is required;
8. canonical output is independent of host locale and timezone;
9. canonical output is independent of unordered container iteration;
10. canonical output contains no secret or ambient process data;
11. identical canonical inputs produce identical bytes and fingerprints;
12. material input changes alter the appropriate fingerprint;
13. no model output influences canonical bytes or fingerprints;
14. no external system is contacted;
15. no persistent state is read or written.

## 7. Tenant-Isolation Requirements

The future invocation envelope must require one resolved tenant identity.

The implementation must reject:

- absent tenant identity;
- empty tenant identity;
- malformed tenant identity;
- conflicting tenant identities;
- tenant identity supplied only through environment state;
- aliases without governed resolution;
- attempts to combine multiple tenant contexts;
- cross-tenant references.

Tests must demonstrate that changing tenant identity changes the canonical
payload and fingerprint.

Diagnostic output must not expose data from another tenant.

## 8. Subject and Scope Requirements

Where present, subject, environment, and release identities must:

- be explicitly represented;
- use canonical identifier rules;
- remain immutable;
- be included in canonicalization;
- be included in fingerprints when material;
- reject conflicting representations;
- never be inferred from filesystem, process, or network context.

The first slice cannot resolve or query missing scope.

## 9. Immutability Requirements

Future authoritative contract values must be immutable after successful
construction.

The implementation must prevent:

- mutation during canonicalization;
- mutation during fingerprinting;
- reference sharing that changes authoritative values;
- nondeterministic lazy evaluation;
- implicit enrichment;
- default insertion after validation;
- replacement of canonical identity.

Tests must verify that input construction and canonical processing do not
mutate caller-owned data.

## 10. Input Validation Requirements

Validation must occur before canonical byte construction.

At minimum, validation must reject:

- missing required fields;
- unknown material contract versions;
- unsupported canonicalization versions;
- malformed identifiers;
- oversized identifiers;
- ambiguous timestamps;
- unsupported timestamp precision;
- invalid enumeration values;
- duplicate canonical-set members;
- prohibited fields;
- unsupported material extensions;
- values outside approved resource boundaries.

Validation failures must be typed and stable.

## 11. Canonicalization Safety Requirements

Canonicalization must define and test:

- exact field inclusion;
- exact field ordering;
- canonical-set ordering;
- canonical-sequence preservation;
- null representation;
- absence representation;
- Boolean representation;
- enumeration representation;
- identifier representation;
- timestamp representation;
- duration representation;
- text encoding and normalization;
- numeric representation;
- binary representation;
- canonical byte encoding;
- contract and canonicalization version markers.

Runtime-library serialization defaults cannot define authoritative canonical
behavior implicitly.

## 12. Fingerprint Safety Requirements

Fingerprint construction must:

- use an explicitly approved digest algorithm;
- use an explicit domain-separation label;
- bind the canonicalization version;
- bind the contract version;
- consume canonical bytes only;
- reject incomplete canonical payloads;
- return a stable lowercase or otherwise explicitly governed digest form;
- avoid secret material;
- avoid nondeterministic salt;
- avoid process-specific or host-specific input.

A digest mismatch must fail validation and cannot be silently recomputed as
trusted evidence.

## 13. Domain-Separation Requirements

Different fingerprint purposes must use distinct governed labels.

A future implementation must not reuse one digest ambiguously as:

- an invocation fingerprint;
- a result fingerprint;
- an integrity signature;
- a certificate signature;
- execution authorization;
- deployment authorization.

A fingerprint is not a signature and is not proof of authority.

## 14. Threat Model

The proposed slice must account for:

- cross-tenant substitution;
- identifier collision attempts;
- ambiguous encoding;
- Unicode-equivalent but byte-distinct text;
- duplicate-key injection;
- duplicate-set-member injection;
- timestamp ambiguity;
- numeric representation ambiguity;
- field-order manipulation;
- collection-order manipulation;
- version downgrade;
- algorithm substitution;
- extension-field smuggling;
- oversized-input denial of service;
- diagnostic data leakage;
- malicious test-vector modification;
- dependency substitution;
- nondeterministic runtime behavior.

## 15. Version-Downgrade Protection

The implementation must reject:

- absent required versions;
- versions outside the supported set;
- silent fallback to an earlier version;
- automatic nearest-version selection;
- unknown material minor-version behavior;
- canonicalization without a version marker;
- digest algorithms without an approved identifier.

Version compatibility must be explicit and deterministic.

## 16. Duplicate and Collision Handling

The implementation must distinguish:

- duplicate fields;
- duplicate canonical-set members;
- repeated sequence members where repetition is allowed;
- identifier collisions;
- canonical representation collisions;
- digest collisions reported through validation evidence.

Duplicate rejection must occur before authoritative fingerprint acceptance.

No collision-handling behavior may elevate authority.

## 17. Resource Limits

A future implementation-authority proposal must assign exact limits for:

- identifier length;
- text length;
- number of fields;
- collection size;
- nesting depth;
- canonical payload size;
- test-vector size;
- processing duration;
- diagnostic detail;
- memory consumption where enforceable.

The first implementation must not claim readiness until numeric limits are
reviewed and frozen.

Exceeding a limit must produce a typed failure.

## 18. Prohibited Side Effects

The first slice must not:

- open network connections;
- invoke subprocesses;
- read secrets;
- read credentials;
- read provider configuration;
- inspect cloud metadata;
- query NEXUS;
- query databases;
- write files during authoritative processing;
- publish events;
- emit certificates;
- mutate external state;
- call models;
- execute remediation;
- trigger deployment.

Tests must detect or structurally exclude prohibited side effects.

## 19. Environment Independence

Authoritative output must not depend on:

- local timezone;
- locale;
- machine hostname;
- username;
- process identifier;
- working directory;
- filesystem ordering;
- environment variables;
- wall-clock time not supplied as canonical input;
- random values;
- memory layout;
- thread scheduling;
- network availability.

Cross-environment test evidence is required before implementation acceptance.

## 20. Dependency Policy

The proposed slice should use only:

- the approved language standard library;
- an approved standard-library cryptographic digest capability;
- the repository's existing approved test framework, when separately
  authorized.

No new third-party runtime dependency is proposed.

Any dependency must have:

- exact identity;
- exact approved version or governed constraint;
- provenance;
- integrity verification;
- license review;
- vulnerability review;
- transitive-dependency review;
- maintenance assessment;
- removal or replacement plan.

## 21. Supply-Chain Requirements

Before future implementation acceptance, evidence must address:

- source provenance;
- reviewed commit identity;
- dependency lock integrity where applicable;
- reproducible or controlled build behavior;
- software bill of materials;
- vulnerability scanning;
- secret scanning;
- static analysis;
- license policy;
- artifact integrity;
- protected review and merge flow.

Phase 3 does not authorize adding supply-chain tooling.

## 22. Secret and Sensitive-Data Requirements

The future slice must not require secrets.

Canonical payloads, fingerprints, failures, and diagnostics must not include:

- credentials;
- tokens;
- private keys;
- raw secret values;
- unnecessary personal data;
- cross-tenant content;
- unrestricted raw evidence;
- environment dumps;
- stack traces containing sensitive values.

Test vectors must contain synthetic, non-sensitive data only.

## 23. Error-Safety Requirements

Failures must:

- use stable typed codes;
- identify the failing stage;
- avoid claiming a domain outcome;
- avoid leaking sensitive values;
- avoid unstable exception text as identity;
- avoid cross-tenant references;
- preserve bounded diagnostic context;
- classify retryability deterministically.

Unexpected internal failures must remain failures and cannot produce
`CONFORMANT`.

## 24. Logging and Diagnostic Boundary

The first slice does not authorize an operational logging integration.

If future diagnostic events are proposed, they must:

- be non-authoritative;
- be bounded;
- omit secrets;
- omit unnecessary canonical payloads;
- retain tenant-safe correlation;
- never become fingerprint inputs unless canonically declared;
- never mutate processing behavior.

Console output must not become a contract.

## 25. Deterministic Validation Evidence

A future implementation must provide evidence that:

- repeated identical inputs produce identical canonical bytes;
- repeated identical inputs produce identical fingerprints;
- reordered canonical-set inputs converge;
- reordered canonical-sequence inputs remain distinguishable where material;
- null and absence follow their declared semantics;
- every material field affects the fingerprint;
- non-material presentation fields do not affect the fingerprint;
- malformed inputs fail consistently;
- unsupported versions fail consistently;
- tenant changes alter fingerprints;
- timezone and locale changes do not alter outputs;
- input objects remain unmodified.

## 26. Negative Test Requirements

Future negative tests must cover:

- missing tenant;
- conflicting tenant;
- malformed identity;
- empty required collection;
- duplicate canonical-set members;
- unsupported contract version;
- unsupported canonicalization version;
- unsupported digest algorithm;
- invalid timestamp;
- excessive input size;
- prohibited extension field;
- ambiguous numeric representation;
- canonical byte mismatch;
- fingerprint mismatch;
- attempted mutable input reuse.

This document does not create or execute those tests.

## 27. Test-Vector Integrity

Future test vectors must have:

- stable vector identities;
- explicit versions;
- documented provenance;
- expected canonical representations;
- expected fingerprints;
- expected failures;
- integrity hashes;
- review ownership;
- change-control requirements.

A changed test vector must not silently redefine canonical behavior.

## 28. Review Separation

A future implementation slice requires independent review of:

- contract fidelity;
- deterministic behavior;
- security invariants;
- tenant isolation;
- resource limits;
- dependency and supply-chain posture;
- negative tests;
- test-vector integrity;
- prohibited side effects;
- authority leakage.

The implementation author cannot unilaterally declare acceptance.

## 29. Proposed Validation Commands

A later implementation-authority proposal must freeze exact commands for:

- formatting;
- linting;
- type checking;
- unit tests;
- deterministic replay;
- test-vector verification;
- dependency inspection;
- vulnerability inspection;
- secret scanning;
- changed-file boundary verification;
- staged-object verification.

These commands are not selected or authorized by this planning document.

## 30. Acceptance Evidence

A future implementation candidate must preserve:

- canonical baseline identity;
- exact branch identity;
- exact source and test boundary;
- exact dependency state;
- exact content hashes;
- test-vector identities;
- deterministic execution results;
- security-validation results;
- clean staged objects;
- independent acceptance review;
- explicit merge authorization;
- post-merge identity, tree, content, and synchronization verification.

Passing tests alone cannot activate implementation authority.

## 31. Rollback Conditions

A future implementation candidate must be abandoned, reverted, or returned for
review if:

- canonical semantics diverge;
- deterministic results cannot be reproduced;
- tenant isolation fails;
- material inputs are omitted from fingerprints;
- unsupported versions are accepted;
- prohibited side effects occur;
- new unreviewed dependencies appear;
- resource limits are absent or ineffective;
- test vectors are ambiguous;
- authority boundaries are weakened;
- the reviewed file boundary changes;
- content identity cannot be established.

## 32. Abandonment Safety

Abandoning the proposed first slice must require no:

- data migration;
- provider rollback;
- NEXUS mutation;
- certificate revocation;
- runtime traffic transition;
- production-state repair.

This is supported by keeping the first slice pure, local, and side-effect-free.

## 33. Implementation-Authority Proposal Requirements

A separate implementation-authority proposal must identify:

- exact implementation objective;
- exact source files;
- exact test and vector files;
- approved language and runtime versions;
- approved dependencies;
- canonical contract versions;
- deterministic behaviors;
- prohibited behaviors;
- numeric resource limits;
- validation commands;
- acceptance evidence;
- rollback and abandonment conditions;
- independent reviewers;
- merge requirements;
- post-merge effective point.

Without that proposal, implementation authority remains `NONE`.

## 34. Activation Effective Point

The proposed first implementation slice may begin if and only if:

1. Phase 3 planning is canonically accepted and closed;
2. the implementation proposal is separately created;
3. its exact file boundary is frozen;
4. all contract and safety mappings converge;
5. numeric resource limits are frozen;
6. dependencies are explicitly approved;
7. deterministic test vectors are frozen;
8. the proposal receives independent architecture, security, and acceptance
   review;
9. every review finding is resolved;
10. explicit merge authorization is granted;
11. the authority proposal is merged to canonical `main`;
12. post-merge identity, parentage, tree, content, and clean synchronization
    verification passes.

Before that effective point:

- Phase 3 implementation authority: `NONE`;
- runtime-evaluation authority: `NONE`;
- integration authority: `NONE`;
- persistence authority: `NONE`;
- deployment authority: `NONE`;
- production authority: `NONE`;
- Phase 4 authority: `NONE`.

## 35. Non-Automatic Transition

Acceptance of the Phase 3 planning package does not activate the proposed
first implementation slice.

Approval, readiness, or merge of the planning package alone does not activate
implementation.

Phase 4 does not activate automatically after Phase 3 planning or future
implementation.

## 36. Non-Authorization

This safety plan creates no authority for:

- the proposed six future files;
- source code;
- executable schemas;
- tests or fixtures;
- dependencies or build changes;
- APIs or services;
- provider adapters;
- live evidence ingestion;
- NEXUS, ATA, PAA, or Humanize integration;
- persistence;
- runtime evaluation;
- certificate generation or signing;
- deployment;
- production access;
- enforcement;
- remediation;
- Phase 4.
