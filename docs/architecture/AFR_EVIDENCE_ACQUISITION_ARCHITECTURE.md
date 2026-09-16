# AFR Evidence Acquisition Architecture

## 1. Purpose

This document defines the planned provider-neutral architecture boundary for
bounded, least-privilege, read-only acquisition of attributable operational
observations for later Phase 4 ingress.

It is documentation-only and authorizes no implementation, live source
access, network behavior, credential use, persistence, integration, runtime
evaluation, certificate work, deployment, enforcement, or remediation.

## 2. Canonical Context

The capability is:

`EVIDENCE_ACQUISITION_AND_COLLECTION_BOUNDARY_PLANNING`

The mission is:

`DEFINE_BOUNDED_READ_ONLY_COLLECTION_OF_ATTRIBUTABLE_OPERATIONAL_OBSERVATIONS_FOR_PHASE4_INGRESS`

The architectural position is:

`BETWEEN_APPROVED_PROVIDER_ENTERPRISE_SOURCES_AND_PHASE4_SUPPLIED_OPERATIONAL_OBSERVATION`

## 3. Architectural Boundary

The boundary begins with an explicitly governed read-only collection request
against an approved provider or enterprise source and ends with an attributable
collection result represented as a supplied operational observation for Phase
4.

The boundary ends before Phase 4 evidence eligibility.

## 4. Conceptual Responsibilities

The planned responsibilities are:

- collector and source identity;
- tenant, subject, environment, and scope binding;
- read-only authorization-context attribution;
- request identity;
- source-response identity;
- collection-result identity;
- collection-time representation;
- source-native observation-time preservation where available;
- scope and completeness accounting;
- pagination and segmentation accounting;
- partial and failed collection representation;
- raw-response identity and preservation requirements;
- bounded transformation metadata;
- Phase 4 handoff preparation;
- audit-safe structured failure representation.

These are architecture semantics, not runtime components.

## 5. Conceptual Flow

```text
APPROVED_PROVIDER_OR_ENTERPRISE_SOURCE
  -> BOUNDED_READ_ONLY_COLLECTION_REQUEST
  -> SOURCE_RESPONSE_OR_EXPLICIT_SOURCE_FAILURE
  -> ATTRIBUTABLE_COLLECTION_RESULT
  -> SUPPLIED_OPERATIONAL_OBSERVATION
  -> PHASE_4_EVIDENCE_INTAKE_AND_ELIGIBILITY_BOUNDARY
```

No transition authorizes provider mutation.

## 6. Collector Identity Boundary

Collector identity must be explicit, versioned, attributable, and bound to the
collection request.

A collector cannot derive authority from process presence, host placement,
ambient credentials, local configuration, or provider account membership.

## 7. Source Identity Boundary

Source identity must identify the authoritative provider or enterprise source
and the explicit source boundary relevant to the request.

Source-native account, subscription, project, cluster, namespace, tenant, or
endpoint values are represented only when explicitly supplied and applicable.

## 8. Authorization Context Boundary

A collection request references a bounded authorization context without
embedding credential secrets.

The context must describe the approved read-only operation class and scope.

The architecture creates no credential issuance, storage, rotation, or use
authority.

## 9. Request Identity

Collection-request identity binds collector, source, tenant, subject,
environment, requested scope, operation class, representation or API version,
authorization-context reference, and applicable policy version.

Material bound-input changes change request identity.

## 10. Response Identity

Where a source response exists, response identity binds source, request,
representation, source response metadata, source-native time where available,
and source-native or governed response bytes as permitted.

A missing response remains explicit and cannot be represented as an empty
successful response.

## 11. Result Identity

Collection-result identity binds request identity, response identity or
explicit absence, collection outcome, scope accounting, temporal metadata,
representation, versions, failures, and bounded transformation metadata.

The result identity does not imply evidence eligibility.

## 12. Temporal Model

The architecture distinguishes request, collection-start, collection-complete,
source-observation, source-response, result-construction, and Phase 4 handoff
times.

Source-native time is preserved where available.

Missing or ambiguous source-native time is explicit.

Phase 5 does not create Phase 4 trusted-time or freshness decisions.

## 13. Scope Model

The architecture distinguishes requested, source-accepted, observed,
successful, failed, unsupported, omitted, filtered, paginated, and segmented
scope.

Every completeness claim is relative to an explicit bounded request.

Unobserved state is not absence.

## 14. Pagination and Segmentation

A paginated or segmented collection preserves page or segment identity,
continuation state, duplicates, omissions, failures, source-reported totals
where available, collector-observed totals, and bounded limits.

Partial pagination cannot be silently represented as complete.

## 15. Collection Outcome Model

Collection results use only collection-state classes:

- `COLLECTION_COMPLETE`;
- `COLLECTION_PARTIAL`;
- `COLLECTION_FAILED`;
- `COLLECTION_UNSUPPORTED`;
- `COLLECTION_CANCELLED`.

These are not evidence-eligibility or conformance outcomes.

## 16. Failure Model

Structured source and collector failures include a stable class, semantic
location, source and request identity, bounded safe context, relevant version,
scope impact, and whether collection continued, partially completed, or
stopped.

Failure records expose no credentials, secrets, unnecessary payloads, stack
traces, provider internals beyond bounded safe context, or nondeterministic
diagnostics.

## 17. Raw Response Boundary

The architecture distinguishes source-native bytes from redacted, minimized,
parsed, normalized, collector-generated, transformed, and Phase 4 handoff
representations.

Raw-response preservation planning is conditional on security, privacy,
contractual, and provider constraints and creates no storage authority.

## 18. Least-Privilege Read-Only Boundary

A future collector is limited to explicitly approved read-only operations.

The architecture prohibits implicit escalation into write, mutation,
acknowledgement, tagging, quarantine, remediation, deployment, policy change,
or other control-plane action.

Read authority is not remediation authority.

## 19. Resource Boundary

Planning defines conceptual versioned bounds for source-response bytes, page
or segment count, item count, nesting depth, metadata cardinality, failure
records, and deterministic local transformation work.

Bound exhaustion produces an explicit partial or failed collection state.

A complete result cannot be preserved by silent truncation.

## 20. Phase 4 Handoff Boundary

A supplied operational observation preserves:

- collector and source identity;
- tenant, subject, environment, and scope;
- request, response, and result identity;
- collection and source-native time;
- collection outcome;
- scope accounting;
- partial state;
- representation and versions;
- bounded transformation metadata;
- structured failures;
- raw-response identity or reference where permitted.

Phase 4 independently validates and classifies evidence eligibility.

## 21. Security and Privacy

Source responses are untrusted until bounded validation and attribution.

The architecture requires tenant and subject isolation, source authenticity,
scope minimization, sensitive-data minimization, credential non-persistence,
bounded resource use, audit-safe failures, provenance continuity, and
supply-chain independence.

## 22. Provider Neutrality

Semantics are independent of providers, clouds, cluster managers, CI/CD
systems, observability vendors, security products, SaaS products, databases,
data warehouses, model gateways, MCP systems, SDKs, and APIs.

Provider-specific adapter behavior is future separately governed work.

## 23. Authority Separation

Providers and enterprise systems remain authoritative for their own bounded
source state.

NEXUS remains authoritative for approved architecture truth where applicable.

Phase 4 retains observation-to-evidence eligibility authority.

AFR deterministic evaluation retains conformance authority.

ATA retains consequential runtime commit authority where applicable.

Collection cannot elevate source state to another authority domain.

## 24. Prohibited Effects and Stop Conditions

This architecture creates no source, tests, executable schema, dependency,
configuration, collector, adapter, live source call, credential, filesystem,
network, persistence, model, Phase 4 eligibility implementation, kernel
invocation, NEXUS/ARCP/ATA integration, certificate, deployment, enforcement,
remediation, or implementation authority.

Planning stops if any becomes necessary or if accepted Phase 0 through Phase 4
semantics require amendment.

## 25. Authority State

`AFR_PHASE_5_PLANNING_AUTHORITY =
BOUNDED_EVIDENCE_ACQUISITION_AND_COLLECTION_BOUNDARY_PLANNING_ONLY`

`AFR_PHASE_5_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_5_LIVE_COLLECTION_AUTHORITY = NONE`

`AFR_PHASE_5_PROVIDER_ADAPTER_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_5_CREDENTIAL_AUTHORITY = NONE`

`AFR_PHASE_5_NETWORK_AUTHORITY = NONE`

`AFR_PHASE_5_PERSISTENCE_AUTHORITY = NONE`

`AFR_PHASE_5_NEXUS_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_5_ARCP_AUTHORITY = NONE`

`AFR_PHASE_5_ATA_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_5_RUNTIME_AUTHORITY = NONE`

`AFR_PHASE_5_CERTIFICATE_AUTHORITY = NONE`

`AFR_PHASE_5_DEPLOYMENT_AUTHORITY = NONE`

`AFR_PHASE_5_ENFORCEMENT_AUTHORITY = NONE`

`AFR_PHASE_5_REMEDIATION_AUTHORITY = NONE`
