# AFR Phase 1 Trust Invariants

## 1. Purpose

This document defines the mandatory trust invariants for AFR canonical
information contracts and deterministic evaluation semantics.

These invariants constrain future design and implementation. They do not
authorize code, controls, credentials, integrations, persistence, execution,
certificate issuance, deployment, or production access.

## 2. Trust Position

AFR operates across distinct authority and trust domains:

- architecture-truth authorities;
- provider and enterprise observation sources;
- evidence collectors;
- AFR evidence-trust functions;
- deterministic evaluators;
- policy authorities;
- certificate authorities in a future phase;
- downstream consumers;
- human reviewers.

No identity, record, system, or trust domain is trusted solely because it can
reach AFR or produce syntactically valid content.

## 3. Foundational Invariants

Every authoritative AFR evaluation must preserve:

1. one resolved tenant context;
2. one bounded subject and evaluation scope;
3. validated architecture-truth authority;
4. attributable source and collector identities;
5. evidence provenance and integrity;
6. explicit freshness and trusted-time semantics;
7. immutable material evaluation inputs;
8. deterministic outcome selection;
9. complete traceability;
10. downstream authority containment.

Failure of a required invariant prevents `CONFORMANT`.

## 4. Authority Separation Invariant

Architecture truth, observations, evidence eligibility, evaluation,
enforcement, and presentation remain separate authority domains.

Specifically:

- NEXUS or another approved architecture authority owns architecture truth;
- providers and enterprise systems report bounded observations;
- AFR determines observation eligibility and bounded conformance;
- ATA retains consequential runtime commit authority;
- PAA may coordinate review but cannot alter truth or findings;
- Humanize may present approved outputs but cannot originate evidence.

No downstream consumer can increase the authority of an AFR record.

## 5. Tenant Isolation Invariant

Every authoritative input, intermediate decision, result, and provenance event
must be bound to exactly one resolved tenant context.

Tenant identity must propagate through:

- truth-snapshot references;
- architecture claims;
- observations;
- eligibility decisions;
- canonical evidence;
- evidence sets;
- evaluation definitions and contexts;
- claim-level results;
- aggregate results;
- findings;
- future certificate representations;
- provenance events.

A missing or mismatched tenant identity prevents authoritative evaluation.

Cross-tenant evidence substitution, joining, leakage, result reuse, or
certificate reuse is prohibited.

A future cross-tenant aggregate requires separate authority and cannot inherit
authorization from Phase 1.

## 6. Subject and Scope Invariant

Evidence may participate only when its tenant, subject, environment, release,
deployment, resource, time, and requested scope match the evaluation context.

A broad provider observation cannot support a narrower claim unless the
relevant subject and scope are deterministically established.

A partial observation cannot be represented as complete coverage.

Display names, mutable labels, or inferred similarity are insufficient for
authoritative subject binding.

## 7. Architecture-Truth Authority Invariant

AFR must establish that architecture truth is:

- issued by a recognized authority;
- approved;
- immutable;
- versioned;
- integrity-verifiable;
- applicable to the evaluated tenant and subject;
- unambiguous about supersession;
- compatible with the evaluation definition.

For NEXUS-governed systems, NEXUS remains authoritative.

AFR cannot:

- originate architecture truth;
- infer approval from object presence;
- treat drafts as approved;
- repair missing meaning through inference;
- mutate NEXUS state;
- supersede NEXUS decisions;
- treat provider state as architecture intent.

An unresolved truth-authority condition produces `INCONCLUSIVE`.

## 8. Identity Invariant

Every material action and record must be attributable to a resolved identity.

Identity classes remain distinguishable:

- architecture authority;
- truth exporter;
- observation source;
- evidence collector;
- normalization workload;
- eligibility evaluator;
- conformance evaluator;
- policy approver;
- human reviewer;
- future certificate issuer;
- downstream consumer.

One identity class cannot impersonate or inherit another class’s authority.

A collector identity is not the observation-source identity.

Workloads cannot expand their own authority or approve their own trust status.

## 9. Least-Authority Invariant

Future observation collection must use bounded read-only authority.

Collection authority must not include:

- provider mutation;
- remediation;
- permission expansion;
- architecture approval;
- lifecycle transition;
- certificate issuance;
- runtime commit.

Phase 1 does not authorize collectors or credentials.

## 10. Provenance Invariant

Every material input must preserve attributable provenance sufficient to
answer:

- who or what produced it;
- from which source;
- under which tenant and scope;
- using which collection or transformation definition;
- at what observed, collected, and ingested times;
- through which transformations;
- with which integrity references;
- under which version and compatibility constraints.

Missing or unverifiable required provenance prevents positive eligibility.

Narrative explanation is not a substitute for provenance.

## 11. Integrity Invariant

Integrity protection must conceptually bind:

- truth snapshots;
- claims;
- raw observations;
- canonical evidence;
- eligibility decisions;
- evidence sets;
- evaluation definitions;
- policies;
- evaluator versions;
- evaluation contexts;
- results;
- findings;
- future certificates;
- provenance events.

Integrity failure cannot be repaired by re-labeling, normalization, model
inference, or presentation.

Phase 1 does not select integrity algorithms or key-management systems.

## 12. Immutability Invariant

Material inputs and authoritative results become immutable within a completed
evaluation.

New information produces a new version, evidence set, evaluation, result, or
supersession relationship.

It must not silently mutate:

- an approved truth snapshot;
- a source observation;
- an eligibility decision;
- an evaluated evidence set;
- an evaluation definition;
- a completed result;
- an evaluation fingerprint.

Historical reproducibility requires preservation of prior identities.

## 13. Freshness and Time Invariant

Every time-sensitive assertion must identify the applicable time semantics.

AFR must distinguish:

- source observation time;
- collection time;
- ingestion time;
- evaluation time;
- evidence freshness deadline;
- result validity deadline;
- certificate expiry in a future phase;
- supersession time;
- future revocation time.

Ingestion time cannot substitute for observation time.

A newer timestamp alone does not prove newer operational state.

Unknown or untrusted required time semantics prevent `CONFORMANT`.

Expired required evidence produces `STALE` unless current eligible evidence
independently establishes `NON_CONFORMANT`.

## 14. Evidence Eligibility Invariant

An observation cannot support a claim until eligibility is explicitly
determined for the evaluation context.

Eligibility requires successful validation of:

- tenant and subject binding;
- source and collector identity;
- provenance;
- integrity;
- scope;
- freshness;
- compatibility;
- normalization lineage;
- collection completeness;
- source-specific trust conditions.

Normalization cannot elevate evidence authority.

Evidence eligible for one evaluation is not automatically eligible for another.

## 15. Completeness Invariant

All mandatory evidence dependencies must be satisfied before `CONFORMANT`.

AFR must preserve:

- requested evidence;
- received evidence;
- unavailable evidence;
- partial collection;
- rejected evidence;
- stale evidence;
- unverifiable evidence;
- contradictions.

Optional evidence cannot silently replace missing mandatory evidence.

Absence of evidence is not proof of conformance or violation.

## 16. Contradiction-Preservation Invariant

Every eligible material contradiction must remain visible and linked to:

- the affected claim;
- contradicting evidence;
- scope and time;
- evaluation rule;
- materiality;
- outcome effect;
- resolution state.

Supporting evidence cannot silently cancel or hide contradictory evidence.

Presentation, aggregation, or model-generated explanation cannot suppress a
material contradiction.

## 17. Determinism Invariant

The same canonical material inputs must produce the same authoritative outcome
and fingerprint.

Authoritative outcome selection must not depend on:

- sampling;
- model inference;
- free-form interpretation;
- presentation order;
- undocumented defaults;
- mutable external state not captured in the evidence set;
- reviewer preference.

Human review may approve semantics or resolve governed ambiguity, but the
approved resolution must become an explicit versioned input.

## 18. Fail-Closed Invariant

`CONFORMANT` is prohibited when a required condition is:

- missing;
- ambiguous;
- unverifiable;
- incompatible;
- stale;
- partially scoped;
- integrity-failed;
- tenant-mismatched;
- subject-mismatched;
- contradicted.

Fail-closed does not mean every incomplete condition becomes
`NON_CONFORMANT`.

Use:

- `NON_CONFORMANT` for deterministically established violation;
- `STALE` for expired mandatory evidence without current decisive violation;
- `INCONCLUSIVE` when required semantics or evidence cannot support a decision;
- `CONFORMANT` only for complete eligible support without material
  contradiction.

## 19. Aggregation Invariant

Aggregation cannot increase confidence or authority beyond the included
claim-level results.

An aggregate result must preserve:

- every required and critical claim;
- every weaker material outcome;
- all material gaps and contradictions;
- coverage;
- aggregation-policy identity and version;
- limitations;
- validity window.

No majority, score, weight, summary, or model output may conceal a required
`NON_CONFORMANT`, `STALE`, or `INCONCLUSIVE` result.

## 20. Fingerprint Invariant

An evaluation fingerprint must bind every material deterministic input.

A fingerprint must change when any material truth, claim, evidence, policy,
definition, evaluator, context, compatibility, or trusted-time input changes.

A fingerprint does not itself establish correctness or authority.

Phase 1 does not select canonical serialization or cryptographic algorithms.

## 21. Model-Containment Invariant

A model cannot authoritatively:

- establish truth authority;
- approve architecture claims;
- determine evidence eligibility;
- invent missing evidence;
- suppress contradictions;
- select claim-level or aggregate outcomes;
- calculate authoritative fingerprints;
- issue certificates;
- authorize deployment;
- grant runtime authority.

Model output may later assist explanation or review preparation only when
separately authorized and contained outside the authoritative decision path.

## 22. Downstream Containment Invariant

Downstream consumers receive only the authority explicitly represented by the
AFR output.

They cannot:

- mutate AFR outcomes;
- convert findings into architecture decisions;
- convert certificates into runtime permission;
- treat narratives as evidence;
- remove limitations;
- extend validity windows;
- reuse results outside tenant, subject, scope, or time boundaries.

ATA must apply its own policy and authority semantics to any future AFR input.

## 23. Certificate Containment Invariant

A future certificate represents a bounded completed evaluation.

It cannot:

- exceed evaluated scope;
- survive expiry without re-evaluation;
- omit material limitations;
- grant deployment authority;
- grant execution authority;
- act as an ATA authorization;
- replace underlying evidence and provenance.

Phase 1 does not authorize certificate generation, signing, issuance, or
revocation.

## 24. Audit and Traceability Invariant

Every authoritative result must be traceable to:

- truth authority and snapshot;
- evaluated claims;
- observation sources;
- collector identities;
- eligibility decisions;
- evidence set;
- gaps and contradictions;
- evaluation definition;
- policy version;
- evaluator version;
- evaluation context;
- outcome rule;
- fingerprint;
- evaluation and validity times.

Missing material traceability prevents an authoritative positive assertion.

## 25. Failure-Visibility Invariant

Failures cannot be converted into positive evidence or hidden by retry,
aggregation, normalization, or presentation.

Material failures include:

- authority-validation failure;
- identity failure;
- collection failure;
- partial collection;
- provenance failure;
- integrity failure;
- compatibility failure;
- trusted-time failure;
- tenant or subject mismatch;
- evaluator failure;
- downstream delivery failure.

A downstream delivery failure does not alter the immutable evaluation result,
but must remain observable.

## 26. Threat Conditions

Future controls must address at least:

- truth-snapshot substitution;
- draft-to-approved confusion;
- stale truth replay;
- evidence tampering;
- evidence replay;
- cross-tenant substitution;
- collector impersonation;
- source impersonation;
- scope expansion;
- partial-result concealment;
- normalization corruption;
- contradiction suppression;
- policy downgrade;
- evaluator-version substitution;
- timestamp manipulation;
- result mutation;
- certificate misuse;
- downstream authority escalation;
- model-induced authoritative drift.

Phase 1 identifies these conditions without implementing mitigations.

## 27. Deferred Security Decisions

Phase 1 does not select:

- identity provider;
- authorization engine;
- key-management service;
- signing algorithm;
- hashing algorithm;
- canonical serialization;
- storage controls;
- network controls;
- secret-management system;
- monitoring platform;
- incident-response platform;
- deployment environment.

Those decisions require later authority and evidence.

## 28. Phase 1 Constraint

These trust invariants are planning documentation only.

They create no implementation, integration, runtime, persistence, collection,
certificate, deployment, production, or Phase 2 authority.
