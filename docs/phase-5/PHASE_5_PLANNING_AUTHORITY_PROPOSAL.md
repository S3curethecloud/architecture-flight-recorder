# AFR Phase 5 Planning-Authority Proposal

## 1. Purpose

This document proposes conditional planning authority for the next bounded
Architecture Flight Recorder capability:

`EVIDENCE_ACQUISITION_AND_COLLECTION_BOUNDARY_PLANNING`

It is a planning-authority proposal candidate only.

It creates no Phase 5 planning authority before canonical merge and successful
post-merge verification through the complete effective point defined here.

It creates no implementation, live collection, provider integration,
credential, network, persistence, NEXUS, ARCP, ATA, runtime evaluation,
certificate, deployment, enforcement, remediation, or production authority.

## 2. Canonical Foundation

This proposal begins from:

- canonical `main`:
  `75cb8f4339911b830b4faed09f24bc69267c7b2f`;
- canonical tree:
  `9216178e83836c80dc593dc18ea6da805d7441e6`;
- Phase 4 planning status: `COMPLETE`;
- Phase 4 planning authority: `CONSUMED_CLOSED`;
- Phase 4 first-slice implementation status: `COMPLETE`;
- Phase 4 implementation authority: `CONSUMED_CLOSED`;
- Phase 4 additional implementation authority: `NONE`;
- Phase 5 start authority: `NONE`.

Phase 4 cannot be reopened, extended, or reinterpreted by this proposal.

This proposal does not establish that every Phase 4 semantic requires
executable implementation.

## 3. Noncanonical Discovery and Selection Evidence

Separately governed read-only lifecycle gates established:

`AFR_PHASE_5_CAPABILITY_CANDIDATE =
EVIDENCE_ACQUISITION_AND_COLLECTION_BOUNDARY_PLANNING`

`AFR_PHASE_5_MISSION =
DEFINE_BOUNDED_READ_ONLY_COLLECTION_OF_ATTRIBUTABLE_OPERATIONAL_OBSERVATIONS_FOR_PHASE4_INGRESS`

`AFR_PHASE_5_POSITION =
BETWEEN_APPROVED_PROVIDER_ENTERPRISE_SOURCES_AND_PHASE4_SUPPLIED_OPERATIONAL_OBSERVATION`

The candidate was selected because:

- the Evidence Acquisition Plane is a canonical AFR architectural plane;
- the boundary is AFR-owned;
- it is directly adjacent to Phase 4's supplied-observation boundary;
- it does not require unresolved upstream NEXUS export semantics for planning;
- it is not already substantially governed by Phase 1 through Phase 3;
- it can be planned provider-neutrally without runtime or provider mutation;
- findings/certificate and delivery/integration remain downstream capabilities.

These discovery and selection results are noncanonical review evidence. They
do not independently create Phase 5 authority.

## 4. Cross-Program Disposition

NEXUS remains authoritative for approved architecture truth.

Architecture-truth intake is not selected as the Phase 5 capability because
the NEXUS-to-AFR export contract remains an upstream governance dependency.

This proposal does not define:

- a NEXUS export contract;
- ARCP canonical semantics;
- ATA policy or runtime authority;
- cross-program integration behavior.

Dependency recognition does not create integration authority.

## 5. Exact Proposal Boundary

The future repository proposal change is limited exactly to:

1. `docs/SOT.md`
2. `docs/phase-5/PHASE_5_PLANNING_AUTHORITY_PROPOSAL.md`

No third repository document is authorized by this proposal.

The current R1 candidate is prepared outside the repository for review only.

## 6. Requested Planning Authority

This proposal requests:

`AFR_PHASE_5_PLANNING_AUTHORITY =
BOUNDED_EVIDENCE_ACQUISITION_AND_COLLECTION_BOUNDARY_PLANNING_ONLY`

The requested authority is documentation-only.

It may define planning semantics and architecture for bounded read-only
collection of attributable operational observations for later Phase 4 ingress.

It may not create executable collection behavior.

## 7. Proposed Future Planning Package

If and only if this proposal becomes effective, Phase 5 planning
materialization is proposed to be limited to exactly:

1. `docs/SOT.md`
2. `docs/phase-5/PHASE_5_PLAN.md`
3. `docs/phase-5/PHASE_5_ACCEPTANCE_CRITERIA.md`
4. `docs/architecture/AFR_EVIDENCE_ACQUISITION_ARCHITECTURE.md`
5. `docs/contracts/AFR_OBSERVATION_ACQUISITION_CONTRACT.md`
6. `docs/security/AFR_PHASE_5_EVIDENCE_ACQUISITION_TRUST_BOUNDARY.md`

These are future documentation paths only.

This proposal does not itself authorize their creation.

Renaming, relocating, or adding another planning document requires separate
authority.

## 8. Collector and Source Identity Planning

Planning must determine:

- collector identity;
- source identity;
- source class;
- tenant binding;
- subject binding;
- environment binding;
- collection-scope binding;
- collection-request identity;
- observation identity;
- provider or enterprise source reference;
- collector authorization context;
- least-privilege read-only identity requirements.

Identity cannot be inferred from ambient process, filesystem, network,
credential, hostname, provider, or presentation context.

## 9. Collection and Observation Time Semantics

Planning must distinguish:

- request time;
- collection start time;
- collection completion time;
- provider/source observation time where available;
- source response time where meaningful;
- handoff time to Phase 4;
- collection validity or applicability windows where required.

A timestamp alone cannot prove freshness, completeness, or authority.

Phase 5 planning cannot redefine Phase 4 trusted-time or evidence-freshness
semantics.

## 10. Collection Scope and Completeness

Planning must define bounded semantics for:

- requested collection scope;
- observed collection scope;
- successful scope;
- failed scope;
- unsupported scope;
- omitted scope;
- partial collection;
- pagination or segmented collection boundaries;
- source-side filtering;
- collector-side filtering where permitted;
- completeness claims.

A collector must not claim completeness beyond what was actually observed and
successfully bounded.

Unknown or partial collection must remain explicit.

## 11. Source Failure and Partial Collection

Planning must define explicit representations for:

- provider access failure;
- source timeout;
- source throttling;
- partial response;
- pagination failure;
- unsupported endpoint or operation;
- authorization denial;
- malformed source response;
- ambiguous source identity;
- collection cancellation;
- collector internal failure.

Collection failure cannot be converted into negative evidence, positive
evidence, evidence eligibility, or conformance.

## 12. Raw Source Response Preservation

Planning may define requirements for preserving raw source responses where
permitted by security, privacy, contractual, and provider constraints.

Planning must distinguish:

- raw response identity;
- source-native representation;
- redacted or minimized representation;
- collector-generated metadata;
- transformation metadata;
- handoff representation.

Preservation requirements cannot create persistence authority.

## 13. Provider-Neutral Collector Contract

Planning must remain provider-neutral.

The planning architecture must not depend on AWS, Azure, GCP, Kubernetes,
CI/CD products, observability vendors, SaaS products, model gateways, MCP
servers, or other provider-specific APIs.

Provider-specific mappings may become separate future work only under
separately granted authority.

No provider adapter is authorized by this proposal.

## 14. Phase 4 Handoff Boundary

The conceptual Phase 5 boundary ends at a supplied operational observation
prepared for Phase 4 intake.

The proposed conceptual flow is:

```text
APPROVED_PROVIDER_OR_ENTERPRISE_SOURCE
    -> BOUNDED_READ_ONLY_COLLECTION_REQUEST
    -> ATTRIBUTABLE_COLLECTION_RESULT
    -> SUPPLIED_OPERATIONAL_OBSERVATION
    -> PHASE_4_EVIDENCE_INTAKE_AND_ELIGIBILITY_BOUNDARY
```

Phase 5 planning must not determine whether the observation is eligible
evidence.

Phase 5 planning must not invoke the deterministic conformance kernel.

Phase 5 planning must not select a conformance result.

## 15. Authority Separation

Phase 5 planning must preserve:

- provider-state authority with the provider or enterprise source;
- architecture-truth authority with NEXUS or another approved authority;
- observation-to-evidence eligibility authority within the Phase 4 boundary;
- conformance-evaluation authority within AFR's deterministic evaluation
  boundary;
- consequential runtime commit authority with ATA where applicable.

Collection cannot elevate observation authority.

Presentation cannot elevate collection authority.

## 16. Security, Privacy, and Audit Planning

Planning must address:

- least-privilege read-only collector identities;
- tenant and subject isolation;
- source authenticity;
- collection request attribution;
- source-response integrity inputs;
- secret and credential non-persistence;
- sensitive-data minimization;
- collection-scope minimization;
- audit-safe failure records;
- provenance continuity into Phase 4;
- supply-chain independence;
- bounded resource use;
- safe cancellation and failure exposure.

This planning creates no credential, secret, network, provider-access, or
production authority.

## 17. Explicitly Prohibited Scope

This proposal creates no authority for:

- source code;
- tests, vectors, fixtures, or executable schemas;
- dependency or build-system changes;
- live evidence collection;
- provider adapters;
- cloud or enterprise API calls;
- credentials or secrets;
- filesystem access by a future runtime collector;
- network access;
- persistence, databases, queues, streams, or caches;
- NEXUS integration;
- ARCP integration or semantic definition;
- ATA integration;
- Phase 4 eligibility implementation;
- deterministic kernel invocation;
- runtime conformance evaluation;
- model calls or model-based repair;
- certificate generation, signing, or issuance;
- APIs, services, workers, schedulers, or command-line interfaces;
- deployment or production access;
- runtime enforcement;
- remediation.

## 18. Stop Conditions

Planning must stop and require new authority if:

- upstream architecture-truth export semantics become necessary;
- NEXUS or ARCP semantics become necessary;
- provider-specific implementation becomes necessary;
- live collection becomes necessary;
- credentials or secrets become necessary;
- network access becomes necessary;
- persistence becomes necessary;
- Phase 4 evidence-eligibility semantics require amendment;
- Phase 1 through Phase 3 canonical semantics require amendment;
- deterministic kernel invocation becomes necessary;
- certificate work becomes necessary;
- executable schemas or dependencies become necessary;
- the six-document planning boundary becomes insufficient;
- implementation or runtime behavior becomes necessary.

## 19. Complete Pre-Activation Authority State

Before the proposal effective point:

`AFR_PHASE_5_PLANNING_AUTHORITY_PROPOSAL =
DRAFT_NONCANONICAL_REVIEW_CANDIDATE`

`AFR_PHASE_5_CANONICAL_CAPABILITY_DEFINITION =
NOT_ESTABLISHED`

`PHASE_5_START_AUTHORITY = NONE`

`AFR_PHASE_5_PLANNING_AUTHORITY = NONE`

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

## 20. Proposal Effective Point

Phase 5 planning authority becomes effective if and only if:

1. this proposal remains limited to its exact two-document repository boundary;
2. both proposal documents are frozen by exact content hash;
3. the complete proposal receives independent architecture, security,
   semantic, non-drift, and authority-leakage review;
4. every blocking finding is resolved;
5. the exact reviewed objects are materialized, staged, and committed under
   separately granted authority;
6. the proposal branch resolves to the reviewed commit and tree;
7. a Draft pull request preserves the exact base, head, tree, one-commit
   identity, two-document boundary, and frozen content identities;
8. the Draft pull request receives independent acceptance review;
9. the pull request is explicitly transitioned from Draft to Ready;
10. explicit merge authorization is granted for the exact Ready identity;
11. the exact reviewed proposal is merged to canonical `main`;
12. independent post-merge identity, ordered-parent, tree, exact-boundary, and
    content verification passes;
13. local and remote canonical `main` converge on the verified merge;
14. the canonical `main` checkout, worktree, and index are independently
    verified clean.

No earlier gate implies a later gate.

Proposal preparation, review, freezing, repository materialization, staging,
commit, Draft PR creation, acceptance, or Ready transition cannot independently
activate Phase 5 planning authority.

Merge without successful post-merge verification also cannot activate Phase 5
planning authority.

## 21. State After Activation

After and only after the complete effective point:

`AFR_PHASE_5_CAPABILITY =
EVIDENCE_ACQUISITION_AND_COLLECTION_BOUNDARY_PLANNING`

`AFR_PHASE_5_PLANNING_AUTHORITY =
BOUNDED_EVIDENCE_ACQUISITION_AND_COLLECTION_BOUNDARY_PLANNING_ONLY`

All implementation and runtime-adjacent authorities remain `NONE`:

- `AFR_PHASE_5_IMPLEMENTATION_AUTHORITY = NONE`
- `AFR_PHASE_5_LIVE_COLLECTION_AUTHORITY = NONE`
- `AFR_PHASE_5_PROVIDER_ADAPTER_IMPLEMENTATION_AUTHORITY = NONE`
- `AFR_PHASE_5_CREDENTIAL_AUTHORITY = NONE`
- `AFR_PHASE_5_NETWORK_AUTHORITY = NONE`
- `AFR_PHASE_5_PERSISTENCE_AUTHORITY = NONE`
- `AFR_PHASE_5_NEXUS_INTEGRATION_AUTHORITY = NONE`
- `AFR_PHASE_5_ARCP_AUTHORITY = NONE`
- `AFR_PHASE_5_ATA_INTEGRATION_AUTHORITY = NONE`
- `AFR_PHASE_5_RUNTIME_AUTHORITY = NONE`
- `AFR_PHASE_5_CERTIFICATE_AUTHORITY = NONE`
- `AFR_PHASE_5_DEPLOYMENT_AUTHORITY = NONE`
- `AFR_PHASE_5_ENFORCEMENT_AUTHORITY = NONE`
- `AFR_PHASE_5_REMEDIATION_AUTHORITY = NONE`

Planning acceptance later requires its own independently reviewed, merged,
verified, and separately closed planning lifecycle.

## 22. Non-Activation Statement

This proposal candidate does not itself create, approve, materialize in the AFR
repository, stage, commit, publish, merge, activate, or execute the Phase 5
planning package.

It authorizes nothing before its complete effective point.

It cannot authorize implementation, live collection, provider integration,
credentials, network access, persistence, NEXUS/ARCP/ATA integration, runtime
evaluation, certificates, deployment, enforcement, remediation, or production
activity.

No gate implies the next.
