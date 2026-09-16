# AFR Observation Acquisition Contract

## 1. Purpose

This documentation-only contract defines the planned semantic contract for
bounded, least-privilege, read-only acquisition of attributable operational
observations for later Phase 4 intake.

It creates no executable schema, source, collector, provider adapter, live
collection, credential, network, persistence, integration, runtime, or
implementation authority.

## 2. Contract Boundary

Input is a governed collection request plus explicit collector identity,
source identity, tenant, subject, environment, requested scope,
authorization-context reference, representation or API version, and bounded
resource policy.

Output is exactly one attributable collection result and a supplied
operational observation suitable for Phase 4 handoff, or an explicit
collection failure that may itself be represented in the result.

The contract does not produce eligible evidence.

## 3. Collection Outcome Vocabulary

The collection-state classes are:

- `COLLECTION_COMPLETE`;
- `COLLECTION_PARTIAL`;
- `COLLECTION_FAILED`;
- `COLLECTION_UNSUPPORTED`;
- `COLLECTION_CANCELLED`.

They are mutually exclusive for one collection result.

## 4. Eligibility and Conformance Separation

This contract cannot emit or infer:

- `ELIGIBLE`;
- `INELIGIBLE`;
- `QUARANTINED`;
- `CONFORMANT`;
- `NON_CONFORMANT`;
- `INCONCLUSIVE`;
- `STALE`;
- any other Phase 4 or kernel-owned outcome.

Collection status is not evidence status.

## 5. Required Request Bindings

A governed request must explicitly bind:

- request identifier or identity inputs;
- collector identifier and version;
- source identifier and class;
- tenant;
- subject and subject type;
- environment;
- requested scope;
- read-only operation class;
- authorization-context reference;
- representation or API version;
- request-policy version;
- resource-policy version.

No required binding may be inferred from credentials or ambient state.

## 6. Request Identity Rules

Request identity binds all material governed request inputs.

Secrets and credential material are excluded from request identity.

Material request changes require a different request identity.

## 7. Source Identity Rules

Source identity must be explicit, attributable, and consistent with the
requested source class and scope.

Source-native account, project, subscription, cluster, namespace, tenant, or
endpoint identity is represented only when explicitly supplied and applicable.

Ambiguous or conflicting source identity fails closed.

## 8. Collector Authorization Rules

The authorization context must describe an approved read-only operation and
bounded source scope.

The contract prohibits interpretation of general account access as unrestricted
collection authority.

Write, mutation, remediation, deployment, acknowledgement, tagging, deletion,
quarantine, or policy-change authority is outside this contract.

## 9. Temporal Rules

The contract distinguishes:

- request time;
- collection start time;
- collection completion time;
- source-native observation time where available;
- source response time where meaningful;
- result construction time;
- Phase 4 handoff time.

Missing source-native time remains explicit.

This contract does not determine Phase 4 freshness.

## 10. Response Presence Rules

The contract distinguishes:

- response present;
- response absent due to failure;
- response partial;
- response malformed;
- response unsupported;
- response empty but successfully returned where source semantics permit;
- response identity unavailable.

These states cannot be silently collapsed.

## 11. Response Identity Rules

Where a response exists, its identity binds source, request, representation,
applicable versions, source-native metadata, and the response bytes or governed
response representation permitted by policy.

Redaction or minimization produces a distinct representation and must preserve
transformation metadata.

## 12. Scope Accounting Rules

A collection result must represent:

- requested scope;
- source-accepted scope where known;
- observed scope;
- successful scope;
- failed scope;
- unsupported scope;
- omitted scope;
- filtered scope.

Scope categories cannot be silently discarded.

## 13. Completeness Rules

`COLLECTION_COMPLETE` is allowed only relative to an explicit bounded request
for which the successful scope covers the source-accepted or otherwise
governed expected scope with no unresolved failed, unsupported, omitted, or
unobserved required segment.

A complete result cannot be inferred from lack of observed errors alone.

Unknown state is not absence.

## 14. Pagination and Segmentation Rules

The contract preserves page or segment identity, continuation state, source
totals where available, observed totals, duplicate segments, missing segments,
and continuation failure.

Any unresolved required page or segment forces a non-complete result.

## 15. Partial Collection Rules

`COLLECTION_PARTIAL` preserves the successfully observed portion and explicitly
records failed, unsupported, omitted, or unobserved required scope.

Partial collection must not be promoted to complete collection.

Partial collection does not imply partial evidence eligibility.

## 16. Failure Rules

Structured failures may represent:

- `AUTHORIZATION_DENIED`;
- `SOURCE_ACCESS_FAILURE`;
- `SOURCE_TIMEOUT`;
- `SOURCE_THROTTLED`;
- `PARTIAL_RESPONSE`;
- `PAGINATION_FAILURE`;
- `UNSUPPORTED_OPERATION`;
- `MALFORMED_SOURCE_RESPONSE`;
- `AMBIGUOUS_SOURCE_IDENTITY`;
- `INCONSISTENT_SCOPE`;
- `SOURCE_VERSION_MISMATCH`;
- `RESOURCE_BOUND_EXCEEDED`;
- `COLLECTION_CANCELLED`;
- `COLLECTOR_INTERNAL_FAILURE`.

The labels are planning vocabulary, not executable error codes.

## 17. Failure Safety Rules

A failure record contains only bounded safe context necessary for attribution,
scope impact, audit, and future diagnosis.

It excludes credentials, secrets, unnecessary response payload, stack traces,
and unbounded provider internals.

Failure cannot be converted into negative evidence or conformance.

## 18. Raw Response Rules

The contract distinguishes source-native response bytes, raw-response identity,
redacted or minimized bytes, parsed representation, collector metadata,
transformation metadata, and handoff representation.

Preservation is conditional on security, privacy, contractual, and provider
constraints.

No storage mechanism or retention policy is authorized.

## 19. Result Identity Rules

Result identity binds request identity, source identity, response identity or
explicit absence, collection outcome, scope accounting, temporal metadata,
versions, structured failures, and transformation metadata.

Material changes to those inputs require a different result identity.

## 20. Bounded Resource Rules

Planning defines versioned future limits for source-response bytes, page or
segment count, item count, nesting depth, metadata cardinality, failure count,
and local transformation work.

Bound exhaustion must produce an explicit partial, failed, unsupported, or
cancelled result as applicable.

Silent truncation cannot preserve `COLLECTION_COMPLETE`.

## 21. Supplied Observation Construction

A supplied operational observation for Phase 4 preserves all material
collection identity, attribution, scope, time, representation, failure, and
transformation information necessary for Phase 4 to apply its own eligibility
rules.

Construction cannot classify evidence eligibility or invoke the deterministic
kernel.

## 22. Provider Neutrality

The contract does not depend on any provider SDK, API, cloud, SaaS product,
cluster manager, CI/CD system, observability tool, security product, model
gateway, MCP implementation, database, or data warehouse.

A future adapter may translate source-native responses but cannot define this
contract or expand authority.

## 23. Authority and Phase Separation

Provider or enterprise source state remains authoritative at the source.

NEXUS architecture truth remains separate.

Phase 4 evidence eligibility remains separate.

AFR conformance evaluation remains separate.

ATA runtime commit authority remains separate.

`DEPENDENCY_RECOGNITION != INTEGRATION_PLANNING_AUTHORITY`

`INTEGRATION_PLANNING_AUTHORITY != INTEGRATION_IMPLEMENTATION_AUTHORITY`

`INTEGRATION_IMPLEMENTATION_AUTHORITY != RUNTIME_AUTHORITY`

## 24. Prohibited Effects and Stop Conditions

This contract authorizes no source, tests, executable schema, dependency,
configuration, live collection, provider adapter, credential, network,
filesystem, persistence, model, Phase 4 eligibility implementation, kernel
invocation, NEXUS/ARCP/ATA integration, certificate, deployment, enforcement,
remediation, or implementation work.

Planning stops if any becomes necessary or accepted Phase 0 through Phase 4
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
