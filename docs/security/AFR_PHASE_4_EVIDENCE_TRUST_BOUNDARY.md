# AFR Phase 4 Evidence Trust Boundary

## 1. Purpose

This document defines the security and trust constraints for planned operational-observation intake and evidence eligibility. It is documentation-only and creates no implementation, collection, integration, persistence, kernel, runtime, certificate, deployment, enforcement, or remediation authority.

## 2. Trust Posture

Every supplied observation, payload, identifier, timestamp, provenance statement, integrity reference, source assertion, and version declaration is untrusted until deterministically validated under explicit policy and resource bounds.

## 3. Boundary Position

The trust boundary lies between externally supplied observations and immutable eligible evidence. It ends before any future separately authorized deterministic-kernel invocation and produces no conformance outcome.

## 4. Protected Assets

Protected assets include tenant and subject isolation, observation and evidence identity, normalized content identity, provenance, integrity material, trusted-time and freshness inputs, scope and environment bindings, versioned policy, deterministic decisions, failure records, and Phase 3 semantics.

## 5. Trust Inputs

Only explicit immutable version-bound inputs may influence eligibility. Ambient credentials, process identity, filesystem paths, endpoints, provider accounts, deployment context, network state, model output, randomness, arrival order, and elapsed processing time are non-authoritative.

## 6. Threat Actors and Conditions

The boundary assumes malformed, oversized, stale, replayed, duplicated, conflicting, substituted, cross-tenant, cross-subject, cross-environment, cross-scope, ambiguously timed, provenance-deficient, integrity-deficient, and unsupported observations may be supplied intentionally or accidentally.

## 7. Identity and Isolation

Tenant, subject, environment, scope, source, release where applicable, observation identity, and evidence identity must be explicit and mutually consistent. Cross-boundary substitution and identifier reuse with materially changed content fail closed. Ambient identity inference is prohibited.

## 8. Provenance Trust

Required provenance must be attributable, complete, supported, structurally valid, deterministically bounded, and bound to the observation. Missing, malformed, incomplete, unsupported, or unverifiable provenance cannot produce `ELIGIBLE` evidence.

## 9. Integrity Trust

Integrity mechanisms and verification inputs must be explicit, supported, version-bound, and tied to the supplied content and observation identity. Missing, malformed, unverifiable, unsupported, or mismatched integrity material cannot produce `ELIGIBLE` evidence.

## 10. Trusted Time and Freshness

Observed, received, applicable, trusted-evaluation times, validity intervals, freshness policy, and versions remain explicit. Naive, ambiguous, malformed, contradictory, stale, expired, or unsupported temporal states fail closed. Wall-clock duration cannot select a canonical result.

## 11. Replay, Duplication, and Conflict

Byte-identical replay, semantic duplication, stale replay, changed-content identifier reuse, reordered delivery, cross-boundary substitution, and conflicting observations remain distinguishable. Deduplication cannot erase provenance, integrity, freshness, ordering, or conflict evidence.

## 12. Partial Evidence

Partial evidence cannot be promoted to complete evidence. Missing required identity, trust, time, scope, content, representation, or version material produces an explicit non-eligible outcome. Silent repair, inference, truncation, omission, sampling, and best-effort continuation are prohibited.

## 13. Eligibility and Conformance Separation

Eligibility classifications are `ELIGIBLE`, `INELIGIBLE`, `QUARANTINED`, `UNSUPPORTED`, and `PROCESSING_FAILURE`. This boundary cannot emit `CONFORMANT`, `NON_CONFORMANT`, `INCONCLUSIVE`, `STALE`, or another conformance outcome. Processing failures remain distinct from both.

## 14. Resource-Exhaustion Controls

Versioned limits cover total ingress bytes, envelope field count, collection cardinality, nesting depth, provenance-chain length, integrity-reference length, normalized evidence bytes, and deterministic processing work units. Violations fail closed before evidence construction.

## 15. Failure Safety

Failures are deterministic, structured, bounded, and audit-safe. Records include stable code, field path or semantic location, classification, applicable version, bounded context, and construction-stop state. They exclude secrets, credentials, unnecessary payload, stack traces, provider internals, and nondeterministic diagnostics.

## 16. Sensitive-Data Minimization

Only data required for deterministic validation, eligibility, identity, auditability, and future handoff may be represented. Failure evidence and logs must minimize payload exposure and prevent cross-tenant, cross-subject, and cross-scope disclosure.

## 17. Adapter and Supply-Chain Boundary

Semantics remain independent of providers, SDKs, APIs, plugins, remote code, models, and network services. A future adapter cannot decide eligibility, infer bindings, weaken checks, modify canonical semantics, or expand authority. Planning requires no new dependency or executable schema.

## 18. Kernel and Persistence Boundary

No kernel invocation, filesystem access, network access, database, queue, cache, stream, replay store, secret, credential, or production configuration is authorized. Immutable eligible evidence is only prepared for a future separately governed handoff.

## 19. Cross-Program Non-Drift

`DISPOSITION_A = PHASE_4_DOES_NOT_REQUIRE_ARCHITECTURE_TRUTH_CONTRACT_WORK` remains controlling. ARCP names and semantics remain `UNRESOLVED_PENDING_NEXUS_PHASE_19_GOVERNANCE`; NEXUS Phase 19 naming remains upstream. AFR creates no NEXUS, ARCP, ATA, or architecture-truth authority.

## 20. Authority Separation

`DEPENDENCY_RECOGNITION != INTEGRATION_PLANNING_AUTHORITY`

`INTEGRATION_PLANNING_AUTHORITY != INTEGRATION_IMPLEMENTATION_AUTHORITY`

`INTEGRATION_IMPLEMENTATION_AUTHORITY != RUNTIME_AUTHORITY`

`FUTURE_NEXUS_TO_AFR_ARCHITECTURE_TRUTH_CONSUMER_CONTRACT` remains a non-canonical placeholder, not a schema, API, adapter, implementation, active contract, or authority.

## 21. Abuse and Misuse Cases

The planned controls must address identity spoofing, tenant or subject substitution, provenance fabrication, integrity-reference substitution, timestamp manipulation, stale replay, collision or identifier reuse, resource exhaustion, parser ambiguity, unsupported-version downgrade, conflict suppression, partial-evidence promotion, and sensitive-data leakage.

## 22. Prohibited Effects and Stop Conditions

This boundary authorizes no source, test, vector, fixture, executable schema, dependency, configuration, collector, adapter, live collection, filesystem, network, model, persistence, kernel, runtime evaluation, integration, certificate, deployment, enforcement, remediation, or implementation. Planning stops if any is required or accepted Phase 0 through Phase 3 semantics need amendment.

## 23. Review Evidence

Acceptance requires exact six-document and hash verification, semantic convergence, threat and trust review, deterministic-resource review, cross-program non-drift review, authority-leakage review, independent whole-package review, staged-object verification, commit and remote verification, explicit readiness and merge authorization, canonical post-merge verification, and separately governed closure. No gate implies the next.

## 24. Authority State

`AFR_PHASE_4_PLANNING_AUTHORITY = BOUNDED_OPERATIONAL_EVIDENCE_INTAKE_AND_ELIGIBILITY_PLANNING_ONLY`

`AFR_PHASE_4_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_4_LIVE_EVIDENCE_COLLECTION_AUTHORITY = NONE`

`AFR_PHASE_4_PROVIDER_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_4_NEXUS_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_4_ARCP_AUTHORITY = NONE`

`AFR_PHASE_4_RUNTIME_EVALUATION_AUTHORITY = NONE`

`AFR_PHASE_4_PERSISTENCE_AUTHORITY = NONE`

`AFR_PHASE_4_CERTIFICATE_AUTHORITY = NONE`

`AFR_PHASE_4_DEPLOYMENT_AUTHORITY = NONE`

`AFR_PHASE_4_ENFORCEMENT_AUTHORITY = NONE`

`AFR_PHASE_4_REMEDIATION_AUTHORITY = NONE`

`AFR_PHASE_4_AUTHORITY = BOUNDED_PLANNING_ONLY`
