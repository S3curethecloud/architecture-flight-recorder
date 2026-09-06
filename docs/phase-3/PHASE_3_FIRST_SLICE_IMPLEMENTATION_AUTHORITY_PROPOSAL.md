# Phase 3 First-Slice Implementation-Authority Proposal

## 1. Purpose

This document proposes narrowly bounded implementation authority for the first
Architecture Flight Recorder deterministic-kernel implementation slice.

It is an authority proposal only. It creates no implementation authority before
canonical merge and successful post-merge verification.

It does not reopen Phase 3 planning and does not activate Phase 4.

## 2. Canonical Foundation

This proposal depends on the canonical Phase 3 implementation-readiness
planning package and closure:

- Phase 3 planning-package commit:
  `7bd9b3b387606765202a8ba8a7c0fe22c5759e2d`;
- Phase 3 planning-package merge:
  `45512c2d4ea2c6d6fd46f33ac312f6624513cdb9`;
- Phase 3 closure commit:
  `114649be4943c6be0ea667abb9c45cd2b4c0357b`;
- Phase 3 closure merge:
  `d349d9893b4f528a9ef79c8bab7d3dc0e6f7f7f3`;
- Phase 3 closure tree:
  `93cceff24ce081003e1a0c77039fa01041af366a`;
- Phase 3 status: `COMPLETE`;
- Phase 3 planning authority: `CONSUMED_CLOSED`.

The recorded closure-merge title anomaly is non-substantive metadata and does
not alter the reviewed closure tree or content.

## 3. Current Authority

Until this proposal reaches its effective point:

- proposal status: `DRAFT_REVIEW_CANDIDATE`;
- Phase 3 implementation authority: `NONE`;
- runtime-evaluation authority: `NONE`;
- provider-integration authority: `NONE`;
- NEXUS-integration authority: `NONE`;
- persistence authority: `NONE`;
- deployment authority: `NONE`;
- production authority: `NONE`;
- Phase 4 authority: `NONE`.

## 4. Proposed Authority

The proposed authority is:

`BOUNDED_PHASE_3_FIRST_SLICE_IMPLEMENTATION_ONLY`

It would authorize only the exact implementation and deterministic validation
work defined in this proposal.

It would not authorize expansion by implication.

## 5. Exact Future File Boundary

The complete proposed implementation boundary is exactly:

1. `src/afr/kernel/contracts.py`
2. `src/afr/kernel/canonicalization.py`
3. `src/afr/kernel/fingerprints.py`
4. `tests/unit/kernel/test_canonicalization.py`
5. `tests/unit/kernel/test_fingerprints.py`
6. `tests/vectors/kernel/canonicalization-v1.json`

No seventh file is authorized.

Renaming, relocating, generating, or adding another source, test,
configuration, dependency, schema, fixture, cache, or metadata file requires
separate authority.

## 6. Permitted Implementation Scope

If activated, the authority would permit:

- immutable or equivalently mutation-resistant typed value representations
  required by the first slice;
- deterministic validation of first-slice contract fields;
- pure canonical representation construction;
- deterministic ordering and normalization defined by canonical planning;
- deterministic fingerprint-input construction;
- version-bound fingerprint calculation using only an already available
  approved standard-library capability;
- unit tests for canonicalization and fingerprint behavior;
- deterministic positive, negative, equivalence, and fail-closed vectors;
- validation that identical valid inputs produce identical canonical bytes and
  fingerprints.

All permitted behavior must remain pure, deterministic, tenant-bound where
applicable, and side-effect-free.

## 7. Required Contract Properties

Future typed representations must preserve:

- architecture truth as an external authoritative reference;
- observations as distinct from architecture truth;
- evidence eligibility as an explicit prior decision;
- tenant, subject, environment, release, and time boundaries;
- stable identifiers and explicit semantic versions;
- provenance and integrity concepts;
- absence, null, duplicate, ordering, and unsupported-version distinctions;
- processing failures as distinct from conformance outcomes;
- model output exclusion from authoritative decisions;
- ATA consequential runtime commit authority.

The first slice may represent these concepts but may not perform live
conformance evaluation.

## 8. Canonicalization Requirements

Canonicalization must:

- be deterministic for identical valid inputs and semantic versions;
- use explicit field inclusion and exclusion;
- preserve the distinction between absence and explicit null where canonical
  planning requires it;
- reject prohibited, ambiguous, duplicate, or unsupported representations;
- use deterministic collection ordering;
- define text, identifier, timestamp, numeric, and byte boundaries;
- fail closed rather than repair untrusted input silently;
- avoid locale, platform, process, clock, randomness, environment, or network
  dependence;
- produce canonical bytes without external side effects.

## 9. Fingerprint Requirements

Fingerprint construction must:

- bind every material first-slice deterministic input;
- bind the canonicalization version and fingerprint algorithm identifier;
- consume canonical bytes rather than noncanonical source representations;
- produce identical fingerprints for identical canonical inputs;
- distinguish materially different canonical inputs;
- reject unsupported algorithms and versions;
- never represent a fingerprint as approval, execution authority, conformance,
  or runtime permission.

## 10. Deterministic Test Requirements

The authorized tests and vector file must cover:

- canonicalization equivalence;
- deterministic collection ordering;
- absence versus explicit null;
- duplicate and prohibited-field rejection;
- unsupported-version rejection;
- tenant and subject substitution rejection;
- deterministic fingerprint reproduction;
- material-input fingerprint divergence;
- malformed-vector failure;
- processing failures remaining distinct from conformance outcomes;
- no clock, randomness, environment, filesystem, network, or provider
  dependence.

Tests may exercise only the three proposed source files.

## 11. Security and Supply-Chain Constraints

The slice must:

- add no dependency;
- use no unpinned tool or package;
- access no secret, credential, token, or production configuration;
- make no network request;
- perform no filesystem write during kernel processing;
- open no database or persistence connection;
- invoke no subprocess or shell;
- deserialize no executable object format;
- dynamically import no provider-controlled module;
- load no plugin or remote code;
- emit no sensitive canonical payload to logs;
- preserve tenant isolation and fail-closed validation.

Resource limits are mandatory. Before fingerprint production, the
implementation must deterministically reject any input exceeding explicitly
versioned bounds for:

- total input byte size;
- collection cardinality and nesting depth;
- canonical serialized byte size;
- deterministic processing work units.

A wall-clock timeout may provide an external safety stop, but elapsed time
cannot select, modify, or legitimize a canonical result. Exceeding any resource
limit must produce an explicit processing failure before fingerprint
production. The implementation may not truncate, sample, omit, or silently
repair input to remain within a limit.

Any required dependency or build-system mutation invalidates this authority and
requires a new proposal.

## 12. Prohibited Scope

This proposal does not authorize:

- provider adapters or provider collection;
- live evidence ingestion;
- NEXUS export or integration;
- ATA integration or runtime commit;
- conformance evaluation execution;
- aggregate outcome production;
- certificate signing or issuance;
- persistence, caching, queues, or databases;
- APIs, services, workers, schedulers, or command-line interfaces;
- telemetry export or external logging;
- policy enforcement or release blocking;
- remediation or infrastructure mutation;
- deployment or production access;
- Phase 4 planning or implementation.

## 13. NEXUS and ATA Boundaries

NEXUS remains authoritative for approved architecture truth.

The proposed slice may define a typed reference to architecture truth but
cannot discover, approve, reinterpret, mutate, or export NEXUS state.

ATA retains consequential runtime commit authority.

No canonicalized record, fingerprint, test result, or future AFR object may
grant runtime execution, deployment, enforcement, or remediation authority.

## 14. Failure and Stop Conditions

Implementation must stop without broadening scope if:

- any proposed file outside the six-file boundary becomes necessary;
- any dependency or build configuration change becomes necessary;
- canonical planning contains an unresolved ambiguity;
- deterministic behavior cannot be demonstrated;
- an unsupported version would otherwise be accepted;
- tenant or subject boundaries cannot be preserved;
- a test requires network, provider, persistence, or runtime integration;
- an implementation behavior conflicts with canonical Phase 1, Phase 2, or
  Phase 3 planning;
- a review finding invalidates the frozen implementation candidate.

Stopping does not authorize an alternative implementation.

## 15. Required Review

This proposal requires independent:

- architecture review;
- canonical-semantic preservation review;
- deterministic canonicalization review;
- fingerprint-construction review;
- typed-contract review;
- test-design review;
- security and tenant-isolation review;
- dependency and supply-chain review;
- NEXUS non-duplication review;
- ATA authority-boundary review;
- implementation-boundary review;
- authority-leakage review.

All findings must be resolved before activation.

## 16. Activation Effective Point

Before the effective point:

- `AFR_PHASE_3_STATUS = COMPLETE`
- `AFR_PHASE_3_PLANNING_AUTHORITY = CONSUMED_CLOSED`
- `AFR_PHASE_3_IMPLEMENTATION_AUTHORITY_PROPOSAL =
  DRAFT_REVIEW_CANDIDATE`
- `AFR_PHASE_3_IMPLEMENTATION_AUTHORITY = NONE`
- `AFR_PHASE_4_AUTHORITY = NONE`

The proposed authority activates if and only if:

1. the proposal change remains limited to `docs/SOT.md` and
   `docs/phase-3/PHASE_3_FIRST_SLICE_IMPLEMENTATION_AUTHORITY_PROPOSAL.md`;
2. the proposal preserves the exact six-file future implementation boundary;
3. the proposal is independently reviewed across every required dimension;
4. all proposal-review findings are resolved;
5. the reviewed proposal is staged and committed exactly;
6. its branch and draft pull request are verified against the reviewed
   identity and content;
7. the pull request receives independent acceptance review;
8. explicit merge authorization is granted;
9. the reviewed proposal is merged to canonical `main`;
10. post-merge identity, parentage, tree, exact two-file proposal boundary, and
    content verification pass;
11. local and remote canonical `main` converge on the verified merge;
12. the local canonical checkout is clean.

Opening, reviewing, approving, or marking the proposal pull request ready does
not satisfy this effective point.

## 17. State After Activation

After and only after the effective point:

- `AFR_PHASE_3_STATUS = COMPLETE`
- `AFR_PHASE_3_PLANNING_AUTHORITY = CONSUMED_CLOSED`
- `AFR_PHASE_3_IMPLEMENTATION_AUTHORITY =
  BOUNDED_PHASE_3_FIRST_SLICE_IMPLEMENTATION_ONLY`
- `AFR_PHASE_3_RUNTIME_EVALUATION_AUTHORITY = NONE`
- `AFR_PHASE_3_PROVIDER_INTEGRATION_AUTHORITY = NONE`
- `AFR_PHASE_3_NEXUS_INTEGRATION_AUTHORITY = NONE`
- `AFR_PHASE_3_PERSISTENCE_AUTHORITY = NONE`
- `AFR_PHASE_3_DEPLOYMENT_AUTHORITY = NONE`
- `AFR_PHASE_4_AUTHORITY = NONE`

Activation would authorize only a separately created implementation branch
from the verified activation merge and only the six named implementation
files.

It would not itself create, validate, accept, merge, deploy, or execute the
implementation.

## 18. Post-Merge Implementation Closure Reconciliation

The exact six-file implementation authorized by this proposal was independently
reviewed, committed, pushed, reviewed through PR #13, explicitly authorized for
merge, merged, and verified against canonical `main`.

Canonical implementation evidence:

- activation baseline:
  `9f2da0bec9a67551f20c83546dffd0da764732eb`;
- reviewed implementation commit:
  `f821d1a6d91113c1bbcecd780ad348064105b312`;
- reviewed implementation tree:
  `5ba6638f8df57671e738df686e7978352ab1b7df`;
- canonical merge:
  `d29b426d2709cc4e8c51a875d87d5386219a9e3b`;
- canonical merge tree:
  `5ba6638f8df57671e738df686e7978352ab1b7df`;
- canonical merge parents:
  `9f2da0bec9a67551f20c83546dffd0da764732eb`
  and `f821d1a6d91113c1bbcecd780ad348064105b312`;
- pull request: `#13`;
- exact changed-file count: `6`;
- canonical test reproduction: `32 PASS`;
- canonical acceptance:
  `AFR_PHASE_3_FIRST_SLICE_CANONICAL_ACCEPTANCE = PASS`.

Canonical file hashes:

1. `e3af3ce22ae6fa2afc198e027ae1b15c380e27a858c2d44aa9719796a9b19b20`
   — `src/afr/kernel/contracts.py`
2. `4e665d03f65be659b489fb27fd09dad84b1f581cf77bd05f6878af66be5cb449`
   — `src/afr/kernel/canonicalization.py`
3. `61116106e93930f4c2ce94e8f6eb83cbca517dcc5a54aaa8f201c10b4b91f547`
   — `src/afr/kernel/fingerprints.py`
4. `a24fff80a3ab466511a68409414ec686dc9e8a43138925927d54d2c6b6564e3a`
   — `tests/unit/kernel/test_canonicalization.py`
5. `b477bac4a9562445de8a04f1a267f9e9a26fdc052705824a6eaf0c5c6d5b4fec`
   — `tests/unit/kernel/test_fingerprints.py`
6. `2b9d9b3ab0486757e720ddc3c60533bd9a1eda055e5718c29c69c7928ce539f8`
   — `tests/vectors/kernel/canonicalization-v1.json`

The activated authority has been fully exercised within the exact six-file
boundary and is pending terminal closure.

### Closure Effective Point

Before the closure effective point:

- `AFR_PHASE_3_STATUS = COMPLETE`
- `AFR_PHASE_3_FIRST_SLICE_IMPLEMENTATION_STATUS =
  CANONICALLY_ACCEPTED`
- `AFR_PHASE_3_PLANNING_AUTHORITY = CONSUMED_CLOSED`
- `AFR_PHASE_3_IMPLEMENTATION_AUTHORITY =
  CONSUMED_PENDING_CLOSURE`
- `AFR_PHASE_3_RUNTIME_EVALUATION_AUTHORITY = NONE`
- `AFR_PHASE_3_PROVIDER_INTEGRATION_AUTHORITY = NONE`
- `AFR_PHASE_3_NEXUS_INTEGRATION_AUTHORITY = NONE`
- `AFR_PHASE_3_PERSISTENCE_AUTHORITY = NONE`
- `AFR_PHASE_3_DEPLOYMENT_AUTHORITY = NONE`
- `AFR_PHASE_4_AUTHORITY = NONE`

Closure becomes effective if and only if:

1. the closure reconciliation remains limited to `docs/SOT.md` and this
   document;
2. both closure documents are frozen and independently reviewed;
3. all closure-review findings are resolved;
4. the exact reviewed candidate is staged, committed, and pushed;
5. the closure pull request preserves the reviewed commit, tree, exact
   two-file boundary, and both content hashes;
6. the pull request receives independent acceptance review;
7. the pull request is explicitly transitioned from draft to ready;
8. explicit closure merge authorization is granted;
9. the reviewed closure candidate is merged to canonical `main`;
10. post-merge identity, both parents, tree, exact file boundary, and content
    verification pass;
11. local and remote canonical `main` converge cleanly;
12. the canonical worktree and index are clean.

A draft pull request, review, approval, readiness transition, or merge without
successful post-merge verification does not satisfy this effective point.

After and only after the closure effective point:

- `AFR_PHASE_3_STATUS = COMPLETE`
- `AFR_PHASE_3_FIRST_SLICE_IMPLEMENTATION_STATUS = COMPLETE`
- `AFR_PHASE_3_PLANNING_AUTHORITY = CONSUMED_CLOSED`
- `AFR_PHASE_3_IMPLEMENTATION_AUTHORITY = CONSUMED_CLOSED`
- `AFR_PHASE_3_RUNTIME_EVALUATION_AUTHORITY = NONE`
- `AFR_PHASE_3_PROVIDER_INTEGRATION_AUTHORITY = NONE`
- `AFR_PHASE_3_NEXUS_INTEGRATION_AUTHORITY = NONE`
- `AFR_PHASE_3_PERSISTENCE_AUTHORITY = NONE`
- `AFR_PHASE_3_DEPLOYMENT_AUTHORITY = NONE`
- `AFR_PHASE_4_AUTHORITY = NONE`

This closure cannot authorize another implementation slice, runtime evaluation,
provider or NEXUS integration, ATA runtime action, persistence, deployment,
production use, enforcement, remediation, or Phase 4.
