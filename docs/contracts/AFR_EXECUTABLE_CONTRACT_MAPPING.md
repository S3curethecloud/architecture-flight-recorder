# AFR Executable Contract Mapping

## 1. Purpose

This document maps canonical AFR information concepts and deterministic kernel
semantics into requirements for future typed implementation contracts.

Despite its title, this is a non-executable planning document.

It is not a schema, source file, generated model, API specification, test
fixture, serialization definition, package, or implementation authorization.

## 2. Governing Sources

Every future typed contract must preserve:

- AFR product doctrine;
- the NEXUS authoritative-truth boundary;
- the canonical AFR information model;
- AFR evaluation semantics;
- Phase 1 trust invariants;
- the deterministic kernel architecture;
- the kernel execution contract;
- the Phase 2 kernel trust boundary;
- the Phase 3 kernel implementation blueprint.

A mapping conflict with a governing source must fail closed.

## 3. Mapping Vocabulary

Field obligations use these normative planning terms:

- `REQUIRED`: the field must be supplied and validated;
- `OPTIONAL`: the field may be absent without changing authoritative meaning;
- `CONDITIONAL`: the field is required when its stated condition applies;
- `DERIVED`: the field is calculated deterministically from canonical inputs;
- `FORBIDDEN`: the field must not appear in the authoritative contract;
- `REFERENCE`: the field identifies an external immutable object;
- `CANONICAL_SET`: an unordered semantic set with canonical ordering rules;
- `CANONICAL_SEQUENCE`: an order-sensitive sequence;
- `OPAQUE_IDENTIFIER`: an identifier whose internal syntax conveys no
  authority.

These terms do not define executable validation syntax.

## 4. Universal Contract Envelope

Every future authoritative kernel record must include or inherit:

| Concept | Obligation | Constraint |
|---|---|---|
| Contract kind | `REQUIRED` | Stable registered identifier |
| Contract version | `REQUIRED` | Explicitly supported version |
| Tenant identity | `REQUIRED` | Exactly one resolved tenant |
| Record identity | `REQUIRED` | Stable opaque identifier |
| Record version | `REQUIRED` | Immutable version identity |
| Created time | `REQUIRED` | Canonical trusted-time representation |
| Source identity | `CONDITIONAL` | Required for externally sourced records |
| Integrity metadata | `CONDITIONAL` | Required where authority depends on integrity |
| Extensions | `OPTIONAL` | Namespaced and non-authoritative |
| Ambient authority | `FORBIDDEN` | Never inferred from process context |

Unknown fields cannot silently alter authoritative semantics.

## 5. Canonical Scalar Requirements

Future typed representations must distinguish:

- opaque identifiers;
- tenant identifiers;
- subject identifiers;
- environment identifiers;
- release identifiers;
- contract versions;
- policy versions;
- evaluator versions;
- canonicalization versions;
- timestamps;
- durations;
- digest algorithms;
- digest values;
- bounded text;
- enumerations.

Scalar parsing must not infer authority, tenancy, approval, or eligibility.

## 6. Identifier Mapping

An identifier representation must:

- preserve exact identity;
- be non-empty;
- have an explicit maximum length;
- exclude surrounding whitespace;
- use one canonical text encoding;
- avoid case folding unless the governing contract declares it;
- avoid semantic interpretation of prefixes;
- reject malformed or unsupported namespaces;
- remain stable across serialization and runtime environments.

Identifier aliases cannot substitute for canonical identity without an explicit
governed resolution record.

## 7. Version Mapping

Every material semantic contract must expose its version explicitly.

Version handling must distinguish:

- supported version;
- unsupported version;
- malformed version;
- absent required version;
- deprecated but still supported version;
- superseded version.

A future implementation cannot select the nearest version, silently downgrade,
or apply an unapproved default.

## 8. Time Mapping

Canonical time representations must:

- identify an absolute instant;
- use an approved precision;
- use an approved timezone normalization;
- reject ambiguous local time;
- reject unsupported leap or calendar behavior;
- distinguish observed time from collection time;
- distinguish evaluation time from validity boundaries;
- preserve freshness inputs.

Host-local time and locale cannot affect authoritative evaluation.

## 9. Invocation Contract Mapping

The future invocation contract maps:

| Field | Obligation | Validation owner |
|---|---|---|
| Invocation identity | `REQUIRED` | Invocation validation |
| Tenant identity | `REQUIRED` | Invocation and scope validation |
| Subject identity | `REQUIRED` | Invocation and scope validation |
| Environment identity | `REQUIRED` | Scope validation |
| Release identity | `REQUIRED` | Scope validation |
| Truth-snapshot reference | `REQUIRED` | Truth-authority validation |
| Claim identities | `CANONICAL_SET` | Invocation validation |
| Evidence references | `CANONICAL_SET` | Evidence eligibility |
| Evaluation-definition reference | `REQUIRED` | Evaluation selection |
| Policy version | `REQUIRED` | Evaluation selection |
| Evaluator version | `REQUIRED` | Evaluation selection |
| Canonicalization version | `REQUIRED` | Canonicalization |
| Evaluation time | `REQUIRED` | Trusted-time validation |
| Presentation request | `FORBIDDEN` | Outside authoritative invocation |

The invocation identity binds one immutable evaluation attempt.

## 10. Architecture-Truth Reference Mapping

The future truth reference must identify:

- authority identity;
- tenant identity;
- engagement or governing-context identity where applicable;
- subject and system scope;
- snapshot identity;
- snapshot version;
- approval state;
- approval identity;
- approval time;
- supersession state;
- integrity fingerprint;
- compatibility version;
- referenced claim identities;
- explicit limitations.

The reference cannot contain a locally inferred approval state.

NEXUS remains authoritative for NEXUS-governed architecture truth.

## 11. Architecture Claim Mapping

The future claim representation must identify:

| Field | Obligation |
|---|---|
| Claim identity | `REQUIRED` |
| Claim version | `REQUIRED` |
| Truth-snapshot identity | `REFERENCE` |
| Tenant identity | `REQUIRED` |
| Subject scope | `REQUIRED` |
| Environment scope | `CONDITIONAL` |
| Release scope | `CONDITIONAL` |
| Claim kind | `REQUIRED` |
| Expected condition | `REQUIRED` |
| Materiality | `REQUIRED` |
| Evaluation-definition reference | `REQUIRED` |
| Evidence requirements | `CANONICAL_SET` |
| Freshness requirements | `REQUIRED` |
| Limitations | `CANONICAL_SET` |

A claim cannot be created, approved, or semantically completed by AFR.

## 12. Observation Mapping

The future observation representation must preserve:

- observation identity;
- observation version;
- tenant and subject scope;
- source identity;
- collector identity;
- observed time;
- collection time;
- raw integrity reference;
- normalization history;
- observed resource identity;
- observed property;
- observed value;
- provider version where material;
- declared limitations.

An observation is not eligible evidence merely because it is validly typed.

## 13. Evidence-Eligibility Decision Mapping

The eligibility decision must map:

| Field | Obligation |
|---|---|
| Decision identity | `REQUIRED` |
| Invocation identity | `REFERENCE` |
| Observation identity | `REFERENCE` |
| Claim identity | `REFERENCE` |
| Eligibility status | `REQUIRED` |
| Eligibility-reason codes | `CANONICAL_SET` |
| Source validation | `REQUIRED` |
| Collector validation | `REQUIRED` |
| Tenant validation | `REQUIRED` |
| Subject validation | `REQUIRED` |
| Integrity validation | `REQUIRED` |
| Freshness validation | `REQUIRED` |
| Applicability validation | `REQUIRED` |
| Contradiction classification | `CONDITIONAL` |
| Decision version | `REQUIRED` |

Eligibility status must distinguish at least:

- `ELIGIBLE`;
- `INELIGIBLE`;
- `UNRESOLVED`.

Normalization or model classification cannot elevate eligibility.

## 14. Evaluation-Definition Mapping

The future evaluation-definition reference must identify:

- evaluation-definition identity;
- version;
- applicable claim kind;
- required evidence classes;
- deterministic rule identity;
- rule version;
- contradiction behavior;
- missing-evidence behavior;
- freshness requirements;
- outcome derivation version;
- aggregation relevance;
- supported contract versions.

Rules cannot be generated or amended during an invocation.

## 15. Evaluation Context Mapping

The evaluation context must bind:

- invocation identity;
- tenant and subject;
- environment and release;
- truth snapshot;
- claims;
- observations;
- eligibility decisions;
- evaluation definitions;
- policy version;
- evaluator version;
- canonicalization version;
- evaluation time;
- validity boundaries.

Every material context component must participate in fingerprint construction.

## 16. Claim Result Mapping

A future claim result must include:

| Field | Obligation |
|---|---|
| Result identity | `DERIVED` |
| Invocation identity | `REFERENCE` |
| Claim identity | `REFERENCE` |
| Outcome | `REQUIRED` |
| Supporting evidence | `CANONICAL_SET` |
| Contradictory evidence | `CANONICAL_SET` |
| Excluded evidence | `CANONICAL_SET` |
| Evaluation-definition identity | `REFERENCE` |
| Rule version | `REQUIRED` |
| Reason codes | `CANONICAL_SET` |
| Limitations | `CANONICAL_SET` |
| Validity boundary | `REQUIRED` |
| Trace references | `CANONICAL_SET` |

The outcome is limited to:

- `CONFORMANT`;
- `NON_CONFORMANT`;
- `INCONCLUSIVE`;
- `STALE`.

Processing failures cannot occupy the outcome field.

## 17. Aggregate Result Mapping

The aggregate result must identify:

- invocation identity;
- included claim-result identities;
- excluded or failed claim identities;
- aggregate outcome;
- precedence version;
- material limitations;
- scope;
- evaluation time;
- validity boundary;
- fingerprint.

The aggregate cannot omit a weaker material claim result to produce a stronger
outcome.

## 18. Limitation Mapping

Limitations must be first-class typed concepts.

A limitation must include:

- stable reason code;
- affected scope;
- affected claim or result references;
- materiality;
- time boundary where applicable;
- human-readable non-authoritative detail.

Free-form text alone cannot define authoritative limitation identity.

## 19. Failure Mapping

Failures remain distinct from domain outcomes.

The future failure envelope must include:

| Field | Obligation |
|---|---|
| Failure code | `REQUIRED` |
| Failure category | `REQUIRED` |
| Invocation identity | `CONDITIONAL` |
| Stage identity | `REQUIRED` |
| Bounded affected references | `CANONICAL_SET` |
| Diagnostic code | `CONDITIONAL` |
| Retry classification | `REQUIRED` |
| Safe public detail | `OPTIONAL` |
| Internal exception text | `FORBIDDEN` as stable identity |
| Conformance outcome | `FORBIDDEN` |

Required failure categories include:

- invocation;
- truth authority;
- scope binding;
- evidence eligibility;
- unsupported version;
- canonicalization;
- integrity;
- determinism;
- resource boundary;
- internal processing.

## 20. Canonicalization Mapping

The future canonicalization contract must define:

- included contract kinds and versions;
- canonical field names;
- canonical field ordering;
- set ordering keys;
- sequence-preservation rules;
- null representation;
- absence representation;
- duplicate rejection;
- identifier encoding;
- enumeration encoding;
- timestamp encoding;
- duration encoding;
- text normalization;
- numeric encoding;
- binary encoding;
- canonical byte encoding;
- domain-separation labels.

No implementation-library default may become canonical implicitly.

## 21. Fingerprint Envelope Mapping

A future fingerprint envelope must include:

- fingerprint version;
- canonicalization version;
- digest algorithm;
- domain-separation label;
- canonical payload digest;
- material input manifest;
- optional result digest when separately governed.

The manifest must bind every authoritative input without embedding secrets or
unnecessary raw evidence.

## 22. Derived-Field Discipline

A derived field must have:

- one identified derivation definition;
- one identified derivation version;
- canonical input dependencies;
- deterministic failure behavior;
- test-vector coverage;
- no external side effects.

Derived values cannot depend on current wall-clock time unless the canonical
evaluation time is an explicit input.

## 23. Optional-Field Discipline

An optional field may be omitted only when omission:

- has defined canonical meaning;
- does not weaken a required condition;
- does not alter authority;
- does not alter tenant or subject scope;
- does not conceal a limitation;
- has deterministic canonical representation.

Optional must not mean unchecked.

## 24. Extension Discipline

Extensions must:

- use governed namespaces;
- declare a version;
- be ignored only when explicitly safe;
- never override canonical fields;
- never elevate authority;
- never change outcome semantics implicitly;
- be included in fingerprints when materially evaluated.

Unsupported material extensions must fail closed.

## 25. Validation Ownership

Each invariant must have exactly one primary validation owner.

Downstream stages may verify preserved invariants but cannot redefine them.

Primary ownership is:

| Invariant | Primary owner |
|---|---|
| Invocation completeness | Invocation validation |
| Truth authority | Truth-authority validation |
| Tenant and subject equality | Scope binding |
| Evidence usability | Evidence eligibility |
| Rule compatibility | Evaluation selection |
| Claim outcome | Claim evaluation |
| Aggregate precedence | Aggregate construction |
| Canonical bytes | Canonicalization |
| Digest construction | Fingerprinting |
| Result completeness | Result construction |

Ambiguous ownership is an implementation-readiness failure.

## 26. Unknown and Unsupported Values

Future typed contracts must distinguish:

- unknown but safely ignorable;
- unknown and material;
- unsupported version;
- malformed value;
- absent required value;
- conflicting value;
- duplicate value.

Unknown material values and unsupported versions must fail closed.

## 27. Ordering Requirements

Canonical sets must use an explicitly defined stable ordering key.

Canonical sequences must preserve semantically meaningful order.

A future implementation cannot rely on:

- insertion order;
- hash-map order;
- filesystem order;
- database return order;
- provider response order;
- locale-aware sorting;
- runtime-specific object ordering.

## 28. Deterministic Test-Vector Requirements

Future test vectors must specify:

- vector identity;
- vector version;
- canonical input representation;
- expected canonical bytes or their approved encoding;
- expected fingerprint;
- expected typed result or failure;
- governing contract versions;
- canonicalization version;
- digest algorithm;
- provenance of the vector;
- positive or negative classification.

Vectors must cover:

- equivalent input orderings;
- material value changes;
- null versus absence;
- duplicate rejection;
- unsupported versions;
- malformed identifiers;
- timezone normalization;
- Unicode normalization;
- evidence ordering;
- limitation ordering;
- fingerprint sensitivity;
- cross-tenant rejection.

This document does not create test vectors.

## 29. Proposed First-Slice Contract Boundary

The proposed future first slice is limited to:

- minimal canonical scalar concepts;
- an immutable versioned invocation envelope;
- canonical representation construction;
- deterministic fingerprint construction;
- typed canonicalization failures.

It excludes:

- architecture-truth ingestion;
- provider observations;
- evidence eligibility;
- claim evaluation;
- aggregation;
- persistence;
- network access;
- runtime services;
- models;
- certificate issuance;
- enforcement;
- remediation.

## 30. Proposed Future File Boundary

Subject to a separate implementation-authority proposal, the recommended first
slice may be limited to exactly:

1. `src/afr/kernel/contracts.py`
2. `src/afr/kernel/canonicalization.py`
3. `src/afr/kernel/fingerprints.py`
4. `tests/unit/kernel/test_canonicalization.py`
5. `tests/unit/kernel/test_fingerprints.py`
6. `tests/vectors/kernel/canonicalization-v1.json`

These paths are planning candidates only.

They do not exist through authority created by this document and must converge
with the Phase 3 safety plan and any later implementation-authority proposal.

## 31. Dependency Constraint

The proposed first slice should require only:

- the approved language standard library;
- an approved cryptographic digest implementation available through that
  standard library;
- the existing approved test framework, if separately authorized.

No new third-party runtime dependency is proposed.

Dependency selection remains subject to separate implementation review.

## 32. Mapping Acceptance Conditions

The mapping is implementation-ready only when:

- every canonical concept has one unambiguous mapping;
- field obligations converge across all Phase 3 documents;
- validation ownership is singular and explicit;
- failures remain distinct from outcomes;
- canonicalization rules are complete;
- fingerprint material is complete;
- future test vectors are specified;
- the proposed first slice is exact and bounded;
- security requirements are preserved;
- no authority leakage exists.

## 33. Non-Authorization

This mapping creates no authority for:

- source code;
- executable schemas;
- generated models;
- tests or fixtures;
- the proposed future file boundary;
- dependencies;
- APIs or services;
- provider adapters;
- live evidence ingestion;
- NEXUS integration;
- persistence;
- runtime evaluation;
- certificate issuance;
- deployment;
- production access;
- enforcement;
- remediation;
- Phase 4.
