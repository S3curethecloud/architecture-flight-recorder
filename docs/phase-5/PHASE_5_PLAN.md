# AFR Phase 5 Plan

## 1. Purpose

Phase 5 plans the bounded AFR capability:

`EVIDENCE_ACQUISITION_AND_COLLECTION_BOUNDARY_PLANNING`

The phase defines documentation-only semantics for bounded, least-privilege,
read-only acquisition of attributable operational observations from approved
provider or enterprise sources for later supply to the Phase 4 evidence-intake
and eligibility boundary.

This plan creates no implementation, live collection, provider integration,
credential, network, persistence, NEXUS, ARCP, ATA, runtime, certificate,
deployment, enforcement, remediation, or production authority.

## 2. Canonical Baseline

Phase 5 planning begins from:

- canonical `main`:
  `d19e0c7b0d3b8812bb5e23d01ba01c28d2b5b589`;
- canonical tree:
  `ee8120180c663bef3d13d6d5ada8acf6284e4421`;
- Phase 4 planning status: `COMPLETE`;
- Phase 4 planning authority: `CONSUMED_CLOSED`;
- Phase 4 first-slice implementation status: `COMPLETE`;
- Phase 4 implementation authority: `CONSUMED_CLOSED`;
- Phase 4 additional implementation authority: `NONE`;
- Phase 5 planning authority:
  `BOUNDED_EVIDENCE_ACQUISITION_AND_COLLECTION_BOUNDARY_PLANNING_ONLY`.

The Phase 5 planning-authority proposal effective point is complete.

Accepted Phase 0 through Phase 4 semantics remain immutable inputs. Phase 5
planning cannot reopen or amend them.

## 3. Mission and Position

The bounded mission is:

`DEFINE_BOUNDED_READ_ONLY_COLLECTION_OF_ATTRIBUTABLE_OPERATIONAL_OBSERVATIONS_FOR_PHASE4_INGRESS`

The architectural position is:

`BETWEEN_APPROVED_PROVIDER_ENTERPRISE_SOURCES_AND_PHASE4_SUPPLIED_OPERATIONAL_OBSERVATION`

Phase 5 plans an acquisition boundary. It does not implement a collector,
adapter, SDK integration, service, worker, scheduler, queue consumer, network
client, persistence layer, or provider-specific control-plane operation.

## 4. Exact Planning Package

Planning materialization is limited to:

1. `docs/SOT.md`
2. `docs/phase-5/PHASE_5_PLAN.md`
3. `docs/phase-5/PHASE_5_ACCEPTANCE_CRITERIA.md`
4. `docs/architecture/AFR_EVIDENCE_ACQUISITION_ARCHITECTURE.md`
5. `docs/contracts/AFR_OBSERVATION_ACQUISITION_CONTRACT.md`
6. `docs/security/AFR_PHASE_5_EVIDENCE_ACQUISITION_TRUST_BOUNDARY.md`

No seventh document, source file, test, vector, fixture, executable schema,
dependency, configuration, migration, generated runtime artifact, or
provider-specific adapter is authorized.

## 5. Planning Outcomes

Phase 5 must produce coherent documentation for:

- collector identity;
- source identity and source class;
- tenant, subject, environment, and collection-scope binding;
- collector authorization context;
- collection-request and collection-result identity;
- source-response identity;
- collection and source-observation time semantics;
- requested, observed, successful, failed, unsupported, omitted, and filtered
  scope;
- partial collection and bounded completeness claims;
- pagination and segmented collection semantics;
- source failure and cancellation;
- raw source-response identity and preservation requirements where permitted;
- least-privilege read-only identity requirements;
- provider-neutral collector contracts;
- bounded transformation and handoff metadata;
- security, privacy, auditability, provenance, and supply-chain constraints;
- handoff to Phase 4 supplied operational observations.

The documents must converge on one vocabulary, one lifecycle, one failure
model, one security boundary, and one authority boundary.

## 6. Canonical Semantic Foundation

Phase 5 relies on canonical Phase 0 through Phase 4 semantics for:

- AFR system and authority boundaries;
- observation identity and explicit binding principles;
- deterministic failure and bounded-resource principles where applicable;
- tenant and subject isolation;
- provenance and integrity requirements;
- Phase 4 supplied-observation intake;
- Phase 4 evidence-eligibility ownership;
- pre-conformance separation;
- immutable evidence construction after Phase 4 eligibility.

Phase 5 cannot redefine Phase 4 evidence eligibility, freshness, trusted-time,
or conformance semantics.

Any semantic not proven from canonical AFR evidence must be classified
explicitly as a Phase 5 planning definition, `RESERVED_FUTURE`, or
`NOT_ESTABLISHED`, as applicable.

## 7. Acquisition Boundary

The conceptual Phase 5 flow is:

```text
APPROVED_PROVIDER_OR_ENTERPRISE_SOURCE
    -> BOUNDED_READ_ONLY_COLLECTION_REQUEST
    -> SOURCE_RESPONSE_OR_EXPLICIT_SOURCE_FAILURE
    -> ATTRIBUTABLE_COLLECTION_RESULT
    -> SUPPLIED_OPERATIONAL_OBSERVATION
    -> PHASE_4_EVIDENCE_INTAKE_AND_ELIGIBILITY_BOUNDARY
```

The Phase 5 boundary ends before evidence eligibility.

No collection result is itself eligible evidence.

## 8. Collector Identity

Planning must define an explicit collector identity that can be attributed
without relying on ambient process state.

Collector identity planning must address:

- collector identifier;
- collector version;
- collector class;
- tenant authorization context;
- subject or target context;
- environment context;
- approved source class;
- approved operation class;
- authorization-policy reference;
- request identity.

A future collector cannot self-assert expanded authority.

## 9. Source Identity

Planning must define:

- source identifier;
- source class;
- provider or enterprise source reference;
- source account, project, subscription, cluster, tenant, namespace, or other
  source-native boundary only when explicitly supplied and applicable;
- source endpoint identity where applicable;
- source API or representation version where applicable;
- source authenticity inputs.

Source identity cannot be inferred from credentials, DNS, hostname, local
configuration, environment variables, or deployment placement.

## 10. Tenant, Subject, Environment, and Scope Binding

Every collection request and result must explicitly bind:

- tenant;
- subject and subject type;
- environment;
- requested scope;
- source;
- collector;
- applicable version information.

Cross-tenant, cross-subject, cross-environment, or cross-scope substitution
must fail closed in a future implementation.

Phase 5 planning creates no source access.

## 11. Collection Request Identity

Planning must define a stable request identity over the explicitly governed
request inputs, including:

- collector identity;
- source identity;
- tenant;
- subject;
- environment;
- requested scope;
- requested operation;
- representation or API version;
- authorization-context reference;
- request-policy version;
- request-time metadata where applicable.

Request identity cannot be based on secrets or credential material.

## 12. Collection Result Identity

Planning must define result identity over:

- request identity;
- source identity;
- response identity or explicit absence;
- observed scope;
- successful scope;
- failed scope;
- unsupported scope;
- omitted scope;
- collection status;
- source-native observation time where available;
- collection start and completion times;
- representation and version;
- bounded transformation metadata.

Material changes to bound inputs must change result identity.

## 13. Time Semantics

Planning must distinguish:

- request time;
- collection start time;
- collection completion time;
- source-native observation time where available;
- source response time where meaningful;
- result construction time;
- handoff time to Phase 4.

Missing source-native time remains explicit as missing or unknown.

Phase 5 cannot fabricate trusted time or redefine Phase 4 freshness policy.

## 14. Scope and Completeness

Planning must distinguish:

- requested scope;
- source-accepted scope;
- observed scope;
- successful scope;
- failed scope;
- unsupported scope;
- omitted scope;
- filtered scope;
- paginated or segmented scope;
- partial collection;
- complete collection relative to an explicit bounded request.

Completeness claims must be relative to an explicit scope and cannot exceed
what the collector actually observed successfully.

Unknown or unobserved state cannot be treated as absent state.

## 15. Pagination and Segmentation

Planning must define semantics for:

- page or segment identity;
- continuation-token presence;
- page ordering where meaningful;
- duplicate pages or segments;
- missing pages or segments;
- continuation failure;
- source-reported total where available;
- collector-observed total;
- bounded page and item limits;
- partial completion.

A failed page or segment cannot be silently omitted while preserving a
complete-collection claim.

## 16. Collection Outcome Model

Planning must define collection outcomes that remain distinct from Phase 4
eligibility and AFR conformance.

The planned collection-result classes are:

- `COLLECTION_COMPLETE`;
- `COLLECTION_PARTIAL`;
- `COLLECTION_FAILED`;
- `COLLECTION_UNSUPPORTED`;
- `COLLECTION_CANCELLED`.

These labels describe collection state only.

They must never be mapped directly to evidence eligibility or conformance.

## 17. Source Failure Model

Planning must define structured representations for:

- authorization denial;
- source access failure;
- timeout;
- throttling;
- partial response;
- pagination or segmentation failure;
- unsupported endpoint or operation;
- malformed response;
- ambiguous source identity;
- inconsistent scope;
- source version mismatch;
- bounded-resource exhaustion;
- cancellation;
- collector internal failure.

Failure does not imply negative evidence, positive evidence, absence, or
conformance.

## 18. Raw Source Response Planning

Planning may define preservation requirements for source-native bytes where
permitted by security, privacy, contract, and provider constraints.

Planning must distinguish:

- source-native response bytes;
- response identity;
- response metadata;
- redacted representation;
- minimized representation;
- parsed representation;
- collector-generated metadata;
- transformation metadata;
- Phase 4 handoff representation.

This planning creates no persistence, retention, filesystem, database,
object-store, queue, cache, or stream authority.

## 19. Read-Only and Least-Privilege Planning

A future collector must be restricted to explicitly approved read-only source
operations.

Planning must define:

- least-privilege operation classes;
- explicit read-only scope;
- denial of write and mutation operations;
- separation between source-read authority and remediation authority;
- credential non-persistence;
- authorization-context attribution;
- bounded collection scope;
- stop-on-authority-ambiguity behavior.

This plan creates no credentials and authorizes no live operation.

## 20. Provider Neutrality

The planning semantics must be independent of:

- AWS;
- Azure;
- Google Cloud;
- Kubernetes;
- CI/CD products;
- observability vendors;
- security products;
- SaaS products;
- data warehouses;
- model gateways;
- MCP servers;
- provider SDKs and APIs.

Provider-specific mappings require separately governed future work.

## 21. Phase 4 Handoff

The handoff representation must preserve:

- collector and source identity;
- tenant, subject, environment, and scope bindings;
- collection-request identity;
- collection-result identity;
- source-response identity or explicit absence;
- collection times;
- source-native observation time where available;
- collection outcome;
- partial-collection state;
- successful, failed, unsupported, omitted, and filtered scope;
- representation and version;
- bounded transformation metadata;
- structured source failures;
- raw-response identity or reference where permitted.

Phase 4 independently evaluates whether the supplied observation can become
eligible evidence.

## 22. Security, Privacy, and Audit Workstream

Planning must address:

- untrusted source responses by default;
- least-privilege read-only identities;
- tenant and subject isolation;
- source authenticity;
- request and result attribution;
- response-integrity inputs;
- secret and credential non-persistence;
- sensitive-data minimization;
- scope minimization;
- bounded response and pagination processing;
- audit-safe structured failures;
- provenance continuity;
- supply-chain independence;
- safe cancellation;
- bounded resource use.

No secret, credential, network, filesystem, persistence, plugin, subprocess,
remote-code, or production access is authorized by this planning.

## 23. Cross-Program and Phase-Boundary Non-Drift

NEXUS remains authoritative for approved architecture truth where applicable.

Provider and enterprise sources remain authoritative for their own bounded
source state.

Phase 4 remains authoritative for observation-to-evidence eligibility.

AFR deterministic evaluation remains authoritative for conformance outcomes.

ATA retains consequential runtime commit authority where applicable.

Planning must preserve:

`DEPENDENCY_RECOGNITION != INTEGRATION_PLANNING_AUTHORITY`

`INTEGRATION_PLANNING_AUTHORITY != INTEGRATION_IMPLEMENTATION_AUTHORITY`

`INTEGRATION_IMPLEMENTATION_AUTHORITY != RUNTIME_AUTHORITY`

Collection cannot elevate source state to architecture truth, evidence
eligibility, conformance, or runtime authority.

## 24. Explicitly Prohibited Work

Phase 5 planning creates no authority for:

- source code;
- tests, vectors, fixtures, or executable schemas;
- dependency, build-system, or configuration changes;
- live evidence collection;
- provider adapters;
- cloud or enterprise API calls;
- credentials or secrets;
- filesystem or network access;
- persistence, databases, queues, streams, caches, or object stores;
- NEXUS integration;
- ARCP integration or semantic definition;
- ATA integration;
- Phase 4 eligibility implementation or amendment;
- deterministic-kernel invocation;
- runtime conformance evaluation;
- model calls or model-based repair;
- certificate generation, signing, or issuance;
- APIs, services, workers, schedulers, or command-line interfaces;
- deployment or production access;
- runtime enforcement;
- remediation.

## 25. Stop Conditions

Planning must stop and require separate authority if:

- architecture-truth export semantics become necessary;
- NEXUS or ARCP semantics must be defined;
- provider-specific behavior becomes normative;
- live collection becomes necessary;
- credentials or secrets become necessary;
- network access becomes necessary;
- persistence becomes necessary;
- Phase 4 eligibility semantics require amendment;
- accepted Phase 0 through Phase 4 semantics require amendment;
- a seventh planning document becomes necessary;
- executable schemas, source, tests, dependencies, or configuration become
  necessary;
- implementation or runtime behavior becomes necessary.

## 26. Review Sequence

The planning package must pass:

- exact six-document boundary verification;
- exact-content and serialization freeze;
- SHA-256 freeze;
- architecture review;
- contract and semantic review;
- collection-scope and completeness review;
- temporal-semantics review;
- failure-model review;
- bounded-resource review;
- security and privacy review;
- provider-neutrality review;
- Phase 4 boundary non-drift review;
- NEXUS, ARCP, and ATA authority non-drift review;
- authority-leakage review;
- independent whole-package re-review;
- repository materialization review;
- staged-object verification;
- exact commit and tree verification;
- remote branch and pull-request verification;
- explicit readiness transition;
- explicit merge authorization;
- post-merge canonical verification;
- separately governed planning closure.

No earlier gate implies a later gate.

## 27. Completion Condition

Phase 5 planning is complete only after the exact reviewed package is merged
to canonical `main`, independently verified locally and remotely, and
reconciled through a separately governed planning closure.

Planning completion does not create implementation authority.

## 28. Authority State

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
