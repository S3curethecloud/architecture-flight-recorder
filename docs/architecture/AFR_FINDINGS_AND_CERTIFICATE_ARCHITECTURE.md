# AFR Findings and Certificate Architecture

## 1. Purpose

This document defines the Phase 6 architecture boundary for immutable
conformance findings and future integrity-bound certificate representations.

## 2. Canonical Context

AFR evaluates conformance against authoritative architecture truth and accepted
operational evidence.

NEXUS remains authoritative for approved architecture truth where applicable.

Phase 6 begins only after deterministic AFR evaluation is complete.

## 3. Architectural Boundary

The boundary is:

```text
COMPLETED_DETERMINISTIC_EVALUATION_RESULT
    -> FINDINGS_AND_CERTIFICATE_BOUNDARY
    -> IMMUTABLE_CONFORMANCE_FINDING
    -> FUTURE_INTEGRITY_BOUND_CERTIFICATE_REPRESENTATION
    -> FUTURE_SEPARATELY_AUTHORIZED_DELIVERY_AND_INTEGRATION
```

Phase 6 owns planning semantics only for the middle boundary.

## 4. Conceptual Responsibilities

The boundary plans for:

- immutable findings;
- evaluation lineage;
- architecture-claim lineage;
- canonical outcome preservation;
- evidence gaps and contradictions;
- limitations;
- drift and staleness;
- validity;
- certificate eligibility boundaries;
- integrity-bound representation;
- expiry and supersession;
- future revocation relationships;
- audit provenance.

## 5. Completed-Evaluation Input

The architecture consumes only accepted completed-evaluation semantics.

It cannot invoke the evaluator to obtain a more favorable result.

It cannot repair missing evidence or missing authority.

## 6. Finding Plane

The conceptual finding plane transforms an accepted completed result into a
bounded immutable finding representation.

The transformation is representational, not a reevaluation.

## 7. Finding Identity

Finding identity must be bound to:

- source evaluation identity;
- applicable result or claim identity;
- tenant;
- subject;
- context and scope;
- time;
- finding representation version.

Identity semantics must prevent silent replacement.

## 8. Outcome Preservation

The finding plane preserves:

- `CONFORMANT`;
- `NON_CONFORMANT`;
- `INCONCLUSIVE`;
- `STALE`.

A finding cannot alter the source outcome.

## 9. Claim and Evidence Lineage

A finding preserves references to authoritative claims and applicable support
or contradiction evidence.

Phase 6 does not originate architecture claims.

## 10. Gaps, Contradictions, and Limitations

Evidence gaps, contradictions, and limitations are first-class preserved
semantics.

They must not disappear during finding or certificate representation.

## 11. Drift and Staleness

Drift is a bounded result related to an authoritative claim and evaluated
context.

Staleness indicates that applicability or validity no longer supports a current
conformance assertion.

Neither grants remediation authority.

## 12. Scope Model

The architecture preserves exact:

- tenant;
- subject;
- environment;
- release;
- deployment;
- evaluated scope.

Scope widening is prohibited.

## 13. Temporal Model

The architecture distinguishes evaluation, finding, applicability, expiry,
supersession, and future revocation times.

Historical objects remain immutable.

## 14. Certificate Eligibility Boundary

Eligibility is a policy-governed deterministic decision outside model
authority.

Certificate representation is permitted only within the bounded source
evaluation.

## 15. Certificate Representation

A future certificate representation is a bounded integrity-bearing envelope
over accepted evaluation semantics.

It is not a new evaluation.

It is not an architecture approval.

It is not execution authority.

## 16. Integrity Boundary

Integrity metadata may establish that the representation has not been altered
and may identify a future issuer.

Phase 6 does not choose cryptography or infrastructure.

## 17. Authority Separation

The architecture separates:

- architecture authority;
- evaluator;
- finding constructor;
- future issuer;
- future verifier;
- consumer;
- human reviewer;
- ATA runtime authority.

No class inherits another authority domain.

## 18. Expiry, Supersession, and Future Revocation

Expiry terminates applicability without deleting history.

Supersession links predecessor and successor objects.

Future revocation affects certificate usability but does not rewrite the
underlying evaluation.

## 19. Replay and Reuse Boundary

Representation reuse must fail outside the exact tenant, subject, environment,
release, deployment, scope, validity interval, and identity binding.

## 20. Model Boundary

A model is not an authoritative component for:

- outcome determination;
- eligibility determination;
- evidence acceptance;
- integrity calculation;
- authority grants.

## 21. NEXUS Boundary

NEXUS remains the architecture-truth authority.

Phase 6 may preserve references already bound into completed AFR evaluation
results.

It cannot create or mutate NEXUS truth.

## 22. Downstream Boundary

Delivery and Integration remains deferred.

Phase 6 defines no downstream API, event, queue, webhook, feed, gateway, or
consumer mutation behavior.

## 23. Security and Audit Boundary

The architecture must preserve:

- lineage;
- integrity;
- tenant isolation;
- limitation preservation;
- replay resistance;
- issuer attribution;
- audit provenance;
- immutable historical truth.

## 24. Failure Safety

Missing mandatory identity, invalid authority, incomplete binding, expired
validity, cross-context reuse, or unresolved required evidence must fail
closed.

Failure cannot silently produce a current `CONFORMANT` certificate
representation.

## 25. Prohibited Effects and Stop Conditions

The architecture creates no authority for implementation, persistence,
cryptography selection, signing, issuance, keys, network, providers,
integrations, runtime, deployment, enforcement, or remediation.

Any need for those capabilities requires a new separately governed authority.

## 26. Authority State

`AFR_PHASE_6_PLANNING_AUTHORITY =
BOUNDED_CONFORMANCE_FINDINGS_AND_CERTIFICATE_BOUNDARY_PLANNING_ONLY`

`IMPLEMENTATION_AUTHORITY = NONE`

`CERTIFICATE_GENERATION_AUTHORITY = NONE`

`CERTIFICATE_SIGNING_AUTHORITY = NONE`

`CERTIFICATE_ISSUANCE_AUTHORITY = NONE`

`RUNTIME_AUTHORITY = NONE`
