# Architecture Flight Recorder Reference Architecture

## 1. Purpose

This document defines the provider-neutral conceptual architecture for
Architecture Flight Recorder.

It identifies the architectural planes, responsibilities, information flow,
control points, and fail-closed behavior required by the product doctrine.

It does not select technologies, define implementation schemas, or authorize
runtime construction.

## 2. Architectural Objective

AFR must transform two independently authoritative inputs:

1. approved architecture truth;
2. attributable observations of deployed reality;

into a deterministic, reproducible, time-bound conformance result.

The architecture must preserve the separation between truth, observation,
evidence eligibility, evaluation, enforcement, and presentation.

## 3. Architectural Planes

### Architecture-Truth Intake Plane

The Architecture-Truth Intake Plane receives immutable, versioned snapshots
from an approved architecture authority.

Its conceptual responsibilities are:

- authenticate the source;
- validate tenant and engagement scope;
- validate approval status;
- validate version and integrity;
- preserve authoritative object references;
- reject drafts or ambiguous authority;
- store the received snapshot immutably;
- prevent AFR from rewriting authoritative truth.

For NEXUS, the export contract remains future work and is not authorized by
Phase 0.

### Evidence Acquisition Plane

The Evidence Acquisition Plane obtains bounded read-only observations from
approved provider and enterprise sources.

Its conceptual responsibilities are:

- use least-privilege read-only identities;
- identify the collector and source;
- bind observations to tenant and subject;
- capture collection and observation time;
- preserve raw source responses where permitted;
- report partial collection and source failure explicitly;
- avoid provider mutation or automated remediation.

No evidence collectors are authorized during Phase 0.

### Evidence Trust Plane

The Evidence Trust Plane determines whether an observation is eligible to
participate in evaluation.

Its conceptual responsibilities are:

- verify source and collector identity;
- verify tenant and subject scope;
- validate provenance and integrity;
- validate freshness;
- detect replay or substitution;
- preserve normalization lineage;
- identify contradictions;
- distinguish unavailable evidence from negative evidence;
- reject evidence that cannot satisfy required trust conditions.

Normalization cannot increase the authority of an observation.

### Conformance Definition Plane

The Conformance Definition Plane preserves versioned evaluation definitions.

A definition conceptually identifies:

- applicable architecture claims;
- required and optional evidence;
- claim-to-evidence relationships;
- support and contradiction semantics;
- scope conditions;
- freshness requirements;
- completeness rules;
- outcome rules;
- policy and evaluator compatibility.

An evaluation definition cannot create architecture truth.

### Deterministic Evaluation Plane

The Deterministic Evaluation Plane compares eligible evidence with approved
architecture truth.

Its conceptual responsibilities are:

- resolve the exact evaluation context;
- validate input compatibility;
- calculate claim-level outcomes;
- preserve evidence gaps and contradictions;
- apply fail-closed outcome rules;
- generate deterministic fingerprints;
- preserve the complete decision trace;
- prevent model inference from selecting authoritative outcomes.

The minimum canonical outcomes are:

- `CONFORMANT`;
- `NON_CONFORMANT`;
- `INCONCLUSIVE`;
- `STALE`.

### Findings and Certificate Plane

The Findings and Certificate Plane preserves bounded evaluation results.

Its conceptual responsibilities are:

- create immutable conformance findings;
- record evidence gaps and limitations;
- associate drift with authoritative claim references;
- preserve evaluation identity and timing;
- prepare integrity-bound certificate representations;
- support expiry, supersession, and future revocation;
- prevent a certificate from being interpreted as execution authority.

Certificate issuance and signing are not authorized during Phase 0.

### Delivery and Integration Plane

The Delivery and Integration Plane exposes approved findings to authorized
consumers.

Potential future consumers include:

- PAA for explanation and remediation coordination;
- Humanize for presentation;
- CI/CD or release governance for bounded release decisions;
- ATA as one bounded policy input;
- audit and assurance consumers.

Downstream consumers cannot change the authoritative AFR result.

### Governance and Control Plane

The Governance and Control Plane applies cross-cutting controls to every plane.

Its conceptual responsibilities include:

- tenant isolation;
- workload and human identity;
- authorization;
- policy versioning;
- key and certificate governance;
- audit logging;
- provenance;
- retention;
- privacy and data minimization;
- evaluator release governance;
- connector approval;
- time and freshness policy;
- incident response;
- operational observability.

## 4. Conceptual Components

### Truth Snapshot Receiver

Receives an immutable architecture-truth snapshot through an approved
read-only contract.

### Truth Authority Validator

Validates source authority, approval state, version, scope, and integrity.

### Evidence Collector

Obtains a bounded observation using a least-privilege read-only identity.

### Evidence Trust Gateway

Validates whether an observation is eligible evidence.

### Evidence Normalizer

Produces a canonical representation while preserving the original observation
and complete transformation lineage.

### Evidence Repository

Preserves raw observations, canonical evidence, provenance, integrity,
freshness, and tenant binding.

### Evaluation Definition Registry

Preserves approved, immutable evaluation definitions and version relationships.

### Conformance Evaluator

Produces deterministic claim-level and aggregate outcomes from eligible inputs.

### Finding Repository

Preserves immutable outcomes, gaps, contradictions, limitations, and
fingerprints.

### Certificate Preparation Service

Builds a bounded certificate representation from a completed evaluation.

It does not grant authority and is not authorized for implementation in
Phase 0.

### Audit and Provenance Ledger

Preserves attributable records of ingestion, validation, evaluation, delivery,
expiry, supersession, and future revocation events.

### Consumer Gateway

Provides tenant-aware, authorized, read-only access to approved outputs.

## 5. Canonical Information Flow

The conceptual information flow is:

1. NEXUS or another approved authority approves architecture truth.
2. The authority exports an immutable versioned snapshot.
3. AFR validates the snapshot's authority, scope, version, and integrity.
4. Approved collectors obtain bounded read-only provider observations.
5. AFR validates observation identity, provenance, integrity, and freshness.
6. Eligible observations become evidence without gaining additional authority.
7. AFR resolves an approved evaluation definition and policy version.
8. The deterministic evaluator compares claims with eligible evidence.
9. AFR produces claim-level outcomes, gaps, contradictions, and limitations.
10. AFR derives a bounded aggregate result without hiding weaker outcomes.
11. AFR preserves the complete evaluation trace and fingerprint.
12. AFR may prepare a time-bound certificate representation.
13. Authorized consumers receive read-only findings.
14. Any remediation or architecture-change proposal returns through governed
    human, PAA, NEXUS, and enterprise-system processes.
15. AFR evaluates new evidence rather than mutating the environment itself.

## 6. Aggregate Result Doctrine

An aggregate result must never conceal a material weaker claim-level result.

A future aggregation policy must explicitly define:

- critical claims;
- required claim coverage;
- treatment of `NON_CONFORMANT`;
- treatment of `INCONCLUSIVE`;
- treatment of `STALE`;
- unresolved contradictions;
- evidence completeness;
- certificate eligibility.

No simple majority or model-generated summary may convert weaker material
outcomes into aggregate `CONFORMANT`.

## 7. Identity Architecture

Every interaction must resolve an attributable identity.

Conceptual identity classes include:

- architecture authority;
- truth exporter;
- evidence collector;
- provider source;
- evaluator workload;
- policy approver;
- certificate issuer;
- human reviewer;
- downstream consumer.

Identity must be bound to tenant, role, scope, and action.

A workload cannot expand its own authorization or impersonate another
authority domain.

## 8. Data Architecture

Conceptual data classes include:

- architecture-truth snapshot;
- architecture claim reference;
- raw evidence observation;
- canonical evidence record;
- evidence eligibility result;
- evaluation definition;
- evaluation request;
- claim-level result;
- aggregate result;
- evidence gap;
- drift finding;
- certificate representation;
- provenance event.

These are conceptual classes only. Phase 0 does not authorize schemas or
persistence models.

## 9. Integrity Architecture

Integrity protection must conceptually cover:

- received truth snapshots;
- raw observations;
- normalized evidence;
- evaluation definitions;
- policy versions;
- evaluator versions;
- conformance findings;
- certificate representations;
- audit and provenance events.

Integrity mechanisms must bind material inputs to evaluation outputs so that
substitution or later mutation is detectable.

## 10. Time Architecture

AFR results depend on trusted time semantics.

The future architecture must distinguish:

- source observation time;
- collection time;
- ingestion time;
- evaluation time;
- evidence freshness deadline;
- result validity deadline;
- certificate expiry;
- supersession time;
- future revocation time.

A newer timestamp alone cannot prove that evidence reflects a newer state.

## 11. Failure Architecture

AFR must expose failures rather than convert them into positive evidence.

Conceptual failure classes include:

- truth-authority failure;
- truth-integrity failure;
- collector identity failure;
- provider access failure;
- partial collection;
- evidence-integrity failure;
- stale evidence;
- contradictory evidence;
- tenant mismatch;
- subject mismatch;
- missing evaluation definition;
- evaluator-version mismatch;
- policy-version mismatch;
- certificate preparation failure;
- downstream delivery failure.

Failures affecting required inputs prevent `CONFORMANT`.

## 12. Deployment Independence

The reference architecture is provider-neutral and deployment-neutral.

Phase 0 does not select:

- a cloud provider;
- a runtime platform;
- a programming language;
- a database;
- a queue or event bus;
- a policy engine;
- a signing service;
- an observability platform;
- an API protocol;
- a deployment topology.

Those decisions require later phase authority and evidence.

## 13. Phase 0 Constraint

This reference architecture authorizes conceptual planning only.

It does not authorize components, schemas, code, tests, adapters, credentials,
provider access, model access, persistence, certificate issuance, deployment,
or production operation.
