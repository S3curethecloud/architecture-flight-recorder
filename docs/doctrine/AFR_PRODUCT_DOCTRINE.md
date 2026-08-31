# Architecture Flight Recorder Product Doctrine

## 1. Mission

Architecture Flight Recorder continuously determines whether bounded,
attributable operational evidence supports approved architecture truth.

Its mission is to make architecture conformance observable, reproducible, and
time-bound after architecture approval and deployment.

## 2. Protected Concern

AFR protects the integrity of the relationship between:

- what the architecture authority approved;
- what was actually released;
- what is currently deployed;
- what operational evidence can substantiate;
- what a conformance result is permitted to claim.

AFR does not prove that an architecture is universally correct. It determines
whether defined evidence supports defined approved claims within an explicit
scope and time window.

## 3. Architecture Truth Decay

Architecture truth decay occurs when deployed reality no longer supports the
approved architecture truth or when available evidence can no longer establish
that support.

Truth decay can result from:

- configuration drift;
- identity or permission expansion;
- unapproved tools or capabilities;
- model or prompt changes;
- retrieval-source or data-boundary changes;
- release-artifact divergence;
- expired or missing evaluations;
- policy-version divergence;
- dependency or provider changes;
- incomplete, stale, or contradictory evidence.

Truth decay is not limited to confirmed violations. Loss of sufficient evidence
is itself a material conformance condition.

## 4. Architecture Truth

Architecture truth is an approved, attributable, versioned representation of
architecture intent and constraints.

For NEXUS-governed systems, NEXUS remains authoritative for that truth.

AFR may evaluate architecture truth, but it cannot:

- create it;
- approve it;
- modify it;
- supersede it;
- infer missing authoritative meaning;
- treat observations as replacements for it.

## 5. Operational Evidence

Operational evidence is an attributable observation about a bounded system,
resource, configuration, identity, release, evaluation, or runtime condition.

Evidence must preserve:

- tenant and system scope;
- source identity;
- collection identity;
- collection time;
- observed time when available;
- provenance;
- integrity information;
- freshness;
- normalization history;
- relevant version information.

Evidence authority cannot be elevated by normalization, aggregation, model
inference, or presentation.

## 6. Architecture Conformance

Architecture conformance is the result of evaluating approved architecture
truth against eligible operational evidence using an identified evaluation
definition.

Conformance is always:

- bounded to identified claims;
- bounded to an identified system and tenant;
- bounded to an evidence set;
- bounded to an evaluation version;
- bounded to a time window;
- reproducible from preserved inputs;
- no stronger than its weakest required evidence dependency.

Conformance is not equivalent to:

- architecture correctness;
- security certification;
- regulatory approval;
- production authorization;
- absence of all risk;
- proof of future behavior.

## 7. Canonical Outcome Doctrine

AFR must support at least these outcome meanings:

### CONFORMANT

Eligible evidence supports the evaluated architecture claim within the declared
scope and freshness window, and no eligible contradictory evidence remains
unresolved.

### NON_CONFORMANT

Eligible evidence contradicts the evaluated architecture claim or demonstrates
that a required conformance condition is not satisfied.

### INCONCLUSIVE

AFR cannot determine conformance because required truth, evidence, provenance,
identity, scope, or evaluation semantics are incomplete, ambiguous, or
conflicting.

### STALE

Previously eligible evidence or a prior result has exceeded its authorized
freshness window and cannot support a current conformance assertion.

No outcome may be silently converted into another outcome for convenience.

## 8. Fail-Closed Doctrine

AFR fails closed with respect to claims of conformance.

Missing, ambiguous, conflicting, unverifiable, cross-tenant, or stale inputs
cannot produce `CONFORMANT`.

Fail-closed does not mean that AFR automatically declares every incomplete
condition `NON_CONFORMANT`. When evidence cannot support either conclusion,
AFR uses `INCONCLUSIVE` or `STALE` as appropriate.

## 9. Determinism Doctrine

The same authoritative truth snapshot, eligible evidence set, evaluation
definition, policy version, and evaluator version must produce the same
conformance outcome and fingerprint.

Non-deterministic model output cannot become the authoritative conformance
decision.

Models may eventually assist with explanation, classification proposals, or
human review preparation, but deterministic controls must validate any material
used by the authoritative evaluation path.

## 10. Certificate Doctrine

An Architecture Conformance Certificate is a signed or integrity-bound
representation of a completed bounded evaluation.

A certificate must identify:

- the evaluated subject;
- the architecture-truth snapshot;
- the evaluated claims;
- the eligible evidence set;
- the evaluation and policy versions;
- the outcome;
- the evaluation time and validity window;
- unresolved limitations;
- integrity and issuer information.

A certificate is not:

- permanent proof;
- execution authority;
- deployment authority;
- an ATA authorization;
- a substitute for underlying evidence;
- a guarantee of conditions outside its evaluated scope.

Certificate issuance and signing are not authorized during Phase 0.

## 11. Ecosystem Doctrine

### NEXUS

NEXUS defines and approves architecture truth. AFR verifies operational
conformance against a future approved, immutable export of that truth.

### ATA

ATA governs consequential runtime trust and commit authority. AFR may
eventually provide conformance evidence to ATA, but cannot grant authority.

### Personal Architect Agent

PAA may initiate governed work, explain findings, and coordinate proposed
remediation. It cannot rewrite architecture truth or AFR outcomes.

### Humanize Enterprise

Humanize may present approved AFR evidence and narratives. It cannot originate
evidence or become the conformance authority.

### Providers and Enterprise Systems

Providers and enterprise systems expose observations about their own bounded
state. Their observations remain subject to identity, provenance, integrity,
freshness, completeness, and scope validation.

## 12. Tenant Doctrine

Every authoritative input, evaluation, finding, and certificate must be bound
to exactly one tenant context unless an explicitly governed aggregate is later
authorized.

Cross-tenant evidence substitution, evaluation, leakage, or certificate reuse
is prohibited.

## 13. Non-Goals

AFR is not:

- an architecture design agent;
- a system of record for NEXUS engagement state;
- an IAM platform;
- a SIEM;
- a cloud-security posture manager;
- an observability platform;
- an agent framework;
- a policy engine replacement;
- a deployment orchestrator;
- an autonomous remediation engine;
- an ATA replacement;
- a client-document authoring system.

AFR may integrate with some of these systems later without assuming their
ownership or authority.

## 14. Governing Principle

> AFR may assert only what the approved truth, eligible evidence, evaluation
> semantics, and time boundary can jointly support.

## 15. Phase 0 Authority

This doctrine defines product direction and boundaries only.

It creates no authority for runtime implementation, provider integration,
evidence collection, evaluation execution, persistence, certificate issuance,
external-system integration, deployment, or production mutation.
