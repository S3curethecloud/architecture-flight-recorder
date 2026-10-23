# AFR Phase 11 Continuous Conformance Evaluation Runtime Trust Boundary

## 1. Purpose

This document defines the Phase 11 planning trust boundary for a future continuous
conformance evaluation runtime. It creates no executable runtime authority.

## 2. Protected assets

Protected assets include:

- qualified architecture-truth identity;
- admitted truth-to-evidence binding identity;
- tenant and subject isolation;
- evaluation-cycle identity;
- attempt identity and history;
- evaluation definitions and policy versions;
- evaluator and canonicalization versions;
- trusted-time context;
- claim and aggregate outcomes;
- result fingerprints;
- immutable completed results;
- failure and limitation records;
- supersession linkage.

## 3. Primary threats

The planning model must address:

- cross-tenant or cross-subject substitution;
- truth-anchor substitution;
- evidence-binding substitution;
- stale-evidence reuse;
- version downgrade or implicit latest selection;
- duplicate-trigger amplification;
- replay of prior requests;
- concurrent conflicting attempts;
- late-result overwrite;
- retry that silently changes material inputs;
- scheduler or queue time masquerading as trusted time;
- model-assisted outcome manipulation;
- audit projection changing authoritative state;
- Phase 11 result laundering into Phase 12 finding or certificate authority;
- NEXUS read authority laundering into mutation authority.

## 4. Trust zones

### Zone A - Architecture truth

NEXUS remains authoritative for qualified architecture truth. AFR reads qualified
truth under the accepted consumer contract and cannot mutate or repair it.

### Zone B - Admitted operational evidence

Phase 10 admissibility remains upstream. Evidence is not promoted merely because a
runtime can access it. Exact admitted binding identity is required.

### Zone C - Runtime request and trigger intake

Requests and triggers are untrusted until required identity, scope, version, and
authority conditions are validated.

### Zone D - Deterministic evaluation execution

Only an accepted deterministic kernel may produce authoritative claim outcomes.
Models, transport metadata, retries, and observability cannot choose outcomes.

### Zone E - Result acceptance

A result becomes terminal only after exact identity, scope, fingerprint, version,
time, and concurrency validation.

### Zone F - Downstream consumers

Phase 12 and other consumers are downstream. They cannot retroactively rewrite a
Phase 11 result, and Phase 11 cannot assume their authority.

## 5. Fail-closed doctrine

A future runtime must block authoritative completion when mandatory truth, evidence,
scope, version, time, policy, evaluator, canonicalization, fingerprint, or
concurrency state is unresolved.

Availability pressure does not justify default conformance.

## 6. Tenant and subject isolation

No cycle may mix tenants or subjects. Cross-scope evidence, results, retries, cache
entries, or deduplication keys must not be reused unless an accepted contract proves
that the identity and scope are identical.

## 7. Replay and duplicate boundary

Duplicate transport delivery is not automatically malicious, but it must be
classified deterministically. Replayed or duplicate input cannot create a second
conflicting accepted terminal result for one cycle identity.

## 8. Concurrency boundary

Concurrent execution creates a race risk at result acceptance. A later
implementation must provide a deterministic acceptance mechanism and evidence that
a late writer cannot replace an already accepted terminal result.

## 9. Time trust boundary

Observation time, capture time, admission time, evaluation time, and scheduler time
have different trust semantics. A system clock value is not authoritative merely
because it is recent.

## 10. Model boundary

Model inference is non-authoritative. A model cannot:

- repair missing truth;
- create evidence;
- waive admission failures;
- select conformance rules;
- choose canonical outcomes;
- suppress limitations;
- override concurrency controls;
- grant Phase 12 or NEXUS authority.

## 11. Provider boundary

No provider credential, provider read, collector, network call, telemetry
subscription, or live evidence ingestion is authorized by this planning package.

## 12. Persistence and transport boundary

A future runtime may require persistence, scheduling, or transport, but this
planning package selects and authorizes none. Storage and transport mechanisms must
not become authority sources.

## 13. Result and Phase 12 boundary

A completed Phase 11 evaluation remains a bounded conformance result. It is not by
itself a drift finding, certificate, deployment permission, remediation action, or
architecture-risk interpretation.

## 14. Nonmutation guarantees during planning

During detached Phase 11 preparation:

- AFR repository mutation: NONE;
- AFR index or ref mutation: NONE;
- provider access: NONE;
- operational-evidence ingestion: NONE;
- runtime evaluation execution: NONE;
- NEXUS repository mutation: NONE;
- Phase 12 authority: NONE.

## 15. Stop conditions

Stop planning if satisfying the trust boundary would require:

- executable runtime behavior;
- live provider or evidence access;
- an unapproved seventh planning document;
- NEXUS mutation or qualified-anchor rebind;
- Phase 12 finding or certificate authority;
- silent weakening of Phase 10 admissibility;
- silent change to canonical evaluation semantics.
