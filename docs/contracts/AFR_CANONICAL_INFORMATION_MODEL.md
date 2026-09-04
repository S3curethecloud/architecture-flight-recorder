# AFR Canonical Information Model

## 1. Purpose

This document defines the normative conceptual information model for
Architecture Flight Recorder.

It defines semantic records, identities, relationships, invariants, and
authority boundaries. It is not an executable schema, API contract,
serialization format, database model, or implementation authorization.

## 2. Modeling Principles

Every authoritative AFR record must be:

- attributable;
- tenant-bound;
- subject-bound where applicable;
- versioned;
- scope-bounded;
- time-bounded;
- integrity-verifiable;
- traceable to its material inputs;
- immutable after authoritative creation;
- explicit about limitations and unresolved conditions.

Syntactic validity alone never establishes authority or evidence eligibility.

## 3. Common Record Semantics

Every authoritative record conceptually carries:

- stable record identity;
- record type;
- contract version;
- tenant identity;
- issuing or creating identity;
- creation time;
- applicable subject and scope;
- semantic version or immutable revision;
- integrity fingerprint;
- provenance references;
- supersession state;
- explicit limitations.

Optional fields cannot silently replace missing mandatory semantics.

## 4. Tenant Context

A Tenant Context identifies the single tenant authority domain within which an
AFR record is valid.

It conceptually includes:

- tenant identity;
- tenant namespace;
- applicable organization or account scope;
- resolved authority domain;
- isolation-policy reference.

A record without resolved tenant context is ineligible for authoritative
evaluation.

Cross-tenant joining, substitution, reuse, or certificate application is
prohibited unless a separately governed aggregate capability is authorized.

## 5. Subject Reference

A Subject Reference identifies the system, service, agent, workload, release,
resource, or bounded architecture subject being evaluated.

It conceptually includes:

- stable subject identity;
- subject type;
- tenant identity;
- environment;
- release identity when applicable;
- deployment identity when applicable;
- parent-system identity;
- explicit evaluation scope.

Subject identity cannot be inferred solely from a display name or provider
resource label.

## 6. Architecture-Truth Snapshot Reference

An Architecture-Truth Snapshot Reference identifies an immutable approved
snapshot owned by an external architecture authority.

It conceptually includes:

- architecture-authority identity;
- tenant and engagement identity;
- snapshot identity;
- snapshot version;
- approval state;
- approval identity and time;
- included-object references;
- subject and scope binding;
- supersession state;
- compatibility version;
- integrity fingerprint;
- explicit omissions and limitations.

For NEXUS-governed systems, NEXUS remains authoritative for the snapshot.

AFR preserves and references the received truth. It cannot author, approve,
modify, supersede, enrich, or infer missing authoritative meaning.

This document does not define or authorize a NEXUS export contract.

## 7. Architecture Claim

An Architecture Claim is an approved, evaluable assertion referenced from an
authoritative truth snapshot.

It conceptually includes:

- stable claim identity;
- truth-snapshot reference;
- authoritative source-object reference;
- claim type;
- normative assertion;
- tenant and subject binding;
- environment and release scope;
- applicability conditions;
- criticality;
- required evidence classes;
- freshness requirements;
- evaluation-definition reference;
- supersession state;
- explicit limitations.

An AFR record may reference a claim but cannot create its architecture
authority.

A claim must not be reconstructed through model inference when authoritative
semantics are missing.

## 8. Evidence Observation

An Evidence Observation is an attributable report of bounded operational state
from a provider or enterprise source.

It conceptually includes:

- observation identity;
- tenant and subject binding;
- source-system identity;
- collector identity;
- collection method;
- requested scope;
- returned scope;
- observation time when available;
- collection time;
- ingestion time;
- raw-content integrity fingerprint;
- source version or revision;
- collection completeness;
- source-reported limitations;
- collection failure details.

An observation is not automatically eligible evidence.

A provider observation describes bounded operational state; it does not define
approved architecture intent.

## 9. Evidence Eligibility Decision

An Evidence Eligibility Decision determines whether an observation may
participate in a specific evaluation context.

It conceptually includes:

- decision identity;
- observation reference;
- evaluation-context reference;
- tenant-match result;
- subject-match result;
- source-identity result;
- collector-identity result;
- provenance result;
- integrity result;
- scope result;
- freshness result;
- compatibility result;
- normalization-lineage result;
- contradiction indicators;
- eligibility outcome;
- rejection reasons;
- policy and evaluator versions;
- decision fingerprint.

Eligibility outcomes must distinguish at least:

- `ELIGIBLE`;
- `INELIGIBLE`;
- `PARTIAL`;
- `UNVERIFIABLE`;
- `STALE`.

Normalization or aggregation cannot elevate an observation’s authority.

## 10. Canonical Evidence Record

A Canonical Evidence Record is a normalized representation of an observation
that preserves the original observation and complete transformation lineage.

It conceptually includes:

- canonical evidence identity;
- source-observation reference;
- normalization-definition version;
- normalized content;
- tenant and subject binding;
- evidence class;
- observed and collected times;
- freshness deadline;
- provenance chain;
- integrity fingerprints;
- eligibility-decision references;
- known limitations.

Canonicalization does not prove correctness, completeness, or eligibility.

## 11. Evaluation Definition

An Evaluation Definition is an approved, immutable semantic definition for
evaluating identified claim types.

It conceptually includes:

- definition identity and version;
- applicable claim types;
- required and optional evidence classes;
- claim-to-evidence matching rules;
- tenant, subject, environment, and release constraints;
- support semantics;
- contradiction semantics;
- completeness requirements;
- freshness requirements;
- outcome rules;
- aggregate constraints;
- policy compatibility;
- evaluator compatibility;
- integrity fingerprint;
- approval and supersession state.

An evaluation definition cannot create or modify architecture truth.

## 12. Evaluation Context

An Evaluation Context fixes the complete boundary of one evaluation.

It conceptually includes:

- evaluation identity;
- tenant identity;
- subject identity;
- environment;
- release and deployment identity when applicable;
- truth-snapshot reference;
- evaluated claim references;
- evaluation-definition reference;
- policy version;
- evaluator version;
- evaluation time;
- eligible evidence-set reference;
- requested scope;
- explicit exclusions and limitations.

An unresolved context prevents an authoritative positive result.

## 13. Evidence Set

An Evidence Set is the immutable collection of eligible evidence references
considered by one evaluation.

It conceptually includes:

- evidence-set identity;
- evaluation-context reference;
- ordered evidence references;
- eligibility-decision references;
- evidence gaps;
- contradiction references;
- completeness result;
- set fingerprint.

Evidence added after evaluation requires a new evidence set and a new
evaluation. It cannot silently alter an existing result.

## 14. Evidence Gap

An Evidence Gap records a required evidence dependency that is missing,
partial, unverifiable, incompatible, or stale.

It conceptually includes:

- gap identity;
- affected claim;
- required evidence class;
- gap category;
- cause;
- materiality;
- discovery time;
- applicable limitation;
- resolution state.

Absence of evidence is not proof of either conformance or non-conformance.

## 15. Contradiction

A Contradiction records eligible evidence that conflicts with:

- an approved claim;
- other eligible evidence;
- declared scope;
- identity or tenant binding;
- expected release or deployment state.

It conceptually includes:

- contradiction identity;
- affected claim;
- conflicting evidence references;
- contradiction category;
- materiality;
- unresolved status;
- effect on outcome.

A material unresolved contradiction cannot be suppressed or converted into
`CONFORMANT`.

## 16. Claim-Level Result

A Claim-Level Result is AFR’s authoritative bounded outcome for one evaluated
claim.

It conceptually includes:

- result identity;
- evaluation-context reference;
- claim reference;
- evidence-set reference;
- evaluation-definition version;
- policy and evaluator versions;
- outcome;
- deterministic rationale;
- supporting evidence references;
- contradicting evidence references;
- evidence gaps;
- limitations;
- evaluation time;
- validity deadline;
- result fingerprint;
- supersession state.

Canonical outcomes are:

- `CONFORMANT`;
- `NON_CONFORMANT`;
- `INCONCLUSIVE`;
- `STALE`.

## 17. Aggregate Result

An Aggregate Result summarizes an explicitly identified set of claim-level
results without concealing weaker material outcomes.

It conceptually includes:

- aggregate-result identity;
- evaluation-context reference;
- included claim-result references;
- aggregation-policy version;
- critical-claim coverage;
- completeness state;
- unresolved gaps and contradictions;
- aggregate outcome;
- limitations;
- aggregate fingerprint.

A majority of conformant claims cannot override a material
`NON_CONFORMANT`, `INCONCLUSIVE`, or `STALE` result contrary to the approved
aggregation policy.

## 18. Drift Finding

A Drift Finding identifies a material mismatch between eligible operational
evidence and approved architecture truth.

It conceptually includes:

- finding identity;
- claim-level result reference;
- authoritative claim reference;
- contradicting evidence references;
- affected tenant and subject;
- materiality;
- discovery and validity times;
- deterministic explanation;
- limitations;
- status and supersession references.

A finding is not an architecture decision, remediation authorization, or
runtime permission.

## 19. Evaluation Fingerprint

An Evaluation Fingerprint integrity-binds every material deterministic input,
including:

- truth-snapshot identity and fingerprint;
- evaluated claim identities;
- evidence-set fingerprint;
- evaluation-definition identity and version;
- policy version;
- evaluator version;
- evaluation context;
- trusted evaluation time semantics;
- applicable normalization versions.

Changing any material input requires a distinct fingerprint and evaluation.

This document does not select a hashing algorithm or canonical serialization.

## 20. Provenance Event

A Provenance Event records an attributable lifecycle action involving an AFR
record.

Conceptual event classes include:

- received;
- validated;
- rejected;
- normalized;
- evaluated;
- issued;
- accessed;
- expired;
- superseded;
- revoked in a future authorized phase.

A provenance event cannot retroactively change an immutable record.

## 21. Relationship Invariants

The canonical relationships are:

1. A truth snapshot contains or references approved claims.
2. A claim belongs to one authoritative truth snapshot version.
3. An observation comes from one attributable source and collector context.
4. An eligibility decision evaluates one observation in one evaluation context.
5. An evidence set contains only explicitly referenced eligible evidence.
6. A claim-level result evaluates one claim using one immutable evidence set.
7. An aggregate result references identified claim-level results.
8. A drift finding references an authoritative claim and its bounded result.
9. Every result is reproducible from fingerprint-bound inputs.
10. Every authoritative record belongs to exactly one resolved tenant context.

## 22. Invalid-State Doctrine

The following states are invalid for an authoritative positive result:

- missing tenant or subject identity;
- unresolved truth authority;
- absent approval state;
- mutable or unverifiable truth;
- unknown claim scope;
- evidence without attributable provenance;
- integrity failure;
- stale required evidence;
- unresolved material contradiction;
- missing required evidence;
- unsupported contract, policy, or evaluator version;
- cross-tenant evidence;
- model-selected authoritative outcome.

Invalid states must remain explicit and cannot be repaired through inference.

## 23. Deferred Decisions

Phase 1 does not decide:

- programming language;
- executable type system;
- schema language;
- serialization format;
- database;
- API or event protocol;
- hashing or signing algorithm;
- provider adapter;
- NEXUS export implementation;
- evaluator implementation;
- certificate implementation;
- deployment topology.

These require separately activated authority.

## 24. Phase 1 Constraint

This information model is normative planning documentation only.

It creates no authority for executable schemas, code, tests, persistence,
integration, collection, evaluation execution, certificate issuance,
deployment, production access, or Phase 2.
