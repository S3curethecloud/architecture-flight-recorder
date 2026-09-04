# AFR Evaluation Semantics

## 1. Purpose

This document defines the normative deterministic semantics by which
Architecture Flight Recorder evaluates approved architecture claims against
eligible operational evidence.

It defines planning semantics only. It is not an algorithm implementation,
policy engine, executable rule set, schema, API, or runtime authorization.

## 2. Evaluation Principle

AFR may assert only what the following can jointly support:

- an approved immutable architecture-truth snapshot;
- identified architecture claims;
- an eligible evidence set;
- an approved evaluation definition;
- an identified policy version;
- an identified evaluator version;
- a resolved evaluation context;
- trusted time semantics.

No input class may substitute for another.

## 3. Canonical Outcomes

Every evaluated claim must resolve to exactly one canonical outcome:

- `CONFORMANT`;
- `NON_CONFORMANT`;
- `INCONCLUSIVE`;
- `STALE`.

The outcome must remain accompanied by all material evidence gaps,
contradictions, limitations, and eligibility decisions.

An outcome label alone is not an authoritative result.

## 4. Deterministic Evaluation Identity

One evaluation is uniquely bounded by:

- tenant;
- subject;
- environment;
- release or deployment when applicable;
- truth-snapshot identity and fingerprint;
- evaluated claim identities;
- evidence-set identity and fingerprint;
- evaluation-definition identity and version;
- policy version;
- evaluator version;
- evaluation time;
- trusted-time inputs;
- contract compatibility versions.

A change to any material input requires a distinct evaluation and fingerprint.

## 5. Required Evaluation Sequence

The normative evaluation sequence is:

1. resolve tenant and subject context;
2. validate architecture-truth authority;
3. validate claim applicability and scope;
4. validate contract and version compatibility;
5. identify candidate observations;
6. evaluate observation eligibility;
7. construct the immutable eligible evidence set;
8. record gaps, partial collection, and contradictions;
9. evaluate claim support and contradiction;
10. select the claim-level outcome;
11. record deterministic rationale and limitations;
12. calculate the evaluation fingerprint;
13. apply aggregation semantics when requested;
14. preserve the immutable result and provenance direction.

Later steps cannot repair a failure in an earlier authority or identity gate.

## 6. Truth-Authority Gate

Before claim evaluation, AFR must establish:

- recognized architecture authority;
- resolved tenant and engagement scope;
- immutable truth-snapshot identity;
- supported snapshot version;
- approved lifecycle state;
- verifiable integrity;
- unambiguous supersession state;
- stable claim references;
- applicable subject and environment scope.

Failure to establish truth authority produces `INCONCLUSIVE`.

An unapproved, draft, mutable, unsupported, or unverifiable truth snapshot
cannot produce `CONFORMANT` or `NON_CONFORMANT` because the approved expectation
has not been established.

AFR cannot reconstruct missing authoritative meaning through inference.

## 7. Claim-Applicability Gate

A claim participates only when its declared applicability includes the
evaluation context.

Applicability must resolve:

- tenant;
- subject;
- environment;
- release or deployment;
- effective time;
- supersession state;
- declared conditional scope.

An inapplicable claim is excluded with an explicit reason. It must not be
reported as conformant.

Ambiguous applicability produces `INCONCLUSIVE` when the claim is required for
the requested evaluation scope.

## 8. Compatibility Gate

AFR must establish compatibility among:

- truth contract version;
- claim semantics;
- evidence contract version;
- evaluation-definition version;
- policy version;
- evaluator version;
- normalization versions.

Unsupported or ambiguous material compatibility produces `INCONCLUSIVE`.

Compatibility cannot be guessed from similar field names or model inference.

## 9. Candidate Observation Selection

Candidate observations must be selected using declared deterministic scope
rules.

Selection must preserve:

- requested sources;
- returned sources;
- collection completeness;
- tenant and subject binding;
- environment and release scope;
- observation and collection time;
- source and collector identities;
- raw observation fingerprint.

Unselected or unavailable sources required by the evaluation definition become
explicit evidence gaps.

## 10. Evidence Eligibility

An observation is `ELIGIBLE` only when all required eligibility dimensions
pass:

- tenant match;
- subject match;
- source identity;
- collector identity;
- collection authorization;
- provenance;
- integrity;
- requested and returned scope;
- freshness;
- contract compatibility;
- normalization lineage;
- source-specific trust requirements.

An observation that fails a required dimension cannot support `CONFORMANT`.

Eligibility outcomes are:

### ELIGIBLE

All required trust and scope conditions pass for the evaluation context.

### INELIGIBLE

One or more required conditions fail conclusively.

### PARTIAL

The observation is attributable and valid for only part of the required scope.

### UNVERIFIABLE

Required identity, provenance, integrity, or collection semantics cannot be
established.

### STALE

The observation exceeds its authorized freshness boundary.

Only `ELIGIBLE` evidence may positively support a claim.

An approved evaluation definition may use an eligible partial-scope fragment
only when that fragment is explicitly bounded and cannot be mistaken for
complete coverage.

## 11. Evidence Freshness

Freshness is determined by an approved rule using relevant time semantics,
which may include:

- source observation time;
- collection time;
- ingestion time;
- evaluation time;
- source validity interval;
- allowed collection age;
- allowed observation age.

A recent ingestion timestamp cannot make an old observation current.

Unknown required time semantics prevent positive eligibility.

Evidence that crosses its freshness deadline becomes `STALE`; previous
conformance does not remain current merely because no newer evidence exists.

## 12. Evidence Completeness

Completeness is evaluated against the evidence dependencies declared by the
evaluation definition.

Completeness states are:

- `COMPLETE`;
- `PARTIAL`;
- `MISSING`;
- `UNVERIFIABLE`;
- `CONFLICTING`.

`COMPLETE` requires every mandatory evidence dependency to be satisfied within
its required scope and freshness boundary.

Optional evidence cannot compensate for missing mandatory evidence unless the
approved evaluation definition explicitly defines an equivalent evidence path.

## 13. Support Semantics

Evidence supports a claim only when an identified evaluation rule establishes
that the eligible observation satisfies the claim’s normative condition.

Support must be:

- claim-specific;
- scope-matched;
- time-valid;
- attributable;
- reproducible;
- traceable to exact evidence;
- produced by a versioned evaluation definition.

Similarity, plausibility, absence of alerts, or model confidence is not
deterministic support.

## 14. Contradiction Semantics

Evidence contradicts a claim when an identified deterministic rule establishes
that eligible observed state violates the claim’s normative condition.

Every material contradiction must preserve:

- claim reference;
- contradicting evidence;
- evaluated rule;
- scope;
- time;
- materiality;
- unresolved status;
- effect on the outcome.

Supporting evidence cannot silently cancel material contradictory evidence.

When eligible evidence independently establishes violation, missing additional
evidence does not hide that violation; the claim remains `NON_CONFORMANT` with
all evidence gaps recorded.

## 15. Missing Evidence Semantics

Missing evidence means AFR lacks an eligible observation required to decide the
claim.

Missing evidence is not:

- evidence of conformance;
- automatically evidence of violation;
- permission to infer expected state;
- permission to reuse evidence from another tenant or scope.

Missing required evidence normally produces `INCONCLUSIVE`.

When the required evidence existed previously but has exceeded its authorized
freshness boundary, the outcome is `STALE`.

## 16. CONFORMANT

A claim is `CONFORMANT` only when:

- truth authority is valid;
- claim applicability is resolved;
- all material versions are compatible;
- every mandatory evidence dependency is satisfied;
- all supporting evidence is eligible and current;
- deterministic support rules pass;
- no unresolved eligible material contradiction exists;
- tenant, subject, environment, release, and time scope match;
- the result’s limitations do not invalidate the assertion.

`CONFORMANT` applies only to the declared evaluated scope and validity window.

It is not proof of architecture correctness, regulatory compliance, future
behavior, deployment authorization, or runtime authority.

## 17. NON_CONFORMANT

A claim is `NON_CONFORMANT` when eligible evidence deterministically
establishes that a required architecture condition is not satisfied.

`NON_CONFORMANT` requires:

- valid truth authority;
- resolved claim applicability;
- attributable eligible contradictory evidence;
- an identified contradiction rule;
- sufficient scope to establish the violation.

All missing evidence, limitations, and additional contradictions remain
visible.

## 18. INCONCLUSIVE

A claim is `INCONCLUSIVE` when AFR cannot establish either conformance or
non-conformance because material decision inputs are:

- missing;
- ambiguous;
- unverifiable;
- incompatible;
- partially scoped;
- conflicting without deterministic resolution;
- bound to unresolved authority, tenant, subject, or release context.

`INCONCLUSIVE` must never be presented as a weak form of conformance.

## 19. STALE

A claim is `STALE` when evidence that would otherwise be required to support a
current assertion has exceeded its authorized freshness window.

`STALE` means no current conformance assertion is permitted.

If current eligible evidence independently establishes a violation, the claim
is `NON_CONFORMANT`, while stale evidence remains recorded as a limitation.

## 20. Claim-Level Outcome Precedence

After truth, applicability, and compatibility gates pass, outcome selection
uses this precedence:

1. independently established material violation produces `NON_CONFORMANT`;
2. expired mandatory evidence without current decisive contradiction produces
   `STALE`;
3. missing, ambiguous, partial, unverifiable, or unresolved conflicting inputs
   produce `INCONCLUSIVE`;
4. only complete eligible support without material contradiction produces
   `CONFORMANT`.

The precedence cannot be reordered by presentation logic or model output.

## 21. Aggregate Evaluation

An aggregate result must be computed only through an approved, versioned
aggregation policy.

The policy must identify:

- included claims;
- required claims;
- critical claims;
- claim weights if any;
- minimum coverage;
- handling of each canonical outcome;
- treatment of gaps and contradictions;
- aggregate validity window;
- certificate eligibility constraints.

No simple majority rule may produce aggregate `CONFORMANT` when a required or
critical claim has a weaker unresolved outcome.

## 22. Aggregate Outcome Constraints

Unless a stricter approved policy applies:

1. any required or critical `NON_CONFORMANT` result makes the aggregate
   `NON_CONFORMANT`;
2. otherwise, any required or critical `STALE` result makes the aggregate
   `STALE`;
3. otherwise, any required or critical `INCONCLUSIVE` result makes the
   aggregate `INCONCLUSIVE`;
4. aggregate `CONFORMANT` requires all required and critical claims to be
   `CONFORMANT` and required coverage to be complete.

Non-required claims and weighting cannot conceal required weaker outcomes.

Every aggregate result must expose the complete claim-outcome distribution.

## 23. Deterministic Rationale

Every result must provide a deterministic rationale identifying:

- evaluated claim;
- applicable rule;
- decisive inputs;
- supporting evidence;
- contradicting evidence;
- gaps;
- eligibility failures;
- outcome-selection rule;
- limitations;
- validity window.

Human-readable explanation may supplement this rationale but cannot replace or
alter it.

## 24. Fingerprint Semantics

The evaluation fingerprint must integrity-bind every material deterministic
input identified by the canonical information model.

The same canonicalized material inputs must produce the same fingerprint and
outcome.

A different material input must not reuse the prior evaluation identity.

Phase 1 does not choose a canonical serialization or cryptographic algorithm.

## 25. Re-evaluation and Supersession

New evidence, a new truth snapshot, a new policy, a new evaluation definition,
a new evaluator version, or a changed evaluation context requires a new
evaluation.

A new result may supersede an older result but cannot mutate it.

Supersession must preserve:

- prior result identity;
- new result identity;
- reason;
- effective time;
- provenance direction.

## 26. Model Boundary

A model may later assist with non-authoritative explanation or review
preparation.

A model cannot:

- establish truth authority;
- determine evidence eligibility;
- create missing evidence;
- suppress contradictions;
- select claim or aggregate outcomes;
- calculate authoritative fingerprints;
- grant certificate, deployment, or runtime authority.

Model confidence is not evidence confidence or conformance authority.

## 27. Failure Semantics

Failures remain explicit.

Examples include:

- truth validation failure;
- source or collector identity failure;
- integrity failure;
- collection failure;
- partial collection;
- tenant or subject mismatch;
- version incompatibility;
- missing evaluation definition;
- trusted-time failure;
- downstream delivery failure.

A failure affecting required evaluation inputs cannot produce `CONFORMANT`.

A downstream delivery failure does not retroactively change an immutable
evaluation outcome, but it must remain observable.

## 28. Certificate Boundary

A future certificate may represent a completed bounded evaluation.

Certificate eligibility requires an approved policy and cannot exceed:

- evaluated claims;
- evidence scope;
- result scope;
- validity window;
- recorded limitations.

A certificate is never execution authority, deployment authority, or an ATA
authorization.

Phase 1 does not authorize certificate creation, signing, issuance, or
revocation.

## 29. Deferred Decisions

Phase 1 does not select:

- implementation language;
- rule engine;
- policy language;
- executable schema;
- canonical serialization;
- fingerprint algorithm;
- persistence model;
- API or event protocol;
- provider integration;
- NEXUS integration;
- certificate mechanism;
- deployment topology.

## 30. Phase 1 Constraint

These semantics are normative planning documentation only.

They create no authority for code, tests, executable rules, persistence,
integration, live evidence collection, evaluation execution, certificate
issuance, deployment, production access, or Phase 2.
