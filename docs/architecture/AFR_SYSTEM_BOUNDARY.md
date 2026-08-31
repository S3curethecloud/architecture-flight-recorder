# Architecture Flight Recorder System Boundary

## 1. Purpose

This document defines the ownership, authority, information-flow, and
non-duplication boundaries of Architecture Flight Recorder.

It describes intended architecture direction only. It does not authorize
implementation or integration.

## 2. Bounded Context

AFR occupies the bounded context between approved architecture truth and
observed deployed reality.

Its bounded responsibility is:

> Determine whether eligible operational evidence supports identified,
> approved architecture claims within an explicit scope and time boundary.

AFR begins with an immutable architecture-truth snapshot and attributable
operational evidence. It ends with a bounded conformance result and its
provenance.

## 3. Authority Domains

### Architecture-Truth Authority

NEXUS owns architecture-truth authority for NEXUS-governed systems.

This includes approved:

- architecture requirements;
- architecture decisions;
- architecture constraints;
- control profiles;
- semantic-action architecture;
- delegation and authority architecture;
- transaction and state invariants;
- rollout conditions;
- evidence references associated with architecture approval.

AFR cannot originate or mutate these authoritative objects.

### Operational-State Authority

Providers and enterprise systems remain authoritative sources for observations
about their own bounded operational state.

An observation is not automatically eligible evidence. AFR must still validate
its identity, scope, provenance, integrity, freshness, and collection context.

### Conformance-Evaluation Authority

AFR owns only the bounded conformance result produced from:

- an identified architecture-truth snapshot;
- an identified eligible evidence set;
- an identified evaluation definition;
- an identified policy version;
- an identified evaluator version;
- an identified evaluation time.

AFR conformance authority does not extend to architecture approval, provider
configuration, deployment permission, or runtime execution.

### Runtime Commit Authority

ATA retains consequential autonomous-action trust and commit authority where
ATA is applicable.

AFR cannot grant, expand, or impersonate ATA authority.

A future ATA policy may consume an AFR result as one input, but ATA must apply
its own authority and policy semantics.

### Coordination Authority

PAA may initiate governed requests, explain findings, and coordinate proposed
human remediation workflows.

PAA cannot modify authoritative AFR findings, NEXUS truth, evidence, or
evaluation records.

### Presentation Authority

Humanize may transform approved AFR outputs into client, executive, or
audit-facing presentations.

Humanize cannot originate evidence, change outcomes, or become the system of
record for conformance.

## 4. Conceptual Inputs

AFR may eventually accept the following input classes.

### Architecture-Truth Snapshot

An immutable, versioned, attributable export from an architecture authority.

For NEXUS, the export contract does not yet exist and is not authorized by
Phase 0.

### Evidence Observation

An attributable observation collected from a provider or enterprise system.

An observation must not be treated as eligible evidence until validation is
complete.

### Evaluation Definition

A deterministic definition that states:

- which claims are evaluated;
- which evidence is required;
- how evidence is matched;
- which freshness rules apply;
- what constitutes support or contradiction;
- when the result must be inconclusive or stale.

### Policy Context

A versioned set of bounded conformance policies. Policy context cannot create
architecture truth or runtime authority.

### Evaluation Context

The tenant, subject, environment, release, system, and evaluation time against
which the evaluation is performed.

## 5. Conceptual Outputs

### Conformance Finding

A deterministic result for an evaluated claim with outcome, rationale,
provenance, limitations, and fingerprint.

### Evidence Gap

An explicit record that required eligible evidence is unavailable, incomplete,
unverifiable, conflicting, or stale.

An evidence gap cannot be silently converted into conformance.

### Architecture Drift Finding

A result indicating that eligible evidence contradicts approved architecture
truth or demonstrates a material mismatch.

### Staleness Finding

A result indicating that prior evidence or conformance has exceeded its
authorized freshness window.

### Conformance Certificate

An integrity-bound representation of a bounded completed evaluation.

A certificate does not grant deployment or runtime authority.

### Remediation Proposal Input

A bounded, non-authoritative output that a human or PAA may use to prepare a
remediation proposal.

AFR does not execute remediation.

## 6. NEXUS Integration Boundary

The future NEXUS-to-AFR direction is read-only:

- NEXUS exports approved architecture truth;
- AFR validates export identity and integrity;
- AFR preserves the received version without modification;
- AFR evaluates operational evidence against that version;
- AFR may report findings using stable NEXUS object references.

AFR must not:

- write into NEXUS engagement state;
- approve or supersede architecture decisions;
- compile new architecture requirements;
- reinterpret missing semantics;
- infer approval from object presence;
- treat draft objects as approved truth;
- modify NEXUS lifecycle state;
- cause a NEXUS stage transition.

Any proposed architecture change discovered through AFR must return through the
normal PAA and NEXUS intake, review, and approval lifecycle.

## 7. Provider Integration Boundary

Future evidence collectors may perform bounded read-only observation.

They must not:

- modify provider state;
- remediate configuration;
- expand their own permissions;
- reuse evidence across tenants;
- hide collection failures;
- convert provider errors into positive evidence;
- infer unobserved state;
- claim completeness beyond the collection scope.

Provider adapters are not authorized during Phase 0.

## 8. Evaluation Boundary

The authoritative evaluation path must be deterministic.

The evaluation boundary must reject or downgrade inputs when:

- tenant identity is missing or mismatched;
- subject identity is missing or mismatched;
- truth is unapproved, ambiguous, or unverifiable;
- evidence provenance is incomplete;
- evidence integrity cannot be established;
- evidence is outside the required scope;
- evidence is stale;
- required evidence is absent;
- contradictory evidence is unresolved;
- evaluation or policy semantics are unknown.

Only eligible inputs may contribute to `CONFORMANT`.

## 9. Model Boundary

A model may eventually assist with:

- human-readable explanations;
- proposed evidence classification;
- proposed claim-to-evidence mappings;
- remediation drafting;
- review preparation.

A model cannot authoritatively:

- create architecture truth;
- approve claims;
- determine evidence eligibility;
- suppress contradictory evidence;
- select a conformance outcome;
- issue a certificate;
- grant deployment or runtime authority.

Any model-assisted material entering a governed path must be independently
validated by deterministic controls or explicit human review.

## 10. Persistence Boundary

Future AFR persistence may preserve received inputs, evaluation records,
findings, certificates, and provenance.

AFR persistence must not become a duplicate mutable store for NEXUS
architecture truth. Received truth snapshots remain immutable representations
of externally authoritative versions.

Persistence design and implementation are not authorized during Phase 0.

## 11. Tenant Boundary

Every AFR input and output must belong to a resolved tenant context.

Tenant context must propagate through:

- truth ingestion;
- evidence collection;
- evidence normalization;
- evaluation;
- findings;
- certificate issuance;
- downstream delivery.

Cross-tenant joins, evidence substitution, finding reuse, or certificate reuse
are prohibited unless a separately governed aggregate capability is explicitly
authorized later.

## 12. Feedback Boundary

AFR may identify drift or insufficient evidence.

The permitted conceptual feedback path is:

1. AFR produces a bounded finding.
2. A human or PAA reviews and explains the finding.
3. A remediation or architecture-change request enters the governed process.
4. NEXUS determines whether architecture truth must change.
5. Authorized enterprise systems determine whether deployed state must change.
6. AFR evaluates new evidence against the applicable approved truth.

AFR does not directly close its own findings through ungoverned mutation.

## 13. Prohibited Authority Flows

The following authority flows are prohibited:

- evidence observation to architecture approval;
- AFR finding to NEXUS state mutation;
- AFR certificate to automatic execution authority;
- model inference to authoritative conformance;
- Humanize narrative to evidence authority;
- PAA explanation to finding mutation;
- provider metadata to inferred architecture intent;
- missing evidence to `CONFORMANT`;
- cross-tenant evidence to any authoritative result.

## 14. Phase 0 Boundary

Phase 0 authorizes this system-boundary definition only.

It creates no authority for:

- source code;
- schemas;
- provider adapters;
- NEXUS adapters;
- model integration;
- persistence;
- evaluation execution;
- certificate generation;
- external writes;
- deployment;
- production mutation.
