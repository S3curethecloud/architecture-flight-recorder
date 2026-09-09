# AFR Operational Evidence Intake Architecture

## 1. Purpose

This document defines the planned adapter-neutral boundary by which a supplied operational observation may be validated and classified for eligibility as immutable AFR evidence. It authorizes no implementation or runtime behavior.

## 2. Canonical Context

The capability is `OPERATIONAL_EVIDENCE_INTAKE_AND_ELIGIBILITY_PLANNING`. Its mission is `DEFINE_BOUNDED_OBSERVATION_TO_ELIGIBLE_EVIDENCE_SEMANTICS`, positioned `BETWEEN_EXTERNAL_OBSERVATIONS_AND_THE_DETERMINISTIC_KERNEL`. Phase 3 semantics remain immutable.

## 3. Architectural Boundary

The boundary begins with an explicitly supplied observation and ends with immutable eligible evidence or an explicit `INELIGIBLE`, `QUARANTINED`, `UNSUPPORTED`, or `PROCESSING_FAILURE` result. It performs no collection, persistence, integration, kernel invocation, or conformance evaluation.

## 4. Conceptual Responsibilities

The planned responsibilities are envelope validation; identity and binding validation; provenance, integrity, trusted-time, freshness, replay, substitution, conflict, and resource assessment; eligibility classification; immutable evidence construction; and handoff preparation. They are semantics, not runtime components.

## 5. Conceptual Flow

```text
SUPPLIED_OPERATIONAL_OBSERVATION
  -> OBSERVATION_ENVELOPE_VALIDATION
  -> IDENTITY_AND_BINDING_VALIDATION
  -> PROVENANCE_INTEGRITY_AND_FRESHNESS_ASSESSMENT
  -> REPLAY_CONFLICT_AND_RESOURCE_ASSESSMENT
  -> DETERMINISTIC_ELIGIBILITY_DECISION
  -> IMMUTABLE_ELIGIBLE_EVIDENCE
  -> FUTURE_SEPARATELY_AUTHORIZED_KERNEL_INVOCATION
```

Every transition is fail-closed.

## 6. Observation Envelope

The envelope declares observation and source identifiers, source class, tenant, subject and type, environment, scope, release binding where applicable, observed and received times, applicable time or validity interval, representation, input-byte measurement, integrity and provenance references, optional-field presence, content reference, and envelope version. No binding may be inferred from ambient state.

## 7. Observation Identity

Observation identity binds content to tenant, subject, environment, scope, source, time, representation, versions, provenance, and integrity material. Identifier reuse with materially changed content is a conflict and fails closed.

## 8. Evidence Identity

Eligible evidence identity binds observation identity, normalized content identity, tenant, subject, environment, scope, source, provenance, integrity material, time, freshness policy, eligibility-policy version, and envelope and evidence-model versions. Identical governed inputs reproduce identity; any material change changes it.

## 9. Eligibility Model

The classifications are `ELIGIBLE`, `INELIGIBLE`, `QUARANTINED`, `UNSUPPORTED`, and `PROCESSING_FAILURE`. Eligibility is pre-conformance and must never emit `CONFORMANT`, `NON_CONFORMANT`, `INCONCLUSIVE`, `STALE`, or another conformance outcome.

## 10. Deterministic Inputs

Eligibility depends only on supplied immutable version-bound inputs. Randomness, models, arrival order, provider behavior, network state, ambient configuration, operator convenience, and elapsed processing time cannot select or modify a canonical result.

## 11. Provenance and Integrity

The architecture distinguishes complete, incomplete, malformed, unsupported, and unverifiable provenance and integrity material. Missing, malformed, unsupported, mismatched, or unverifiable required trust material cannot produce eligible evidence.

## 12. Time and Freshness

Observed, received, applicable, trusted-evaluation times, validity intervals, freshness policies, and their versions remain explicit. Naive, ambiguous, malformed, unsupported, or contradictory timestamps fail closed. Wall-clock timeout may stop work but cannot select a result.

## 13. Replay, Duplication, and Substitution

The architecture distinguishes byte-identical replay, semantic duplication, changed-content identifier reuse, stale replay, cross-tenant, cross-subject, cross-environment, and cross-scope substitution, reordered delivery, and conflict. Deduplication cannot erase provenance, integrity, freshness, ordering, or conflict evidence.

## 14. Conflict and Partial Evidence

Contradictory observations and inconsistent bindings produce explicit deterministic outcomes. Partial evidence cannot be promoted to complete evidence. Missing data cannot be inferred or silently repaired. Arrival order, model judgment, provider priority, and convenience cannot resolve conflict.

## 15. Resource Boundary

Versioned limits cover total ingress bytes, envelope field count, collection cardinality, nesting depth, provenance-chain length, integrity-reference length, normalized evidence bytes, and deterministic processing work units. Resource-limit violations fail closed; truncation, sampling, omission, silent repair, and best-effort continuation are prohibited.

## 16. Adapter Neutrality

Semantics are independent of cloud providers, Kubernetes, CI/CD, model gateways, MCP, observability and security vendors, SDKs, and APIs. A future adapter may translate observations but cannot determine eligibility, define AFR semantics, infer bindings, bypass validation, expand authority, or invoke the kernel.

## 17. Kernel Handoff

Only immutable `ELIGIBLE` evidence may be prepared for a future separately authorized handoff. Required identity, trust, time, boundary, version, resource, and decision metadata must be preserved. Phase 4 planning does not invoke or simulate the kernel.

## 18. Failure Model

Failures are deterministic, structured, bounded, and audit-safe, with a stable code, field path or semantic location, classification, applicable version, bounded context, and construction-stop state. They expose no secrets, credentials, unnecessary payloads, stack traces, provider internals, or nondeterministic diagnostics.

## 19. Security and Privacy

All observations are untrusted. Strict type and version validation, tenant and subject isolation, replay and substitution resistance, provenance, integrity, trusted-time, freshness, resource controls, minimization, audit safety, and supply-chain independence are required. No filesystem, network, secrets, production configuration, persistence, subprocess, plugin, or remote-code access is required or authorized.

## 20. Cross-Program Non-Drift

`DISPOSITION_A = PHASE_4_DOES_NOT_REQUIRE_ARCHITECTURE_TRUTH_CONTRACT_WORK` remains controlling. `ARCP_CANONICAL_NAME` and `ARCP_CANONICAL_SEMANTICS` remain `UNRESOLVED_PENDING_NEXUS_PHASE_19_GOVERNANCE`. `NEXUS_PHASE_19_CANONICAL_CAPABILITY_NAME = MUST_BE_VERIFIED_FROM_CANONICAL_NEXUS_STATE`. AFR cannot canonicalize them.

## 21. Authority Separation

`DEPENDENCY_RECOGNITION != INTEGRATION_PLANNING_AUTHORITY`

`INTEGRATION_PLANNING_AUTHORITY != INTEGRATION_IMPLEMENTATION_AUTHORITY`

`INTEGRATION_IMPLEMENTATION_AUTHORITY != RUNTIME_AUTHORITY`

`FUTURE_NEXUS_TO_AFR_ARCHITECTURE_TRUTH_CONSUMER_CONTRACT` remains a non-canonical placeholder, not a schema, API, adapter, implementation, active contract, or authority grant.

## 22. Prohibited Effects

This architecture creates no source, test, vector, fixture, schema, adapter, service, dependency, configuration, filesystem, network, collection, evaluation, kernel, integration, model, persistence, certificate, deployment, enforcement, remediation, or implementation authority.

## 23. Stop Conditions

Planning stops if it requires architecture-truth contract work, canonical NEXUS or ARCP naming, a seventh document, schemas, source or tests, provider-specific normative behavior, live collection, persistence, kernel invocation, or amendment of accepted Phase 0 through Phase 3 semantics.

## 24. Authority State

`AFR_PHASE_4_PLANNING_AUTHORITY = BOUNDED_OPERATIONAL_EVIDENCE_INTAKE_AND_ELIGIBILITY_PLANNING_ONLY`

`AFR_PHASE_4_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_4_LIVE_EVIDENCE_COLLECTION_AUTHORITY = NONE`

`AFR_PHASE_4_PROVIDER_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_4_NEXUS_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_4_ARCP_AUTHORITY = NONE`

`AFR_PHASE_4_RUNTIME_EVALUATION_AUTHORITY = NONE`

`AFR_PHASE_4_PERSISTENCE_AUTHORITY = NONE`

`AFR_PHASE_4_DEPLOYMENT_AUTHORITY = NONE`

`AFR_PHASE_4_AUTHORITY = BOUNDED_PLANNING_ONLY`
