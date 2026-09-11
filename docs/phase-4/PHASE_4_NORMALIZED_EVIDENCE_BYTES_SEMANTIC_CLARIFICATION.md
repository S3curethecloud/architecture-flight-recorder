# AFR Phase 4 Normalized-Evidence-Bytes Semantic Clarification

## 1. Purpose

This document defines the bounded Phase 4 semantic clarification for the
existing canonical resource term `normalized evidence bytes`.

It resolves only the measurement semantics authorized by the canonical
Phase 4 normalized-evidence-bytes semantic-amendment authority.

It does not reopen Phase 4 generally and creates no source-code,
implementation, integration, live-collection, persistence, kernel-invocation,
certificate, deployment, enforcement, remediation, production, or subsequent-
phase authority.

## 2. Canonical Authority and Base

This clarification is governed by State 1 of the canonical
normalized-evidence-bytes semantic-amendment authority lifecycle.

State 1 became effective only after all nineteen authority-proposal
effective-point requirements completed, including the canonical merge of
PR #18 and the separately required post-merge identity, ordered-parent, tree,
frozen-content, local/remote convergence, and clean-worktree verification.

The merge of PR #18 alone was not authority-establishing.

The clarification is bound to exactly:

`REPOSITORY = S3curethecloud/architecture-flight-recorder`

`CANONICAL_BRANCH = main`

`EXPECTED_CANONICAL_BASE_COMMIT = d618688cb2b54e319d73e6cb70f3a2f8e19c9c92`

`EXPECTED_CANONICAL_BASE_TREE = 9b8f577e4df894edc26fd8b36c1921b217ba0cbe`

`EXPECTED_CANONICAL_BASE_SOT_BLOB = 8130d344eced5306e4f2c8cbee00c3ef02d63237`

If canonical `main` moves before this clarification reaches its canonical
effective point:

`BASE_MOVED = STOP`

`SILENT_REBASE = PROHIBITED`

`SILENT_BASE_SUBSTITUTION = PROHIBITED`

Before the clarification effective point:

`STATE_1 = BOUNDED_NORMALIZED_EVIDENCE_BYTES_SEMANTIC_AMENDMENT_DOCUMENTATION_ONLY`

`AFR_PHASE_4_NORMALIZED_EVIDENCE_BYTES_SEMANTIC_AMENDMENT_AUTHORITY = BOUNDED_NORMALIZED_EVIDENCE_BYTES_SEMANTIC_AMENDMENT_DOCUMENTATION_ONLY`

`IMPLEMENTATION_AUTHORITY = NONE`

## 3. Exact Canonical Boundary

The semantic clarification may change exactly:

1. `docs/SOT.md`
2. `docs/phase-4/PHASE_4_NORMALIZED_EVIDENCE_BYTES_SEMANTIC_CLARIFICATION.md`

No third canonical repository path is authorized.

Historical Phase 4 planning records and the semantic-amendment authority
proposal remain preserved and are not rewritten.

## 4. Existing Canonical Resource Surface

The Phase 4 deterministic resource surface remains exactly:

1. total ingress bytes;
2. envelope field count;
3. collection cardinality;
4. nesting depth;
5. provenance-chain length;
6. integrity-reference length;
7. normalized evidence bytes;
8. deterministic processing work units.

The existing canonical rule remains exactly:

`Any violation fails closed before evidence construction.`

This clarification changes only the meaning and admission semantics of item 7
and its explicitly stated relationship to the other already-existing Phase 4
resource checks.

## 5. Exact Measured Object

`NORMALIZED_EVIDENCE_BYTES_MEASURED_OBJECT = PRE_CONSTRUCTION_NORMALIZED_EVIDENCE_PROJECTION_CANONICAL_BYTES`

A `PRE_CONSTRUCTION_NORMALIZED_EVIDENCE_PROJECTION` is a measurement-only,
immutable, deterministic projection of already-validated Phase 4 evidence
material that would otherwise be eligible for construction.

It is not the final eligible-evidence object, an evidence-identity object, an
eligibility-decision record, a completed resource-accounting record, a
conformance-kernel input, a persistence object, a transport object, a provider
or adapter object, or a runtime object.

## 6. Closed Projection Schema

`NORMALIZED_EVIDENCE_PROJECTION_SCHEMA_VERSION = 1.0.0`

The projection is exactly one canonical mapping.

Except for the optional keys governed by Section 7, its root key membership is
closed and consists exactly of:

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

No additional root key is permitted by projection schema version `1.0.0`.

`PROJECTION_SCHEMA_OPEN_EXTENSION_POINT = NONE`

A later need for an additional projection member requires separately governed
Phase 4 semantic authority and a new projection-schema version.

## 7. Exact Optional-Field Presence Schema

The root key `optional_field_presence` is always present.

Its value is exactly one mapping containing exactly these five boolean keys:

1. `release_binding`
2. `applicable_time`
3. `validity_interval`
4. `trusted_evaluation_time`
5. `freshness_policy`

No sixth presence key is permitted by schema version `1.0.0`.

The presence rules are exactly:

- `release_binding = false` omits root key `release_binding`;
- `release_binding = true` requires root key `release_binding`;
- `applicable_time = false` omits root key `applicable_time`;
- `applicable_time = true` requires root key `applicable_time`;
- `validity_interval = false` omits both `valid_from` and `valid_until`;
- `validity_interval = true` requires both `valid_from` and `valid_until`;
- `trusted_evaluation_time = false` omits root key `trusted_evaluation_time`;
- `trusted_evaluation_time = true` requires root key `trusted_evaluation_time`;
- `freshness_policy = false` omits both `freshness_policy` and `freshness_policy_version`;
- `freshness_policy = true` requires both `freshness_policy` and `freshness_policy_version`.

All root keys not governed by this section are mandatory for a formable
projection.

For an optional semantic whose presence boolean is true, explicit null remains
distinct from empty and from absence. If canonical Phase 4 validation permits
that explicit null on a path that can otherwise become eligible, it is
serialized as JSON `null`. If canonical validation does not permit it, the
earlier validation result controls and no projection is required solely to
replace that earlier result.

## 8. Exact Semantic-to-Key Mapping

Each projection key receives exactly the already-validated canonical Phase 4
semantic value identified below:

- `projection_schema_version`: fixed string `1.0.0`;
- `projection_serialization_version`: fixed string `1.0.0`;
- `observation_id`: originating observation identifier;
- `observation_envelope_version`: originating observation-envelope version;
- `source_id`: validated source identifier;
- `source_class`: validated source class;
- `tenant_id`: validated tenant identifier;
- `subject_id`: validated subject identifier;
- `subject_type`: validated subject type;
- `environment_id`: validated environment identifier;
- `scope_id`: validated scope identifier;
- `release_binding`: validated release/deployment binding when present;
- `observed_at`: validated observed time;
- `received_at`: validated received time;
- `applicable_time`: validated applicable time when present;
- `valid_from` and `valid_until`: validated validity interval when present;
- `representation`: validated declared payload/content representation;
- `representation_version`: validated representation version;
- `integrity_reference`: validated integrity reference;
- `integrity_mechanism_version`: validated integrity-mechanism version;
- `provenance_chain_reference`: validated provenance-chain reference;
- `provenance_version`: validated provenance version;
- `content_reference`: validated content reference;
- `normalized_content`: exact already-normalized canonical content value;
- `normalized_content_identity`: already-determined normalized-content identity;
- `trusted_evaluation_time`: validated trusted-evaluation time when present;
- `freshness_policy`: validated freshness-policy identifier/reference/value when present;
- `freshness_policy_version`: validated freshness-policy version when present;
- `eligibility_policy_version`: governing eligibility-policy version;
- `evidence_model_version`: governing evidence-model version;
- `optional_field_presence`: exact five-boolean map from Section 7.

This mapping is exhaustive for projection schema version `1.0.0`.

The projection contains no unspecified category such as `other bindings`,
`additional metadata`, provider metadata, or future evidence fields by
implication.

## 9. Provenance and Integrity Participation

For projection schema version `1.0.0`, provenance participates only through
`source_id`, `source_class`, `provenance_chain_reference`, and
`provenance_version`.

Integrity participates only through `integrity_reference` and
`integrity_mechanism_version`.

External provenance-chain bodies, verifier sessions, detached verification
artifacts, credentials, secrets, transient provider state, network state,
implementation stack data, and validation logs are excluded.

This section defines measurement membership only. It does not weaken, replace,
reinterpret, or expand canonical provenance or integrity validation and trust
semantics.

## 10. Normalized-Content Value Domain and Collection Ordering

The `normalized_content` member participates as the exact canonical normalized
value, not merely through its identity.

Before projection measurement begins, that value must already be representable
by the bound projection serialization grammar.

For projection serialization:

- mapping keys are strings and are ordered by canonical key bytes;
- ordered sequences preserve their already-established semantic sequence order;
- sequence order must not be invented from arrival order or implementation iteration accidents;
- an unordered collection has no implicit projection representation;
- unsupported or unordered value structures must be resolved by earlier canonical Phase 4 validation/normalization semantics and cannot be silently ordered by the projection serializer;
- floating-point values are unsupported by serialization version `1.0.0`;
- untyped raw bytes are unsupported by serialization version `1.0.0`;
- no implementation-specific object or dataclass field layout may change the projection schema.

The projection measurement does not define a new content-normalization
algorithm.

## 11. Explicit Projection Exclusions

The projection excludes exactly:

- final evidence identity;
- final eligibility decision;
- the `normalized evidence bytes` count itself;
- completed resource-accounting record;
- any processing-failure record;
- post-construction audit wrappers;
- external provenance-chain bodies;
- external integrity-verifier artifacts;
- transport, compression, or encryption framing;
- detached signatures;
- persistence metadata;
- provider-specific metadata or SDK framing;
- database, queue, cache, or stream envelopes;
- kernel invocation material;
- conformance results;
- implementation-specific diagnostics;
- runtime, deployment, enforcement, or remediation metadata.

No excluded item is reintroduced through a generic extension field because no
generic extension field exists in projection schema version `1.0.0`.

## 12. Exact Canonical Representation

`NORMALIZED_EVIDENCE_PROJECTION_SERIALIZATION = DETERMINISTIC_CANONICAL_UTF8_VALUE_SERIALIZATION_V1`

`NORMALIZED_EVIDENCE_PROJECTION_SERIALIZATION_VERSION = 1.0.0`

The byte grammar is the Phase 4 representation reuse of the accepted Phase 3
`CANONICALIZATION_VERSION = 1.0.0` value-encoding semantics.

Representation reuse includes only the deterministic byte rules required by
the closed projection schema and normalized-content value domain:

- UTF-8 output;
- NFC string normalization;
- deterministic JSON string escaping;
- no insignificant whitespace;
- deterministic mapping-member ordering by canonical key bytes;
- semantic sequence-order preservation;
- explicit JSON `null` for present explicit null;
- omission only of exact optional root keys authorized by Section 7;
- lowercase JSON booleans;
- base-10 ASCII integer representation;
- timezone-aware timestamps normalized to UTC `Z`;
- rejection of floating-point values;
- rejection of untyped raw bytes;
- rejection of unsupported value types.

The exact Phase 4 projection schema, not dataclass discovery, arbitrary object
introspection, provider object layout, or implementation-specific membership,
determines the serialized record.

`PHASE3_CANONICALIZE_FUNCTION_INVOCATION_REQUIRED = NO`

`PHASE3_RESOURCE_ACCOUNTING_REUSED_FOR_PHASE4_NORMALIZED_EVIDENCE_BYTES = NO`

A future implementation may reuse an accepted Phase 3 representation primitive
only under separately granted implementation authority and only if that reuse
is proven byte-equivalent to this exact Phase 4 projection schema and
serialization contract.

## 13. Serialization and Schema Version Binding

The projection has two distinct version bindings:

`NORMALIZED_EVIDENCE_PROJECTION_SCHEMA_VERSION = 1.0.0`

`NORMALIZED_EVIDENCE_PROJECTION_SERIALIZATION_VERSION = 1.0.0`

The schema version fixes field membership, field names, optional-field
presence rules, semantic-to-key mapping, and exclusions.

The serialization version fixes byte encoding.

A later Phase 3 change cannot silently change either Phase 4 version.

Any future schema or representation change requires separately governed Phase 4
authority.

## 14. Lifecycle Measurement Point

`NORMALIZED_EVIDENCE_BYTES_MEASUREMENT_POINT = LAST_MANDATORY_PRE_CONSTRUCTION_ADMISSION_CHECK`

Measurement occurs only after all mandatory non-projection validation and
resource checks for an otherwise-eligible path have succeeded, normalized
content and normalized-content identity are available, all projection members
and presence states are determined, and all members are known to be formable
under projection schema `1.0.0` and serialization version `1.0.0`.

Measurement occurs before an `ELIGIBLE` decision becomes final, before final
evidence identity commitment, before completed resource accounting, and before
immutable eligible evidence construction.

If an earlier deterministic validation, trust, type, version, freshness,
conflict, replay, or non-projection resource result has already selected a
non-eligible or processing-failure outcome, projection measurement is not
performed solely to replace that result.

## 15. Normalized Content Participation

`NORMALIZED_CONTENT_PARTICIPATES_IN_NORMALIZED_EVIDENCE_BYTES = YES`

`NORMALIZED_CONTENT_IDENTITY_ONLY_IS_SUFFICIENT = NO`

`NORMALIZED_EVIDENCE_BYTES_EQUALS_NORMALIZED_CONTENT_BYTES = NO`

The normalized-content identity participates through the exact
`normalized_content_identity` member but does not substitute for normalized
content.

## 16. Eligible-Evidence Metadata Participation

`ELIGIBLE_EVIDENCE_METADATA_PARTICIPATION = CLOSED_PROJECTION_SCHEMA_V1_ONLY`

Eligible-evidence metadata participation is exactly the closed member set
defined by Sections 6 through 9.

There is no version-1 rule permitting additional metadata merely because a
future evidence object happens to preserve it.

Such a change requires a new separately governed projection-schema version.

## 17. Relationship to the Eligibility Decision

`ELIGIBILITY_DECISION_INCLUDED_IN_NORMALIZED_EVIDENCE_PROJECTION = NO`

The eligibility decision does not participate because the byte-limit check is
itself a prerequisite for finalizing `ELIGIBLE`.

If the projection exceeds the applicable normalized-evidence-byte limit, the
observation cannot produce `ELIGIBLE` evidence.

The limit creates no conformance result.

## 18. Deterministic Resource Accounting and Precedence

`NORMALIZED_EVIDENCE_BYTES = BYTE_LENGTH_OF_CANONICAL_PRE_CONSTRUCTION_NORMALIZED_EVIDENCE_PROJECTION`

The applicable limit is owned by a Phase 4 versioned resource policy.

The normalized-evidence byte count is recorded in the completed resource-
accounting record only after the admission check succeeds.

The completed resource-accounting record is excluded from the projection so
the measured quantity is not self-referential.

The relationship to deterministic processing work units is exactly:

`NORMALIZED_EVIDENCE_PROJECTION_MEASUREMENT_CONSUMES_PHASE4_WORK_UNITS = NO`

The projection measurement/counting pass is a distinct resource-admission
operation and does not increment or consume the canonical Phase 4
`deterministic processing work units` quantity.

This statement does not redefine how any other Phase 4 operation is charged to
work units.

Resource precedence for an otherwise-eligible path is exactly:

1. complete all mandatory validations and all resource checks whose canonical quantities are available before projection measurement;
2. if an earlier check selects a deterministic non-eligible or processing-failure outcome, stop according to that existing outcome and do not run projection measurement solely to supersede it;
3. establish projection serialization-formability;
4. measure the exact projection bytes;
5. if the normalized-evidence-byte maximum would be exceeded, stop before evidence construction with the failure ownership defined by Section 22;
6. only after that admission succeeds may the `ELIGIBLE` path finalize its decision record, evidence identity, completed resource accounting, and immutable eligible evidence.

Because measurement does not consume work units, the projection byte check
cannot simultaneously create a new work-unit exceedance.

`NORMALIZED_EVIDENCE_BYTES_AND_WORK_UNITS_SIMULTANEOUS_MEASUREMENT_FAILURE = NOT_APPLICABLE`

No equality or substitution relationship is created among total ingress bytes,
collection cardinality, work units, or normalized evidence bytes.

## 19. Evidence-Identity Relationship

`NORMALIZED_EVIDENCE_BYTES_IS_EVIDENCE_IDENTITY_INPUT = NO`

The byte count is a derived resource-accounting value and must not replace,
weaken, or collapse existing evidence-identity bindings.

The projection contains the exact underlying identity-relevant fields selected
by projection schema version `1.0.0`.

The final evidence identity is established according to existing evidence-
identity semantics after normalized-evidence-byte admission succeeds.

The final evidence identity itself is excluded from the measured projection.

## 20. Inclusive and Exclusive Byte Boundary

The byte count includes every octet emitted by the canonical projection
serialization, including root and nested field-name bytes, canonical escaping,
structural delimiters, separators, canonical scalar bytes, explicit-null bytes,
sequence delimiters, mapping delimiters, and the fixed schema and serialization
version values carried by the projection.

The byte count excludes every item listed in Section 11.

`NORMALIZED_EVIDENCE_BYTES_UNIT = OCTETS`

## 21. Deterministic Pre-Construction Admission Mechanism

The canonical quantity is the number of octets the complete closed projection
would emit under schema version `1.0.0` and serialization version `1.0.0`.

A future implementation may compute that quantity through bounded streaming
serialization into a counting sink. Complete byte-buffer materialization is not
required.

The counting operation must follow the exact closed schema and canonical
serialization rules, count bytes rather than characters/code points, stop
fail-closed when the applicable normalized-evidence-byte maximum would be
exceeded, never truncate/sample/omit/repair/reorder/compress to fit, never use
wall-clock duration to change the result, and produce the same pass/fail
admission result for identical governed inputs.

## 22. Failure Ownership and Resource Reference

A normalized-evidence-byte limit violation has exactly this semantic ownership:

`FAILURE_CLASSIFICATION = PROCESSING_FAILURE`

`FAILURE_RESOURCE_REFERENCE = normalized_evidence_bytes`

`FAILURE_SEMANTIC_LOCATION = normalized_evidence_bytes`

`FAILURE_CONSTRUCTION_STATE = STOPPED_BEFORE_EVIDENCE_CONSTRUCTION`

This clarification deliberately does not select or import an exact stable
failure-code token.

`NORMALIZED_EVIDENCE_BYTES_STABLE_FAILURE_CODE = NOT_SELECTED_BY_THIS_CLARIFICATION`

`PHASE3_RESOURCE_LIMIT_EXCEEDED_CODE_IMPORT = PROHIBITED`

The accepted Phase 3 implementation enum token `RESOURCE_LIMIT_EXCEEDED` does
not become a Phase 4 canonical failure code by implication.

Before future implementation can be accepted, the fresh separately governed
Phase 4 implementation-contract path must bind exactly one stable Phase 4
failure code to the above classification, resource reference, semantic
location, and construction-stop state without altering them.

This resolves the authorized failure-ownership and resource-reference questions
without expanding the existing Phase 4 failure taxonomy or importing Phase 3
implementation vocabulary.

Unsupported type, representation, version, trust, or other earlier conditions
remain governed by their existing Phase 4 classifications and precedence.

## 23. Relationship to Phase 3 maximum_canonical_bytes

`PHASE3_MAXIMUM_CANONICAL_BYTES_TO_NORMALIZED_EVIDENCE_BYTES_RELATIONSHIP = INDEPENDENT_NOT_SUBSTITUTABLE`

`PHASE3_MAXIMUM_CANONICAL_BYTES_SUBSTITUTION = PROHIBITED`

`PHASE4_NORMALIZED_EVIDENCE_BYTES_LIMIT_OWNERSHIP = PHASE_4`

Phase 3 `maximum_canonical_bytes` remains a Phase 3 canonicalization resource
semantic. Phase 4 `normalized evidence bytes` remains a Phase 4 evidence-
eligibility resource semantic. Representation-grammar reuse does not create
resource-limit equality.

## 24. Distinct Phase 3 Projection Bound

`DISTINCT_PHASE3_PROJECTION_BOUND_REQUIRED = NO`

This clarification does not add or amend a Phase 3 resource limit.

Any implementation-internal mechanical ceiling required to reuse a Phase 3
primitive must be separately justified under implementation authority and must
not become canonical by implication or reject input valid under the canonical
Phase 4 normalized-evidence-byte limit absent separately governed authority.

## 25. Presence, Type, Time, and Determinism Non-Drift

The canonical distinctions among absent optional, explicit null, empty,
missing required, unsupported value, unsupported type, and unsupported version
remain unchanged.

Explicit trusted-time and freshness semantics remain unchanged. No ambient-time
dependency is created.

Identical governed inputs under identical governing versions must produce the
same exact projection mapping, projection bytes, and normalized-evidence-byte
count.

## 26. Security and Privacy Non-Expansion

The existing Phase 4 security and trust boundary remains unchanged.

`PHASE_4_SECURITY_TRUST_BOUNDARY_EXPANSION = NO`

The projection must not include secrets, credentials, transient provider
sessions, external verifier state, unnecessary payload duplication, stack
traces, filesystem paths, network state, or implementation-specific
diagnostics.

Tenant, subject, environment, scope, provenance, integrity, trusted-time,
freshness, replay, substitution, and sensitive-data-minimization semantics
remain unchanged.

## 27. Eligibility and Conformance Non-Drift

The only Phase 4 eligibility classifications remain `ELIGIBLE`, `INELIGIBLE`,
`QUARANTINED`, `UNSUPPORTED`, and `PROCESSING_FAILURE`.

Eligibility remains pre-conformance.

This clarification does not authorize `CONFORMANT`, `NON_CONFORMANT`,
`INCONCLUSIVE`, `STALE`, or another conformance result as an eligibility
outcome.

## 28. Cross-Program Non-Drift

`DISPOSITION_A = PHASE_4_DOES_NOT_REQUIRE_ARCHITECTURE_TRUTH_CONTRACT_WORK`

`ARCP_WORKING_LABEL = ARCP`

`ARCP_CANONICAL_NAME = UNRESOLVED_PENDING_NEXUS_PHASE_19_GOVERNANCE`

`ARCP_CANONICAL_SEMANTICS = UNRESOLVED_PENDING_NEXUS_PHASE_19_GOVERNANCE`

`NEXUS_PHASE_19_DIRECTION = RESERVED_UPSTREAM_ARCHITECTURE_DIRECTION`

`NEXUS_PHASE_19_CANONICAL_CAPABILITY_NAME = MUST_BE_VERIFIED_FROM_CANONICAL_NEXUS_STATE`

This clarification creates no NEXUS, ARCP, ATA, architecture-truth,
integration, or runtime authority.

## 29. Historical and Implementation Non-Drift

This clarification is prospective. Historical Phase 4 planning and prior non-
canonical implementation candidates are not rewritten.

No prior implementation candidate receives retroactive acceptance.

After this clarification becomes canonical and State 2 is established, any
future Phase 4 implementation candidate must be a fresh candidate prepared
against the repaired canonical state.

The future implementation-contract path must resolve implementation details,
including the exact stable Phase 4 failure-code binding required by Section 22,
before source/test implementation may be accepted.

`IMPLEMENTATION_AUTHORITY = NONE`

## 30. Clarification Effective Point and State 2

The clarification does not consume State 1 merely by being prepared, reviewed,
frozen, hashed, materialized, staged, committed, published, placed in a pull
request, marked Ready, authorized for merge, or merged.

State 2 may be established only if all separately governed clarification gates
complete successfully, including exact two-document preimage preparation,
independent integrated adversarial acceptance, blocker resolution if required,
exact-content freeze, serialization freeze, SHA-256 computation/freeze,
post-freeze reverification, exact materialization, staging, commit, remote
publication, Draft PR, independent PR acceptance, Draft-to-Ready transition,
Ready-state verification, explicit merge authorization, exact two-parent
canonical merge, independent post-merge verification, local/remote convergence,
and clean canonical worktree/index verification.

After and only after the complete clarification effective point:

`STATE_2 = CONSUMED_PENDING_CLOSURE`

`AFR_PHASE_4_NORMALIZED_EVIDENCE_BYTES_SEMANTIC_AMENDMENT_AUTHORITY = CONSUMED_PENDING_CLOSURE`

`NORMALIZED_EVIDENCE_BYTES_CANONICAL_MEASUREMENT = BYTE_LENGTH_OF_CANONICAL_PRE_CONSTRUCTION_NORMALIZED_EVIDENCE_PROJECTION`

`IMPLEMENTATION_AUTHORITY = NONE`

State 3 still requires separately governed canonical closure.

## 31. Required Clarification Merge Topology

`FROZEN_BASE = d618688cb2b54e319d73e6cb70f3a2f8e19c9c92`

`MERGE_PARENT_COUNT = 2`

`MERGE_PARENT_1 = FROZEN_BASE`

`MERGE_PARENT_2 = VERIFIED_HEAD`

`MERGE_TREE = VERIFIED_HEAD_TREE`

`SQUASH_MERGE = PROHIBITED`

`REBASE_MERGE = PROHIBITED`

`FAST_FORWARD_SUBSTITUTION = PROHIBITED`

`CHANGED_HEAD = PROHIBITED`

`CHANGED_TREE = PROHIBITED`

A moved base or changed head/tree requires a new governance decision.

## 32. No Automatic Implementation or Phase Transition

Canonical semantic clarification would resolve the normalized-evidence-bytes
semantic stop only. It would not itself authorize implementation.

A fresh Phase 4 implementation candidate and separately governed
implementation-authority path remain required before executable work.

Phase 5 remains unauthorized unless and until Phase 4 implementation and its
required closure are separately completed and a Phase 5 authority path is
established.

No gate implies the next.
