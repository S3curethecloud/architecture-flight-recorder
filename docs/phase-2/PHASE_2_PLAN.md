# Phase 2 Plan: Deterministic Conformance Kernel

## 1. Purpose

Phase 2 defines the planning architecture, conceptual execution contract,
trust boundary, and acceptance conditions for AFR's deterministic conformance
kernel.

This phase is documentation-only. It does not implement or execute the kernel.

## 2. Authority

Authorized planning authority:

`BOUNDED_DETERMINISTIC_CONFORMANCE_KERNEL_PLANNING_ONLY`

Implementation, runtime, integration, persistence, deployment, and Phase 3
authority remain `NONE`.

## 3. Objective

Define a technology-neutral kernel that deterministically evaluates approved
architecture claims against eligible operational evidence while preserving the
canonical Phase 1 information model and evaluation semantics.

The same authoritative truth snapshot, eligible evidence set, evaluation
definition, policy version, evaluator version, scope, and trusted-time context
must produce the same outcome and evaluation fingerprint.

## 4. Governing Inputs

The planned kernel consumes only conceptually validated instances of:

- an immutable architecture-truth snapshot;
- one or more approved architecture claims;
- attributable observations;
- evidence-eligibility determinations;
- an approved evaluation definition;
- a policy version;
- an evaluator version;
- a resolved tenant and subject scope;
- a trusted-time and freshness context.

Phase 2 does not define live ingestion or external integration.

## 5. Conceptual Kernel Stages

The planned deterministic pipeline contains these bounded stages:

1. **Invocation validation** — validate required identities, scope, versions,
   and declared inputs.
2. **Truth-authority validation** — verify that the truth snapshot is approved,
   immutable, attributable, compatible, and in scope.
3. **Tenant and subject binding** — ensure all material inputs resolve to the
   same authorized tenant, subject, environment, and release context.
4. **Evidence eligibility** — evaluate provenance, integrity, source,
   collector, freshness, time, scope, and compatibility.
5. **Claim rule selection** — select only the approved deterministic rule bound
   to the claim and evaluation definition.
6. **Claim evaluation** — derive one canonical claim-level outcome.
7. **Aggregate evaluation** — combine claim outcomes without masking weaker
   material outcomes.
8. **Fingerprint construction** — bind every material deterministic input and
   version into one reproducible identity.
9. **Result construction** — create a bounded result with limitations,
   traceability, and validity information.
10. **Audit projection** — expose a non-authoritative explanation of how the
    result was derived.

These are planning components, not implemented services or functions.

## 6. Fail-Closed Gate Ordering

Evaluation cannot proceed when a prerequisite gate fails.

Gate ordering must prevent:

- unapproved truth from entering evaluation;
- unresolved tenants or subjects from being evaluated;
- ineligible evidence from supporting `CONFORMANT`;
- unsupported versions from selecting fallback semantics;
- missing required evidence from becoming implicit support;
- contradictory evidence from being silently suppressed;
- model output from selecting an authoritative result.

A blocked prerequisite produces an explicitly defined invalid, inconclusive,
or stale condition rather than invented certainty.

## 7. Outcome Preservation

Phase 2 must preserve these Phase 1 meanings:

- `CONFORMANT` requires complete eligible supporting evidence and no unresolved
  material contradiction.
- `NON_CONFORMANT` requires eligible evidence demonstrating that a required
  condition is not satisfied.
- `INCONCLUSIVE` represents insufficient, ambiguous, conflicting, unresolved,
  or incompatible material inputs.
- `STALE` prevents expired evidence or results from supporting a current
  assertion.

The kernel must not collapse these outcomes into a Boolean.

## 8. Aggregate Constraints

Aggregate evaluation must:

- retain every claim-level result;
- preserve every material `NON_CONFORMANT`, `INCONCLUSIVE`, and `STALE`
  condition;
- prohibit a stronger aggregate assertion than its material dependencies;
- preserve scope and limitation information;
- use an approved deterministic precedence definition;
- reject unknown or incompatible outcome values.

Aggregation is not evidence normalization and cannot elevate authority.

## 9. Evaluation Fingerprint

The planning package must define a fingerprint that binds at least:

- tenant identity;
- subject and system identity;
- environment and release identity;
- truth-snapshot identity and integrity value;
- evaluated claim identities and versions;
- eligible evidence identities and integrity values;
- evidence-eligibility decisions;
- evaluation-definition identity and version;
- policy version;
- evaluator version;
- trusted-time context;
- applicable scope and compatibility versions;
- canonical ordering and representation rules.

A fingerprint identifies evaluated inputs and semantics. It does not grant
execution authority.

## 10. Reproducibility

The planned kernel must make it possible to determine:

- which authoritative truth was evaluated;
- which evidence was eligible or rejected and why;
- which deterministic rule was selected;
- which versions governed evaluation;
- how the claim outcome was derived;
- how the aggregate result was derived;
- whether the same preserved inputs reproduce the same fingerprint and result.

Phase 2 does not authorize storage or replay execution.

## 11. Model Boundary

Models may later assist with explanations or human-review preparation.

Models cannot:

- validate truth authority;
- determine evidence eligibility;
- select authoritative rules;
- choose claim outcomes;
- override aggregate precedence;
- alter fingerprints;
- grant runtime or deployment authority.

No model integration is authorized in Phase 2.

## 12. NEXUS Boundary

NEXUS remains authoritative for approved architecture truth.

The kernel architecture may define a conceptual validated truth input, but
Phase 2 cannot define or implement a NEXUS export, access NEXUS persistence,
modify NEXUS state, infer approval, or repair missing architecture semantics.

## 13. ATA and Downstream Boundary

ATA retains consequential runtime commit authority.

An AFR result may eventually be an input to an external policy decision, but
the kernel cannot authorize, execute, enforce, deploy, or remediate.

PAA and Humanize remain non-authoritative downstream consumers.

## 14. Security Planning

The Phase 2 trust boundary must address:

- cross-tenant substitution;
- truth or evidence replay;
- source and collector impersonation;
- integrity-value substitution;
- stale-evidence reuse;
- version downgrade;
- rule substitution;
- canonicalization ambiguity;
- outcome suppression;
- fingerprint collision assumptions;
- explanation-layer authority confusion;
- cross-evaluation data leakage.

## 15. Planned Deliverables

Phase 2 produces exactly:

1. the SOT Phase 2 planning record;
2. this plan;
3. Phase 2 acceptance criteria;
4. deterministic kernel architecture;
5. conceptual kernel execution contract;
6. kernel trust-boundary documentation.

## 16. Explicit Non-Deliverables

Phase 2 does not produce:

- source code;
- executable schemas;
- tests or fixtures;
- packages or dependencies;
- APIs or services;
- provider adapters or collectors;
- NEXUS, ATA, PAA, or Humanize integrations;
- persistence;
- queues or streams;
- certificate generation;
- deployment artifacts;
- production evaluation;
- runtime enforcement;
- remediation.

## 17. Review Strategy

The completed six-file package requires independent review for:

- Phase 0 doctrine consistency;
- Phase 1 model and semantic consistency;
- deterministic stage and gate ordering;
- outcome and aggregation correctness;
- fingerprint completeness;
- security and tenant isolation;
- NEXUS non-duplication;
- ATA authority preservation;
- implementation-authority leakage;
- Phase 3 authority leakage.

## 18. Exit Condition

Phase 2 planning is accepted only after:

- the exact six-file boundary is verified;
- every acceptance criterion is satisfied;
- all content hashes are frozen;
- the package is independently reviewed;
- all findings are resolved;
- the reviewed package is committed and pushed;
- its PR is independently accepted and explicitly authorized for merge;
- canonical merge and post-merge verification succeed;
- local and remote canonical `main` converge cleanly.

Phase 2 planning acceptance does not authorize implementation or Phase 3.

## 19. Closure Requirement

After canonical planning acceptance, Phase 2 must be terminally closed through
a separately governed post-merge closure reconciliation.

Closure cannot activate implementation or Phase 3.
