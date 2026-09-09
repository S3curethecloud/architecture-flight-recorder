# AFR Evidence Eligibility Contract

## 1. Purpose

This documentation-only contract defines deterministic preconditions by which a supplied operational observation may become immutable eligible evidence. It creates no executable schema, implementation, integration, collection, persistence, kernel invocation, or runtime authority.

## 2. Contract Boundary

Input is an explicitly supplied observation envelope plus explicit versioned eligibility policy, trusted-time input, integrity-verification input, and resource limits. Output is exactly one eligibility decision and, only for `ELIGIBLE`, an immutable evidence representation prepared for future separately authorized handoff.

## 3. Decision Vocabulary

The only eligibility classifications are `ELIGIBLE`, `INELIGIBLE`, `QUARANTINED`, `UNSUPPORTED`, and `PROCESSING_FAILURE`. They are mutually exclusive.

## 4. Conformance Separation

Eligibility is pre-conformance. This contract cannot emit `CONFORMANT`, `NON_CONFORMANT`, `INCONCLUSIVE`, `STALE`, or any other conformance outcome. Processing failures are distinct from both eligibility and conformance.

## 5. Required Envelope Fields

Required fields are observation identifier, envelope version, source identifier and class, tenant, subject and type, environment, scope, observed and received times, representation, declared input bytes, integrity reference, provenance-chain reference, explicit optional-field presence, and content reference. Applicable time, validity interval, and release binding are required when policy declares them applicable.

## 6. Presence and Type Rules

Absent, explicit-null, empty, missing-required, unsupported-value, unsupported-type, and unsupported-version states remain distinct. Required data cannot be defaulted, coerced, inferred, silently repaired, or derived from ambient state.

## 7. Version Rules

Envelope, evidence-model, eligibility-policy, representation, integrity-mechanism, provenance, and applicable freshness-policy versions must be explicit and supported. Missing or unsupported required versions produce `UNSUPPORTED` or `PROCESSING_FAILURE` according to the frozen failure taxonomy and never `ELIGIBLE`.

## 8. Identity Binding

Observation and evidence identity bind normalized content identity, tenant, subject, environment, scope, source, provenance, integrity material, observed and received time, freshness policy, eligibility policy, envelope version, and evidence-model version. Material bound-input changes must change evidence identity.

## 9. Tenant and Subject Isolation

Cross-tenant replay, cross-subject substitution, and inconsistent tenant or subject bindings fail closed. Credentials, process identity, provider accounts, endpoints, paths, or deployment context cannot supply or override these bindings.

## 10. Provenance Rules

Required provenance must be attributable, complete, structurally valid, version-supported, and within its deterministic length bound. Missing, incomplete, malformed, unsupported, or unverifiable required provenance cannot yield `ELIGIBLE`.

## 11. Integrity Rules

Required integrity material and verification inputs must be present, supported, bound to the observation, and deterministically valid. Missing, malformed, unsupported, unverifiable, or mismatched integrity material cannot yield `ELIGIBLE`.

## 12. Time and Freshness Rules

Observed, received, applicable, trusted-evaluation times, validity intervals, freshness policy, and policy version must be explicit when required. Naive, ambiguous, malformed, contradictory, expired, or unsupported temporal inputs fail closed. Elapsed processing time cannot select a decision.

## 13. Replay and Duplicate Rules

Byte-identical replay, semantic duplication, changed-content identifier reuse, stale replay, reordered delivery, and cross-boundary substitution remain distinguishable. Deduplication cannot discard provenance, integrity, freshness, ordering, or conflict information.

## 14. Conflict Rules

Identifier reuse with materially changed content, contradictory observations, and inconsistent material bindings produce explicit deterministic conflict handling. Arrival order, provider priority, models, randomness, or operator convenience cannot resolve conflict.

## 15. Partial-Evidence Rules

Partial evidence cannot be promoted to complete evidence. Missing identity, trust, time, scope, version, or required content material produces a deterministic non-eligible result. Truncation, omission, sampling, and best-effort continuation cannot make evidence eligible.

## 16. Resource Rules

Versioned limits cover total ingress bytes, envelope field count, collection cardinality, nesting depth, provenance-chain length, integrity-reference length, normalized evidence bytes, and deterministic processing work units. Any violation fails closed before evidence construction.

## 17. Determinism Rules

Identical governed inputs must produce byte-identical decision records and eligible-evidence representations. Randomness, model output, network availability, provider behavior, ambient configuration, wall-clock duration, and iteration-order accidents cannot affect canonical output.

## 18. Failure Record

A structured failure contains a stable code, field path or semantic location, classification, applicable contract or policy version, bounded safe context, and whether evidence construction began or stopped. It contains no secrets, credentials, unnecessary payload, stack trace, provider internals, or nondeterministic diagnostic data.

## 19. Eligible-Evidence Construction

Construction occurs only after every mandatory validation passes. The immutable result preserves observation and evidence identities, all boundary and trust bindings, relevant timestamps and versions, resource accounting, and the eligibility decision. Construction cannot invoke the Phase 3 kernel.

## 20. Adapter Neutrality

This contract is independent of providers, SDKs, APIs, clouds, Kubernetes, CI/CD, model gateways, MCP, observability, and security products. An adapter may later translate inputs but cannot decide eligibility, infer bindings, change this contract, weaken validation, or invoke the kernel.

## 21. Cross-Program Non-Drift

`DISPOSITION_A = PHASE_4_DOES_NOT_REQUIRE_ARCHITECTURE_TRUTH_CONTRACT_WORK` remains controlling. ARCP canonical naming and semantics remain `UNRESOLVED_PENDING_NEXUS_PHASE_19_GOVERNANCE`; NEXUS Phase 19 naming must be verified from canonical NEXUS state. AFR creates no architecture-truth or cross-program integration authority.

## 22. Authority Separation

`DEPENDENCY_RECOGNITION != INTEGRATION_PLANNING_AUTHORITY`

`INTEGRATION_PLANNING_AUTHORITY != INTEGRATION_IMPLEMENTATION_AUTHORITY`

`INTEGRATION_IMPLEMENTATION_AUTHORITY != RUNTIME_AUTHORITY`

`FUTURE_NEXUS_TO_AFR_ARCHITECTURE_TRUTH_CONSUMER_CONTRACT` remains a non-canonical placeholder, not a schema, API, adapter, implementation, active contract, or authority.

## 23. Prohibited Effects and Stop Conditions

This contract authorizes no source, test, vector, fixture, executable schema, dependency, configuration, adapter, collection, filesystem, network, model, persistence, kernel, evaluation, integration, certificate, deployment, enforcement, remediation, or implementation work. Planning stops if any becomes necessary or accepted Phase 0 through Phase 3 semantics require amendment.

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
