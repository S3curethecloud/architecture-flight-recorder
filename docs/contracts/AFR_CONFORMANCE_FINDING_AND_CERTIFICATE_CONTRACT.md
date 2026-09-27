# AFR Conformance Finding and Certificate Contract

## 1. Purpose

This contract defines deterministic Phase 6 planning requirements for
conformance findings and future certificate representations.

## 2. Contract Boundary

This is a planning contract.

It does not define executable schemas, persistence, signing code, keys,
network behavior, or runtime APIs.

## 3. Canonical Outcome Vocabulary

The only canonical conformance outcomes are:

- `CONFORMANT`;
- `NON_CONFORMANT`;
- `INCONCLUSIVE`;
- `STALE`.

Processing and delivery failures are not substitute conformance outcomes.

## 4. Completed-Evaluation Preconditions

A finding requires an accepted completed evaluation with all mandatory
authority and identity bindings.

Missing required input must fail closed.

## 5. Outcome Non-Recomputation Rule

`finding.outcome` must preserve the applicable completed evaluation result.

Phase 6 cannot derive a more favorable outcome.

## 6. Required Finding Bindings

A finding must bind, as applicable:

- finding identity;
- evaluation identity;
- result or claim identity;
- authoritative claim reference;
- outcome;
- deterministic rationale;
- tenant;
- subject;
- environment;
- release;
- deployment;
- scope;
- evaluation time;
- finding time;
- validity deadline;
- evaluation fingerprint;
- finding representation version;
- provenance.

## 7. Finding Identity Rules

Finding identity must be deterministic under the approved identity contract.

Two semantically distinct bounded findings must not silently share identity.

Historical identity is immutable.

## 8. Claim Rules

Claim-level findings must preserve authoritative claim references.

A finding cannot add a claim that was not within the accepted evaluation.

## 9. Evidence Rules

Supporting and contradicting evidence references must remain traceable to the
source evaluation.

Evidence cannot be fabricated, silently omitted, or substituted to change the
result.

## 10. Gap and Contradiction Rules

Evidence gaps and unresolved contradictions remain explicit.

A required gap cannot be represented as successful evidence.

## 11. Limitation Rules

Recorded limitations must survive finding and certificate representation.

Downstream representation cannot narrow away a limitation that materially
affects interpretation.

## 12. Drift and Staleness Rules

Drift remains bound to authoritative claim and evaluated context.

`STALE` cannot be converted to current `CONFORMANT`.

## 13. Tenant and Scope Rules

Exact tenant, subject, environment, release, deployment, and evaluated scope
must be preserved.

Cross-context reuse fails closed.

## 14. Temporal Rules

The contract distinguishes:

- evaluation time;
- finding time;
- validity deadline;
- applicability interval;
- expiry;
- supersession;
- future revocation effective time.

## 15. Certificate Eligibility Rules

Certificate eligibility requires an approved deterministic policy decision.

A model cannot provide the authoritative decision.

Eligibility cannot exceed the evaluation's claims, evidence, result, scope,
validity, or limitations.

## 16. Certificate Representation Bindings

A future representation may bind:

- certificate identity;
- representation version;
- evaluation identity;
- result references;
- claim references;
- tenant and subject;
- environment, release, deployment, and scope;
- truth-snapshot references;
- evidence-set fingerprint;
- evaluation fingerprint;
- policy and evaluator versions;
- canonicalization and fingerprint versions;
- evaluation time;
- applicability interval;
- validity deadline;
- limitations;
- supersession state;
- future issuer identity;
- future integrity metadata;
- expiry;
- future revocation relationship;
- verification version;
- provenance.

## 17. Integrity Metadata Rules

Integrity metadata establishes representation integrity and future issuer
attribution only.

It cannot create conformance, architecture approval, deployment authority, or
runtime authority.

## 18. Evaluator, Issuer, Verifier, and Consumer Separation

Evaluation authority, future issuance authority, verification authority, and
consumer authority must remain distinct.

## 19. Expiry, Supersession, and Future Revocation Rules

Expiry does not delete history.

Supersession preserves predecessor and successor identities.

Future revocation does not rewrite evaluation truth.

## 20. Replay Rules

A finding or future certificate representation must not be accepted outside
its bound tenant, subject, environment, release, deployment, scope, validity,
or identity context.

## 21. Model-Exclusion Rules

A model must not authoritatively:

- determine outcome;
- determine eligibility;
- fabricate evidence;
- suppress evidence;
- repair missing evidence;
- widen scope;
- substitute authoritative fingerprints;
- grant authority.

## 22. Fail-Closed Rules

The following conditions fail closed:

- missing mandatory identity;
- invalid authority binding;
- missing required evidence;
- unresolved mandatory contradiction;
- expired or stale applicability;
- cross-tenant use;
- cross-subject use;
- cross-environment or cross-release use;
- scope expansion;
- invalid integrity binding.

Fail-closed handling cannot yield current `CONFORMANT`.

## 23. Provider Neutrality

Phase 6 planning is provider neutral.

No provider-specific representation, cryptographic service, KMS, HSM, PKI, or
storage technology is normative.

## 24. Authority and Phase Separation

The contract creates no NEXUS, ARCP, ATA, PAA, Humanize, provider, delivery,
runtime, or deployment authority.

## 25. Prohibited Effects and Stop Conditions

Implementation, persistence, certificate generation, signing, issuance,
revocation execution, keys, credentials, network, integration, runtime,
deployment, enforcement, remediation, and production activity require separate
authority.

## 26. Authority State

`AFR_PHASE_6_PLANNING_AUTHORITY =
BOUNDED_CONFORMANCE_FINDINGS_AND_CERTIFICATE_BOUNDARY_PLANNING_ONLY`

`IMPLEMENTATION_AUTHORITY = NONE`

`PERSISTENCE_AUTHORITY = NONE`

`CERTIFICATE_GENERATION_AUTHORITY = NONE`

`CERTIFICATE_SIGNING_AUTHORITY = NONE`

`CERTIFICATE_ISSUANCE_AUTHORITY = NONE`

`KEY_GENERATION_AUTHORITY = NONE`

`RUNTIME_AUTHORITY = NONE`
