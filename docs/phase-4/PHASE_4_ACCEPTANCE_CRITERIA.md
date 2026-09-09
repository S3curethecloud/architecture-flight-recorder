# AFR Phase 4 Acceptance Criteria

## 1. Purpose

These criteria govern acceptance of the documentation-only Phase 4 planning
package for:

`OPERATIONAL_EVIDENCE_INTAKE_AND_ELIGIBILITY_PLANNING`

They determine whether the planning package defines a coherent, deterministic,
adapter-neutral, and fail-closed boundary between supplied operational
observations and eligible evidence.

Satisfying these criteria does not authorize implementation, live collection,
integration, persistence, runtime kernel invocation, certificates, deployment,
enforcement, remediation, or production use.

## 2. Canonical Baseline

Phase 4 planning is acceptable only if:

- canonical `main` remains based on
  `25deed93df00d1db044a24164b9e46ca5a9e759d`;
- the activation tree remains
  `19ce8d96fe36052ef072635393a170bdca2d7ce0`;
- Phase 3 remains complete and terminally closed;
- Phase 3 planning and implementation authorities remain consumed and closed;
- all Phase 3 implementation artifacts remain byte-identical;
- no Phase 0 through Phase 3 semantic is silently reopened or amended.

## 3. Exact Planning-Package Boundary

The complete Phase 4 planning candidate must contain changes to exactly:

1. `docs/SOT.md`
2. `docs/phase-4/PHASE_4_PLAN.md`
3. `docs/phase-4/PHASE_4_ACCEPTANCE_CRITERIA.md`
4. `docs/architecture/AFR_OPERATIONAL_EVIDENCE_INTAKE_ARCHITECTURE.md`
5. `docs/contracts/AFR_EVIDENCE_ELIGIBILITY_CONTRACT.md`
6. `docs/security/AFR_PHASE_4_EVIDENCE_TRUST_BOUNDARY.md`

Acceptance fails if a seventh file or any source, test, vector, fixture,
executable schema, dependency, configuration, migration, or build artifact is
introduced.

## 4. Document Convergence

All six planning documents must converge on:

- one capability identity;
- one observation-to-evidence lifecycle;
- one eligibility vocabulary;
- one processing-failure taxonomy;
- one deterministic resource model;
- one adapter-neutral handoff boundary;
- one security and trust boundary;
- one cross-program non-drift position;
- one authority boundary.

Contradictory definitions, implicit defaults, or document-specific semantic
variants are blocking findings.

## 5. Observation-Envelope Acceptance

The planned observation envelope must explicitly define:

- observation identifier;
- envelope version;
- source identifier and source class;
- tenant identifier;
- subject identifier and subject type;
- environment and scope identifiers;
- release or deployment binding where applicable;
- observed, received, and applicable times;
- validity interval where applicable;
- declared payload representation;
- declared input-byte measurement;
- integrity reference;
- provenance-chain reference;
- explicit optional-field presence;
- content reference suitable for later canonical treatment.

No required binding may be inferred from credentials, process state,
filesystem location, network endpoint, provider account, deployment context,
or any other ambient state.

## 6. Evidence-Identity Acceptance

The planned evidence identity must bind:

- originating observation identity;
- normalized content identity;
- tenant;
- subject;
- environment;
- scope;
- source and provenance;
- integrity material;
- observed and received time;
- freshness policy;
- eligibility-policy version;
- envelope and evidence-model versions.

Identifier reuse with materially changed content must fail closed and must not
be treated as duplication.

## 7. Eligibility-Decision Acceptance

The planning package must distinguish exactly:

- `ELIGIBLE`;
- `INELIGIBLE`;
- `QUARANTINED`;
- `UNSUPPORTED`;
- `PROCESSING_FAILURE`.

Eligibility must remain a pre-conformance decision.

An eligibility decision must not emit `CONFORMANT`, `NON_CONFORMANT`,
`INCONCLUSIVE`, `STALE`, or any other conformance outcome.

Processing failures must remain distinct from eligibility classifications and
conformance outcomes.

## 8. Deterministic-Input Acceptance

Eligibility may depend only on explicit, immutable, and version-bound inputs.

The planning package must prohibit canonical decisions based on:

- elapsed processing time;
- randomness;
- model output;
- provider-specific behavior;
- network availability;
- ambient configuration;
- arrival-order convenience;
- operator discretion not represented in versioned policy.

Unsupported or malformed inputs must fail closed through deterministic,
structured outcomes.

## 9. Absence, Null, and Type Acceptance

The package must preserve distinctions among:

- absent optional fields;
- explicit nulls;
- empty values;
- missing required fields;
- unsupported values;
- unsupported types;
- unsupported versions.

These states must not be silently collapsed, inferred, defaulted, coerced, or
repaired.

## 10. Provenance, Integrity, and Freshness Acceptance

The planning package must define deterministic requirements for:

- source attribution;
- provenance completeness;
- provenance-chain validation inputs;
- integrity-verification inputs;
- observed and received time;
- trusted-time inputs;
- freshness policies;
- validity intervals;
- stale or expired observations;
- unavailable or unsupported trust material.

Missing or unverifiable trust material must not produce eligible evidence.

## 11. Tenant, Subject, Scope, and Version Acceptance

Eligibility and evidence identity must remain explicitly bound to tenant,
subject, environment, scope, release where applicable, and relevant versions.

The planning package must reject or quarantine, as explicitly defined:

- cross-tenant replay;
- cross-subject substitution;
- cross-environment substitution;
- cross-scope substitution;
- policy-version mismatch;
- envelope-version mismatch;
- evidence-model-version mismatch.

No ambient identity inference is permitted.

## 12. Replay and Duplication Acceptance

The package must distinguish:

- byte-identical replay;
- semantically equivalent duplication;
- identifier reuse with changed content;
- stale replay;
- cross-boundary replay;
- reordered delivery;
- conflicting observations.

Deduplication must not erase provenance, integrity, freshness, ordering, or
conflict information.

The semantics must not depend on an authorized replay store, database, queue,
cache, stream, or distributed coordination system.

## 13. Conflict and Partial-Evidence Acceptance

The package must define deterministic handling for:

- contradictory observations;
- incomplete envelopes;
- missing bindings;
- incomplete provenance;
- unavailable integrity material;
- ambiguous timestamps;
- expired freshness;
- unknown source classes;
- unsupported representations;
- unsupported versions;
- partially eligible evidence sets.

Partial evidence must not be promoted to complete evidence.

Conflict must not be resolved through arrival order, model judgment, provider
priority, silent omission, or operator convenience.

## 14. Deterministic Resource Acceptance

The package must define explicit, versioned limits for:

- total ingress bytes;
- envelope field count;
- collection cardinality;
- nesting depth;
- provenance-chain length;
- integrity-reference length;
- normalized evidence bytes;
- deterministic processing work units.

Resource-limit violations must fail closed.

Truncation, sampling, omission, best-effort continuation, and silent repair
must be prohibited.

A wall-clock timeout may stop external processing, but elapsed time must not
select or change a canonical result.

## 15. Adapter-Neutrality Acceptance

Eligibility semantics must remain independent of cloud providers, Kubernetes,
CI/CD products, model gateways, MCP systems, observability vendors, security
products, SDKs, and APIs.

A future adapter may translate a provider observation into a governed
envelope. It must not:

- determine eligibility;
- create canonical semantics;
- expand its authority;
- bypass required bindings;
- invoke the deterministic kernel;
- weaken failure or resource behavior.

No adapter implementation or live collection is authorized.

## 16. Kernel-Handoff Acceptance

The planning package must preserve this conceptual sequence:

```text
SUPPLIED_OPERATIONAL_OBSERVATION
    -> VALIDATED_OBSERVATION_ENVELOPE
    -> DETERMINISTIC_ELIGIBILITY_DECISION
    -> IMMUTABLE_ELIGIBLE_EVIDENCE
    -> FUTURE_SEPARATELY_AUTHORIZED_KERNEL_INVOCATION
```

Phase 4 planning must not invoke the kernel.

Any planned handoff must preserve accepted Phase 3 canonicalization,

fingerprint, failure, resource, tenant, subject, time, provenance, and version

semantics without amendment.

## 17. Security and Privacy Acceptance

The planning package must address:

-  untrusted input by default;
-  strict type and version validation;
-  tenant and subject isolation;
-  replay and substitution resistance;
-  provenance completeness;
-  integrity-verification inputs;
-  freshness and trusted-time inputs;
-  resource-exhaustion controls;
-  sensitive-data minimization;
-  audit-safe structured failures;
-  fail-closed unsupported-version behavior;
-  supply-chain independence.

Planning must require no filesystem, network, secret, credential, production

configuration, database, queue, cache, subprocess, plugin, or remote-code

access.

## 18. Canonical-Evidence Acceptance

Any semantic classified as `EXISTING_CANONICAL` must cite exact canonical

Phase 0 through Phase 3 evidence.

The following invariant is mandatory:

`ANY AFR SEMANTIC NOT PROVEN FROM CANONICAL PHASE 0-3 EVIDENCE MUST NOT BE CLASSIFIED AS EXISTING_CANONICAL.`

Absent, ambiguous, incomplete, or insufficient evidence requires

`RESERVED_FUTURE` or `NOT_ESTABLISHED`, as applicable.

Custodian directives and addenda are non-canonical inputs and cannot establish

canonical semantics or authority.

## 19. Cross-Program Non-Drift Acceptance

The planning package must preserve:

`ARCP_WORKING_LABEL = ARCP`

`ARCP_CANONICAL_NAME = UNRESOLVED_PENDING_NEXUS_PHASE_19_GOVERNANCE`

`ARCP_CANONICAL_SEMANTICS = UNRESOLVED_PENDING_NEXUS_PHASE_19_GOVERNANCE`

`NEXUS_PHASE_19_DIRECTION = RESERVED_UPSTREAM_ARCHITECTURE_DIRECTION`

`NEXUS_PHASE_19_CANONICAL_CAPABILITY_NAME = MUST_BE_VERIFIED_FROM_CANONICAL_NEXUS_STATE`

AFR must not independently name, define, expand, or canonicalize ARCP or

NEXUS Phase 19 semantics.

## 20. Dependency and Authority Separation Acceptance

The package must preserve:

`DEPENDENCY_RECOGNITION != INTEGRATION_PLANNING_AUTHORITY`

`INTEGRATION_PLANNING_AUTHORITY != INTEGRATION_IMPLEMENTATION_AUTHORITY`

`INTEGRATION_IMPLEMENTATION_AUTHORITY != RUNTIME_AUTHORITY`

`FUTURE_NEXUS_TO_AFR_ARCHITECTURE_TRUTH_CONSUMER_CONTRACT` must remain a

non-canonical placeholder—not a canonical name, schema, API, adapter,

implementation, active contract, or integration authority.

## 21. Prohibited-Scope Acceptance

Acceptance fails if the planning package creates authority for:

-  source code;
-  tests, vectors, fixtures, or executable schemas;
-  dependency, build-system, or configuration changes;
-  collectors or provider adapters;
-  live evidence collection;
-  filesystem or network behavior;
-  runtime conformance evaluation;
-  kernel invocation;
-  NEXUS, ARCP, or ATA integration;
-  model calls or model-based repair;
-  persistence, databases, queues, caches, or streams;
-  certificate work;
-  deployment or production access;
-  enforcement;
-  remediation;
-  another Phase 3 implementation slice;
-  Phase 4 implementation.

## 22. Stop-Condition Acceptance

Planning must stop and require separate authority if:

-  Disposition A becomes invalid;
-  architecture-truth contract work becomes necessary;
-  NEXUS or ARCP semantics must be defined;
-  a seventh document becomes necessary;
-  an executable schema becomes necessary;
-  source or test materialization becomes necessary;
-  provider-specific behavior becomes normative;
-  live collection becomes necessary;
-  persistence becomes necessary;
-  runtime kernel invocation becomes necessary;
-  accepted Phase 0 through Phase 3 semantics require amendment.

A stop condition must fail closed and cannot be waived by implementation

convenience.

## 23. Review and Evidence Acceptance

The exact six-document package must pass:

-  exact path-boundary verification;
-  frozen content-hash verification;
-  architecture review;
-  contract and semantic review;
-  deterministic and resource review;
-  security and privacy review;
-  NEXUS, ARCP, and ATA non-drift review;
-  authority-leakage review;
-  independent whole-package re-review;
-  staged-object verification;
-  commit and tree verification;
-  remote branch and pull-request verification;
-  explicit readiness transition;
-  explicit merge authorization;
-  post-merge canonical verification;
-  separately governed closure reconciliation.

No review gate implies or authorizes a later gate.

## 24. Completion and Authority Acceptance

Phase 4 planning is complete only after the exact reviewed package is merged

to canonical `main`, verified locally and remotely, and reconciled through a

separately governed post-merge closure.

Planning completion does not create implementation authority.

The authority state remains:

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
