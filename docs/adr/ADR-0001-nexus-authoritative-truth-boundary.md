# ADR-0001: NEXUS Authoritative Truth Boundary

## Status

Accepted architecture direction, effective only upon canonical merge.

Before canonical merge, this ADR remains proposed and creates no authority.

Implementation deferred.

## Context

NEXUS is a reusable AI Platform Architecture Agent that transforms ambiguous
requests into governed, evidence-backed, production-ready architecture through
a phase-gated lifecycle.

NEXUS already owns authoritative architecture concepts including:

- engagement state;
- discovery and problem framing;
- architecture requirements;
- architecture decisions;
- control profiles;
- semantic-action architecture;
- delegation, authority, and intent architecture;
- transaction and state invariants;
- evaluation and rollout conditions;
- architecture evidence and provenance.

Architecture Flight Recorder exists to determine whether deployed operational
reality continues to support approved architecture truth.

Without an explicit boundary, AFR could duplicate or undermine NEXUS by:

- creating its own architecture claims;
- maintaining a competing mutable architecture store;
- inferring approval from incomplete NEXUS objects;
- rewriting missing semantics;
- superseding architecture decisions;
- modifying engagement or lifecycle state;
- treating provider observations as architecture truth.

A stable authority boundary is therefore required before any integration is
designed or implemented.

## Decision

NEXUS remains authoritative for approved architecture truth in NEXUS-governed
systems.

AFR is a downstream, read-only conformance consumer of a future approved NEXUS
architecture-truth export.

The future direction of authoritative information is:

1. NEXUS approves architecture truth.
2. NEXUS exports an immutable, versioned, attributable snapshot.
3. AFR validates the export's authority, scope, version, and integrity.
4. AFR preserves the received snapshot without semantic mutation.
5. AFR compares eligible operational evidence with the approved truth.
6. AFR produces bounded conformance findings referencing stable NEXUS objects.
7. Any proposed architecture change returns through governed intake, review,
   and approval rather than direct AFR mutation.

AFR does not become authoritative for:

- NEXUS engagement state;
- architecture requirements;
- architecture decisions;
- architecture approval;
- NEXUS lifecycle transitions;
- architectural supersession;
- runtime commit authority;
- provider mutation.

## Required Future Export Properties

A future NEXUS architecture-truth export must be governed separately.

At minimum, its contract must eventually address:

- tenant identity;
- engagement identity;
- subject and system scope;
- lifecycle and approval state;
- snapshot identity;
- snapshot version;
- source commit or authoritative version identity where applicable;
- included architecture-object identities;
- object approval state;
- immutable object content or canonical references;
- relationships and traceability;
- applicable control and evaluation references;
- creation and approval identity;
- creation and approval time;
- supersession state;
- integrity fingerprint;
- compatibility version;
- explicit limitations and omitted semantics.

This ADR does not define that export schema.

## Validation Rules

AFR must not accept a NEXUS truth snapshot as authoritative solely because it
is syntactically valid.

Future validation must fail closed when:

- source identity is unresolved;
- tenant or engagement scope is unresolved;
- approval state is absent or ambiguous;
- the snapshot is mutable;
- version identity is missing;
- integrity cannot be established;
- required semantics are omitted;
- referenced objects cannot be resolved;
- supersession state is ambiguous;
- the export contract version is unsupported.

A failed truth validation cannot produce `CONFORMANT`.

## Mutation Boundary

AFR must never use the integration to:

- create or edit NEXUS objects;
- attach evidence to NEXUS state directly;
- approve or reject NEXUS decisions;
- change lifecycle stages;
- compile architecture requirements;
- resolve architecture risk;
- activate ATA applicability;
- grant ATA runtime authority;
- close NEXUS gaps or findings;
- execute remediation.

Future feedback from AFR must be treated as a non-authoritative request or
finding that re-enters the appropriate governed workflow.

## Evidence Boundary

NEXUS architecture evidence and AFR operational evidence remain distinct.

NEXUS evidence may support the approval and provenance of architecture truth.

AFR evidence supports a bounded determination about deployed operational
conformance.

AFR must not silently reinterpret NEXUS approval evidence as current
operational evidence.

Provider observations must not replace NEXUS architecture truth.

## Rationale

This decision:

- preserves one architecture source of truth;
- prevents competing decision systems;
- protects NEXUS lifecycle authority;
- allows AFR to specialize in continuous conformance;
- supports deterministic provenance;
- keeps provider observations separate from architecture intent;
- permits future reuse with other approved architecture authorities;
- prevents remediation from bypassing governed review;
- preserves ATA's separate runtime authority.

## Consequences

### Positive

- NEXUS and AFR have non-overlapping authoritative responsibilities.
- AFR can evolve independently without duplicating NEXUS.
- Findings can retain stable traceability to approved architecture.
- Architecture changes remain governed.
- Conformance can be reproduced against immutable truth versions.
- AFR can remain provider-neutral.

### Constraints

- AFR cannot operate authoritatively without an approved truth source.
- NEXUS requires a separately governed export contract before integration.
- Missing export semantics must produce an inconclusive or blocked condition.
- AFR must preserve multiple truth versions for historical reproducibility.
- Remediation requires coordination with external governed systems.

### Risks

- An export that is too broad could expose unnecessary engagement data.
- An export that is too narrow could make conformance inconclusive.
- Version or supersession ambiguity could cause evaluation against stale truth.
- Consumers could incorrectly treat AFR findings as architecture decisions.
- Tight implementation coupling could undermine bounded-context independence.

These risks must be addressed by later contract, security, and implementation
phases.

## Alternatives Considered

### AFR Maintains Independent Architecture Truth

Rejected because it would create a competing source of truth and duplicate
NEXUS architecture responsibilities.

### AFR Reads Mutable NEXUS Persistence Directly

Rejected because it would couple AFR to internal storage, bypass an explicit
export contract, and risk consuming draft or transitional state.

### AFR Writes Findings Directly into NEXUS State

Rejected for the initial boundary because it would grant mutation authority and
could bypass NEXUS intake, review, evidence, and lifecycle controls.

### Provider State Defines Expected Architecture

Rejected because deployed state describes what exists, not what was approved.

### Model Inference Reconstructs Missing Architecture Claims

Rejected because non-deterministic inference cannot create authoritative
architecture truth.

## Phase 0 Authority

This ADR accepts the architecture direction only.

It does not authorize:

- modification of the NEXUS repository;
- creation of a NEXUS export;
- AFR integration code;
- API or event contracts;
- schemas;
- credentials;
- persistence;
- provider collection;
- evaluation execution;
- certificate generation;
- deployment;
- production access.

Any implementation requires separately reviewed and explicitly activated
authority.
