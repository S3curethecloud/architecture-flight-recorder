# AFR Phase 12 Drift, Findings, Certificates, and Command Center Architecture

## 1. Architectural purpose

Phase 12 defines the technology-neutral architecture that converts accepted
Phase 11 evaluation results into deterministic Phase 12 finding, drift, and
certificate representations and exposes them through a durable read-oriented
AFR Command Center.

This is a planning artifact. It does not implement or execute Phase 12.

## 2. Architectural invariants

- `NEXUS_ARCHITECTURE_TRUTH != AFR_CONFORMANCE_RESULT`
- `AFR_FINDING != NEXUS_ARCHITECTURE_RISK`
- `AFR_CONFORMANCE != NEXUS_ARCHITECTURE_ACCEPTANCE`
- `AFR_READ_AUTHORITY != NEXUS_MUTATION_AUTHORITY`
- `PHASE_11_EVALUATION_RESULT != PHASE_12_FINDING_OR_CERTIFICATE`
- `COMMAND_CENTER_PRESENTATION != EXECUTION_AUTHORITY`
- `COMMAND_CENTER_VISIBILITY != PROVIDER_MUTATION_AUTHORITY`
- `CERTIFICATE_DISPLAY != CERTIFICATE_ISSUANCE_AUTHORITY`
- `PHASE_13_INTEGRATION != PHASE_12_FINDING_REINTERPRETATION`
- `PHASE_14_HARDENING != PHASE_12_SEMANTIC_REDEFINITION`

## 3. Input boundary

Phase 12 consumes only qualified, accepted Phase 11 evaluation results and the
immutable identities bound into those results.

A raw provider payload, transport event, model output, dashboard widget, or operator
label cannot become authoritative Phase 12 input merely because it is available.

## 4. Logical components

### 4.1 EvaluationResultReader

Reads accepted Phase 11 results without mutation and verifies identity, scope,
version, provenance, and terminal-result status.

### 4.2 FindingDeriver

Deterministically derives one Phase 12 finding state from accepted source state
under an exact finding-derivation contract version.

### 4.3 DriftDetector

Compares compatible prior and current accepted finding identities and emits a
bounded drift representation only when a material change is proven.

### 4.4 CertificateComposer

Builds a deterministic certificate representation from an accepted finding set,
scope, validity policy, and exact source identities. It does not sign or issue.

### 4.5 ConformanceSummaryProjector

Produces traceable summary state, including an optional versioned Architecture
Conformance Score, without obscuring unresolved states.

### 4.6 ReadModelProjector

Projects canonical Phase 12 state into versioned provider-neutral read models.

### 4.7 CommandCenterShell

Provides the durable human-facing shell. It renders read models and authority
state but cannot mutate authoritative AFR or NEXUS state.

### 4.8 CapabilityRegistry

Declares optional modules and adapters, their versions, compatibility ranges,
authority requirements, source types, and supported surfaces.

### 4.9 AdapterBoundary

Separates provider/downstream-specific integration from stable Command Center
contracts. Phase 12 activates no downstream adapter.

### 4.10 TimelineAuditProjector

Produces immutable historical projections for evaluation, finding, drift,
certificate, authority, and supersession events.

## 5. Finding state model

The Phase 12 finding-state domain is:

- `SUPPORTED`
- `CONTRADICTED`
- `STALE`
- `INCONCLUSIVE`
- `EVIDENCE_UNAVAILABLE`

The exact derivation mapping must be contract-bound and deterministic. Presentation
state cannot override the upstream evaluation record.

## 6. Finding immutability

An accepted finding is immutable. New truth, evidence, policy, evaluator, time, or
scope state produces a distinct later finding linked to the prior finding through
supersession metadata.

## 7. Drift architecture

A drift event is a derived comparison record, not a mutation.

Drift classes may include:

- support-to-contradiction;
- support-to-stale;
- support-to-inconclusive;
- evidence-unavailable transition;
- contradiction-to-supported;
- material truth identity change;
- material evidence binding change;
- material policy/evaluator version change.

Exact class semantics must be versioned before implementation.

## 8. Certificate architecture

A certificate representation binds an immutable certificate-content model to exact
finding/evaluation/evidence/truth identities and a validity interval.

Signing and issuance are separate future authority boundaries. A displayed
certificate candidate is not proof of issuance.

## 9. Architecture Conformance Score architecture

The score is an optional derived view.

It must include:

- formula ID and version;
- eligible finding count;
- supported count;
- contradicted count;
- stale count;
- inconclusive count;
- evidence-unavailable count;
- exclusions;
- exact finding-set identity.

If required inputs are unresolved, the score is unavailable rather than optimistic.

## 10. Command Center semantic surfaces

The durable shell supports these semantic surfaces:

1. Executive Status / Traceable Conformance Summary
2. Live Findings
3. Architecture Drift
4. Evidence Health
5. Evaluation Runs
6. Conformance Certificates / Attestations
7. System / Tenant / Architecture Scope
8. Critical Alerts
9. Flight Recorder Timeline
10. Governance / Audit

Surface semantics are stable even if navigation layout changes.

## 11. Authority-state overlay

Every relevant surface must expose whether the displayed capability is:

- planned;
- accepted;
- implemented;
- runtime-qualified;
- available;
- authorized;
- degraded;
- unavailable;
- stale;
- blocked.

Absence of authority cannot be rendered as successful availability.

## 12. Evidence and provenance overlay

Every finding, drift item, certificate representation, score, and material
summary must be traceable to exact source identities and provenance.

## 13. Provider-neutral shell

The shell consumes versioned read models rather than provider-native payloads.

Provider-specific fields may appear only inside explicitly typed adapter payloads
that cannot redefine canonical AFR semantics.

## 14. Capability registry architecture

Each optional capability registration contains:

- stable capability ID;
- capability contract version;
- compatibility range;
- source class;
- read/write posture;
- required authority class;
- supported shell surfaces;
- freshness model;
- failure model;
- provenance contract;
- lifecycle state.

Registration is descriptive. It is not authority.

## 15. Extension boundary

Phase 13 adds operational-delivery and downstream-consumer modules through adapter
interfaces. The Phase 12 shell, finding state model, read-model envelope, and
authority/provenance semantics remain stable or explicitly versioned.

## 16. Hardening boundary

Phase 14 adds production hardening around the accepted architecture:

- security controls;
- reliability and SLOs;
- performance and capacity;
- observability;
- E2E qualification;
- upgrade/rollback evidence;
- final NEXUS/ARCP compatibility certification.

Hardening cannot silently redefine Phase 12 semantics.

## 17. Failure architecture

Failure classes include:

- unresolved source evaluation identity;
- incompatible read-model version;
- incomplete provenance;
- stale required state;
- evidence unavailable;
- cross-tenant or cross-subject scope mismatch;
- finding derivation failure;
- drift comparison incompatibility;
- certificate composition failure;
- score derivation failure;
- adapter unavailable or unauthorized;
- internal invariant failure.

Failure cannot be translated into `SUPPORTED`.

## 18. Security zones

The architecture separates:

1. NEXUS architecture truth;
2. admitted operational evidence;
3. Phase 11 evaluation results;
4. Phase 12 finding/drift/certificate derivation;
5. Command Center read models;
6. Command Center presentation shell;
7. Phase 13 adapter modules;
8. Phase 14 production-hardening controls.

## 19. Side-effect boundary

This architecture defines no implemented UI, API, database, scheduler, signing
service, provider adapter, notification service, remediation engine, deployment,
production runtime, NEXUS mutation path, or ATA commit path.
