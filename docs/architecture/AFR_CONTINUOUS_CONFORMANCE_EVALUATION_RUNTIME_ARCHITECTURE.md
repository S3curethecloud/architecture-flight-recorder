# AFR Continuous Conformance Evaluation Runtime Architecture

## 1. Architectural purpose

Phase 11 defines the technology-neutral runtime architecture for repeated bounded
conformance evaluations after Phase 10 has established deterministic truth and
operational-evidence binding semantics.

This is a planning artifact. It does not implement or execute the runtime.

## 2. Architectural invariants

- `NEXUS_ARCHITECTURE_TRUTH != AFR_CONFORMANCE_RESULT`
- `AFR_FINDING != NEXUS_ARCHITECTURE_RISK`
- `AFR_CONFORMANCE != NEXUS_ARCHITECTURE_ACCEPTANCE`
- `AFR_READ_AUTHORITY != NEXUS_MUTATION_AUTHORITY`
- `ADMISSIBILITY != CONFORMANCE`
- `EVALUATION_CYCLE_IDENTITY != EXECUTION_ATTEMPT_IDENTITY`
- `PHASE_11_RESULT != PHASE_12_FINDING_OR_CERTIFICATE`
- `PLANNING_AUTHORITY != RUNTIME_EXECUTION_AUTHORITY`

## 3. Input boundary

A future runtime accepts only explicitly qualified inputs:

- qualified architecture-truth reference;
- admitted Phase 10 truth-to-evidence binding or deterministic admitted set;
- evaluated claim set;
- evaluation definition;
- conformance policy;
- evaluator version;
- trusted-time context;
- canonicalization and fingerprint versions;
- bounded tenant, subject, environment, release, and evaluation scope.

A raw provider payload is not a valid runtime input merely because it is available.

## 4. Logical runtime components

### 4.1 RequestAdmission

Validates required identity, scope, authority, and version fields before a cycle
may be considered for execution.

### 4.2 EvaluationCycleIdentityBuilder

Constructs one deterministic immutable identity for the complete material input
set. Equivalent canonical inputs must resolve to the same cycle identity.

### 4.3 TriggerQualifier

Classifies a candidate reevaluation trigger without itself authorizing execution.
Trigger sources may later include new admitted evidence, new qualified truth,
version changes, freshness expiration, or explicit bounded requests.

### 4.4 ExecutionAdmissionGate

Determines whether a qualified cycle may invoke the deterministic kernel under the
future runtime authority. Planning does not activate this gate.

### 4.5 DeterministicKernelInvoker

Invokes only an independently accepted deterministic kernel implementation with
exact version and scope bindings. It cannot select rules through inference.

### 4.6 AttemptCoordinator

Tracks attempt identity, duplicate delivery, retry, concurrency, timeout, and late
completion without allowing two conflicting accepted terminal results for one
cycle identity.

### 4.7 ResultValidator

Verifies result identity, scope, outcome domain, fingerprint, limitations, and
version bindings before a result can become the terminal result for a cycle.

### 4.8 SupersessionLinker

Links a distinct later cycle to an earlier immutable result when material inputs
change. Supersession never edits the prior result.

### 4.9 AuditProjection

Produces non-authoritative observability for request, cycle, attempt, gate,
result, failure, and supersession state. Projection cannot change authority.

## 5. Planned state model

The runtime planning model distinguishes conceptual cycle states such as:

- `REQUESTED`;
- `ADMISSION_BLOCKED`;
- `READY_FOR_EXECUTION`;
- `EXECUTING`;
- `RESULT_VALIDATING`;
- `COMPLETED`;
- `FAILED`;
- `SUPERSEDED`.

These labels are planning vocabulary, not executable enums. Future acceptance must
freeze exact state semantics before implementation.

## 6. Attempt model

One cycle may have multiple execution attempts only under deterministic retry rules.
Each attempt has its own identity and terminal attempt state. A failed attempt does
not change the material cycle identity. An accepted terminal result prevents a late
attempt from replacing it silently.

## 7. Idempotency and duplicate delivery

Duplicate request or trigger delivery must be resolved using canonical material
identity rather than transport message identity alone. Safe deduplication cannot
erase audit history or conceal repeated malicious delivery.

## 8. Concurrency boundary

Concurrent attempts for the same cycle require an explicit deterministic conflict
rule. A later implementation must prove that at most one authoritative terminal
result is accepted for one cycle identity.

This planning artifact selects no lock, database transaction, lease, queue, or
consensus mechanism.

## 9. Time and freshness architecture

The runtime must preserve the distinction among evidence observation time, capture
time, admission time, evaluation time, result validity, and reevaluation deadline.
The trusted-time source and skew policy must be versioned before runtime execution.

## 10. Kernel boundary

The runtime orchestrates evaluation; it does not redefine kernel semantics. Canonical
claim outcomes remain `CONFORMANT`, `NON_CONFORMANT`, `INCONCLUSIVE`, and `STALE`
under the accepted evaluation semantics.

A runtime transport or scheduler cannot reorder outcome precedence.

## 11. Evidence and provider boundary

Phase 11 runtime planning starts from Phase 10 admitted evidence bindings. Provider
collection, credentials, network access, and operational-evidence ingestion remain
separately governed and cannot be inferred from runtime planning authority.

## 12. Failure architecture

Failure classes include unresolved admission, incompatible versions, stale inputs,
kernel failure, timeout, concurrency conflict, canonicalization or fingerprint
failure, result validation failure, and internal invariant failure.

Failures remain evidence. They cannot be translated into conformance.

## 13. Result boundary

The accepted runtime result is an immutable bounded evaluation record. It may later
be consumed by Phase 12, but Phase 11 does not create drift findings, certificate
representations, signing authority, issuance authority, or remediation authority.

## 14. Security boundaries

The architecture separates:

1. NEXUS truth authority from AFR;
2. Phase 10 evidence admission from Phase 11 evaluation;
3. trigger qualification from execution admission;
4. cycle identity from attempt identity;
5. kernel execution from runtime orchestration;
6. authoritative result state from audit projection;
7. Phase 11 evaluation from Phase 12 findings and certificates;
8. tenant and subject scopes from one another.

## 15. Side-effect boundary

This architecture defines no implemented API, scheduler, queue, database, worker,
credential, provider call, deployment, persistence layer, signing service,
certificate issuer, remediation engine, NEXUS mutation path, or production runtime.
