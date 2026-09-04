# AFR Deterministic Conformance Kernel Architecture

## 1. Purpose

This document defines the technology-neutral architecture of the AFR
deterministic conformance kernel.

It is a planning artifact, not source code, an executable schema, an API,
a deployment design, or implementation authority.

## 2. Objective

For identical canonical inputs and governing versions, the kernel must produce
the same eligibility decisions, rules, outcomes, fingerprint, and result.

The kernel determines bounded conformance. It does not author architecture
truth, collect live evidence, grant runtime authority, deploy, or remediate.

## 3. Authority Separation

- NEXUS or another approved authority owns architecture truth.
- Observation sources describe bounded operational state.
- AFR evidence-trust functions determine evidence eligibility.
- The AFR kernel determines bounded conformance.
- ATA retains consequential runtime commit authority.
- PAA and Humanize remain non-authoritative consumers.

No boundary crossing implicitly elevates authority.

## 4. Kernel Invariants

Every evaluation must preserve:

1. one resolved tenant;
2. one bounded subject;
3. one immutable approved truth snapshot;
4. explicit claim identities and versions;
5. attributable evidence and eligibility decisions;
6. deterministic policy, rule, and evaluator versions;
7. declared trusted-time and freshness context;
8. canonical ordering and representation;
9. traceability from inputs to outcomes;
10. separation of conformance from enforcement.

## 5. Logical Components

The planned kernel contains:

- an invocation boundary;
- a truth-authority gate;
- a tenant and subject binding gate;
- a version-compatibility gate;
- an evidence-eligibility gate;
- a deterministic rule resolver;
- a claim evaluator;
- an aggregate evaluator;
- a fingerprint builder;
- a result assembler;
- a non-authoritative audit projection.

These are logical responsibilities, not implemented services.

## 6. Mandatory Stage Order

The stage order is:

1. validate invocation;
2. validate truth authority;
3. bind tenant and subject;
4. validate version compatibility;
5. determine evidence eligibility;
6. resolve deterministic rules;
7. evaluate claims;
8. aggregate claim outcomes;
9. construct the fingerprint;
10. assemble the result;
11. project audit explanation.

A later stage cannot repair, override, or bypass a failed earlier gate.

## 7. Evaluation States

Conceptual states are:

- `RECEIVED`;
- `INVOCATION_VALIDATED`;
- `TRUTH_VALIDATED`;
- `SCOPE_BOUND`;
- `VERSIONS_VALIDATED`;
- `EVIDENCE_CLASSIFIED`;
- `RULES_RESOLVED`;
- `CLAIMS_EVALUATED`;
- `AGGREGATED`;
- `FINGERPRINTED`;
- `RESULT_ASSEMBLED`;
- `COMPLETED`;
- `BLOCKED`.

Transitions are monotonic for one evaluation identity.

Material input changes require a new evaluation identity.

## 8. Invocation Gate

The invocation must resolve:

- tenant;
- subject and system;
- environment and release where applicable;
- truth snapshot;
- evaluated claims;
- evidence candidates;
- evaluation definition;
- policy and evaluator versions;
- trusted-time context;
- evaluation scope.

Missing or ambiguous mandatory context blocks evaluation.

## 9. Truth-Authority Gate

Truth validation must establish:

- recognized authority;
- approved snapshot state;
- immutable identity;
- integrity;
- tenant and subject applicability;
- compatible contract version;
- required claims;
- explicit supersession state.

Syntactic validity alone cannot establish authority.

A failed truth gate cannot produce `CONFORMANT`.

## 10. Scope and Version Gates

Every material input must resolve to the same authorized tenant and compatible
subject, environment, release, scope, and time context.

Unsupported or ambiguous truth, claim, evidence, policy, evaluator,
canonicalization, or fingerprint versions fail closed.

Automatic downgrade and nearest-version selection are prohibited.

## 11. Evidence Eligibility

Eligibility is determined separately for each evidence candidate and claim.

It considers:

- tenant and subject binding;
- source and collector identity;
- provenance and integrity;
- observation and collection time;
- freshness;
- environment and release applicability;
- semantic compatibility;
- duplication, replay, and contradiction indicators.

Ineligible evidence remains traceable but cannot support `CONFORMANT`.

## 12. Rule Resolution

Rules must be selected by explicit identity and compatible version.

Rule selection cannot use model inference, textual similarity, implicit
defaults, latest-version convenience, or cross-tenant reuse.

Missing or ambiguous authoritative rules produce a blocked or `INCONCLUSIVE`
condition under the approved semantics.

## 13. Claim Evaluation

Each claim evaluation binds:

- one approved claim;
- one deterministic rule;
- eligible evidence;
- material ineligible-evidence references;
- contradictions;
- scope and trusted time;
- governing versions;
- limitations.

The evaluator produces exactly one canonical claim outcome.

## 14. Canonical Outcomes

- `CONFORMANT` requires complete eligible support with no unresolved material
  contradiction.
- `NON_CONFORMANT` requires eligible evidence showing a required condition is
  not satisfied.
- `INCONCLUSIVE` represents insufficient, ambiguous, conflicting, or
  incompatible material inputs.
- `STALE` prevents expired evidence or results from supporting a current
  assertion.

These outcomes are not Boolean aliases.

## 15. Aggregate Constraints

Aggregation must:

- retain all claim-level results;
- preserve material weaker outcomes;
- use explicit versioned precedence;
- preserve scope and limitations;
- reject unknown outcomes;
- never average away non-conformance;
- never treat `INCONCLUSIVE` or `STALE` as conformant.

Aggregation cannot elevate evidence or truth authority.

## 16. Evaluation Fingerprint

The fingerprint binds:

- tenant, subject, environment, and release;
- truth snapshot and claims;
- eligible evidence;
- material ineligible-evidence references;
- eligibility decisions;
- resolved rules;
- evaluation, policy, and evaluator versions;
- trusted-time context;
- outcomes and limitations;
- canonicalization and fingerprint versions.

Ordering must be canonical and independent of input arrival order.

A fingerprint is not an authorization token.

## 17. Result Boundary

The result identifies:

- evaluation and scope;
- evaluated truth and claims;
- claim and aggregate outcomes;
- evidence and eligibility references;
- governing versions;
- fingerprint;
- evaluation time and validity;
- limitations and unresolved conditions.

A result cannot claim conditions outside its evaluated scope.

## 18. Failure Architecture

Distinct failure classes include:

- invalid invocation;
- unresolved authority;
- cross-tenant input;
- scope mismatch;
- integrity failure;
- unsupported version;
- stale required evidence;
- missing or ambiguous rule;
- contradictory evidence;
- canonicalization failure;
- fingerprint failure;
- internal invariant failure.

Failures cannot be silently converted into `CONFORMANT`.

## 19. Determinism Boundary

Authoritative behavior excludes:

- probabilistic rule selection;
- model-selected outcomes;
- mutable hidden state;
- undeclared clock dependence;
- input-order dependence;
- undocumented defaults;
- unversioned policy or canonicalization behavior.

Models may eventually explain results but cannot alter them.

## 20. NEXUS Boundary

The kernel cannot author, approve, supersede, repair, or mutate NEXUS
architecture truth or lifecycle state.

Any NEXUS export or integration requires separate authority.

## 21. Enforcement Boundary

The kernel cannot grant permissions, authorize tools, release deployments,
mutate providers, issue ATA decisions, or execute remediation.

External governed systems may later consume AFR results under separate
authority.

## 22. Trust Boundaries

The architecture separates:

1. architecture authorities from AFR;
2. observation sources from evidence-trust functions;
3. evidence-trust functions from the kernel;
4. individual kernel stages;
5. the kernel from downstream consumers;
6. AFR conformance from ATA commit authority;
7. tenants and evaluation instances.

## 23. Phase 2 Authority

This architecture is documentation-only.

It authorizes no code, executable schemas, tests, APIs, integrations,
collection, evaluation execution, persistence, certificates, deployment,
production access, remediation, or Phase 3.
