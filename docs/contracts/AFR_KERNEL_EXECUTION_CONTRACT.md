# AFR Kernel Execution Contract

## 1. Purpose

This document defines the conceptual execution contract for the AFR
deterministic conformance kernel.

It defines required inputs, gates, stage obligations, outcomes, failures,
fingerprint requirements, and result guarantees.

It is not an executable schema, API, algorithm, test specification, runtime
implementation, or implementation authority.

## 2. Contract Principle

A kernel evaluation is valid only when every mandatory authority, identity,
scope, compatibility, evidence, rule, and determinism condition is resolved.

The kernel may assert only what approved truth, eligible evidence, governing
semantics, and the declared time boundary jointly support.

## 3. Contract Versioning

Every invocation identifies compatible versions for:

- this conceptual contract;
- the canonical information model;
- evaluation semantics;
- truth representation;
- claim representation;
- evidence representation;
- eligibility policy;
- evaluation definition;
- conformance policy;
- evaluator behavior;
- canonicalization;
- fingerprint construction.

Missing, ambiguous, or unsupported material versions fail closed.

## 4. Invocation Identity

Each evaluation invocation has one immutable identity bound to:

- one tenant;
- one subject and system;
- one requested evaluation scope;
- one truth snapshot;
- one claim set;
- one evidence-candidate set;
- one trusted-time context;
- one governing version set.

Material input changes require a new invocation identity.

## 5. Required Conceptual Inputs

A valid invocation requires:

### Authority Context

- architecture-authority identity;
- truth-snapshot identity;
- approval state;
- integrity identity;
- supersession state;
- truth-contract version.

### Scope Context

- tenant identity;
- subject identity;
- system identity;
- environment identity when applicable;
- release identity when applicable;
- evaluation scope;
- requested validity boundary.

### Claim Context

- claim identity;
- claim version;
- truth-snapshot reference;
- required evidence expectations;
- evaluation-definition reference;
- materiality and scope.

### Evidence Context

- evidence-candidate identities;
- observation-source identities;
- collector identities;
- provenance;
- integrity information;
- observation and collection times;
- freshness constraints;
- environment and release bindings.

### Evaluation Context

- evaluation-definition identity and version;
- policy identity and version;
- evaluator identity and version;
- trusted-time context;
- canonicalization version;
- fingerprint version.

## 6. Optional Inputs

Optional inputs may include:

- non-authoritative labels;
- presentation metadata;
- human-readable descriptions;
- correlation references;
- downstream routing hints.

Optional inputs cannot affect authoritative outcomes unless the approved
contract explicitly classifies them as deterministic material inputs.

## 7. Invocation Preconditions

Before evaluation begins:

1. every required input is present;
2. every identity is syntactically and semantically resolvable;
3. one tenant context is established;
4. subject and system scope are unambiguous;
5. the truth snapshot is immutable and approved;
6. material versions are compatible;
7. trusted-time context is resolved;
8. canonicalization rules are identified.

Failure of a precondition blocks claim evaluation.

## 8. Truth Validation Contract

Truth validation must return one conceptual decision:

- `TRUTH_ELIGIBLE`;
- `TRUTH_INELIGIBLE`;
- `TRUTH_UNRESOLVED`.

`TRUTH_ELIGIBLE` requires resolved authority, approval, integrity, scope,
version compatibility, and supersession state.

Neither syntactic validity nor source proximity establishes authority.

Only `TRUTH_ELIGIBLE` may proceed to claim evaluation.

## 9. Scope Binding Contract

All material inputs must agree on:

- tenant;
- subject;
- system;
- environment;
- release;
- claim scope;
- evidence scope;
- evaluation scope;
- applicable time boundary.

A cross-tenant input is rejected.

An unresolved or contradictory material scope blocks authoritative evaluation.

## 10. Evidence Eligibility Contract

Each evidence candidate receives exactly one eligibility decision:

- `ELIGIBLE`;
- `INELIGIBLE`;
- `UNRESOLVED`;
- `STALE`.

Each decision records deterministic reason codes and the governing eligibility
policy version.

Eligibility must consider identity, provenance, integrity, scope, freshness,
compatibility, duplication, replay, and contradiction state.

Only `ELIGIBLE` evidence may support `CONFORMANT`.

Material rejected evidence remains traceable.

## 11. Rule Resolution Contract

Each claim must resolve to exactly one compatible approved deterministic rule.

Rule resolution binds:

- claim identity and version;
- evaluation-definition identity and version;
- policy identity and version;
- evaluator version;
- rule identity and version.

Zero or multiple authoritative rule matches cannot be resolved by inference or
implicit fallback.

## 12. Claim Evaluation Contract

For every evaluated claim, the kernel must record:

- the claim and truth references;
- the resolved rule;
- eligible evidence;
- material rejected evidence;
- contradictions;
- governing versions;
- trusted-time context;
- derived outcome;
- outcome reasons;
- limitations.

Each claim produces exactly one canonical outcome.

## 13. Outcome Preconditions

### CONFORMANT

Requires all mandatory eligible supporting evidence, valid scope and
freshness, and no unresolved material contradiction.

### NON_CONFORMANT

Requires eligible evidence showing that a mandatory claim condition is not
satisfied.

### INCONCLUSIVE

Applies when material truth, scope, evidence, identity, integrity,
compatibility, rule, or evaluation semantics are insufficient, ambiguous, or
conflicting.

### STALE

Applies when required evidence or a prior result exceeds its authorized
freshness or validity boundary.

No outcome may be silently substituted for another.

## 14. Aggregate Contract

Aggregation consumes the complete ordered claim-result set.

It must:

- retain every claim result;
- preserve every material weaker outcome;
- apply only an approved precedence version;
- preserve limitations;
- remain within the evaluated scope;
- reject unknown outcomes or incompatible result versions.

An aggregate cannot be stronger than its material dependencies permit.

## 15. Canonicalization Contract

Canonicalization must define stable treatment of:

- record field ordering;
- collection ordering;
- duplicate identities;
- textual encoding;
- time representation;
- absent versus empty values;
- identifiers;
- version values;
- reason codes;
- limitations.

Canonicalization cannot infer missing material values.

Input arrival order cannot change authoritative results.

## 16. Fingerprint Contract

The fingerprint binds:

- invocation identity;
- authority and scope context;
- truth snapshot and claims;
- evidence candidates and eligibility decisions;
- resolved deterministic rules;
- claim and aggregate outcomes;
- material failures and limitations;
- trusted-time context;
- all governing versions;
- canonicalization version;
- fingerprint version.

The same canonical material inputs must produce the same fingerprint.

A materially different input must not reuse the prior fingerprint.

## 17. Result Contract

A completed result identifies:

- result and invocation identities;
- tenant and evaluated subject;
- truth snapshot and claims;
- evidence and eligibility decisions;
- claim outcomes;
- aggregate outcome;
- governing versions;
- fingerprint;
- evaluation time;
- validity boundary;
- limitations;
- unresolved conditions;
- derivation references.

A result is not a certificate, deployment authorization, or ATA decision.

## 18. Failure Contract

Failures are recorded separately from conformance outcomes.

Conceptual failure categories include:

- `INVALID_INVOCATION`;
- `UNRESOLVED_AUTHORITY`;
- `TENANT_MISMATCH`;
- `SCOPE_MISMATCH`;
- `INTEGRITY_FAILURE`;
- `UNSUPPORTED_VERSION`;
- `MISSING_RULE`;
- `AMBIGUOUS_RULE`;
- `CANONICALIZATION_FAILURE`;
- `FINGERPRINT_FAILURE`;
- `INTERNAL_INVARIANT_FAILURE`.

A failure cannot default to `CONFORMANT`.

## 19. Stage Postconditions

A stage may transition successfully only when:

- its required inputs were produced by approved earlier stages;
- its deterministic decision is recorded;
- governing versions are identified;
- material limitations are preserved;
- output scope does not exceed input scope;
- no earlier failure is bypassed.

## 20. Idempotency and Replay Semantics

An invocation is semantically repeatable only when all fingerprint-bound
inputs and versions are identical.

Replay must not:

- substitute evidence;
- change trusted time;
- select newer rules;
- change policy versions;
- omit prior contradictions;
- expand scope;
- reuse a result across tenants.

This section does not authorize replay execution or persistence.

## 21. Explanation Boundary

Explanations are projections of preserved deterministic decisions.

They cannot:

- add evidence;
- change eligibility;
- select rules;
- alter outcomes;
- rewrite limitations;
- mutate fingerprints;
- grant authority.

Model-generated explanation remains non-authoritative.

## 22. External-System Boundary

This contract defines no:

- NEXUS export;
- provider adapter;
- cloud collector;
- ATA integration;
- PAA integration;
- Humanize integration;
- API;
- queue;
- database;
- certificate;
- deployment control;
- remediation operation.

All external integrations require separate authority.

## 23. Conformance-to-Contract Evidence

A future implementation proposal must define how it would prove:

- deterministic stage ordering;
- complete gate enforcement;
- outcome preservation;
- canonicalization stability;
- fingerprint reproducibility;
- tenant isolation;
- failure separation;
- model containment;
- absence of authority elevation.

Phase 2 does not create those tests or implementations.

## 24. Phase 2 Authority

This conceptual contract is documentation-only.

It creates no authority for executable schemas, code, tests, APIs, evaluation
execution, integrations, persistence, certificates, deployment, production
access, remediation, or Phase 3.
