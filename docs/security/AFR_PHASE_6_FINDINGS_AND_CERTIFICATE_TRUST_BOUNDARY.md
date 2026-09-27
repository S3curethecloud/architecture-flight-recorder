# AFR Phase 6 Findings and Certificate Trust Boundary

## 1. Purpose

This document defines the Phase 6 trust boundary for immutable findings and
future certificate representations.

## 2. Trust Posture

Completed evaluation output is authoritative only within its accepted AFR
authority and identity boundary.

Phase 6 is fail closed.

No certificate representation may expand trust beyond its source evaluation.

## 3. Boundary Position

```text
COMPLETED_DETERMINISTIC_EVALUATION
    -> FINDING_BOUNDARY
    -> FUTURE_CERTIFICATE_REPRESENTATION
    -> FUTURE_DELIVERY_AND_INTEGRATION
```

Only planning for the finding and certificate-representation boundary is
authorized.

## 4. Protected Assets

Protected assets include:

- evaluation identity;
- authoritative claim references;
- canonical outcomes;
- evidence references;
- evidence gaps;
- contradictions;
- limitations;
- tenant and subject bindings;
- environment and release bindings;
- evaluated scope;
- time and validity;
- fingerprints;
- finding identity;
- future certificate identity;
- provenance.

## 5. Trust Inputs

Trust inputs must originate from accepted completed AFR evaluation semantics.

Unbound external assertions are not authoritative inputs.

## 6. Threat Actors and Conditions

Planning must account for:

- accidental scope widening;
- malicious evidence substitution;
- stale-result reuse;
- cross-tenant replay;
- cross-subject replay;
- forged issuer attribution;
- limitation stripping;
- evidence-gap suppression;
- outcome substitution;
- model hallucination;
- downstream authority escalation.

## 7. Completed-Result Authenticity

A finding requires binding to an accepted completed evaluation identity and
integrity context.

Unverifiable or incomplete provenance fails closed.

## 8. Tenant and Subject Isolation

Tenant and subject boundaries must be explicit.

Cross-tenant or cross-subject reuse is prohibited.

## 9. Scope Non-Expansion

Environment, release, deployment, evaluated scope, and applicability must not
be widened in a finding or certificate representation.

## 10. Outcome Integrity

A finding cannot alter the source evaluation outcome.

Required-input failure, contradiction, or staleness cannot be hidden to obtain
`CONFORMANT`.

## 11. Evidence, Gap, and Limitation Integrity

Evidence support, contradiction, gap, and limitation semantics must survive
all Phase 6 representations.

## 12. Temporal Trust

Validity and freshness are trust properties.

Expired or stale representations must not be interpreted as current
conformance.

## 13. Finding Immutability

Historical findings are immutable.

Corrections require new identities and explicit provenance.

## 14. Certificate-Representation Integrity

A future certificate representation must be integrity bound to its underlying
evaluation and finding semantics.

Integrity cannot add semantic authority.

## 15. Issuer Attribution

A future issuer identity must be explicit and separable from evaluator,
verifier, and consumer identity.

Issuer attribution does not establish universal architecture correctness.

## 16. Evaluator-Issuer-Verifier-Consumer Separation

No identity class may inherit another class's authority solely because it
possesses or processes a finding or certificate.

## 17. Key, PKI, KMS, and HSM Boundary

Phase 6 does not select or create:

- signing keys;
- verification keys;
- PKI;
- trust anchors;
- KMS resources;
- HSM resources;
- key hierarchies;
- rotation mechanisms.

Those require future authority.

## 18. Replay Resistance

A finding or representation must be rejected when replayed outside its bound
tenant, subject, environment, release, deployment, scope, identity, or
validity interval.

## 19. Cross-Context Safety

Cross-tenant, cross-subject, cross-environment, cross-release, and cross-scope
reuse must fail closed.

## 20. Model Safety

A model is untrusted for authoritative outcome, eligibility, evidence,
fingerprint, or authority decisions.

Model output must never silently replace deterministic AFR truth.

## 21. NEXUS Boundary

NEXUS remains authoritative for approved architecture truth.

Phase 6 cannot mutate or originate NEXUS truth.

## 22. Downstream Boundary

Delivery and Integration remains deferred.

Downstream consumers cannot mutate authoritative AFR results.

## 23. Privacy and Audit

Planning must preserve minimum necessary exposure of sensitive evidence
references while retaining sufficient audit provenance.

Audit evidence must identify source evaluation, finding lineage, relevant
authority, and material transformations.

## 24. Abuse and Misuse Cases

Planning must explicitly reject:

- presenting stale conformance as current;
- deleting limitations;
- replacing `INCONCLUSIVE` with `CONFORMANT`;
- cross-tenant reuse;
- claim-set widening;
- issuer/evaluator authority conflation;
- treating signature validity as architecture correctness;
- using a certificate as deployment or runtime permission;
- model-generated evidence substitution.

## 25. Stop Conditions

Stop and request new authority if planning requires:

- persistence;
- live cryptography;
- actual signing or issuance;
- key operations;
- certificate verification infrastructure;
- provider integration;
- network access;
- implementation;
- delivery integration;
- runtime behavior;
- deployment;
- enforcement;
- remediation.

## 26. Review Evidence

Acceptance review must prove:

- exact six-document scope;
- canonical baseline;
- deterministic semantics;
- fail-closed behavior;
- tenant isolation;
- limitation preservation;
- model exclusion;
- NEXUS non-duplication;
- downstream non-drift;
- authority non-expansion.

## 27. Authority State

`AFR_PHASE_6_PLANNING_AUTHORITY =
BOUNDED_CONFORMANCE_FINDINGS_AND_CERTIFICATE_BOUNDARY_PLANNING_ONLY`

`IMPLEMENTATION_AUTHORITY = NONE`

`PERSISTENCE_AUTHORITY = NONE`

`CERTIFICATE_GENERATION_AUTHORITY = NONE`

`CERTIFICATE_SIGNING_AUTHORITY = NONE`

`CERTIFICATE_ISSUANCE_AUTHORITY = NONE`

`CERTIFICATE_REVOCATION_EXECUTION_AUTHORITY = NONE`

`KEY_GENERATION_AUTHORITY = NONE`

`KEY_CUSTODY_AUTHORITY = NONE`

`KMS_HSM_AUTHORITY = NONE`

`NETWORK_AUTHORITY = NONE`

`RUNTIME_AUTHORITY = NONE`

`DEPLOYMENT_AUTHORITY = NONE`
