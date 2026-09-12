# Phase 4 First-Slice Normalized-Evidence-Bytes Implementation-Authority Proposal

## 1. Purpose

This document proposes narrowly bounded implementation authority for the first
Architecture Flight Recorder Phase 4 executable slice after canonical
operational-evidence-intake planning and canonical closure of the
normalized-evidence-bytes semantic clarification.

It is an authority proposal only.

It creates no implementation authority before its complete canonical effective
point and successful post-merge verification.

It does not reopen Phase 4 planning, reopen the normalized-evidence-bytes
semantic amendment, define ARCP, define NEXUS Phase 19, activate Phase 5, or
authorize runtime use.

## 2. Canonical Foundation

This proposal is bound to exactly:

`EXPECTED_CANONICAL_BASE_COMMIT = 9aafaeab4ee16454ffb14c6ce7885f344db4d6de`

`EXPECTED_CANONICAL_BASE_TREE = 63b2c0605724d32d37e802a0108550baa9d76c56`

`EXPECTED_CANONICAL_BASE_SOT_BLOB = 95edd06a371763efbdf9ef618b6c9eec2794c6b0`

The canonical foundation establishes:

- Phase 4 operational-evidence intake and eligibility planning:
  `COMPLETE`;
- Phase 4 planning authority: `CONSUMED_CLOSED`;
- normalized-evidence-bytes semantic-amendment lifecycle:
  `STATE_3 = CONSUMED_CLOSED`;
- normalized-evidence-bytes canonical measurement:
  `BYTE_LENGTH_OF_CANONICAL_PRE_CONSTRUCTION_NORMALIZED_EVIDENCE_PROJECTION`;
- executable implementation authority: `NONE`;
- Phase 5 start authority: `NONE`.

If canonical `main` moves before this proposal reaches its complete effective
point:

`BASE_MOVED = STOP`

`SILENT_REBASE = PROHIBITED`

`SILENT_BASE_SUBSTITUTION = PROHIBITED`

A moved base requires fresh read-only adjudication. It does not authorize
automatic rebasing or candidate rewriting.

## 3. Design Lineage and Review Disposition

The noncanonical implementation-contract design lineage remains historical
review evidence only.

- R1 was rejected with blocking findings A1-A4.
- R2 was rejected with blocking findings B1-B3.
- R3 was rejected with blocking findings C1-C3.
- R4 resolved C1-C3 and then passed independent adversarial review across:
  freshness-policy semantic preservation, Phase 3 runtime-type nonimport,
  NFC mapping-key collision behavior, cycle/recursion determinism, prior
  finding nonregression, exact file boundaries, Phase 3/cross-program
  non-expansion, and activation-authority leakage.

`R1_RETROACTIVE_PASS = NO`

`R2_RETROACTIVE_PASS = NO`

`R3_RETROACTIVE_PASS = NO`

`R4_DESIGN_ACCEPTANCE = ACCEPTED_NONCANONICAL_INPUT_ONLY`

Design acceptance does not equal canonical authority.

## 4. Current Authority

Until the complete proposal effective point:

`AFR_PHASE_4_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_4_LIVE_EVIDENCE_COLLECTION_AUTHORITY = NONE`

`AFR_PHASE_4_PROVIDER_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_4_NEXUS_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_4_ARCP_AUTHORITY = NONE`

`AFR_PHASE_4_RUNTIME_EVALUATION_AUTHORITY = NONE`

`AFR_PHASE_4_PERSISTENCE_AUTHORITY = NONE`

`AFR_PHASE_4_DEPLOYMENT_AUTHORITY = NONE`

`AFR_PHASE_4_ENFORCEMENT_AUTHORITY = NONE`

`AFR_PHASE_4_REMEDIATION_AUTHORITY = NONE`

`PHASE_5_START_AUTHORITY = NONE`

## 5. Proposed Authority

The proposed authority is exactly:

`BOUNDED_PHASE_4_FIRST_SLICE_NORMALIZED_EVIDENCE_BYTES_IMPLEMENTATION_ONLY`

If activated, it authorizes only the exact source, test, and vector work
defined in this proposal.

It does not authorize expansion by implication.

## 6. Exact Authority-Proposal Boundary

The complete proposal boundary is exactly:

1. `docs/SOT.md`
2. `docs/phase-4/PHASE_4_FIRST_SLICE_IMPLEMENTATION_AUTHORITY_PROPOSAL.md`

No third proposal path is authorized.

Candidate preparation outside the repository is not repository
materialization.

## 7. Exact Future Implementation Boundary

If and only if this proposal later reaches its complete effective point, the
complete future implementation boundary is exactly:

1. `src/afr/eligibility/normalized_evidence_bytes.py`
2. `tests/unit/eligibility/test_normalized_evidence_bytes.py`
3. `tests/vectors/eligibility/normalized-evidence-bytes-v1.json`

No fourth file is authorized.

Specifically:

`FUTURE_INIT_FILE = NONE`

`FUTURE_DEPENDENCY_CHANGE = NONE`

`FUTURE_BUILD_CONFIG_CHANGE = NONE`

`PHASE3_SOURCE_OR_TEST_MUTATION = PROHIBITED`

`PHASE3_CANONICALIZE_FUNCTION_INVOCATION = NOT_AUTHORIZED`

`PHASE3_PRIVATE_HELPER_IMPORT = PROHIBITED`

`PHASE3_RESOURCE_ACCOUNTING_REUSE = PROHIBITED`

`PHASE3_GENERIC_RESOURCE_LIMIT_CODE_IMPORT = PROHIBITED`

Renaming, relocating, generating, or adding another source, test, vector,
fixture, package initializer, configuration, dependency, schema, cache,
metadata, or build file requires separate authority.

## 8. Stable Failure Code

The Phase 4 stable code for the normalized-evidence-byte resource violation is
proposed as the exact string constant:

`NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED`

Its runtime representation is:

`exact str constant`

Its value is exactly:

`"NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED"`

It is not an enum.

It binds only:

`FAILURE_CLASSIFICATION = PROCESSING_FAILURE`

`FAILURE_RESOURCE_REFERENCE = normalized_evidence_bytes`

`FAILURE_SEMANTIC_LOCATION = normalized_evidence_bytes`

`FAILURE_CONSTRUCTION_STATE = STOPPED_BEFORE_EVIDENCE_CONSTRUCTION`

The Phase 3 code `RESOURCE_LIMIT_EXCEEDED` is not imported.

## 9. Exact Public API

The public executable surface contains exactly six symbols:

1. `NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED`
2. `NormalizedEvidenceBytesRequest`
3. `NormalizedEvidenceBytesLimitResult`
4. `NormalizedEvidenceBytesLimitFailure`
5. `NormalizedEvidenceBytesContractError`
6. `evaluate_normalized_evidence_bytes_limit`

No seventh public symbol is authorized by this slice.

The public function is exactly:

`evaluate_normalized_evidence_bytes_limit(request: NormalizedEvidenceBytesRequest) -> NormalizedEvidenceBytesLimitResult`

It accepts exactly one positional request object.

The public function is pure and side-effect-free.

It has no filesystem, network, provider, wall-clock, randomness, environment,
subprocess, plugin, persistence, secret, credential, production-configuration,
or ambient-state dependency.

## 10. Request Contract

`NormalizedEvidenceBytesRequest` is a frozen, slotted dataclass.

Request construction owns the required deep snapshot of approved nested
projection-value inputs.

The complete request contains exactly 36 fields:

1. `observation_id: exact_str`
2. `observation_envelope_version: exact_str`
3. `source_id: exact_str`
4. `source_class: exact_str`
5. `tenant_id: exact_str`
6. `subject_id: exact_str`
7. `subject_type: exact_str`
8. `environment_id: exact_str`
9. `scope_id: exact_str`
10. `release_binding: exact_str_or_None`
11. `observed_at: exact_timezone_aware_datetime`
12. `received_at: exact_timezone_aware_datetime`
13. `applicable_time: exact_timezone_aware_datetime_or_None`
14. `valid_from: exact_timezone_aware_datetime_or_None`
15. `valid_until: exact_timezone_aware_datetime_or_None`
16. `representation: exact_str`
17. `representation_version: exact_str`
18. `integrity_reference: exact_str`
19. `integrity_mechanism_version: exact_str`
20. `provenance_chain_reference: exact_str`
21. `provenance_version: exact_str`
22. `content_reference: exact_str`
23. `normalized_content: private_deeply_immutable_projection_value_snapshot`
24. `normalized_content_identity: exact_str`
25. `trusted_evaluation_time: exact_timezone_aware_datetime_or_None`
26. `freshness_policy: private_deeply_immutable_projection_value_snapshot_or_None`
27. `freshness_policy_version: exact_str_or_None`
28. `eligibility_policy_version: exact_str`
29. `evidence_model_version: exact_str`
30. `release_binding_present: exact_bool`
31. `applicable_time_present: exact_bool`
32. `validity_interval_present: exact_bool`
33. `trusted_evaluation_time_present: exact_bool`
34. `freshness_policy_present: exact_bool`
35. `maximum_normalized_evidence_bytes: exact_int_not_bool_greater_than_or_equal_to_zero`
36. `resource_policy_version: exact_str`

Projection schema version `1.0.0` and projection serialization version `1.0.0`
are fixed implementation-contract constants and are not caller-settable
request fields.

String subclasses are not accepted as exact strings.

`bool` is not accepted as an integer.

Naive datetimes are not accepted.

Invalid direct-call construction is a noncanonical programming-contract
failure, not a Phase 4 eligibility decision.

## 11. Optional Presence Contract

The five presence booleans are exactly:

1. `release_binding_present`
2. `applicable_time_present`
3. `validity_interval_present`
4. `trusted_evaluation_time_present`
5. `freshness_policy_present`

Presence handling preserves canonical Phase 4 absence/null distinction.

For `release_binding_present = false`, `release_binding` must be `None` and the
root member is omitted.

For `release_binding_present = true`, the member is present and may be an
explicit null only where earlier canonical Phase 4 validation permits that
state.

For `applicable_time_present = false`, `applicable_time` must be `None` and the
root member is omitted.

For `applicable_time_present = true`, the member is present and may be an
explicit null only where earlier canonical Phase 4 validation permits it.

For `validity_interval_present = false`, both `valid_from` and `valid_until`
must be `None` and both root members are omitted.

For `validity_interval_present = true`, the pair is present together. Earlier
canonical Phase 4 validation determines whether an explicit-null member is
permitted.

For `trusted_evaluation_time_present = false`,
`trusted_evaluation_time` must be `None` and the root member is omitted.

For `trusted_evaluation_time_present = true`, the member is present and may be
explicit null only where earlier canonical Phase 4 validation permits it.

For `freshness_policy_present = false`, both `freshness_policy` and
`freshness_policy_version` must be `None`, and both root members are omitted.

For `freshness_policy_present = true`, both fields participate as the exact
already-validated values. Explicit null remains distinct from absence only
where earlier canonical Phase 4 validation permits that state.

A presence-contract violation raises
`NormalizedEvidenceBytesContractError`.

It does not emit `NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED`.

## 12. Private Deep-Snapshot Domain

The approved private projection-value snapshot scalar domain is exactly:

- `None`;
- exact `bool`;
- exact `int` excluding `bool`;
- exact `str`;
- exact timezone-aware `datetime`.

Approved recursive container inputs are exactly:

- exact `list`;
- exact `tuple`;
- exact `dict` with exact `str` keys.

Nested values may contain only the same approved domain.

The following are prohibited:

- `set`;
- `frozenset`;
- arbitrary mapping subclasses;
- arbitrary sequence subclasses;
- custom objects;
- floats;
- untyped raw bytes.

Request construction recursively snapshots accepted nested containers into
private immutable representations.

Exact list/tuple input is stored as a private immutable tuple of recursively
snapshotted values.

Exact dict input is stored as a private frozen mapping value object containing
recursively snapshotted key/value entries.

No caller container reference is retained.

Snapshotting performs no string normalization, timestamp normalization,
mapping sorting, sequence reordering, coercion, defaulting, inference, or
semantic repair.

A caller mutation after successful request construction cannot alter the
request's governed snapshot.

If caller mutation occurs during deep-snapshot capture and deterministic
capture cannot complete, request construction raises
`NormalizedEvidenceBytesContractError`.

`SNAPSHOT_MUTATION_DURING_CAPTURE = NONCANONICAL_PROGRAMMING_CONTRACT_ERROR_IF_CAPTURE_CANNOT_COMPLETE`

A mutation-during-capture failure is not a canonical Phase 4 processing
failure, is not an eligibility decision, must not expose a partial governed
snapshot, and must not emit `NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED`.

## 13. Cycle and Recursion Contract

The accepted input-container graph must be acyclic along the active traversal
path.

Cycle detection is based on object identity for exact list, tuple, and dict
input containers.

An active-set guard is required.

Re-encountering the same container identity while it is active raises
`NormalizedEvidenceBytesContractError`.

A shared acyclic subobject referenced from multiple non-active paths is allowed
and is snapshotted by value at each occurrence.

Cycle rejection:

- is not a canonical Phase 4 processing failure;
- is not an eligibility decision;
- does not use `NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED`;
- exposes no partial snapshot value.

Snapshot traversal must be independent of Python's ambient recursion limit and
must use an iterative explicit stack or equivalent proven non-recursive control
flow.

Raw `RecursionError` escape and nontermination on a cycle are prohibited.

## 14. Closed Projection Schema

The measured object remains exactly:

`PRE_CONSTRUCTION_NORMALIZED_EVIDENCE_PROJECTION_CANONICAL_BYTES`

`NORMALIZED_EVIDENCE_PROJECTION_SCHEMA_VERSION = 1.0.0`

The root projection contains exactly these 32 schema members, subject only to
the frozen optional-member omission rules:

1. `projection_schema_version`
2. `projection_serialization_version`
3. `observation_id`
4. `observation_envelope_version`
5. `source_id`
6. `source_class`
7. `tenant_id`
8. `subject_id`
9. `subject_type`
10. `environment_id`
11. `scope_id`
12. `release_binding`
13. `observed_at`
14. `received_at`
15. `applicable_time`
16. `valid_from`
17. `valid_until`
18. `representation`
19. `representation_version`
20. `integrity_reference`
21. `integrity_mechanism_version`
22. `provenance_chain_reference`
23. `provenance_version`
24. `content_reference`
25. `normalized_content`
26. `normalized_content_identity`
27. `trusted_evaluation_time`
28. `freshness_policy`
29. `freshness_policy_version`
30. `eligibility_policy_version`
31. `evidence_model_version`
32. `optional_field_presence`

`PROJECTION_SCHEMA_OPEN_EXTENSION_POINT = NONE`

`maximum_normalized_evidence_bytes` and `resource_policy_version` are admission
inputs and do not participate in the measured projection.

The eligibility decision, final evidence identity, completed resource
accounting record, external provenance bodies, verifier sessions, detached
verification artifacts, secrets, credentials, transient provider state, logs,
and implementation stack do not participate.

## 15. Canonical Serialization Contract

Projection serialization is exactly:

`DETERMINISTIC_CANONICAL_UTF8_VALUE_SERIALIZATION_V1`

`PROJECTION_SERIALIZATION_VERSION = 1.0.0`

The implementation must preserve the accepted Phase 4 representation reuse of
the deterministic Phase 3 value-encoding grammar without invoking Phase 3
`canonicalize()` and without importing its resource accounting.

Required byte rules include:

- UTF-8 output;
- Unicode NFC normalization for strings;
- deterministic JSON string escaping;
- no insignificant whitespace;
- lowercase JSON booleans;
- JSON null for explicit null where present and permitted;
- base-10 ASCII integer rendering;
- timezone-aware timestamps normalized to UTC with `Z`;
- deterministic microsecond emission consistent with the accepted grammar;
- mapping keys restricted to strings;
- mapping ordering by canonical key bytes;
- sequence order preserved exactly;
- floating-point values unsupported;
- untyped raw bytes unsupported;
- no implicit ordering of unordered collections.

Implementation-specific object/dataclass layout cannot change projection
membership.

## 16. NFC Canonical Mapping-Key Collision Contract

Each mapping key is an exact string.

For canonical key processing:

1. normalize the key using NFC;
2. deterministically JSON-string encode it;
3. encode the resulting canonical key representation as UTF-8 bytes.

Mapping members are ordered by ascending canonical key bytes.

If two distinct raw input keys produce identical canonical key bytes, request
processing raises `NormalizedEvidenceBytesContractError` before any normalized-
evidence-byte limit-failure selection for that request.

On collision:

- first-wins behavior is prohibited;
- last-wins behavior is prohibited;
- duplicate canonical-member emission is prohibited;
- silent repair is prohibited;
- `NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED` is prohibited.

The rule applies recursively to mappings inside `normalized_content` and
`freshness_policy`.

## 17. Measurement and Admission Contract

The measurement point remains:

`LAST_MANDATORY_PRE_CONSTRUCTION_ADMISSION_CHECK`

The primitive may run only after all mandatory earlier Phase 4 non-projection
validation, trust, type, version, freshness, replay, conflict, and earlier
resource outcomes for the otherwise-eligible path are resolved; all projection
members and presence states are determined; normalized content and its identity
are available; and the complete projection is known to be formable under
schema `1.0.0` and serialization version `1.0.0`.

The deterministic quantity remains:

`NORMALIZED_EVIDENCE_BYTES = BYTE_LENGTH_OF_CANONICAL_PRE_CONSTRUCTION_NORMALIZED_EVIDENCE_PROJECTION`

`NORMALIZED_EVIDENCE_BYTES_UNIT = OCTETS`

Every emitted octet counts.

Character count or code-point count is prohibited.

The measurement consumes no Phase 4 work units.

The byte count is not an evidence-identity input.

A bounded streaming counting sink is permitted.

Full projection-byte-buffer materialization is not required.

A buffered implementation is permitted only if bounded and byte-equivalent to
the same canonical serialization.

Truncating, sampling, omitting, repairing, reordering, or compressing the
projection to fit the limit is prohibited.

## 18. Applicable Maximum Contract

The applicable maximum is supplied only as an already-validated value from a
versioned Phase 4 resource policy.

The primitive does not select the policy and does not create a new policy
domain.

`maximum_normalized_evidence_bytes` must be an exact integer, not `bool`, and
must be greater than or equal to zero as an executable representation
invariant.

A negative direct-call maximum raises
`NormalizedEvidenceBytesContractError`.

That error is not:

- a Phase 4 processing failure;
- an eligibility decision;
- a new policy semantic.

Zero is permitted when already validated upstream.

The admission rule is exactly:

`count == maximum -> PASS`

`count > maximum -> FAIL`

`NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED` may be emitted only for a formable
projection whose emitted octets would exceed the applicable maximum after all
earlier outcomes retain precedence.

## 19. Result Contract

`NormalizedEvidenceBytesLimitResult` is a frozen, slotted dataclass with exactly
three fields:

1. `within_limit: exact_bool`
2. `normalized_evidence_bytes: exact_int_not_bool_greater_than_or_equal_to_zero_or_None`
3. `failure: NormalizedEvidenceBytesLimitFailure_or_None`

Success invariant:

- `within_limit` is exactly `True`;
- `normalized_evidence_bytes` is the exact nonnegative full octet count;
- `failure` is `None`.

Limit-failure invariant:

- `within_limit` is exactly `False`;
- `normalized_evidence_bytes` is `None`;
- `failure` is the exact normalized-evidence-byte limit-failure record.

Invalid result-state construction raises
`NormalizedEvidenceBytesContractError`.

The public result does not return canonical projection bytes, normalized
content, final eligibility decision, final evidence identity, or completed
resource-accounting record.

## 20. Structured Limit-Failure Contract

`NormalizedEvidenceBytesLimitFailure` is a frozen, slotted dataclass with
exactly seven fields:

1. `code: exact_str_equal_NORMALIZED_EVIDENCE_BYTES_LIMIT_EXCEEDED`
2. `classification: exact_str_equal_PROCESSING_FAILURE`
3. `resource_reference: exact_str_equal_normalized_evidence_bytes`
4. `semantic_location: exact_str_equal_normalized_evidence_bytes`
5. `resource_policy_version: exact_str_copied_unchanged_from_request`
6. `safe_context_maximum_normalized_evidence_bytes: exact_int_not_bool_greater_than_or_equal_to_zero_copied_unchanged_from_request`
7. `construction_state: exact_str_equal_STOPPED_BEFORE_EVIDENCE_CONSTRUCTION`

The failure object is the complete Phase 4 structured processing failure for
this exact normalized-evidence-byte limit violation.

It is not the final eligibility decision.

A later separately authorized decision record may embed or reference it without
semantic rewrite.

The bounded safe context is exactly the applicable maximum.

It contains no normalized content, projection bytes, partial byte count,
provider/runtime data, secrets, credentials, stack trace, or unnecessary
payload.

The exact full projection count is not required after fail-closed limit
detection.

## 21. Programming-Contract Error Boundary

`NormalizedEvidenceBytesContractError` extends `ValueError`.

It is a noncanonical executable programming-contract error.

Its constructor carries only:

- `field_path: exact_str`;
- `reason: exact_str`.

It has no raw-invalid-value attribute.

Its message is diagnostic, not canonical control-flow data.

It must not expose secrets, payload, normalized content, projection bytes,
provider state, or runtime state.

The following direct-call defects are programming-contract errors rather than
canonical Phase 4 limit failures:

- malformed public API type;
- inconsistent optional-presence state;
- unsupported runtime value;
- unformable normalized-content or freshness-policy snapshot;
- negative maximum;
- mapping-key canonical collision;
- cyclic container graph;
- any other violation of this exact executable request contract.

These errors do not reinterpret or replace earlier canonical Phase 4 failure
classification.

## 22. Deterministic Test and Vector Requirements

The exact unit-test and vector surfaces must cover, at minimum:

- exact closed 32-member root schema;
- exact five-boolean optional-field-presence schema;
- absence versus present null where earlier validation permits;
- release-binding omission/presence behavior;
- applicable-time omission/presence behavior;
- validity interval both-or-neither behavior;
- trusted-evaluation-time omission/presence behavior;
- freshness-policy structured-value preservation without string coercion;
- freshness-policy absence versus present null;
- normalized-content deep-snapshot immutability after caller mutation;
- freshness-policy deep-snapshot immutability after caller mutation;
- caller list mutation after request construction does not change the snapshot;
- caller dict mutation after request construction does not change the snapshot;
- nested caller mutation after request construction does not change the snapshot;
- mutation during deep-snapshot capture that prevents deterministic completion
  raises `NormalizedEvidenceBytesContractError` and does not emit the stable
  normalized-evidence-byte limit-failure code;
- NFC string equivalence;
- canonical mapping-key ordering;
- NFC-normalized mapping-key collision rejection;
- no first-wins/last-wins/duplicate-member collision repair;
- semantic sequence-order preservation;
- timezone normalization to UTC `Z`;
- float rejection as programming-contract error;
- untyped raw-byte rejection as programming-contract error;
- unordered-container rejection as programming-contract error;
- direct self-referential list rejection;
- direct self-referential dict rejection;
- indirect list/dict cycle rejection;
- shared acyclic subobject acceptance by value;
- cycle outcome independent of ambient recursion limit;
- exact deterministic vector projection bytes;
- exact octet count;
- count equal to maximum passes;
- count greater than maximum returns exact structured limit failure;
- negative maximum produces contract error, not limit failure;
- zero maximum is not rejected as a policy-domain error;
- bool maximum is rejected as a programming-contract error;
- stable code is exact string constant, not enum;
- request field runtime types and optional unions;
- failure frozen/slotted exact fields and types;
- result frozen/slotted exact fields and invariants;
- failure policy version copied unchanged;
- failure safe context contains only the applicable maximum;
- failure exposes no partial count or projection bytes;
- no final eligibility decision in projection or result;
- no final evidence identity in projection or result;
- no completed resource-accounting record in projection or result;
- measurement consumes no Phase 4 work units;
- Phase 3 maximum canonical bytes remains independent;
- no clock, randomness, environment, filesystem, network, provider, secret, or
  persistence dependence.

The vector must include the expected canonical projection UTF-8 hex and the
expected normalized-evidence-byte count.

`EXPECTED_CANONICAL_PROJECTION_UTF8_HEX = REQUIRED`

`EXPECTED_NORMALIZED_EVIDENCE_BYTE_COUNT = REQUIRED`

A different textual encoding does not substitute for the required exact
canonical projection UTF-8 hex field.

A module-private deterministic emitter may be exercised by the authorized unit
test only to verify exact vector bytes.

That private emitter receives no public API authority and no external
production import authority.

The private emitter and public limit evaluator must share one serialization
implementation.

A duplicate independent production serializer in tests is prohibited.

## 23. Security and Supply-Chain Constraints

The implementation must:

- add no dependency;
- change no build configuration;
- use only approved standard-library capabilities already available;
- read no secret, credential, token, or production configuration;
- make no network request;
- perform no filesystem read or write as part of primitive evaluation;
- open no database, queue, cache, or persistence connection;
- invoke no subprocess or shell;
- deserialize no executable object format;
- dynamically import no provider-controlled module;
- load no plugin or remote code;
- emit no sensitive projection or normalized-content payload to logs;
- preserve tenant/subject values exactly as already validated inputs;
- fail closed within the exact executable contract.

## 24. Explicitly Prohibited Scope

This authority does not authorize:

- observation collection;
- provider/cloud adapters;
- general observation-envelope parsing;
- general Phase 4 validation engine;
- provenance verification;
- integrity verification;
- trusted-time engine;
- freshness evaluation engine;
- replay or conflict store;
- persistence;
- database, queue, cache, or stream;
- content normalization algorithm;
- normalized-content identity algorithm;
- final eligibility-decision construction;
- final evidence-identity commitment;
- completed resource-accounting record;
- immutable eligible-evidence construction;
- Phase 3 kernel invocation;
- conformance evaluation;
- NEXUS integration;
- ARCP implementation or runtime use;
- ATA integration;
- APIs, services, workers, schedulers, or CLI;
- filesystem/network runtime integration;
- deployment;
- production execution;
- enforcement;
- remediation;
- Phase 5.

## 25. Stop Conditions

Implementation or proposal progression must stop without broadening scope if:

- a fourth implementation file becomes necessary;
- an additional public API symbol becomes necessary;
- a dependency or build-configuration change becomes necessary;
- a Phase 3 source or test mutation becomes necessary;
- Phase 3 generic resource-limit code reuse becomes necessary;
- the projection schema must change;
- serialization version must change;
- a new optional-presence member is required;
- resource-policy semantic validation must be performed inside this primitive;
- a direct-call misuse would need a canonical Phase 4 eligibility/failure
  classification;
- general envelope validation becomes necessary;
- provenance or integrity verification becomes necessary;
- persistence or replay state becomes necessary;
- kernel invocation becomes necessary;
- NEXUS, ARCP, or ATA semantics become necessary;
- provider-specific behavior becomes necessary;
- filesystem, network, or runtime integration becomes necessary;
- canonical Phase 0 through Phase 4 semantics require amendment;
- independent review identifies a blocking defect in this proposal or future
  implementation candidate.

Stopping does not authorize an alternative implementation.

## 26. Required Proposal Review

Before activation, this proposal requires independent review of:

- canonical-base identity;
- Phase 4 planning non-reopening;
- R8/R2 semantic preservation;
- stable failure-code binding;
- exact public API;
- request field types and optional-presence semantics;
- deep-snapshot immutability;
- freshness-policy value-domain preservation;
- NFC normalization and key-collision behavior;
- cycle/recursion determinism;
- closed projection membership;
- canonical serialization;
- measurement/admission ordering;
- failure/result ownership;
- deterministic test/vector coverage;
- security and supply-chain constraints;
- Phase 3 isolation;
- NEXUS/ARCP/ATA non-expansion;
- exact proposal boundary;
- exact future implementation boundary;
- authority leakage.

All blocking findings must be resolved before activation.

## 27. Proposal Activation Effective Point

Before the effective point:

`AFR_PHASE_4_IMPLEMENTATION_AUTHORITY = NONE`

`PHASE_5_START_AUTHORITY = NONE`

The proposed authority activates if and only if all of the following separately
governed gates complete successfully in order:

1. exact two-document authority-proposal candidate preparation;
2. independent architecture, semantic, security, contract, non-drift, and
   authority review of the complete candidate;
3. all blocking findings resolved in a fresh exact accepted candidate;
4. exact content and identity freeze of both complete future repository-file
   preimages;
5. exact two-document repository materialization;
6. exact staging and staged-object verification;
7. exact proposal commit and remote proposal-branch publication;
8. draft pull-request creation and identity verification;
9. independent pull-request acceptance;
10. explicit Draft-to-Ready transition;
11. explicit merge authorization for the exact Ready identity;
12. exact reviewed two-parent canonical merge;
13. independent post-merge identity, ordered-parent, tree, exact-boundary, and
    content verification;
14. local and remote canonical `main` convergence;
15. clean canonical checkout, worktree, and index verification.

No earlier gate implies a later gate.

Proposal candidate preparation, review, freeze, repository materialization,
staging, commit, publication, draft-PR creation, acceptance review, Ready
transition, merge authorization, or merge alone does not establish
implementation authority.

The canonical activation merge must preserve the separately frozen exact base,
reviewed head, reviewed head tree, and required two-parent topology.

Squash, rebase, fast-forward substitution, changed reviewed head, changed
reviewed tree, or silent moved-base substitution cannot establish authority.

## 28. State After Activation

After and only after the complete proposal effective point:

`AFR_PHASE_4_IMPLEMENTATION_AUTHORITY = BOUNDED_PHASE_4_FIRST_SLICE_NORMALIZED_EVIDENCE_BYTES_IMPLEMENTATION_ONLY`

All other authorities remain absent:

`AFR_PHASE_4_LIVE_EVIDENCE_COLLECTION_AUTHORITY = NONE`

`AFR_PHASE_4_PROVIDER_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_4_NEXUS_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_4_ARCP_AUTHORITY = NONE`

`AFR_PHASE_4_RUNTIME_EVALUATION_AUTHORITY = NONE`

`AFR_PHASE_4_PERSISTENCE_AUTHORITY = NONE`

`AFR_PHASE_4_DEPLOYMENT_AUTHORITY = NONE`

`AFR_PHASE_4_ENFORCEMENT_AUTHORITY = NONE`

`AFR_PHASE_4_REMEDIATION_AUTHORITY = NONE`

`PHASE_5_START_AUTHORITY = NONE`

Activation authorizes only a fresh implementation branch created from the
verified proposal activation merge and only the exact three future
implementation files.

Activation does not itself create, review, accept, merge, deploy, or execute
the implementation.

## 29. Required Implementation Lifecycle After Activation

After future activation, the implementation must still proceed through a
separate governed lifecycle.

At minimum:

1. create a fresh implementation branch from the verified activation merge;
2. materialize exactly the three authorized implementation files and no fourth
   file;
3. reproduce the exact deterministic unit and vector requirements;
4. independently review architecture, semantics, typed contracts,
   deterministic serialization, security, test coverage, Phase 3 isolation,
   exact file boundary, and authority leakage;
5. resolve all blocking implementation findings;
6. freeze exact implementation content and identities;
7. stage and verify the exact implementation objects;
8. create and publish the exact implementation commit/branch;
9. create a draft implementation pull request and verify identity;
10. complete independent PR acceptance;
11. explicitly transition Draft to Ready;
12. obtain explicit merge authorization for the exact Ready identity;
13. merge using the separately required canonical topology;
14. independently verify post-merge identity, parentage, tree, exact three-file
    boundary, content identities, and test/vector reproduction;
15. converge local and remote canonical `main`;
16. verify a clean canonical checkout, worktree, and index;
17. complete separately governed terminal implementation closure.

No implementation gate implies a later gate.

Implementation merge alone does not close or consume the authority.

## 30. Phase 5 Boundary

Phase 5 remains unauthorized.

`PHASE_5_START_AUTHORITY = NONE`

Phase 5 may not begin merely because:

- this authority proposal is prepared;
- this authority proposal is reviewed;
- this authority proposal is merged;
- implementation authority activates;
- implementation files are created;
- implementation tests pass;
- an implementation PR is reviewed or merged.

A separately governed Phase 4 implementation closure must first complete, and
a separate Phase 5 authority path is required.

## 31. Cross-Program Non-Drift

The controlling disposition remains:

`DISPOSITION_A = PHASE_4_DOES_NOT_REQUIRE_ARCHITECTURE_TRUTH_CONTRACT_WORK`

`ARCP_CANONICAL_NAME = UNRESOLVED_PENDING_NEXUS_PHASE_19_GOVERNANCE`

`ARCP_CANONICAL_SEMANTICS = UNRESOLVED_PENDING_NEXUS_PHASE_19_GOVERNANCE`

`NEXUS_PHASE_19_CANONICAL_CAPABILITY_NAME = MUST_BE_VERIFIED_FROM_CANONICAL_NEXUS_STATE`

`DEPENDENCY_RECOGNITION != INTEGRATION_PLANNING_AUTHORITY`

`INTEGRATION_PLANNING_AUTHORITY != INTEGRATION_IMPLEMENTATION_AUTHORITY`

`INTEGRATION_IMPLEMENTATION_AUTHORITY != RUNTIME_AUTHORITY`

This proposal creates no NEXUS, ARCP, ATA, architecture-truth, integration, or
runtime authority.

The noncanonical placeholder
`FUTURE_NEXUS_TO_AFR_ARCHITECTURE_TRUTH_CONSUMER_CONTRACT` remains only a
placeholder and is not a schema, API, adapter, implementation, or active
contract.

## 32. Final Authority Statement

Before complete canonical activation:

`AFR_PHASE_4_IMPLEMENTATION_AUTHORITY = NONE`

After and only after complete canonical activation:

`AFR_PHASE_4_IMPLEMENTATION_AUTHORITY = BOUNDED_PHASE_4_FIRST_SLICE_NORMALIZED_EVIDENCE_BYTES_IMPLEMENTATION_ONLY`

Even after activation:

`RUNTIME_AUTHORITY = NONE`

`PERSISTENCE_AUTHORITY = NONE`

`KERNEL_INVOCATION_AUTHORITY = NONE`

`PROVIDER_INTEGRATION_AUTHORITY = NONE`

`NEXUS_INTEGRATION_AUTHORITY = NONE`

`ARCP_AUTHORITY = NONE`

`ATA_INTEGRATION_AUTHORITY = NONE`

`DEPLOYMENT_AUTHORITY = NONE`

`ENFORCEMENT_AUTHORITY = NONE`

`REMEDIATION_AUTHORITY = NONE`

`PHASE_5_START_AUTHORITY = NONE`

No gate implies the next.
