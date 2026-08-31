# Phase 0 Acceptance Criteria

## Purpose

Phase 0 establishes the Architecture Flight Recorder product doctrine,
ownership boundary, reference architecture, trust model, and authoritative
relationship with NEXUS.

This phase is architecture planning only.

## Product Doctrine

- [ ] AFR has one unambiguous product mission.
- [ ] Architecture truth decay is explicitly defined.
- [ ] Architecture conformance is distinguished from architecture correctness.
- [ ] A conformance result is explicitly time-bound and evidence-bound.
- [ ] AFR is not described as an architecture-authoring system.
- [ ] AFR is not described as an execution-authority system.

## NEXUS Boundary

- [ ] NEXUS remains authoritative for approved architecture truth.
- [ ] AFR consumes only immutable, versioned, read-only truth snapshots.
- [ ] AFR cannot mutate NEXUS engagement state.
- [ ] AFR cannot silently reinterpret missing NEXUS semantics.
- [ ] Incomplete truth produces an inconclusive or blocked evaluation instead
      of invented certainty.

## Evidence Boundary

- [ ] Authoritative architecture truth is distinct from observed evidence.
- [ ] Evidence provenance, collection time, source identity, and freshness are
      mandatory concepts.
- [ ] Absence of evidence is not treated as proof of conformance.
- [ ] Contradictory evidence cannot be discarded silently.
- [ ] Evidence normalization cannot elevate evidence authority.

## Evaluation Boundary

- [ ] Outcomes include at least `CONFORMANT`, `NON_CONFORMANT`,
      `INCONCLUSIVE`, and `STALE`.
- [ ] Evaluation is deterministic for the same truth snapshot, evidence set,
      policy version, and evaluation version.
- [ ] Every outcome is traceable to claims, evidence, and evaluation rules.
- [ ] Model inference cannot produce an authoritative conformance result.
- [ ] A certificate cannot claim more than its evaluated scope supports.

## Ecosystem Boundaries

- [ ] ATA retains consequential runtime commit authority.
- [ ] AFR cannot grant ATA or any agent additional authority.
- [ ] PAA can explain findings but cannot rewrite them.
- [ ] Humanize can present approved evidence but cannot originate it.
- [ ] Provider systems remain authoritative for their observed operational
      state within the limits of collected evidence.

## Security and Trust

- [ ] Trust boundaries are explicitly documented.
- [ ] Evidence tampering, replay, substitution, staleness, and cross-tenant
      leakage are addressed.
- [ ] Fail-closed behavior is defined for missing identity, provenance,
      freshness, or evaluation semantics.
- [ ] Tenant isolation is a foundational invariant.
- [ ] Certificate integrity and revocation concepts are defined without being
      implemented.

## Authority and Scope

- [ ] Every Phase 0 artifact is within the authorized eight-file boundary.
- [ ] No runtime or integration implementation exists.
- [ ] No NEXUS files are modified.
- [ ] No Phase 1 authority is inferred from Phase 0 acceptance.
- [ ] The SOT and all Phase 0 documents agree on ownership and authority.

## Required Exit Evidence

Phase 0 closure requires:

- authorized file-boundary verification;
- Markdown structural validation;
- cross-document terminology review;
- NEXUS non-duplication review;
- security-boundary review;
- clean staged-diff verification.

## Exit Gate

Phase 0 may close only with all of the following:

- `AFR_PHASE_0_ACCEPTANCE = PASS`
- `AFR_PHASE_0_IMPLEMENTATION_AUTHORITY = NONE`
- `AFR_PHASE_1_AUTHORITY = NONE`

Phase 0 acceptance authorizes only a separate Phase 0 closure review. It does
not authorize implementation or Phase 1 planning.
