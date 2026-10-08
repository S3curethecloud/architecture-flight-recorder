# AFR Phase 8 First-Slice Implementation-Authority Proposal Candidate R1

## 1. Purpose

This detached noncanonical proposal candidate defines a narrowly bounded
implementation-authority path for the Phase 8 Read-Only Consumer Gateway first
slice.

It is an authority proposal only. It does not itself create implementation
authority, implement source code, mutate the repository, reopen Phase 8
planning, or activate Phase 9.

## 2. Canonical Foundation

This proposal is subordinate to the terminally closed Phase 8 planning record:

- repository: `S3curethecloud/architecture-flight-recorder`;
- canonical `main`: `09ae20b4cae4d125f52e1a9a11f2ee1c3c559fe7`;
- canonical tree: `9582cbe7f93281b18aa09dbe80d04dcb51d3db8d`;
- Phase 8 terminal closure receipt:
  `51dcb6baa1fe01925317a439c852ac02e9845b5985d713e74e41291da364454b`;
- accepted Route-A successor-scope receipt:
  `31468a7d6574474b9902f7ab2add87bc181a46d15bacad2f2145c067ac4d1aef`;
- accepted detached successor-scope candidate:
  `db53c464267bccb787a9c4ecede12a78fac9f456a54555d44a91a874a8c2d47f`;
- preparation-target manifest:
  `7fa7d9529ae60f98ede7a07c9023aa6ea0b810d7d1d9139c1b5ed0f32ade599f`.

Phase 8 planning remains terminally closed:

`AFR_PHASE_8_PLANNING_STATUS = COMPLETE`

`AFR_PHASE_8_PLANNING_AUTHORITY = CONSUMED_CLOSED`

`PHASE_8_REOPEN_AUTHORITY = NONE`

## 3. Accepted Successor Route

The accepted successor route is:

`ROUTE_A = SEPARATELY_GOVERNED_PHASE_8_FIRST_SLICE_IMPLEMENTATION_AUTHORITY_PROPOSAL`

Route A does not reinterpret Phase 8 planning and does not designate a new
Phase 9 capability.

## 4. Current Authority

Until this proposal reaches a separately governed canonical effective point:

`AFR_PHASE_8_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_8_CONSUMER_GATEWAY_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_8_NETWORK_AUTHORITY = NONE`

`AFR_PHASE_8_CREDENTIAL_AUTHORITY = NONE`

`AFR_PHASE_8_PERSISTENCE_AUTHORITY = NONE`

`AFR_PHASE_8_EXTERNAL_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_8_RUNTIME_AUTHORITY = NONE`

`AFR_PHASE_8_DEPLOYMENT_AUTHORITY = NONE`

`AFR_PHASE_8_ENFORCEMENT_AUTHORITY = NONE`

`AFR_PHASE_8_REMEDIATION_AUTHORITY = NONE`

`AFR_PHASE_8_PRODUCTION_ACCESS_AUTHORITY = NONE`

`PHASE_9_AUTHORITY = NONE`

`PHASE_9_PLANNING_AUTHORITY = NONE`

## 5. Proposed Implementation Authority

The proposed authority is:

`BOUNDED_PHASE_8_READ_ONLY_CONSUMER_GATEWAY_FIRST_SLICE_IMPLEMENTATION_ONLY`

If later activated through the complete authority-proposal lifecycle, it would
authorize only the exact pure-local implementation and deterministic validation
work described in this proposal.

It would not authorize scope expansion by implication.

## 6. Exact Future Implementation File Boundary

The complete future implementation boundary is exactly three files:

1. `src/afr/consumer_gateway/read_only_projection.py`
2. `tests/unit/consumer_gateway/test_read_only_projection.py`
3. `tests/vectors/consumer_gateway/read_only_projection-v1.json`

No fourth implementation file is authorized.

Any additional source file, package initializer, configuration file, dependency
file, schema file, fixture, generated artifact, cache, metadata file, or build
system change requires separate authority.

## 7. Implementation Character

The future slice must remain:

`PURE_LOCAL_SIDE_EFFECT_FREE_DETERMINISTIC_READ_ONLY_PROJECTION_ONLY`

The implementation may use only local in-memory inputs supplied explicitly by
the caller.

It may not discover, fetch, repair, reevaluate, mutate, refresh, persist, or
publish authoritative AFR state.

## 8. Required Logical Inputs

The implementation must require explicit bound input for:

- authoritative source identity;
- source conformance outcome;
- source findings and material limitations;
- source provenance/integrity metadata;
- source scope;
- source freshness, validity, expiry, and supersession state as applicable;
- tenant identity;
- subject identity where applicable;
- consumer identity;
- requested read scope;
- policy identifier/version;
- explicit authorization decision;
- authorization-decision identity;
- authorization-bound source, consumer, tenant, subject, scope, and policy
  context.

Missing or ambiguous mandatory context must fail closed.

## 9. Logical Result Classes

The implementation must return exactly one logical result class:

- `READ_ONLY_PROJECTION_ALLOWED`;
- `READ_ONLY_PROJECTION_DENIED`;
- `READ_ONLY_PROJECTION_FAIL_CLOSED`.

Only `READ_ONLY_PROJECTION_ALLOWED` may carry bounded projected source content.

Denial and fail-closed results must not create replacement conformance outcomes.

## 10. Authorization Binding

Authorization is an explicit supplied input and is never inferred.

An allowed projection requires exact compatible binding across:

- source identity;
- consumer identity;
- tenant;
- subject where applicable;
- requested scope;
- authorized scope;
- source scope;
- policy identifier/version;
- authorization-decision identity.

Missing, denied, ambiguous, mismatched, stale, invalid, replayed, or over-broad
authorization context must deny or fail closed.

## 11. Tenant and Subject Isolation

Tenant isolation is deny-by-default.

Cross-tenant substitution must fail closed.

Unauthorized cross-subject substitution must fail closed.

No implicit tenant or subject fallback is permitted.

No ambient process, environment, cache, model, or caller convention may supply
a missing tenant or subject identity.

## 12. Scope and Privilege Rules

Requested scope must not exceed source scope.

Requested scope must not exceed authorized consumer scope.

Scope narrowing is permitted only when the projected representation remains
truthful and retains all material limitations required to prevent semantic
strengthening.

Scope expansion and privilege expansion are prohibited.

## 13. Deterministic Projection

Identical authoritative source identity and identical bound authorization
context must produce the same logical projection result.

Projection behavior must not depend on:

- wall-clock time except explicit caller-supplied validity data;
- randomness;
- process identity;
- locale;
- environment variables;
- filesystem state;
- network state;
- mutable global state;
- generative-model output.

Stable deterministic ordering must be used wherever ordering affects the
returned representation.

## 14. Source-Semantics Preservation

The implementation must preserve the authoritative meaning of the source.

It must not:

- create or change a conformance outcome;
- convert `NON_CONFORMANT`, `INCONCLUSIVE`, or `STALE` to `CONFORMANT`;
- suppress material findings or limitations when suppression would strengthen
  apparent meaning;
- manufacture provenance, integrity, freshness, validity, expiry, or
  supersession semantics;
- strengthen integrity claims beyond the source;
- rewrite source identity;
- treat projection as new authoritative AFR truth.

## 15. Integrity Envelope

An allowed projection must carry a deterministic logical integrity envelope
that preserves attribution to:

- source identity;
- authorization-decision identity;
- tenant;
- subject where applicable;
- consumer;
- policy identifier/version;
- requested/authorized scope;
- applicable source provenance/integrity metadata;
- applicable freshness/validity state.

This slice selects no signing key, certificate, KMS, HSM, credential, or
cryptographic trust service.

## 16. Fail-Closed Conditions

The future implementation must deny or fail closed for at least:

- unresolved source identity;
- authorization absence;
- authorization denial;
- authorization/source mismatch;
- consumer mismatch;
- tenant mismatch;
- subject mismatch;
- requested-scope expansion;
- requested scope exceeding source scope;
- requested scope exceeding authorized scope;
- policy identifier/version mismatch;
- authorization-decision identity mismatch;
- stale or invalid source when current validity is required;
- source-integrity mismatch represented in the supplied context;
- unsafe limitation omission;
- malformed or unsupported deterministic vector input;
- missing mandatory context.

No fail-closed path may mutate authoritative AFR state.

## 17. Model and Agent Exclusion

Models and agents are non-authoritative for:

- authorization;
- entitlement;
- tenant or subject binding;
- policy selection;
- scope expansion;
- source eligibility;
- integrity verification;
- conformance outcome;
- limitation suppression;
- consequential action.

Generative output must never select an allowed projection result.

## 18. Side-Effect and Integration Prohibitions

The future slice must perform no:

- inbound or outbound network operation;
- API activation;
- credential or secret lookup;
- service-identity use;
- filesystem write;
- database access;
- persistence;
- cache mutation;
- queue operation;
- event publication or consumption;
- webhook operation;
- feed or stream operation;
- external adapter invocation;
- subprocess or shell invocation;
- downstream mutation;
- deployment action;
- enforcement action;
- remediation action;
- production access.

## 19. Dependency and Supply-Chain Boundary

The future three-file implementation may not add or modify a dependency,
package manifest, lock file, build file, workflow, interpreter configuration,
or toolchain configuration.

Only capabilities already available in the canonical repository/runtime may be
used.

If a new dependency or build-system mutation becomes necessary, implementation
must stop and a new authority path is required.

## 20. Deterministic Test Requirements

The unit test and deterministic vector file must cover at least:

- allowed projection with exact binding;
- explicit authorization denial;
- missing authorization;
- source substitution;
- consumer substitution;
- cross-tenant substitution;
- cross-subject substitution;
- requested-scope expansion;
- source-scope violation;
- authorized-scope violation;
- policy-version substitution;
- authorization-decision identity mismatch;
- stale/invalid source handling where current validity is required;
- material-limitation preservation;
- `NON_CONFORMANT` preservation;
- `INCONCLUSIVE` preservation;
- `STALE` preservation;
- deterministic repeatability for identical inputs;
- deterministic divergence for materially different bound inputs;
- no network dependence;
- no filesystem-write dependence;
- no environment/randomness dependence;
- models/agents having no authoritative decision role.

Tests may exercise only the single future implementation module.

## 21. Prohibited Scope

This proposal does not authorize:

- live source acquisition;
- provider adapters;
- HTTP endpoints;
- RPC endpoints;
- service deployment;
- external authentication products;
- external authorization engines;
- credential stores;
- signing infrastructure;
- persistent stores;
- caches;
- queues;
- event buses;
- webhooks;
- feeds;
- streams;
- concrete external consumer adapters;
- telemetry export;
- runtime delivery;
- production deployment;
- policy enforcement;
- remediation;
- infrastructure mutation;
- NEXUS mutation or export;
- ATA consequential runtime commit;
- Phase 9 planning or implementation.

## 22. Stop Conditions

Implementation must stop without broadening scope if:

- any fourth implementation file becomes necessary;
- any existing repository source file must be modified;
- any dependency or build configuration must change;
- Phase 8 planning semantics require amendment;
- a network, credential, persistence, external integration, runtime delivery,
  deployment, enforcement, remediation, or production path becomes necessary;
- deterministic behavior cannot be demonstrated;
- tenant, subject, source, authorization, or scope binding cannot be preserved;
- a model or agent would become authoritative;
- the exact three-file boundary becomes insufficient.

Stopping does not authorize an alternative implementation.

## 23. Required Independent Proposal Review

Before this proposal may be materialized canonically, it requires independent
review of:

- Phase 8 planning non-reopen;
- Route-A lineage;
- exact two-document proposal boundary;
- exact three-file future implementation boundary;
- contract preservation;
- authorization binding;
- tenant and subject isolation;
- scope and privilege preservation;
- source-semantics preservation;
- deterministic projection;
- fail-closed behavior;
- integrity/provenance preservation;
- model/agent exclusion;
- dependency and supply-chain constraints;
- side-effect exclusion;
- implementation-authority leakage;
- Phase 9 non-activation.

All review findings must be resolved before repository materialization
authority may be considered.

## 24. Proposal Repository Boundary

If this detached candidate is independently accepted, any future repository
proposal materialization must remain limited exactly to:

1. `docs/SOT.md`
2. `docs/phase-8/PHASE_8_FIRST_SLICE_IMPLEMENTATION_AUTHORITY_PROPOSAL.md`

No third proposal document is authorized.

## 25. Proposal Activation Effective Point

This detached candidate has no activation effect.

A future canonical implementation-authority proposal could activate the
proposed implementation authority only if a separately governed lifecycle
successfully establishes, at minimum:

1. exact accepted proposal content freeze;
2. separately authorized two-document repository materialization;
3. independent exact-boundary and semantic acceptance;
4. separately authorized staging;
5. independent index verification;
6. separately authorized commit;
7. separately authorized push;
8. exact Draft pull request;
9. independent pull-request acceptance;
10. explicit Draft-to-Ready authorization and transition;
11. explicit merge authorization;
12. merge to canonical `main`;
13. post-merge commit, ordered-parent, tree, exact-boundary, and content
    verification;
14. local and remote canonical `main` convergence;
15. clean canonical checkout, worktree, and index.

No earlier event creates Phase 8 implementation authority.

## 26. State After Future Proposal Activation

Only after the complete future proposal activation effective point may:

`AFR_PHASE_8_IMPLEMENTATION_AUTHORITY = BOUNDED_PHASE_8_READ_ONLY_CONSUMER_GATEWAY_FIRST_SLICE_IMPLEMENTATION_ONLY`

become effective.

Even then:

`AFR_PHASE_8_PLANNING_STATUS = COMPLETE`

`AFR_PHASE_8_PLANNING_AUTHORITY = CONSUMED_CLOSED`

`PHASE_8_REOPEN_AUTHORITY = NONE`

`AFR_PHASE_8_NETWORK_AUTHORITY = NONE`

`AFR_PHASE_8_CREDENTIAL_AUTHORITY = NONE`

`AFR_PHASE_8_PERSISTENCE_AUTHORITY = NONE`

`AFR_PHASE_8_EXTERNAL_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_8_RUNTIME_AUTHORITY = NONE`

`AFR_PHASE_8_DEPLOYMENT_AUTHORITY = NONE`

`AFR_PHASE_8_ENFORCEMENT_AUTHORITY = NONE`

`AFR_PHASE_8_REMEDIATION_AUTHORITY = NONE`

`AFR_PHASE_8_PRODUCTION_ACCESS_AUTHORITY = NONE`

`PHASE_9_AUTHORITY = NONE`

`PHASE_9_PLANNING_AUTHORITY = NONE`

Activation would authorize only a separately governed implementation candidate
using the exact three future implementation files. It would not itself create,
stage, commit, push, merge, deploy, or execute that implementation.

## 27. Current Detached Candidate Effect

`PROPOSAL_CLASS = DETACHED_NONCANONICAL_IMPLEMENTATION_AUTHORITY_PROPOSAL_CANDIDATE`

`PROPOSAL_IS_CANONICAL = NO`

`PROPOSAL_ACTIVATES_IMPLEMENTATION = NO`

`PROPOSAL_ACTIVATES_PHASE_9 = NO`

`REPOSITORY_MUTATION_AUTHORITY = NONE`

`AFR_PHASE_8_IMPLEMENTATION_AUTHORITY = NONE`

`PHASE_9_AUTHORITY = NONE`

## 28. R1 NONPASS Lineage and R1R1 Corrected-Replacement Status

This R1R1 corrected replacement preserves Sections 1 through 27 of rejected R1
without semantic amendment and closes only the independently reconciled
implementation-contract findings A1 through A10.

Rejected R1 identity:

`R1_REJECTED_CANDIDATE_SHA256 = c298a632542f904a58a4885ff28f765932c123e12aaeaf9206745e4aa7a6be26`

`R1_REJECTED_CANDIDATE_BYTES = 15417`

`R1_REJECTED_CANDIDATE_LINES = 520`

`R1_ACCEPTANCE = NONPASS_FINAL`

`R1_PASS_COUNT = 67`

`R1_FAIL_COUNT = 10`

`R1_BLOCKING_FINDING_COUNT = 10`

`R1_RETROACTIVE_PASS = NO`

The accepted read-only reconciliation is bound by:

`R1_NONPASS_RECONCILIATION_RECEIPT_SHA256 = 5d57f5dc7a392d0181733f24c3e07f8041b09aac0b119556724d8844313581c3`

The frozen correction manifest is:

`R1R1_CORRECTION_MANIFEST_SHA256 = 8e60e561b55f1cf3b1307194866304c5e23d9926859e51aaaf5bc651abc7b4ab`

`R1R1_CORRECTED_REPLACEMENT_ID = R1R1`

`R1R1_CHANGE_SCOPE = CLOSE_A1_THROUGH_A10_AND_RECORD_R1_NONPASS_LINEAGE_ONLY`

No R1 finding is erased or retroactively reclassified.

## 29. A1 Closure — Exact Public Executable Surface

The future implementation module public surface contains exactly thirteen
symbols:

1. `AuthorizationDecision`
2. `SourceFreshnessState`
3. `SourceValidityState`
4. `SourceExpiryState`
5. `SourceSupersessionState`
6. `ReadOnlyProjectionResultClass`
7. `ReadOnlyProjectionFailureCode`
8. `AuthorizationContext`
9. `ReadOnlyProjectionRequest`
10. `ReadOnlyProjectionIntegrityEnvelope`
11. `ReadOnlyProjectionResult`
12. `ReadOnlyProjectionContractError`
13. `evaluate_read_only_projection`

No fourteenth public symbol is authorized.

The only public executable function is exactly:

`evaluate_read_only_projection(request: ReadOnlyProjectionRequest) -> ReadOnlyProjectionResult`

It accepts exactly one positional request object.

The function is pure, local, deterministic, side-effect-free, and has no
filesystem, network, credential, environment, wall-clock, randomness,
subprocess, plugin, persistence, service-discovery, or ambient-state
dependency.

`A1_STATUS = CLOSED_BY_R1R1_EXACT_PUBLIC_SURFACE_AND_SIGNATURE`

## 30. A2 Closure — Exact AuthorizationContext Schema

`AuthorizationContext` is a frozen, slotted dataclass with exactly nine public
fields in this order:

1. `decision: AuthorizationDecision`
2. `decision_id: str`
3. `source_id: str`
4. `consumer_id: str`
5. `tenant_id: str`
6. `subject_id: str | None`
7. `authorized_scope: tuple[str, ...]`
8. `policy_id: str`
9. `policy_version: str`

There are no additional public or caller-settable fields.

All `str` values must be exact `str`, not subclasses, must be non-empty, and
must already be Unicode NFC. No normalization or repair is performed.

`subject_id` may be `None` only when subject binding is not applicable. A
request and its authorization context must use the same `subject_id` value,
including the same `None` state.

`authorized_scope` uses the exact scope representation defined in Section 36.

## 31. A2 Closure — Exact ReadOnlyProjectionRequest Schema

`ReadOnlyProjectionRequest` is a frozen, slotted dataclass with exactly twenty-
three public fields in this order:

1. `source_id: str`
2. `source_outcome: str`
3. `findings: tuple[str, ...]`
4. `limitations: tuple[str, ...]`
5. `source_provenance: object`
6. `source_integrity_metadata: object`
7. `source_scope: tuple[str, ...]`
8. `source_freshness: SourceFreshnessState`
9. `source_validity: SourceValidityState`
10. `source_expiry: SourceExpiryState`
11. `source_supersession: SourceSupersessionState`
12. `tenant_id: str`
13. `subject_id: str | None`
14. `consumer_id: str`
15. `requested_scope: tuple[str, ...]`
16. `policy_id: str`
17. `policy_version: str`
18. `authorization: AuthorizationContext`
19. `source_content: object`
20. `current_freshness_required: bool`
21. `valid_source_required: bool`
22. `unexpired_source_required: bool`
23. `unsuperseded_source_required: bool`

There are no additional public or caller-settable request fields.

The exact permitted `source_outcome` values are:

- `CONFORMANT`
- `NON_CONFORMANT`
- `INCONCLUSIVE`
- `STALE`

No other source-outcome value is accepted.

`findings` and `limitations` are exact tuples of exact non-empty NFC strings.
Their order is authoritative input order and is preserved exactly. Duplicate
entries are permitted only when they are already part of the authoritative
source representation; the projection may not silently remove or reorder them.

`source_provenance`, `source_integrity_metadata`, and `source_content` are deep-
snapshotted according to Section 39 before the request becomes valid.

Each of the four `*_required` members is an exact `bool`. They express explicit
caller-supplied applicability requirements and are not inferred from wall-clock
or ambient policy state.

`A2_STATUS = CLOSED_BY_R1R1_EXACT_FROZEN_SLOTTED_INPUT_SCHEMAS`

## 32. A3 Closure — Exact Integrity-Envelope Schema

`ReadOnlyProjectionIntegrityEnvelope` is a frozen, slotted dataclass with
exactly sixteen public fields in this order:

1. `source_id: str`
2. `authorization_decision_id: str`
3. `tenant_id: str`
4. `subject_id: str | None`
5. `consumer_id: str`
6. `policy_id: str`
7. `policy_version: str`
8. `requested_scope: tuple[str, ...]`
9. `authorized_scope: tuple[str, ...]`
10. `source_scope: tuple[str, ...]`
11. `source_provenance: object`
12. `source_integrity_metadata: object`
13. `source_freshness: SourceFreshnessState`
14. `source_validity: SourceValidityState`
15. `source_expiry: SourceExpiryState`
16. `source_supersession: SourceSupersessionState`

The envelope is a logical integrity/attribution envelope only. It is not a
signature, certificate, token, credential, proof of authorization beyond the
supplied decision, or stronger integrity claim than the source provides.

## 33. A3 Closure — Exact Result Schema and Class Invariants

`ReadOnlyProjectionResult` is a frozen, slotted dataclass with exactly eight
public fields in this order:

1. `result_class: ReadOnlyProjectionResultClass`
2. `failure_code: ReadOnlyProjectionFailureCode | None`
3. `failure_field: str | None`
4. `source_outcome: str | None`
5. `projected_content: object | None`
6. `findings: tuple[str, ...]`
7. `limitations: tuple[str, ...]`
8. `integrity_envelope: ReadOnlyProjectionIntegrityEnvelope | None`

For `READ_ONLY_PROJECTION_ALLOWED`:

- `failure_code` is `None`;
- `failure_field` is `None`;
- `source_outcome` is the exact authoritative input outcome;
- `projected_content` is the immutable deterministic scope-narrowed projection
  selected from `source_content` by the exact `requested_scope`;
- `findings` and `limitations` preserve the exact request tuples;
- `integrity_envelope` is present and exactly bound to the request and
  authorization context.

For `READ_ONLY_PROJECTION_DENIED`:

- `failure_code` is exactly `AUTHORIZATION_DENIED`;
- `failure_field` is exactly `authorization.decision`;
- `source_outcome` is `None`;
- `projected_content` is `None`;
- `findings` is `()`;
- `limitations` is `()`;
- `integrity_envelope` is `None`.

For `READ_ONLY_PROJECTION_FAIL_CLOSED`:

- `failure_code` is a non-denial value from Section 34;
- `failure_field` is a non-empty exact field-path string;
- `source_outcome` is `None`;
- `projected_content` is `None`;
- `findings` is `()`;
- `limitations` is `()`;
- `integrity_envelope` is `None`.

A result object violating these invariants is prohibited.

`A3_STATUS = CLOSED_BY_R1R1_EXACT_RESULT_AND_ENVELOPE_SCHEMAS`

## 34. A4 Closure — Exact Result Classes and Stable Failure Codes

`ReadOnlyProjectionResultClass` is a string enum with exactly three values:

- `READ_ONLY_PROJECTION_ALLOWED`
- `READ_ONLY_PROJECTION_DENIED`
- `READ_ONLY_PROJECTION_FAIL_CLOSED`

`ReadOnlyProjectionFailureCode` is a string enum with exactly twelve values:

1. `AUTHORIZATION_DENIED`
2. `SOURCE_BINDING_MISMATCH`
3. `CONSUMER_BINDING_MISMATCH`
4. `TENANT_BINDING_MISMATCH`
5. `SUBJECT_BINDING_MISMATCH`
6. `POLICY_BINDING_MISMATCH`
7. `REQUESTED_SCOPE_EXCEEDS_SOURCE_SCOPE`
8. `REQUESTED_SCOPE_EXCEEDS_AUTHORIZED_SCOPE`
9. `SOURCE_FRESHNESS_UNACCEPTABLE`
10. `SOURCE_VALIDITY_UNACCEPTABLE`
11. `SOURCE_EXPIRY_UNACCEPTABLE`
12. `SOURCE_SUPERSESSION_UNACCEPTABLE`

`AUTHORIZATION_DENIED` binds only to `READ_ONLY_PROJECTION_DENIED`.

All other failure codes bind only to `READ_ONLY_PROJECTION_FAIL_CLOSED`.

Invalid Python types, unsupported enum values, malformed exact tuples,
non-NFC strings, prohibited nested content types, cycles, and invalid resource
shape are construction-contract failures raised as
`ReadOnlyProjectionContractError`; they do not become conformance outcomes.

`A4_STATUS = CLOSED_BY_R1R1_STABLE_RESULT_AND_FAILURE_TAXONOMY`

## 35. A5 Closure — Exact Authorization and Source-State Value Domains

`AuthorizationDecision` is a string enum with exactly:

- `ALLOW`
- `DENY`

`DENY` deterministically returns `READ_ONLY_PROJECTION_DENIED` with
`AUTHORIZATION_DENIED` and exposes no source content.

`ALLOW` does not itself authorize projection. All binding, scope, source-state,
and contract checks must also pass.

`SourceFreshnessState` is a string enum with exactly:

- `CURRENT`
- `STALE`
- `UNKNOWN`

`SourceValidityState` is a string enum with exactly:

- `VALID`
- `INVALID`
- `UNKNOWN`

`SourceExpiryState` is a string enum with exactly:

- `NOT_EXPIRED`
- `EXPIRED`
- `UNKNOWN`

`SourceSupersessionState` is a string enum with exactly:

- `CURRENT`
- `SUPERSEDED`
- `UNKNOWN`

When the corresponding request applicability boolean is `True`, only the
positive state is acceptable:

- `current_freshness_required=True` requires `CURRENT`;
- `valid_source_required=True` requires `VALID`;
- `unexpired_source_required=True` requires `NOT_EXPIRED`;
- `unsuperseded_source_required=True` requires `CURRENT`.

When the corresponding applicability boolean is `False`, the source state is
preserved in the allowed envelope and source semantics; it is not upgraded,
rewritten, or hidden.

`A5_STATUS = CLOSED_BY_R1R1_EXACT_AUTHORIZATION_AND_STATE_VALUE_DOMAINS`

## 36. A6 Closure — Exact Scope Representation

Every scope value in `source_scope`, `requested_scope`, and
`authorization.authorized_scope` is represented as an exact tuple of exact
non-empty NFC strings.

The tuple must satisfy all of the following before evaluation:

1. every member is exact `str`, not a subclass;
2. every member is already Unicode NFC;
3. no member is empty;
4. members are strictly ascending by their UTF-8 byte sequence;
5. no two members are equal;
6. no normalization, sorting, deduplication, wildcard expansion, prefix
   interpretation, hierarchy inference, or repair occurs inside evaluation.

Scope tokens are opaque. A token grants exactly itself and has no implicit
parent, child, prefix, suffix, glob, regex, or namespace meaning.

The deterministic subset relation is exact tuple-set membership over these
already sorted unique opaque tokens.

The implementation must use an order-preserving two-pointer subset comparison
or an equivalent algorithm whose result is identical for all valid tuples.

An allowed result requires both:

`requested_scope SUBSET_OF source_scope`

and:

`requested_scope SUBSET_OF authorization.authorized_scope`

Failure of the first relation returns
`REQUESTED_SCOPE_EXCEEDS_SOURCE_SCOPE`.

Failure of the second returns
`REQUESTED_SCOPE_EXCEEDS_AUTHORIZED_SCOPE`.

`source_content` is an exact dict whose top-level keys are the exact scope
tokens in `source_scope`. After deterministic validation and deep snapshot, the
top-level frozen mapping contains exactly one entry for each `source_scope`
token and no other entry.

For an allowed result, projection selects exactly the top-level entries whose
keys are in `requested_scope`, preserving canonical scope-token order. No value
inside a selected scope entry is filtered or rewritten. No unrequested
top-level scope entry may appear in `projected_content`.

An empty requested scope is valid only if represented exactly as `()` and
produces an empty immutable projected-content mapping.

`A6_STATUS = CLOSED_BY_R1R1_SORTED_UNIQUE_OPAQUE_SCOPE_TUPLE_CONTRACT`

## 37. Exact Authorization-Binding Evaluation Order

For a valid constructed request, `evaluate_read_only_projection` performs the
following checks in this exact order and returns at the first non-passing step:

1. if `authorization.decision` is `DENY`, return `AUTHORIZATION_DENIED`;
2. require `authorization.source_id == source_id`, otherwise
   `SOURCE_BINDING_MISMATCH`;
3. require `authorization.consumer_id == consumer_id`, otherwise
   `CONSUMER_BINDING_MISMATCH`;
4. require `authorization.tenant_id == tenant_id`, otherwise
   `TENANT_BINDING_MISMATCH`;
5. require `authorization.subject_id == subject_id`, including identical
   `None`, otherwise `SUBJECT_BINDING_MISMATCH`;
6. require both `authorization.policy_id == policy_id` and
   `authorization.policy_version == policy_version`, otherwise
   `POLICY_BINDING_MISMATCH`;
7. require `requested_scope` subset of `source_scope`, otherwise
   `REQUESTED_SCOPE_EXCEEDS_SOURCE_SCOPE`;
8. require `requested_scope` subset of `authorization.authorized_scope`,
   otherwise `REQUESTED_SCOPE_EXCEEDS_AUTHORIZED_SCOPE`;
9. if `current_freshness_required`, require `source_freshness == CURRENT`,
   otherwise `SOURCE_FRESHNESS_UNACCEPTABLE`;
10. if `valid_source_required`, require `source_validity == VALID`, otherwise
    `SOURCE_VALIDITY_UNACCEPTABLE`;
11. if `unexpired_source_required`, require `source_expiry == NOT_EXPIRED`,
    otherwise `SOURCE_EXPIRY_UNACCEPTABLE`;
12. if `unsuperseded_source_required`, require
    `source_supersession == CURRENT`, otherwise
    `SOURCE_SUPERSESSION_UNACCEPTABLE`;
13. return `READ_ONLY_PROJECTION_ALLOWED` with the exact immutable source
    snapshot, source outcome, findings, limitations, and integrity envelope.

No later check may override an earlier result.

## 38. A7 Closure — Deterministic Vector Schema Version 1.0.0

The vector file is exactly:

`tests/vectors/consumer_gateway/read_only_projection-v1.json`

Its top-level JSON object contains exactly two members:

1. `schema_version`
2. `cases`

`schema_version` is exactly the JSON string `"1.0.0"`.

`cases` is a JSON array preserving file order.

Each case object contains exactly three members:

1. `case_id`
2. `request`
3. `expected_result`

`case_id` is a unique non-empty NFC JSON string.

The `request` object contains exactly the twenty-three members from Section 31
using the same names. Enum values are encoded as their exact string values.
Tuples are encoded as JSON arrays. `subject_id` may be JSON null. The three
deep-snapshot object members use only the JSON-compatible subset of the domain
in Section 39.

The nested `authorization` object contains exactly the nine members from
Section 30 using the same names.

The `expected_result` object contains exactly eight members:

1. `result_class`
2. `failure_code`
3. `failure_field`
4. `source_outcome`
5. `projected_content`
6. `findings`
7. `limitations`
8. `integrity_envelope`

Nullable result fields are represented by JSON null. Tuple-valued fields use
JSON arrays. For denied/fail-closed cases, `projected_content` and
`integrity_envelope` are JSON null and `findings`/`limitations` are empty
arrays.

The vector schema has no extension members. Unknown, missing, duplicate, or
mis-typed members invalidate the vector case.

The vector file is test input only. It is not runtime configuration and grants
no authority.

`A7_STATUS = CLOSED_BY_R1R1_EXACT_VECTOR_SCHEMA_1_0_0`

## 39. A8 and A9 Closure — Exact Deep-Snapshot Domain and Resource Bounds

The deep-snapshot scalar domain is exactly:

- `None`;
- exact `bool`;
- exact `int` excluding `bool`;
- exact `str` already in Unicode NFC.

The only permitted input containers are exactly:

- exact `list`;
- exact `tuple`;
- exact `dict` with exact non-empty NFC `str` keys.

`source_content` has the additional root-shape requirement defined in Section
36: its root is an exact dict and its exact key set is equal to `source_scope`.
`source_provenance` and `source_integrity_metadata` may use any permitted root
scalar or container shape.

The following are prohibited:

- `float`;
- `bytes`;
- `bytearray`;
- `set`;
- `frozenset`;
- mapping subclasses;
- sequence subclasses;
- custom objects;
- generators;
- iterators;
- executable or pickled objects.

Request construction recursively snapshots accepted containers into private
immutable values before the request becomes valid.

Exact list and tuple input become private immutable tuples preserving sequence
order.

Exact dict input becomes a private immutable tuple of key/value pairs ordered
by ascending key UTF-8 bytes. Caller insertion order does not affect the
snapshot. Dict keys are not normalized or repaired; they must already be NFC.

No caller-owned mutable container reference is retained.

A caller mutation after successful request construction cannot alter the
request snapshot.

Cycles are prohibited. Cycle detection is by object identity along the active
traversal path. Shared acyclic subobjects on distinct inactive paths are
snapshotted by value independently.

Traversal must use an explicit iterative stack or another proven non-recursive
algorithm. Raw recursion-limit dependence is prohibited.

The following hard limits are fixed implementation-contract constants and are
not caller-configurable:

`MAX_SCOPE_ENTRIES = 256`

`MAX_FINDINGS = 512`

`MAX_LIMITATIONS = 512`

`MAX_CONTENT_NODES = 8192`

`MAX_CONTAINER_DEPTH = 32`

`MAX_TOTAL_STRING_UTF8_BYTES = 262144`

`MAX_SCOPE_ENTRIES` applies separately to `source_scope`, `requested_scope`,
and `authorization.authorized_scope`.

`MAX_FINDINGS` applies to `findings` and `MAX_LIMITATIONS` applies to
`limitations`.

`MAX_CONTENT_NODES` is the combined node count across `source_provenance`,
`source_integrity_metadata`, and `source_content`. Each scalar counts as one
node. Each list/tuple/dict container counts as one node. Dict keys do not add a
node but their UTF-8 bytes count toward the string-byte limit.

Root container depth is `1`; each nested container increments depth by one.
Scalars do not increment depth beyond the containing level. An empty root
container therefore has depth `1`.

`MAX_TOTAL_STRING_UTF8_BYTES` is the combined UTF-8 byte length of every
string-valued request field, subject string when present, all three scope
tuples, findings, limitations, authorization string fields, and every nested
dict key or string scalar in the three snapshotted object members. Each
occurrence is counted independently.

Construction checks limits while snapshotting and stops before retaining a
partial governed snapshot.

Exceeding a hard resource bound raises `ReadOnlyProjectionContractError` with
field path `resource_limits` and reason `RESOURCE_LIMIT_EXCEEDED`. This is a
fail-closed programming/input-contract rejection and exposes no projected
content. It is not a `ReadOnlyProjectionFailureCode` because no valid request
object exists to evaluate.

`A8_STATUS = CLOSED_BY_R1R1_VERSION_FIXED_DETERMINISTIC_RESOURCE_BOUNDS`

`A9_STATUS = CLOSED_BY_R1R1_DEEP_SNAPSHOT_IMMUTABILITY_CONTRACT`

## 40. ReadOnlyProjectionContractError Contract

`ReadOnlyProjectionContractError` subclasses `ValueError` and exposes exactly
two read-only attributes:

1. `field_path: str`
2. `reason: str`

It is raised only for invalid direct-call construction or invalid immutable
input-contract state, including:

- wrong exact type;
- unsupported enum object;
- empty required string;
- non-NFC string;
- invalid scope tuple order or duplicate;
- unsupported nested type;
- cyclic content;
- resource-bound excess;
- invalid dataclass invariant.

It is not a conformance outcome, authorization decision, remediation signal,
runtime permission, or substitute for an AFR source outcome.

## 41. A10 Closure — Exact Source Import Boundary

`src/afr/consumer_gateway/read_only_projection.py` may contain exactly these
five import statements and no other source-module imports:

1. `from __future__ import annotations`
2. `from dataclasses import dataclass as _dataclass`
3. `from enum import Enum as _Enum`
4. `from typing import Any as _Any`
5. `import unicodedata as _unicodedata`

All other import statements in the source module are prohibited.

In particular, the source module may not import:

- `afr.kernel`;
- `afr.eligibility`;
- another AFR phase implementation;
- `json`;
- `os`;
- `sys`;
- `time`;
- `datetime`;
- `random`;
- `secrets`;
- `hashlib`;
- `subprocess`;
- `socket`;
- any network library;
- any third-party package.

The source module must not dynamically import modules or load plugins.

The unit test may import the future source module and Python standard-library
helpers already present in the execution environment, but it may not introduce
or require a dependency, package, lock-file, build, or workflow change.

`A10_STATUS = CLOSED_BY_R1R1_EXACT_SOURCE_IMPORT_BOUNDARY`

## 42. R1R1 Required Test/Vector Coverage

The exact two test artifacts must prove at least:

1. exact public symbol count and function signature;
2. frozen/slotted request and authorization context behavior;
3. exact result/envelope invariants;
4. DENY produces only the denied class and no source content;
5. ALLOW still fails closed on every binding mismatch;
6. source, consumer, tenant, subject, and policy substitution failures;
7. source-scope and authorized-scope subset failures independently;
8. exact source-content top-level key equality to `source_scope`;
9. deterministic requested-scope narrowing excludes every unrequested
   top-level scope entry;
10. opaque scope tokens have no prefix/wildcard semantics;
11. scope tuple ordering, duplicate, type, NFC, and cardinality rejection;
12. each explicit source-state applicability requirement;
13. preservation of `NON_CONFORMANT`, `INCONCLUSIVE`, and `STALE` outcomes;
14. exact findings and limitations preservation;
15. integrity-envelope attribution equality;
16. caller mutation after request construction cannot alter governed content;
17. exact list/tuple/dict snapshot behavior;
18. dict-order independence;
19. prohibited nested scalar/container rejection;
20. cycle rejection and shared-acyclic-subobject acceptance;
21. each fixed deterministic resource limit at boundary and boundary+1;
22. total string UTF-8 byte accounting;
23. vector-schema exact-member acceptance and unknown/missing-member rejection;
24. deterministic repeated evaluation equality;
25. source module has exactly the five authorized imports;
26. no filesystem, network, environment, wall-clock, randomness, subprocess,
    plugin, persistence, credential, or external-service dependency.

Testing does not activate implementation authority or runtime delivery.

## 43. R1R1 Corrected-Replacement Authority State

This R1R1 candidate is still detached and noncanonical.

`PROPOSAL_CLASS = DETACHED_NONCANONICAL_IMPLEMENTATION_AUTHORITY_PROPOSAL_CANDIDATE`

`R1R1_CORRECTED_REPLACEMENT = YES`

`R1R1_PROPOSAL_IS_CANONICAL = NO`

`R1R1_PROPOSAL_ACTIVATES_IMPLEMENTATION = NO`

`R1R1_PROPOSAL_ACTIVATES_PHASE_9 = NO`

`REPOSITORY_MUTATION_AUTHORITY = NONE`

`REPOSITORY_PREIMAGE_PREPARATION_AUTHORITY = NONE`

`AFR_PHASE_8_PLANNING_STATUS = COMPLETE`

`AFR_PHASE_8_PLANNING_AUTHORITY = CONSUMED_CLOSED`

`PHASE_8_REOPEN_AUTHORITY = NONE`

`AFR_PHASE_8_IMPLEMENTATION_AUTHORITY = NONE`

`PHASE_9_AUTHORITY = NONE`

`PHASE_9_PLANNING_AUTHORITY = NONE`

Only an independent acceptance review of this exact corrected replacement may
consider whether the A1 through A10 findings are closed. No authority follows
from candidate preparation alone.
## 44. R1R1 Independent-Acceptance NONPASS Lineage and R1R2 Status

The R1R1 corrected replacement remains historical noncanonical review evidence.

Its independent acceptance review recorded:

- review result: `NONPASS`;
- review pass count: `74`;
- review fail count: `3`;
- substantive blocking findings: `2`;
- substantive finding B1:
  `POST_ACTIVATION_CONSUMER_GATEWAY_IMPLEMENTATION_AUTHORITY_STATE_NOT_EXPLICITLY_REBOUND_FROM_NONE_TO_THE_PROPOSED_BOUNDED_AUTHORITY`;
- substantive finding B2:
  `EXACT_FAILURE_FIELD_MAPPING_NOT_DEFINED_FOR_ELEVEN_FAIL_CLOSED_RESULT_CODES`;
- one additional failed check was reconciled as review-harness defect
  `HD_PROJECTED_CONTENT_NONLEAKAGE_LINE_WRAP_MATCHER_R1`;
- the candidate's projected-content non-leakage semantics were independently
  reverified and require no candidate correction.

The immutable lineage inputs are:

`R1R1_INDEPENDENT_ACCEPTANCE_RECEIPT_SHA256 = 4a01f46db4d2f3a89efefcd513edb78e9203990515b36de04c3404fc4f86e974`

`R1R1_NONPASS_RECONCILIATION_RECEIPT_SHA256 = ed2933c636f442f240608feb4aef76b5989e35a0c85c88f4e1c271c5063069df`

`R1R2_CORRECTION_MANIFEST_SHA256 = 3488f194610dc636a8dc905a74e0b41388c75d33973cd373da66fd8f4b0c4a4a`

`R1R1_ACCEPTANCE = NONPASS_FINAL`

`R1R1_RETROACTIVE_PASS = NO`

`R1R2_CORRECTED_REPLACEMENT_ID = R1R2`

`R1R2_CHANGE_SCOPE = CLOSE_B1_B2_AND_RECORD_R1R1_NONPASS_LINEAGE_ONLY`

Sections 1 through 43 above remain the exact byte-for-byte R1R1 prefix.

No R1R1 text is rewritten, deleted, reordered, or retroactively accepted.

## 45. B1 Closure — Atomic Post-Activation Consumer-Gateway Authority Binding

Before the complete proposal activation effective point, the current authority
state remains exactly:

`AFR_PHASE_8_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_8_CONSUMER_GATEWAY_IMPLEMENTATION_AUTHORITY = NONE`

The detached R1R2 candidate itself creates no implementation authority.

If and only if the complete proposal activation effective point defined by the
proposal lifecycle is later established, the two implementation-authority
bindings become effective atomically and must be exactly:

`AFR_PHASE_8_IMPLEMENTATION_AUTHORITY = BOUNDED_PHASE_8_READ_ONLY_CONSUMER_GATEWAY_FIRST_SLICE_IMPLEMENTATION_ONLY`

`AFR_PHASE_8_CONSUMER_GATEWAY_IMPLEMENTATION_AUTHORITY = BOUNDED_PHASE_8_READ_ONLY_CONSUMER_GATEWAY_FIRST_SLICE_IMPLEMENTATION_ONLY`

The generic Phase 8 implementation authority and the Consumer Gateway-specific
implementation authority are two names for the same bounded activation state at
that effective point.

They must never disagree.

If either post-activation binding is absent, differs, is broader, or becomes
effective at a different point, the bounded implementation authority is not
established.

No other authority changes at this effective point.

In particular, all of the following remain `NONE`:

- `AFR_PHASE_8_API_AUTHORITY`;
- `AFR_PHASE_8_EVENT_AUTHORITY`;
- `AFR_PHASE_8_QUEUE_AUTHORITY`;
- `AFR_PHASE_8_WEBHOOK_AUTHORITY`;
- `AFR_PHASE_8_FEED_AUTHORITY`;
- `AFR_PHASE_8_NETWORK_AUTHORITY`;
- `AFR_PHASE_8_CREDENTIAL_AUTHORITY`;
- `AFR_PHASE_8_PERSISTENCE_AUTHORITY`;
- `AFR_PHASE_8_EXTERNAL_INTEGRATION_AUTHORITY`;
- `AFR_PHASE_8_RUNTIME_AUTHORITY`;
- `AFR_PHASE_8_DEPLOYMENT_AUTHORITY`;
- `AFR_PHASE_8_ENFORCEMENT_AUTHORITY`;
- `AFR_PHASE_8_REMEDIATION_AUTHORITY`;
- `AFR_PHASE_8_PRODUCTION_ACCESS_AUTHORITY`;
- `PHASE_9_AUTHORITY`;
- `PHASE_9_PLANNING_AUTHORITY`.

`B1_STATUS = CLOSED_BY_R1R2_ATOMIC_GENERIC_AND_CONSUMER_GATEWAY_POST_ACTIVATION_AUTHORITY_BINDING`

## 46. B2 Closure — Exact Deterministic Failure-Field Mapping

For `READ_ONLY_PROJECTION_DENIED`, the existing exact mapping is preserved:

`AUTHORIZATION_DENIED -> authorization.decision`

For `READ_ONLY_PROJECTION_FAIL_CLOSED`, `failure_field` is determined only by
the exact stable `failure_code` using this complete eleven-entry mapping:

1. `SOURCE_BINDING_MISMATCH -> authorization.source_id`
2. `CONSUMER_BINDING_MISMATCH -> authorization.consumer_id`
3. `TENANT_BINDING_MISMATCH -> authorization.tenant_id`
4. `SUBJECT_BINDING_MISMATCH -> authorization.subject_id`
5. `POLICY_BINDING_MISMATCH -> authorization`
6. `REQUESTED_SCOPE_EXCEEDS_SOURCE_SCOPE -> requested_scope`
7. `REQUESTED_SCOPE_EXCEEDS_AUTHORIZED_SCOPE -> authorization.authorized_scope`
8. `SOURCE_FRESHNESS_UNACCEPTABLE -> source_freshness`
9. `SOURCE_VALIDITY_UNACCEPTABLE -> source_validity`
10. `SOURCE_EXPIRY_UNACCEPTABLE -> source_expiry`
11. `SOURCE_SUPERSESSION_UNACCEPTABLE -> source_supersession`

No alias, alternate path, implementation-selected field, empty string, or
`None` is permitted for these eleven fail-closed codes.

The exact evaluation order in Section 37 determines the first failing
`failure_code`; this mapping then determines the corresponding `failure_field`
without further choice.

Therefore identical valid request inputs produce the same first failure code and
the same externally observable failure field.

The `POLICY_BINDING_MISMATCH` mapping is intentionally the aggregate field path
`authorization` because the frozen evaluation step jointly checks
`authorization.policy_id` and `authorization.policy_version` and emits one
stable failure code for either mismatch.

`B2_FAILURE_FIELD_MAPPING_COUNT = 11`

`B2_STATUS = CLOSED_BY_R1R2_EXACT_FAILURE_CODE_TO_FAILURE_FIELD_MAPPING`

## 47. Reconciled Review-Harness Defect Preservation

The review-harness defect

`HD_PROJECTED_CONTENT_NONLEAKAGE_LINE_WRAP_MATCHER_R1`

is historical review evidence only.

It was caused by a fixed-string matcher requiring the semantic sentence to
exist on one physical line even though the R1R1 candidate wrapped the same
sentence across two physical lines.

The candidate semantic rule remains unchanged and accepted:

No unrequested top-level scope entry may appear in `projected_content`.

`HD_PROJECTED_CONTENT_NONLEAKAGE_CANDIDATE_CORRECTION_REQUIRED = NO`

`HD_PROJECTED_CONTENT_NONLEAKAGE_CANDIDATE_SEMANTIC_STATUS = PRESERVED_PASS`

## 48. R1R2 Corrected-Replacement Authority State

This R1R2 candidate is detached and noncanonical.

`PROPOSAL_CLASS = DETACHED_NONCANONICAL_IMPLEMENTATION_AUTHORITY_PROPOSAL_CANDIDATE`

`R1R2_CORRECTED_REPLACEMENT = YES`

`R1R2_PROPOSAL_IS_CANONICAL = NO`

`R1R2_PROPOSAL_ACTIVATES_IMPLEMENTATION = NO`

`R1R2_PROPOSAL_ACTIVATES_PHASE_9 = NO`

`REPOSITORY_MUTATION_AUTHORITY = NONE`

`REPOSITORY_PREIMAGE_PREPARATION_AUTHORITY = NONE`

`AFR_PHASE_8_PLANNING_STATUS = COMPLETE`

`AFR_PHASE_8_PLANNING_AUTHORITY = CONSUMED_CLOSED`

`PHASE_8_REOPEN_AUTHORITY = NONE`

`AFR_PHASE_8_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_8_CONSUMER_GATEWAY_IMPLEMENTATION_AUTHORITY = NONE`

`PHASE_9_AUTHORITY = NONE`

`PHASE_9_PLANNING_AUTHORITY = NONE`

The future implementation boundary remains exactly three files:

1. `src/afr/consumer_gateway/read_only_projection.py`
2. `tests/unit/consumer_gateway/test_read_only_projection.py`
3. `tests/vectors/consumer_gateway/read_only_projection-v1.json`

`FUTURE_INIT_FILE = NONE`

`FUTURE_DEPENDENCY_CHANGE = NONE`

`FUTURE_BUILD_CONFIG_CHANGE = NONE`

Only an independent acceptance review of this exact R1R2 corrected replacement
may consider whether B1 and B2 are closed and whether repository-preimage
preparation authorization review may be considered.

No authority follows from R1R2 candidate preparation alone.
