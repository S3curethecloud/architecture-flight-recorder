# AFR Continuous Conformance Evaluation Runtime Contract

## 1. Contract posture

`CONTRACT_STATUS=DETACHED_PLANNING_CANDIDATE_NONCANONICAL`

This candidate defines the future deterministic execution contract for Phase 11
continuous conformance evaluation. It grants no execution authority.

## 2. Predecessor bindings

- AFR predecessor main: `14a75d02aa7dfa7c254a56bcf66030937ef9e48c`
- AFR predecessor tree: `b39815ce431f6502ce4cb7b7a645a1ebbb428d7e`
- Phase 10 closure SHA-256: `4e983e35256030c33ce4bbc3f3e41e2417c39cdc02234c5fe4ef1032bb001383`
- qualified NEXUS anchor: `ef1c048ef3c6daaca2f6f1d35fd52341227843b5`
- NEXUS consumer contract ID: `NEXUS_TO_AFR_ARCHITECTURE_TRUTH_CONSUMER_CONTRACT_V1`
- NEXUS consumer contract SHA-256: `a6abb49d5536de89d21131abf7d2d717a242f33b1e4c4f9d8966bd48dc465246`

## 3. Contract principle

One authoritative Phase 11 runtime evaluation is valid only when every mandatory
truth, evidence-binding, identity, scope, version, policy, time, concurrency, and
kernel condition is resolved deterministically.

## 4. Required future request fields

A future executable contract must classify exact required fields. At minimum it
must be able to bind:

`request_contract_version`
`request_id`
`tenant_id`
`subject_id`
`environment_id`
`release_id`
`qualified_truth_reference_id`
`truth_evidence_binding_id`
`claim_set_id`
`evaluation_definition_id`
`evaluation_definition_version`
`conformance_policy_id`
`conformance_policy_version`
`evaluator_id`
`evaluator_version`
`trusted_time_context_id`
`canonicalization_version`
`fingerprint_version`
`requested_scope_id`

No transport identifier may substitute for a missing authoritative field.

## 5. Evaluation-cycle identity contract

The cycle identity must be deterministically derived from canonical material request
fields and exact referenced immutable identities. The covered-field set, ordering,
encoding, null/absence semantics, and digest algorithm must be explicit before
implementation.

Two requests with identical material canonical inputs must not produce different
cycle identities because of delivery time, queue offset, filesystem path, or map
iteration order.

## 6. Attempt identity contract

An execution attempt is distinct from the evaluation cycle. Each attempt must have:

- one cycle identity;
- one attempt identity;
- attempt start and terminal state;
- evaluator/runtime implementation identity;
- deterministic reason for retry or failure when applicable.

Attempt identity cannot become the authoritative evaluation identity.

## 7. Admission contract

Execution admission must fail closed when any required condition is unresolved,
including:

- unqualified truth;
- non-admitted or mismatched evidence binding;
- tenant or subject mismatch;
- environment or release mismatch where material;
- unsupported contract, policy, evaluator, canonicalization, or fingerprint version;
- unresolved trusted time;
- stale mandatory evidence where current evidence is required;
- invalid requested scope;
- unresolved concurrency conflict;
- missing deterministic kernel authority or identity.

## 8. Reevaluation trigger contract

A candidate trigger may reference one or more material changes:

- admitted evidence-binding change;
- qualified truth change;
- policy or evaluation-definition change;
- evaluator or canonicalization change;
- freshness deadline crossing;
- explicit bounded operator request.

Trigger qualification creates no conformance result. The future runtime must derive
a complete cycle identity and pass execution admission separately.

## 9. Duplicate and idempotency contract

Duplicate delivery of equivalent material request content must resolve to the same
cycle identity. Deduplication must preserve observable delivery and attempt history.
A duplicate cannot create a second conflicting authoritative terminal result.

## 10. Concurrency contract

The accepted implementation must define one deterministic acceptance rule for
competing attempts. At most one terminal result may be accepted for one cycle
identity. A late or duplicate result must be rejected or recorded as non-authoritative
without overwriting the accepted result.

## 11. Retry contract

A retry is permitted only under an explicit retryable failure classification.
Retry cannot alter truth, evidence, policy, or evaluation input identity. If a
material input changes, the runtime must create a distinct cycle rather than calling
that change a retry.

## 12. Kernel invocation contract

The runtime may invoke only a compatible independently accepted deterministic kernel
implementation. Invocation binds exact:

- truth reference;
- claim set;
- admitted evidence binding or set;
- evaluation definition;
- policy;
- evaluator version;
- trusted time;
- scope;
- canonicalization and fingerprint versions.

Model output cannot fill a missing mandatory kernel input.

## 13. Canonical outcome contract

Phase 11 preserves the canonical claim outcomes:

- `CONFORMANT`;
- `NON_CONFORMANT`;
- `INCONCLUSIVE`;
- `STALE`.

Runtime orchestration cannot introduce a presentation-only outcome that changes the
canonical meaning or precedence of those outcomes.

## 14. Result validation contract

Before terminal acceptance, a future runtime must validate at least:

- cycle identity;
- tenant and subject scope;
- truth and evidence references;
- claim and aggregate outcomes;
- deterministic rationale references;
- policy/evaluator/version bindings;
- trusted-time and validity fields;
- limitations and unresolved conditions;
- result fingerprint;
- canonicalization version.

Validation failure blocks terminal acceptance.

## 15. Result immutability contract

An accepted terminal result is immutable. Corrections, new evidence, new truth, or
version changes require a distinct later cycle linked through supersession or
replacement metadata. Historical results cannot be rewritten as though they never
existed.

## 16. Freshness contract

The runtime must deterministically determine when a prior result may no longer
support a current assertion. Freshness policy must not use ingestion recency to hide
old observation time or convert missing current evidence into conformance.

## 17. Failure contract

Failures have explicit identities and reason codes. Runtime, transport, storage,
time, kernel, or concurrency failure cannot produce `CONFORMANT` by default.

## 18. Observability contract

Audit and telemetry projections may expose request, cycle, attempt, gate, failure,
result, and supersession state. Observability is non-authoritative and cannot mutate
an evaluation result or grant execution authority.

## 19. Phase 12 boundary

Phase 11 evaluation output is only a bounded completed evaluation input for later
governed consumers. This contract creates no drift finding, certificate, signing,
issuance, revocation, delivery, or remediation authority.

## 20. NEXUS boundary

The runtime consumes qualified NEXUS truth read-only. It cannot author, approve,
supersede, repair, or mutate NEXUS architecture truth and cannot reinterpret NEXUS
ArchitectureRisk.

## 21. Provider and ingestion boundary

This contract does not grant provider credentials, provider reads, live collection,
operational-evidence ingestion, network access, or collector deployment. Those
capabilities require separate explicit authority.

## 22. Technology deferral

This planning contract selects no programming language, API framework, scheduler,
queue, database, lock service, cache, event bus, workflow engine, cloud service,
container platform, deployment topology, or telemetry vendor.

## 23. Planning authority

`PHASE_11_IMPLEMENTATION_AUTHORITY=NONE`

`PHASE_11_RUNTIME_AUTHORITY=NONE`

`PHASE_11_CONFORMANCE_EVALUATION_EXECUTION_AUTHORITY=NONE`

`PHASE_11_OPERATIONAL_EVIDENCE_INGESTION_AUTHORITY=NONE`

`PHASE_11_PROVIDER_READ_AUTHORITY=NONE`

`PHASE_12_ENTRY_AUTHORITY=NONE`
