# AFR Phase 2 Kernel Trust Boundary

## 1. Purpose

This document defines the trust boundaries, assets, threat conditions,
fail-closed requirements, and authority invariants for the planned AFR
deterministic conformance kernel.

It is a planning artifact. It does not implement controls, credentials,
integrations, persistence, runtime evaluation, or deployment.

## 2. Trust Objective

The kernel must ensure that no conformance assertion is stronger than the
approved truth, eligible evidence, deterministic semantics, and declared time
boundary jointly support.

Trust cannot be created by syntax, proximity, normalization, aggregation,
model inference, or presentation.

## 3. Protected Assets

Protected conceptual assets include:

- tenant and subject identities;
- architecture-authority identities;
- approved truth snapshots;
- architecture claims;
- observation and collector identities;
- evidence provenance and integrity;
- evidence-eligibility decisions;
- deterministic rules;
- policy and evaluator versions;
- trusted-time context;
- claim-level results;
- aggregate results;
- evaluation fingerprints;
- limitations and failure records;
- audit derivation records.

## 4. Trust Domains

The architecture separates these trust domains:

1. architecture authorities;
2. provider and enterprise observation sources;
3. evidence collectors;
4. evidence-trust and eligibility functions;
5. deterministic kernel stages;
6. result and audit consumers;
7. ATA and other enforcement systems;
8. tenants;
9. individual evaluation instances.

Authority does not transfer merely because data crosses a boundary.

## 5. Tenant Isolation Boundary

Every material input, intermediate decision, result, and fingerprint must bind
to one resolved tenant.

The kernel must reject:

- unresolved tenant identity;
- cross-tenant evidence;
- cross-tenant truth substitution;
- cross-tenant rule or policy substitution;
- cross-tenant result reuse;
- cross-tenant cache or replay assumptions;
- aggregate evaluation across tenants unless separately authorized.

Tenant identity cannot be inferred from a network, repository, or provider
location alone.

## 6. Subject and Scope Boundary

Every truth snapshot, claim, evidence record, rule, and result must be
compatible with the evaluated subject and scope.

The kernel must not infer missing subject, environment, release, region, or
time scope from nearby records.

Scope mismatch cannot produce `CONFORMANT`.

## 7. Architecture-Truth Authority Boundary

NEXUS remains authoritative for approved architecture truth in NEXUS-governed
systems.

The kernel cannot:

- author or approve truth;
- infer approval;
- supersede truth;
- repair missing semantics;
- reinterpret draft state as approved state;
- modify engagement or lifecycle state;
- treat provider observations as expected architecture.

A truth snapshot is not authoritative solely because it is well formed.

## 8. Observation and Evidence Boundary

Observations describe bounded operational state.

They become not automatically eligible evidence.

Eligibility requires deterministic validation of:

- source identity;
- collector identity;
- tenant and subject binding;
- provenance;
- integrity;
- observation and collection time;
- freshness;
- environment and release applicability;
- semantic compatibility;
- replay and duplication state;
- contradiction state.

Normalization cannot elevate evidence authority.

## 9. Source and Collector Identity

The observation source and evidence collector are separate identities.

The trust model must address:

- source impersonation;
- collector impersonation;
- confused-deputy collection;
- source-to-collector substitution;
- stale collector authorization;
- missing collection context;
- untrusted transformation before collection.

Unresolved identity makes the evidence ineligible.

## 10. Integrity Boundary

Integrity validation must cover all material authoritative inputs and outputs.

Threats include:

- content modification;
- identity substitution;
- reference substitution;
- truncation;
- field omission;
- version substitution;
- reordering that changes meaning;
- detached integrity values;
- result or fingerprint replacement.

An integrity failure cannot be downgraded to a warning supporting conformance.

## 11. Provenance Boundary

Provenance must enable the kernel to determine:

- where an observation originated;
- who or what collected it;
- which transformations occurred;
- which versions governed transformation;
- when observation and collection occurred;
- whether custody remained tenant-bound;
- whether material context was lost.

Incomplete material provenance cannot support `CONFORMANT`.

## 12. Trusted-Time and Freshness Boundary

The kernel must use declared trusted-time context rather than an undeclared
local clock.

The trust model distinguishes:

- observation time;
- collection time;
- evaluation time;
- evidence freshness window;
- truth validity window;
- result validity window.

Clock ambiguity, time rollback, or expired required evidence must fail closed.

## 13. Replay Boundary

Replay threats include reuse of:

- prior truth after supersession;
- stale evidence;
- evidence from another release;
- evidence from another environment;
- evidence from another tenant;
- prior eligibility decisions;
- prior results or fingerprints;
- older compatible-looking policy versions.

Replay detection and response must remain deterministic and traceable.

## 14. Version and Downgrade Boundary

Every material contract, policy, rule, evaluator, canonicalization, and
fingerprint version must be explicit and supported.

The kernel must reject:

- unknown versions;
- ambiguous versions;
- implicit latest versions;
- silent downgrade;
- nearest-compatible selection;
- mixed incompatible versions;
- unversioned semantic defaults.

## 15. Rule-Selection Boundary

Only an explicitly identified, approved, compatible deterministic rule may
govern a claim evaluation.

The trust model prohibits:

- model-selected rules;
- textual-similarity selection;
- tenant-crossing rule reuse;
- runtime rule mutation;
- fallback to a weaker rule;
- rule substitution after eligibility decisions;
- hidden or unversioned defaults.

## 16. Canonicalization Boundary

Canonicalization is security-sensitive because it determines identity and
fingerprint stability.

The design must prevent ambiguity in:

- field ordering;
- collection ordering;
- duplicate handling;
- text encoding;
- identifiers;
- time representation;
- absent and empty values;
- numeric representation;
- reason-code ordering;
- limitation ordering.

Two semantically different inputs must not become indistinguishable through
canonicalization.

## 17. Fingerprint Boundary

A fingerprint must bind every material deterministic input and governing
version.

Threats include:

- omitted material fields;
- algorithm downgrade;
- cross-tenant reuse;
- collision assumptions;
- canonicalization mismatch;
- partial recomputation;
- detached fingerprint substitution;
- reuse after trusted-time or policy changes.

A fingerprint proves evaluated identity, not correctness or authority to act.

## 18. Outcome Integrity Boundary

The kernel must prevent:

- conversion of `INCONCLUSIVE` to `CONFORMANT`;
- conversion of `STALE` to current conformance;
- suppression of `NON_CONFORMANT`;
- discarded contradictions;
- aggregate masking;
- unsupported manual override;
- model-selected outcomes;
- downstream mutation of authoritative results.

Every outcome remains traceable to preserved deterministic decisions.

## 19. Stage Isolation

Each evaluation invocation moves through the authorized kernel stages under
one immutable invocation identity.

Each stage accepts only outputs authorized by earlier stages.

A stage cannot:

- bypass a failed gate;
- repair authority;
- widen scope;
- change tenant;
- replace evidence;
- select a different version silently;
- discard a limitation;
- resume a blocked identity with changed inputs.

Material changes require a new evaluation identity.

## 20. Model Containment

Models are outside the authoritative evaluation path.

A model cannot determine:

- truth authority;
- tenant or scope binding;
- evidence eligibility;
- rule selection;
- claim or aggregate outcomes;
- fingerprint content;
- execution or deployment authority.

Model-generated explanation must be marked non-authoritative.

## 21. Consumer Boundary

Downstream consumers cannot mutate authoritative kernel outputs.

Consumers must not interpret a result as:

- architecture approval;
- security certification;
- regulatory approval;
- deployment authorization;
- execution authority;
- an ATA decision;
- permission to remediate;
- proof outside the evaluated scope or validity window.

## 22. ATA Boundary

ATA retains consequential runtime commit authority.

AFR cannot grant, expand, or bypass ATA authority.

Any future use of AFR results by ATA requires a separate, governed integration
contract and activation.

## 23. Audit Boundary

Audit projections may explain preserved decisions but cannot become
authoritative records by presentation alone.

Audit output must preserve:

- tenant and subject scope;
- authoritative references;
- eligibility decisions;
- rule and version identities;
- outcomes;
- limitations;
- fingerprint identity;
- non-authoritative presentation status.

## 24. Failure Confidentiality

Failure and diagnostic information must not leak:

- cross-tenant identifiers;
- evidence content outside authorized scope;
- provider credentials;
- hidden architecture content;
- internal rule content beyond authorization;
- sensitive provenance;
- other evaluations.

Fail-closed behavior must not become a data-disclosure channel.

## 25. Threat Conditions

The planned trust boundary explicitly addresses:

- tenant substitution;
- subject substitution;
- truth forgery or supersession ambiguity;
- source and collector impersonation;
- evidence tampering;
- evidence replay;
- evidence omission;
- contradiction suppression;
- time rollback;
- stale-evidence reuse;
- semantic-version downgrade;
- rule substitution;
- canonicalization ambiguity;
- fingerprint substitution;
- aggregate masking;
- model authority escalation;
- downstream result mutation;
- explanation-layer confusion;
- cross-evaluation leakage.

## 26. Fail-Closed Requirements

The kernel cannot produce `CONFORMANT` when any material requirement has:

- unresolved identity;
- unresolved authority;
- tenant mismatch;
- scope ambiguity;
- integrity failure;
- incomplete provenance;
- unsupported version;
- stale required evidence;
- ambiguous rule selection;
- unresolved material contradiction;
- canonicalization failure;
- fingerprint failure;
- internal invariant failure.

Fail-closed does not mean every unknown condition becomes
`NON_CONFORMANT`; `INCONCLUSIVE`, `STALE`, or a distinct blocked failure must
be used as defined.

## 27. Required Future Assurance

A future implementation proposal must explain how it would validate:

- tenant isolation;
- deterministic gate ordering;
- integrity and provenance;
- trusted time and freshness;
- replay resistance;
- downgrade resistance;
- rule immutability;
- canonicalization stability;
- fingerprint reproducibility;
- outcome integrity;
- model containment;
- consumer authority separation.

No implementation or testing is authorized by this requirement.

## 28. Phase 2 Authority

This trust-boundary document is planning-only.

It creates no authority for controls, credentials, executable schemas, code,
tests, integrations, live evidence collection, evaluation execution,
persistence, certificates, deployment, production access, remediation, or
Phase 3.
