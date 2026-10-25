# AFR Phase 12 Command Center and Conformance Trust Boundary

## 1. Purpose

This document defines the Phase 12 planning trust boundary for deterministic
findings, drift, certificate representations, and the durable AFR Command Center.

It creates no implementation, runtime, provider, signing, issuance, deployment, or
production authority.

## 2. Protected assets

Protected assets include:

- qualified architecture-truth identity;
- admitted evidence identity and provenance;
- accepted Phase 11 evaluation results;
- Phase 12 finding identity and state;
- drift identity and comparison lineage;
- certificate-content identity and fingerprint;
- score formula identity and source finding set;
- tenant and subject isolation;
- read-model identity and version;
- capability-registry identity;
- adapter compatibility state;
- authority-state presentation;
- audit and historical disposition records.

## 3. Primary threats

The planning model must address:

- cross-tenant or cross-subject substitution;
- evaluation-result substitution;
- unsupported finding-state promotion;
- stale state rendered as current;
- evidence-unavailable state rendered as success;
- inconclusive state collapsed into support;
- drift fabrication from transport or refresh noise;
- certificate display confused with issuance;
- certificate fingerprint substitution;
- conformance-score laundering of unresolved state;
- provider payload shape becoming canonical contract;
- capability registration laundering into authority;
- adapter privilege escalation;
- UI action accidentally acquiring mutation authority;
- model-assisted suppression or reinterpretation of findings;
- Phase 13 integration rewriting Phase 12 semantics;
- Phase 14 hardening rewriting Phase 12 semantics.

## 4. Trust zones

### Zone A - NEXUS architecture truth

NEXUS remains authoritative for approved architecture truth. AFR cannot modify or
repair NEXUS truth.

### Zone B - Admitted operational evidence

Evidence eligibility remains governed by accepted upstream admissibility semantics.
Availability is not eligibility.

### Zone C - Phase 11 evaluation results

Accepted Phase 11 results are immutable upstream inputs. Phase 12 cannot rewrite
them.

### Zone D - Phase 12 derivation

Finding, drift, score, and certificate-content derivation are deterministic,
versioned, and bounded to accepted source state.

### Zone E - Command Center read models

Read models are provider-neutral projections carrying scope, provenance, authority,
freshness, limitations, and source fingerprint.

### Zone F - Command Center shell

The shell presents accepted read models. It is not an architecture-authority,
provider-mutation, remediation, signing, or issuance zone.

### Zone G - Phase 13 adapters

Future adapters are isolated extension modules and require separate authority.

### Zone H - Phase 14 production controls

Future hardening controls protect production behavior but cannot redefine accepted
Phase 12 semantics.

## 5. Fail-closed doctrine

Unresolved mandatory identity, scope, authority, provenance, integrity, version,
freshness, or compatibility state blocks authoritative positive presentation.

Availability pressure does not justify optimistic state.

## 6. Tenant and subject isolation

No finding, drift comparison, certificate representation, score, read model, cache,
or adapter may mix tenant or subject scopes unless an accepted contract explicitly
defines the aggregate scope.

## 7. Finding-state integrity

Only the accepted deterministic derivation contract may assign a finding state.

Models, operators, adapters, UI components, and notification channels cannot
promote a finding to `SUPPORTED`.

## 8. Evidence-unavailable boundary

Missing or inaccessible required evidence is explicit state.

`EVIDENCE_UNAVAILABLE != SUPPORTED`

`EVIDENCE_UNAVAILABLE != EMPTY_SUCCESS`

## 9. Staleness boundary

Stale evidence or expired validity remains visible. Refresh time, page load time,
queue time, or current wall-clock display cannot make stale evidence current.

## 10. Drift integrity

Drift requires comparable prior/current accepted state and a material change.
Transport duplication, polling order, caching, or UI refresh cannot fabricate
drift.

## 11. Certificate trust boundary

Certificate content, signing, issuance, publication, delivery, expiration,
supersession, and revocation are separate concerns.

Phase 12 planning defines content semantics only. It creates no signing or issuance
authority.

## 12. Score trust boundary

The Architecture Conformance Score is derived presentation state.

It cannot:

- become architecture truth;
- replace finding states;
- hide stale/inconclusive/evidence-unavailable counts;
- imply certainty when required state is unresolved.

## 13. Command Center input boundary

The shell accepts only versioned read models. Raw provider payloads, HTML, model
output, transport envelopes, or arbitrary external JSON cannot become trusted shell
state without an accepted adapter/read-model contract.

## 14. Command Center action boundary

Phase 12 Command Center planning is read oriented.

No button, route, widget, keyboard action, API call, or automation may acquire
provider mutation, remediation, NEXUS mutation, ATA commit, certificate issuance,
deployment, or production authority merely because it appears in the UI.

## 15. Capability-registry boundary

Capability registration is metadata, not permission. Required authority must be
resolved independently for every capability use.

## 16. Adapter isolation

A failing or compromised optional adapter must not contaminate core canonical
finding state. Shared critical identity, authority, scope, provenance, or integrity
failure fails closed.

## 17. Model boundary

Model inference is non-authoritative. A model cannot:

- invent or repair evidence;
- create architecture truth;
- choose authoritative finding state;
- override stale or unavailable state;
- suppress limitations;
- fabricate drift;
- sign or issue certificates;
- grant adapter authority;
- authorize remediation;
- redefine Phase 12 semantics.

## 18. Secrets and sensitive data

Command Center read models prohibit raw credentials, tokens, signing keys, and
unnecessary provider secrets. Sensitive data exposure must be minimized and
scope-bound.

## 19. Phase 13 boundary

Phase 13 operational-delivery and downstream-consumer adapters require separate
authority. Their presence cannot mutate or reinterpret Phase 12 accepted state.

## 20. Phase 14 boundary

Phase 14 production hardening and E2E certification require separate authority.
Hardening must preserve Phase 12 semantic identity or use separately governed
versioning.

## 21. Nonmutation guarantees during planning

During detached Phase 12 preparation:

- AFR repository mutation: NONE;
- AFR index/ref/object mutation: NONE;
- provider access: NONE;
- operational-evidence ingestion: NONE;
- finding runtime effect: NONE;
- certificate runtime effect: NONE;
- Command Center implementation: NONE;
- downstream integration: NONE;
- NEXUS mutation: NONE;
- ATA commit effect: NONE;
- Phase 13 authority: NONE;
- Phase 14 authority: NONE.

## 22. Stop conditions

Stop planning if satisfying the trust boundary would require:

- executable UI/runtime behavior;
- provider access or mutation;
- evidence ingestion;
- certificate signing or issuance;
- remediation or enforcement;
- NEXUS mutation;
- ATA commit authority;
- an eighth planning document;
- Phase 13 activation;
- Phase 14 activation;
- silent weakening of Phase 11 evaluation semantics;
- routine replacement of the durable shell instead of explicit versioned evolution.
