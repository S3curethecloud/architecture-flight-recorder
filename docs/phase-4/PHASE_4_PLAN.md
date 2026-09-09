# AFR Phase 4 Plan

## 1. Purpose

Phase 4 plans the bounded AFR capability:

`OPERATIONAL_EVIDENCE_INTAKE_AND_ELIGIBILITY_PLANNING`

The phase defines how externally supplied operational observations may become
eligible, immutable, attributable, tenant-bound evidence before a separately
authorized handoff to the deterministic AFR kernel.

This plan is documentation-only. It creates no implementation, collection,
integration, runtime, persistence, certificate, deployment, enforcement,
remediation, or production authority.

## 2. Canonical Baseline

Phase 4 begins from:

- canonical `main`:
  `25deed93df00d1db044a24164b9e46ca5a9e759d`;
- canonical tree:
  `19ce8d96fe36052ef072635393a170bdca2d7ce0`;
- Phase 3 status: `COMPLETE`;
- Phase 3 planning authority: `CONSUMED_CLOSED`;
- Phase 3 implementation authority: `CONSUMED_CLOSED`;
- Phase 4 planning authority:
  `BOUNDED_OPERATIONAL_EVIDENCE_INTAKE_AND_ELIGIBILITY_PLANNING_ONLY`.

Phase 3 contracts, canonicalization, fingerprints, tests, and deterministic
vectors remain immutable inputs. Phase 4 planning cannot reopen or amend them.

## 3. Mission and Position

The bounded mission is:

`DEFINE_BOUNDED_OBSERVATION_TO_ELIGIBLE_EVIDENCE_SEMANTICS`

The architectural position is:

`BETWEEN_EXTERNAL_OBSERVATIONS_AND_THE_DETERMINISTIC_KERNEL`

Phase 4 plans an adapter-neutral trust boundary. It does not implement an
ingress service, collector, provider adapter, message consumer, persistence
layer, or runtime kernel invocation.

## 4. Controlling Disposition

The controlling cross-program disposition is:

`DISPOSITION_A =
PHASE_4_DOES_NOT_REQUIRE_ARCHITECTURE_TRUTH_CONTRACT_WORK`

NEXUS Phase 19 and ARCP remain reserved upstream architecture directions.
AFR does not define their canonical names or semantics and creates no NEXUS,
ARCP, ATA, or other cross-program integration authority.

## 5. Exact Planning Package

Planning materialization is limited to:

1. `docs/SOT.md`
2. `docs/phase-4/PHASE_4_PLAN.md`
3. `docs/phase-4/PHASE_4_ACCEPTANCE_CRITERIA.md`
4. `docs/architecture/AFR_OPERATIONAL_EVIDENCE_INTAKE_ARCHITECTURE.md`
5. `docs/contracts/AFR_EVIDENCE_ELIGIBILITY_CONTRACT.md`
6. `docs/security/AFR_PHASE_4_EVIDENCE_TRUST_BOUNDARY.md`

No seventh file, executable schema, source file, test, vector, fixture,
dependency, configuration, migration, or build artifact is authorized.

## 6. Planning Outcomes

Phase 4 must produce coherent documentation for:

- observation ingress envelopes;
- observation and evidence identity;
- source identity and source classification;
- provenance and integrity inputs;
- trusted-time, freshness, and validity semantics;
- tenant, subject, environment, release, scope, and version bindings;
- deterministic evidence-eligibility decisions;
- structured processing failures;
- replay, duplication, substitution, conflict, and ordering behavior;
- partial-evidence behavior;
- deterministic resource limits;
- adapter-neutral handoff boundaries;
- security, privacy, auditability, and supply-chain constraints.

The documents must converge on one vocabulary, one lifecycle, one failure
taxonomy, and one authority boundary.

## 7. Canonical Semantic Foundation

Phase 4 relies on canonical Phase 0 through Phase 3 definitions for:

- operational-observation handling;
- evidence eligibility;
- provenance validation;
- integrity validation;
- freshness evaluation;
- deterministic evaluation definitions;
- deterministic rule resolution;
- claim-level conformance evaluation;
- aggregate conformance evaluation;
- conformance fingerprints;
- conformance findings.

Reliance on a canonical semantic does not imply that a Phase 4 implementation
or runtime capability exists.

Any semantic not proven from canonical Phase 0 through Phase 3 evidence must
be classified as `RESERVED_FUTURE` or `NOT_ESTABLISHED`, as applicable. It
must not be represented as `EXISTING_CANONICAL`.

## 8. Observation Envelope Planning

Planning must define the minimum immutable observation envelope, including:

- observation identifier;
- observation-envelope version;
- source identifier;
- source class;
- tenant identifier;
- subject identifier and subject type;
- environment identifier;
- scope identifier;
- release or deployment binding where applicable;
- observed time;
- received time;
- applicable time or validity interval;
- declared payload representation;
- declared input-byte measurement;
- integrity reference;
- provenance-chain reference;
- explicit optional-field presence;
- payload or content reference suitable for later canonical treatment.

No value may be inferred from ambient credentials, process state, filesystem
location, network endpoint, provider account, or deployment context.

## 9. Evidence Identity Planning

Planning must define how eligible evidence receives a stable identity bound to:

- observation identity;
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
be treated as a duplicate.

## 10. Eligibility Decision Model

Planning must distinguish:

- `ELIGIBLE`;
- `INELIGIBLE`;
- `QUARANTINED`;
- `UNSUPPORTED`;
- `PROCESSING_FAILURE`.

Eligibility is a pre-conformance decision. It determines whether an
observation may participate as evidence; it does not determine whether the
evidence supports or contradicts an architecture claim.

An eligibility decision must not emit `CONFORMANT`, `NON_CONFORMANT`,
`INCONCLUSIVE`, `STALE`, or any other conformance outcome.

Processing failures remain separate from eligibility classifications and
conformance outcomes.

## 11. Deterministic Decision Inputs

Eligibility may depend only on explicitly supplied and version-bound inputs,
including:

- envelope completeness;
- supported types and versions;
- tenant and subject binding;
- source-class policy;
- provenance completeness;
- integrity-verification inputs;
- timestamp validity and trusted-time inputs;
- freshness and validity windows;
- replay and substitution indicators;
- deterministic resource limits;
- eligibility-policy version.

Elapsed time, randomness, model output, network availability, ambient
configuration, or provider-specific behavior cannot select or modify a
canonical eligibility result.

## 12. Absence and Null Semantics

Planning must preserve the distinction between:

- an absent optional field;
- a present field with explicit null;
- a present field with an empty value;
- a missing required field;
- an unsupported value.

These states cannot be silently collapsed, defaulted, inferred, or repaired.

## 13. Replay, Duplication, and Substitution

Planning must distinguish:

- byte-identical replay;
- semantically equivalent duplication;
- identifier reuse with changed content;
- stale replay;
- cross-tenant replay;
- cross-subject substitution;
- cross-environment substitution;
- cross-scope substitution;
- reordered delivery;
- conflicting observations.

Deduplication must not erase provenance, freshness, ordering, or conflict
information.

The phase defines semantics only. It does not authorize a replay store,
database, queue, cache, stream, or distributed coordination mechanism.

## 14. Conflict and Partial Evidence

Planning must define deterministic behavior for:

- contradictory observations;
- incomplete envelopes;
- missing required bindings;
- unavailable integrity material;
- incomplete provenance;
- ambiguous timestamps;
- expired freshness windows;
- unknown source classes;
- unsupported representations or versions;
- partially eligible evidence sets.

Partial evidence cannot be promoted to complete evidence. Conflict cannot be
silently resolved through arrival order, model judgment, provider priority, or
operator convenience.

## 15. Deterministic Resource Limits

Planning must define explicitly versioned limits for:

- total ingress bytes;
- envelope field count;
- collection cardinality;
- nesting depth;
- provenance-chain length;
- integrity-reference length;
- normalized evidence bytes;
- deterministic processing work units.

Limits must be enforced conceptually before downstream kernel handoff.
Truncation, sampling, omission, best-effort continuation, and silent repair
are prohibited.

A wall-clock timeout may be an external safety stop, but elapsed time cannot
select, change, or legitimize a canonical result.

## 16. Adapter-Neutrality

The planned semantics must be independent of:

- AWS;
- Azure;
- Google Cloud;
- Kubernetes;
- CI/CD products;
- model gateways;
- MCP systems;
- observability vendors;
- security products;
- provider SDKs and APIs.

A future adapter may translate provider observations into a governed envelope.
It cannot determine eligibility, expand its own authority, or bypass the
adapter-neutral boundary.

No adapter implementation or live collection is authorized.

## 17. Kernel Handoff Boundary

The planned conceptual flow is:

```text
SUPPLIED_OPERATIONAL_OBSERVATION
    -> VALIDATED_OBSERVATION_ENVELOPE
    -> DETERMINISTIC_ELIGIBILITY_DECISION
    -> IMMUTABLE_ELIGIBLE_EVIDENCE
    -> FUTURE_SEPARATELY_AUTHORIZED_KERNEL_INVOCATION
```

Phase 4 planning does not invoke the deterministic kernel.

The handoff must preserve accepted Phase 3 canonicalization, fingerprint,
resource, failure, tenant, subject, time, provenance, and version semantics.

## 18. Security and Privacy Workstream

Planning must address:

untrusted input by default;
strict type and version validation;
tenant and subject isolation;
replay and substitution resistance;
provenance completeness;
integrity-verification inputs;
freshness and trusted-time inputs;
deterministic resource-exhaustion controls;
sensitive-data minimization;
audit-safe structured failures;
fail-closed unsupported-version behavior;
supply-chain independence.

Planning cannot access secrets, credentials, production configuration,
filesystems, networks, databases, queues, caches, subprocesses, plugins, or
remote code.

## 19. Cross-Program Non-Drift

The original custodian directive and bounded addendum remain non-canonical
custodian inputs. They constrain drift but do not establish authority.

The following remain controlling:

ARCP_WORKING_LABEL = ARCP

ARCP_CANONICAL_NAME = UNRESOLVED_PENDING_NEXUS_PHASE_19_GOVERNANCE

ARCP_CANONICAL_SEMANTICS = UNRESOLVED_PENDING_NEXUS_PHASE_19_GOVERNANCE

NEXUS_PHASE_19_DIRECTION = RESERVED_UPSTREAM_ARCHITECTURE_DIRECTION

NEXUS_PHASE_19_CANONICAL_CAPABILITY_NAME = MUST_BE_VERIFIED_FROM_CANONICAL_NEXUS_STATE

DEPENDENCY_RECOGNITION != INTEGRATION_PLANNING_AUTHORITY

INTEGRATION_PLANNING_AUTHORITY != INTEGRATION_IMPLEMENTATION_AUTHORITY

INTEGRATION_IMPLEMENTATION_AUTHORITY != RUNTIME_AUTHORITY

FUTURE_NEXUS_TO_AFR_ARCHITECTURE_TRUTH_CONSUMER_CONTRACT remains a
non-canonical placeholder, not a schema, API, adapter, implementation, or
active contract.

## 20. Explicitly Prohibited Work

Phase 4 planning creates no authority for:

source code;
tests, vectors, fixtures, or executable schemas;
dependency or configuration changes;
collectors or provider adapters;
live evidence collection;
network or filesystem behavior;
runtime conformance evaluation;
kernel invocation;
NEXUS, ARCP, or ATA integration;
model calls or model-based repair;
persistence, databases, queues, caches, or streams;
certificates;
deployment or production access;
enforcement;
remediation;
another Phase 3 implementation slice;
Phase 4 implementation.
## 21. Stop Conditions

Planning must stop and require new authority if:

Disposition A becomes invalid;
architecture-truth contract work becomes necessary;
NEXUS or ARCP semantics must be defined;
a seventh document becomes necessary;
an executable schema becomes necessary;
source or test materialization becomes necessary;
provider-specific behavior becomes normative;
live collection becomes necessary;
persistence becomes necessary;
runtime kernel invocation becomes necessary;
accepted Phase 0 through Phase 3 semantics require amendment.
## 22. Review Sequence

The planning package must pass:

exact six-document boundary verification;
frozen hash verification;
architecture review;
contract and semantic review;
deterministic-resource review;
security and privacy review;
NEXUS, ARCP, and ATA non-drift review;
authority-leakage review;
independent whole-package re-review;
staged-object verification;
exact commit and tree verification;
remote branch and pull-request verification;
explicit readiness and merge authorization;
post-merge canonical verification;
separately governed post-merge closure.

No earlier gate implies a later gate.

## 23. Completion Condition

Phase 4 planning is complete only after the exact planning package is
independently accepted, merged to canonical main, verified locally and
remotely, and reconciled through its separately governed closure.

Planning completion does not create implementation authority.

## 24. Authority State
AFR_PHASE_4_PLANNING_AUTHORITY =
BOUNDED_OPERATIONAL_EVIDENCE_INTAKE_AND_ELIGIBILITY_PLANNING_ONLY

AFR_PHASE_4_IMPLEMENTATION_AUTHORITY = NONE
AFR_PHASE_4_LIVE_EVIDENCE_COLLECTION_AUTHORITY = NONE
AFR_PHASE_4_PROVIDER_INTEGRATION_AUTHORITY = NONE
AFR_PHASE_4_NEXUS_INTEGRATION_AUTHORITY = NONE
AFR_PHASE_4_ARCP_AUTHORITY = NONE
AFR_PHASE_4_RUNTIME_EVALUATION_AUTHORITY = NONE
AFR_PHASE_4_PERSISTENCE_AUTHORITY = NONE
AFR_PHASE_4_CERTIFICATE_AUTHORITY = NONE
AFR_PHASE_4_DEPLOYMENT_AUTHORITY = NONE
AFR_PHASE_4_ENFORCEMENT_AUTHORITY = NONE
AFR_PHASE_4_REMEDIATION_AUTHORITY = NONE
AFR_PHASE_4_AUTHORITY = BOUNDED_PLANNING_ONLY
