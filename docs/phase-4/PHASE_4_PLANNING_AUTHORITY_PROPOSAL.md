# AFR Phase 4 Planning-Authority Proposal

## 1. Purpose

This document proposes conditional planning authority for the next bounded
AFR capability:

`OPERATIONAL_EVIDENCE_INTAKE_AND_ELIGIBILITY_PLANNING`

It is a planning-authority proposal only. It creates no Phase 4 planning
authority before canonical merge and successful post-merge verification.

It creates no implementation, live collection, integration, persistence,
runtime evaluation, certificate, deployment, enforcement, remediation, or
production authority.

## 2. Canonical Foundation

The proposal begins from:

- canonical `main`:
  `5d289f7cdcd52224502ad70e5fef5c99c958dd1a`;
- canonical tree:
  `e120886e59a9fdb615fd76763444af2b997a075b`;
- Phase 3 status: `COMPLETE`;
- Phase 3 planning authority: `CONSUMED_CLOSED`;
- Phase 3 implementation authority: `CONSUMED_CLOSED`.

Phase 3 cannot be reopened, extended, or reinterpreted by this proposal.

## 3. Custodian Input

The reviewed non-canonical custodian input is:

- title:
  `AFR PHASE 4 CROSS-PROGRAM NON-DRIFT CUSTODIAN DIRECTIVE`;
- SHA-256:
  `1350851c7c82be0e1feb724dee31fc3823cd18ef9b167f0caa8839657ed9c0c5`;
- status: `NON_CANONICAL_CUSTODIAN_INPUT`;
- review: `PASS`;
- blocking findings: `NONE`.

Custodian input constrains drift but does not create canonical authority.

## 4. Canonical Discovery Result

Read-only discovery established:

```text
AFR_PHASE_4_CAPABILITY_CANDIDATE =
OPERATIONAL_EVIDENCE_INTAKE_AND_ELIGIBILITY_PLANNING

AFR_PHASE_4_MISSION =
DEFINE_BOUNDED_OBSERVATION_TO_ELIGIBLE_EVIDENCE_SEMANTICS

AFR_PHASE_4_POSITION =
BETWEEN_EXTERNAL_OBSERVATIONS_AND_THE_DETERMINISTIC_KERNEL
```

Phase 1 through Phase 3 already established the canonical information
model, evaluation semantics, deterministic-kernel architecture, executable
contract mapping, typed contracts, canonicalization, fingerprints, and
deterministic tests.

Live evidence intake, provider adapters, runtime evaluation, persistence,
certificates, and deployment remain absent and unauthorized.

## 5. Cross-Program Disposition

Canonical discovery selected:

```text
DISPOSITION_A =
PHASE_4_DOES_NOT_REQUIRE_ARCHITECTURE_TRUTH_CONTRACT_WORK
```

Phase 4 planning can define AFR-owned operational-evidence eligibility
without defining or implementing an upstream architecture-truth contract.

NEXUS Phase 19 and ARCP remain:

`RESERVED_UPSTREAM_DEPENDENCY_ONLY`

This proposal creates no NEXUS, ARCP, export-contract, parsing,
serialization, schema, adapter, or integration authority.

## 6. Exact Proposal Boundary

The current proposal change is limited to:

1. `docs/SOT.md`
2. `docs/phase-4/PHASE_4_PLANNING_AUTHORITY_PROPOSAL.md`

No third file is authorized by this proposal materialization.

## 7. Requested Planning Authority

The proposal requests authority to create and reconcile planning
documentation for:

- an adapter-neutral operational-observation ingress model;
- deterministic evidence-eligibility semantics;
- evidence identity and binding requirements;
- provenance, integrity, freshness, and trusted-time requirements;
- tenant, subject, environment, scope, and version bindings;
- replay, duplication, conflict, partial-evidence, and ordering semantics;
- deterministic resource limits;
- structured intake and eligibility processing failures;
- the handoff boundary to the accepted deterministic kernel;
- security, privacy, audit, and supply-chain constraints.

The requested authority is documentation-only.

## 8. Proposed Future Planning Package

If this proposal becomes effective, planning materialization is limited to:

1. `docs/SOT.md`
2. `docs/phase-4/PHASE_4_PLAN.md`
3. `docs/phase-4/PHASE_4_ACCEPTANCE_CRITERIA.md`
4. `docs/architecture/AFR_OPERATIONAL_EVIDENCE_INTAKE_ARCHITECTURE.md`
5. `docs/contracts/AFR_EVIDENCE_ELIGIBILITY_CONTRACT.md`
6. `docs/security/AFR_PHASE_4_EVIDENCE_TRUST_BOUNDARY.md`

These are future documentation paths only. They do not exist by authority
of this proposal and cannot be created before its effective point.

Renaming, relocating, or adding another document requires separate
authority.

## 9. Observation Ingress Planning Questions

Planning must determine:

- the minimum immutable observation envelope;
- source identity and source-class representation;
- observation identity and version;
- tenant, subject, environment, and scope binding;
- observed, received, and applicable time semantics;
- content integrity and provenance-chain inputs;
- declared input size and deterministic work accounting;
- supported and unsupported payload representations;
- explicit absence and explicit-null semantics;
- rejection of ambiguous or under-bound observations.

Planning cannot implement an ingress service or collector.

## 10. Evidence Eligibility Planning Questions

Planning must define how a supplied observation is classified as:

- eligible evidence;
- ineligible evidence;
- quarantined input;
- unsupported input;
- processing failure.

Eligibility must remain distinct from conformance. An eligible observation
is not automatically supporting or contradicting evidence, and it produces
no conformance outcome by itself.

Processing failures must remain distinct from both eligibility
classifications and conformance outcomes.

## 11. Identity and Binding Requirements

Planning must define explicit bindings for:

- evidence identifier;
- observation identifier;
- source identifier and source class;
- tenant;
- subject;
- environment;
- release or deployment scope where applicable;
- evidence type and schema version;
- provenance;
- integrity reference;
- observed time;
- received time;
- validity and freshness window;
- eligibility-policy version.

No binding may be inferred from ambient process, filesystem, network,
credential, or provider context.

## 12. Replay and Duplication Semantics

Planning must distinguish:

- byte-identical replay;
- semantically equivalent duplicate;
- identifier reuse with changed content;
- stale replay;
- cross-tenant replay;
- cross-subject substitution;
- conflicting observations;
- reordered observations.

Deduplication must not erase provenance, conflict, or freshness information.

No persistence mechanism is authorized to implement replay detection.

## 13. Conflict and Partial-Evidence Semantics

Planning must define deterministic behavior for:

- incomplete observation envelopes;
- missing required bindings;
- contradictory observations;
- partially eligible evidence sets;
- unknown source classes;
- unavailable integrity material;
- ambiguous timestamps;
- expired freshness windows;
- unsupported versions.

Missing or conflicting information must not be silently repaired by a model
or converted into false conformance certainty.

## 14. Deterministic Resource Constraints

Planning must define explicitly versioned limits for:

- input bytes;
- envelope fields;
- collection cardinality;
- nesting depth;
- provenance-chain length;
- integrity-reference length;
- normalized evidence bytes;
- deterministic processing work units.

Limit violations must fail before downstream kernel handoff. Truncation,
sampling, omission, or silent repair is prohibited.

Wall-clock time may provide an external safety stop but cannot select,
modify, validate, or legitimize an eligibility result.

## 15. Adapter-Neutral Boundary

Phase 4 planning must remain independent of AWS, Azure, GCP, Kubernetes,
CI/CD, model gateways, MCP systems, observability vendors, and other
provider-specific APIs.

Provider adapters may later supply observations, but they cannot determine
AFR evidence eligibility or expand their own authority.

No provider adapter or live collection mechanism is authorized.

## 16. Deterministic-Kernel Handoff

Planning must define a one-way conceptual handoff:

```text
SUPPLIED_OPERATIONAL_OBSERVATION
    -> VALIDATED_OBSERVATION_ENVELOPE
    -> ELIGIBILITY_DECISION
    -> IMMUTABLE_ELIGIBLE_EVIDENCE
    -> FUTURE_SEPARATELY_AUTHORIZED_KERNEL_INVOCATION
```

Phase 4 planning does not invoke the kernel.

It must preserve the accepted canonicalization, fingerprint, resource,
failure, tenant, subject, version, and outcome semantics without amending
Phase 3 implementation.

## 17. Security and Trust Requirements

Planning must address:

- untrusted input by default;
- strict type and version validation;
- tenant and subject isolation;
- provenance completeness;
- integrity verification inputs;
- freshness and trusted-time inputs;
- replay and substitution resistance;
- deterministic resource exhaustion controls;
- sensitive-data minimization;
- audit-safe failure records;
- fail-closed unsupported-version behavior;
- supply-chain independence.

Planning cannot introduce credentials, secrets, network calls, filesystem
writes, databases, queues, caches, subprocesses, plugins, or dependencies.

## 18. NEXUS, ARCP, and ATA Boundaries

NEXUS or another approved architecture authority continues to own approved
architecture truth.

AFR remains a read-only consumer of approved architecture truth.

Phase 4 concerns operational observations and evidence eligibility. It
neither defines nor changes architecture truth.

ARCP remains a reserved upstream direction and is not part of the Phase 4
planning package.

AFR eligibility and conformance results create no ATA or other runtime
authority.

## 19. Explicitly Prohibited Scope

This proposal creates no authority for:

- source code;
- tests, vectors, fixtures, or executable schemas;
- dependency or build-system changes;
- live evidence collection;
- provider or cloud adapters;
- filesystem or network access;
- secrets, credentials, or production configuration;
- NEXUS or ARCP integration;
- runtime conformance evaluation;
- model calls or model-based repair;
- persistence, databases, caches, queues, or streams;
- certificate design, generation, signing, or issuance;
- APIs, services, workers, schedulers, or command-line interfaces;
- deployment or production access;
- runtime enforcement;
- remediation;
- ATA integration;
- another Phase 3 implementation slice.

## 20. Stop Conditions

Planning must stop and require new authority if:

- the proposed capability requires architecture-truth contract work;
- Disposition A becomes invalid;
- NEXUS or ARCP semantics become necessary;
- a provider-specific adapter becomes necessary;
- live collection becomes necessary;
- persistence becomes necessary;
- runtime kernel invocation becomes necessary;
- certificate work becomes necessary;
- an executable schema or dependency becomes necessary;
- the six-document planning boundary is insufficient;
- accepted Phase 1 through Phase 3 semantics would need amendment.

### Complete Pre-Activation Authority State

Before the proposal effective point, all of the following remain explicitly
unauthorized:

- `AFR_PHASE_4_PLANNING_AUTHORITY = NONE`
- `AFR_PHASE_4_IMPLEMENTATION_AUTHORITY = NONE`
- `AFR_PHASE_4_LIVE_EVIDENCE_COLLECTION_AUTHORITY = NONE`
- `AFR_PHASE_4_PROVIDER_INTEGRATION_AUTHORITY = NONE`
- `AFR_PHASE_4_NEXUS_INTEGRATION_AUTHORITY = NONE`
- `AFR_PHASE_4_ARCP_AUTHORITY = NONE`
- `AFR_PHASE_4_RUNTIME_EVALUATION_AUTHORITY = NONE`
- `AFR_PHASE_4_PERSISTENCE_AUTHORITY = NONE`
- `AFR_PHASE_4_CERTIFICATE_AUTHORITY = NONE`
- `AFR_PHASE_4_DEPLOYMENT_AUTHORITY = NONE`
- `AFR_PHASE_4_ENFORCEMENT_AUTHORITY = NONE`
- `AFR_PHASE_4_REMEDIATION_AUTHORITY = NONE`
- `AFR_PHASE_4_AUTHORITY = NONE`

## 21. Proposal Effective Point

Current state:

```text
AFR_PHASE_4_PLANNING_AUTHORITY_PROPOSAL =
DRAFT_REVIEW_CANDIDATE

AFR_PHASE_4_PLANNING_AUTHORITY =
NONE

AFR_PHASE_4_IMPLEMENTATION_AUTHORITY =
NONE

AFR_PHASE_4_RUNTIME_EVALUATION_AUTHORITY =
NONE

AFR_PHASE_4_PROVIDER_INTEGRATION_AUTHORITY =
NONE

AFR_PHASE_4_NEXUS_INTEGRATION_AUTHORITY =
NONE

AFR_PHASE_4_PERSISTENCE_AUTHORITY =
NONE

AFR_PHASE_4_CERTIFICATE_AUTHORITY =
NONE

AFR_PHASE_4_DEPLOYMENT_AUTHORITY =
NONE

AFR_PHASE_4_AUTHORITY =
NONE
```

Planning authority becomes effective if and only if:

1. this proposal remains limited to its exact two-document boundary;
2. both documents are frozen by exact content hash;
3. the whole proposal receives independent architecture, security,
   semantic, non-drift, and authority-leakage review;
4. every blocking finding is resolved;
5. the exact reviewed objects are staged and committed;
6. the proposal branch resolves to the reviewed commit and tree;
7. a draft pull request preserves the exact base, head, tree, one-commit
   identity, boundary, and hashes;
8. the pull request receives independent acceptance review;
9. the pull request is explicitly transitioned from draft to ready;
10. explicit merge authorization is granted;
11. the reviewed proposal is merged to canonical `main`;
12. post-merge identity, both parents, tree, exact boundary, and both
    content hashes are verified;
13. local and remote canonical `main` converge cleanly;
14. the canonical worktree and index are clean.

Draft creation, review, approval, or readiness cannot activate planning
authority. Merge without successful post-merge verification also cannot
activate it.

## 22. State After Activation

After and only after the effective point:

```text
AFR_PHASE_4_CAPABILITY =
OPERATIONAL_EVIDENCE_INTAKE_AND_ELIGIBILITY_PLANNING

AFR_PHASE_4_DISPOSITION =
PHASE_4_DOES_NOT_REQUIRE_ARCHITECTURE_TRUTH_CONTRACT_WORK

AFR_PHASE_4_PLANNING_AUTHORITY =
BOUNDED_OPERATIONAL_EVIDENCE_INTAKE_AND_ELIGIBILITY_PLANNING_ONLY

AFR_PHASE_4_IMPLEMENTATION_AUTHORITY =
NONE

AFR_PHASE_4_LIVE_EVIDENCE_COLLECTION_AUTHORITY =
NONE

AFR_PHASE_4_PROVIDER_INTEGRATION_AUTHORITY =
NONE

AFR_PHASE_4_NEXUS_INTEGRATION_AUTHORITY =
NONE

AFR_PHASE_4_ARCP_AUTHORITY =
NONE

AFR_PHASE_4_RUNTIME_EVALUATION_AUTHORITY =
NONE

AFR_PHASE_4_PERSISTENCE_AUTHORITY =
NONE

AFR_PHASE_4_CERTIFICATE_AUTHORITY =
NONE

AFR_PHASE_4_DEPLOYMENT_AUTHORITY =
NONE

AFR_PHASE_4_ENFORCEMENT_AUTHORITY =
NONE

AFR_PHASE_4_REMEDIATION_AUTHORITY =
NONE
```

Planning acceptance will later require its own independently reviewed,
merged, verified, and separately closed acceptance process.

## 23. Non-Activation Statement

This proposal does not itself create, approve, merge, activate, or execute
the Phase 4 planning package.

It authorizes nothing before its complete effective point.

It cannot authorize implementation, collection, integrations, persistence,
runtime evaluation, certificates, deployment, enforcement, remediation, or
production activity.

## 24. Cross-Program Addendum Reconciliation

This proposal records two separate non-canonical custodian inputs:

1. original cross-program non-drift custodian directive, SHA-256
   `1350851c7c82be0e1feb724dee31fc3823cd18ef9b167f0caa8839657ed9c0c5`;
2. bounded custodian addendum, SHA-256
   `786e63267665ccbd44389a08cc4f1046eb357fc93cf448b5a45fc00109630a95`.

Neither custodian input is canonical AFR, NEXUS, ARCP, or ATA evidence.
Neither creates planning, implementation, integration, runtime, persistence,
certificate, deployment, enforcement, remediation, or Phase 4 authority.

`CUSTODIAN_INPUT != CANONICAL_EVIDENCE`

`DESCRIBED_AS_EXISTING != PROVEN_EXISTING_CANONICAL`

Cross-program semantic ownership remains unresolved:

`ARCP_WORKING_LABEL = ARCP`

`ARCP_CANONICAL_NAME =
UNRESOLVED_PENDING_NEXUS_PHASE_19_GOVERNANCE`

`ARCP_CANONICAL_SEMANTICS =
UNRESOLVED_PENDING_NEXUS_PHASE_19_GOVERNANCE`

`NEXUS_PHASE_19_DIRECTION =
RESERVED_UPSTREAM_ARCHITECTURE_DIRECTION`

`NEXUS_PHASE_19_CANONICAL_CAPABILITY_NAME =
MUST_BE_VERIFIED_FROM_CANONICAL_NEXUS_STATE`

AFR does not independently expand, rename, define, or canonicalize ARCP or
the NEXUS Phase 19 capability.

### Semantic Classification Register

The classifications below identify canonical Phase 0 through Phase 3
architecture and contract semantics. `EXISTING_CANONICAL` does not mean that
Phase 4 collection, orchestration, integration, or runtime behavior exists or
is authorized.

| Semantic | Classification | Canonical evidence | Evidence location / identity |
|---|---|---|---|
| Operational-observation handling | `EXISTING_CANONICAL` | Canonical information flow distinguishes observations from evidence and evaluation. | `docs/architecture/AFR_REFERENCE_ARCHITECTURE.md`, §5; `docs/phase-1/PHASE_1_PLAN.md`, §6; canonical tree `e120886e59a9fdb615fd76763444af2b997a075b` |
| Evidence eligibility | `EXISTING_CANONICAL` | Eligibility is a deterministic precondition for evidence use. | `docs/contracts/AFR_CANONICAL_INFORMATION_MODEL.md`, §9; `docs/architecture/AFR_DETERMINISTIC_KERNEL_ARCHITECTURE.md`, §11; canonical tree `e120886e59a9fdb615fd76763444af2b997a075b` |
| Provenance validation | `EXISTING_CANONICAL` | Evidence trust requires attributable source and provenance. | `docs/architecture/AFR_REFERENCE_ARCHITECTURE.md`, Evidence Trust Plane and §5; canonical tree `e120886e59a9fdb615fd76763444af2b997a075b` |
| Integrity validation | `EXISTING_CANONICAL` | Evidence integrity checks are mapped into the deterministic trust boundary. | `docs/contracts/AFR_EXECUTABLE_CONTRACT_MAPPING.md`, §13; `docs/security/AFR_PHASE_2_KERNEL_TRUST_BOUNDARY.md`, §10; canonical tree `e120886e59a9fdb615fd76763444af2b997a075b` |
| Freshness evaluation | `EXISTING_CANONICAL` | Time-bound evidence freshness and stale-state handling are defined. | `docs/contracts/AFR_EVALUATION_SEMANTICS.md`, §11; `docs/security/AFR_PHASE_2_KERNEL_TRUST_BOUNDARY.md`, §12; canonical tree `e120886e59a9fdb615fd76763444af2b997a075b` |
| Deterministic evaluation definitions | `EXISTING_CANONICAL` | Evaluation semantics require deterministic definitions and bounded inputs. | `docs/contracts/AFR_EVALUATION_SEMANTICS.md`, §4; canonical tree `e120886e59a9fdb615fd76763444af2b997a075b` |
| Deterministic rule resolution | `EXISTING_CANONICAL` | Rule resolution and kernel ordering are explicitly deterministic. | `docs/contracts/AFR_KERNEL_EXECUTION_CONTRACT.md`, §11; `docs/architecture/AFR_DETERMINISTIC_KERNEL_ARCHITECTURE.md`, §12; canonical tree `e120886e59a9fdb615fd76763444af2b997a075b` |
| Claim-level conformance evaluation | `EXISTING_CANONICAL` | Claim-level evaluation is defined as a deterministic kernel responsibility. | `docs/architecture/AFR_DETERMINISTIC_KERNEL_ARCHITECTURE.md`, §13; `docs/architecture/AFR_KERNEL_IMPLEMENTATION_BLUEPRINT.md`, §11; canonical tree `e120886e59a9fdb615fd76763444af2b997a075b` |
| Aggregate conformance evaluation | `EXISTING_CANONICAL` | Aggregate outcomes and their composition semantics are defined. | `docs/contracts/AFR_CANONICAL_INFORMATION_MODEL.md`, §17; `docs/contracts/AFR_EVALUATION_SEMANTICS.md`, §22; canonical tree `e120886e59a9fdb615fd76763444af2b997a075b` |
| Conformance fingerprints | `EXISTING_CANONICAL` | Fingerprint semantics are canonical and the first bounded implementation is accepted. | `docs/architecture/AFR_DETERMINISTIC_KERNEL_ARCHITECTURE.md`, §16; `src/afr/kernel/fingerprints.py` at canonical tree `e120886e59a9fdb615fd76763444af2b997a075b` |
| Conformance findings | `EXISTING_CANONICAL` | Findings are canonical AFR records and remain distinct from architecture truth. | `docs/SOT.md`, §3; `docs/adr/ADR-0001-nexus-authoritative-truth-boundary.md`, Decision; canonical tree `e120886e59a9fdb615fd76763444af2b997a075b` |

Every classification is governed by this fail-closed invariant:

`ANY AFR SEMANTIC NOT PROVEN FROM CANONICAL PHASE 0-3 EVIDENCE
MUST NOT BE CLASSIFIED AS EXISTING_CANONICAL.`

If canonical evidence is absent, ambiguous, incomplete, or insufficient, the
semantic must be classified as `RESERVED_FUTURE` or `NOT_ESTABLISHED`, as
applicable. Canonical status must not be inferred from either custodian input.

`RESERVED_FUTURE` and `NOT_ESTABLISHED` semantics must not be described as
implemented, activated, current, or authoritative existing capability.

### Dependency and Authority Separation

The following states are distinct, and none implies the next:

`DEPENDENCY_RECOGNITION`

`INTEGRATION_PLANNING`

`INTEGRATION_IMPLEMENTATION`

`RUNTIME_USE`

Therefore:

`DEPENDENCY_RECOGNITION != INTEGRATION_PLANNING_AUTHORITY`

`INTEGRATION_PLANNING_AUTHORITY !=
INTEGRATION_IMPLEMENTATION_AUTHORITY`

`INTEGRATION_IMPLEMENTATION_AUTHORITY != RUNTIME_AUTHORITY`

`FUTURE_NEXUS_TO_AFR_ARCHITECTURE_TRUTH_CONSUMER_CONTRACT` is preserved
strictly as a non-canonical placeholder description. It is not a canonical
ARCP name, canonical contract name, schema, API, adapter, implementation, or
active integration authority.

The upstream authority state remains:

`NEXUS_PHASE_19_IMPLEMENTATION_AUTHORITY = NONE`

`ARCP_IMPLEMENTATION_AUTHORITY = NONE`

`ARCP_RUNTIME_AUTHORITY = NONE`

This reconciliation does not change the established Phase 4 capability
candidate, Disposition A, exact future six-document boundary, effective point,
scope boundary, non-drift boundary, or non-authorization constraints.

The proposal remains pre-effective and fail-closed:

`AFR_PHASE_4_ADDENDUM_RECONCILIATION =
MATERIALIZED_REVIEW_REQUIRED`

`AFR_PHASE_4_PLANNING_AUTHORITY_PROPOSAL =
DRAFT_REREVIEW_REQUIRED`

`AFR_PHASE_4_PLANNING_AUTHORITY = NONE`

`AFR_PHASE_4_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_4_RUNTIME_EVALUATION_AUTHORITY = NONE`

`AFR_PHASE_4_NEXUS_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_4_ARCP_AUTHORITY = NONE`

`AFR_PHASE_4_AUTHORITY = NONE`

Independent whole-proposal re-review of the complete unstaged two-document
candidate is mandatory before staging may be considered.
