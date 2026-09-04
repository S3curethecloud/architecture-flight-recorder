# Phase 1 Acceptance Criteria

## Purpose

These criteria govern the planning-only Phase 1 package for canonical
information contracts and deterministic evaluation semantics.

## Authority and Scope

- [x] The package contains exactly the six authorized files.
- [x] All changes remain documentation-only.
- [x] Phase 1 implementation authority remains `NONE`.
- [x] Phase 2 authority remains `NONE`.
- [x] No executable schema, source code, test, adapter, or deployment artifact
      exists.
- [x] The SOT accurately records the activated planning authority.

## Canonical Information Model

- [x] Architecture truth references remain externally authoritative.
- [x] Architecture claims have stable identity and bounded scope.
- [x] Observations are distinct from eligible evidence.
- [x] Evidence eligibility is represented explicitly.
- [x] Tenant, subject, environment, and release binding are explicit.
- [x] Provenance and integrity information are mandatory concepts.
- [x] Evidence gaps and contradictions are first-class concepts.
- [x] Evaluation definitions and contexts are versioned concepts.
- [x] Claim-level and aggregate results remain distinct.
- [x] Evaluation fingerprints bind every material deterministic input.
- [x] The model remains technology-neutral and non-executable.

## Evaluation Semantics

- [x] `CONFORMANT` semantics require complete eligible supporting evidence.
- [x] `NON_CONFORMANT` semantics preserve material contradiction.
- [x] `INCONCLUSIVE` semantics cover insufficient or ambiguous inputs.
- [x] `STALE` semantics prevent expired evidence from supporting current
      conformance.
- [x] Missing evidence is not treated as negative evidence or conformance.
- [x] Contradictory evidence cannot be silently suppressed.
- [x] Aggregate results cannot hide weaker material claim outcomes.
- [x] Identical eligible inputs produce identical outcomes and fingerprints.
- [x] Model inference cannot select an authoritative outcome.
- [x] Unsupported contract, policy, or evaluator versions fail closed.

## Trust Invariants

- [x] Every authoritative record is bound to one resolved tenant context.
- [x] Cross-tenant substitution and reuse are prohibited.
- [x] Source and collector identities remain distinguishable.
- [x] Truth authority cannot be inferred from syntactic validity.
- [x] Normalization cannot elevate evidence authority.
- [x] Trusted-time concepts and freshness boundaries are explicit.
- [x] Immutable inputs and results cannot be silently replaced.
- [x] Downstream consumers cannot mutate authoritative findings.
- [x] Certificates remain separate from deployment and execution authority.
- [x] ATA retains consequential runtime commit authority.

## NEXUS and Ecosystem Boundaries

- [x] NEXUS remains authoritative for approved architecture truth.
- [x] No NEXUS export contract or integration is implemented.
- [x] AFR cannot mutate NEXUS engagement or lifecycle state.
- [x] PAA cannot rewrite truth, evidence, or AFR outcomes.
- [x] Humanize cannot originate evidence or conformance.
- [x] Providers remain sources of observations, not architecture intent.
- [x] AFR cannot execute remediation.
- [x] No integration authority is inferred from conceptual relationships.

## Required Exit Evidence

Phase 1 planning acceptance requires:

- exact six-file boundary validation;
- Markdown and whitespace validation;
- cross-document terminology review;
- deterministic-semantics review;
- security and tenant-boundary review;
- NEXUS non-duplication review;
- authority-leakage review;
- clean staged-object verification;
- independent architecture and acceptance review.

## Exit Gate

Phase 1 planning may be accepted only with:

- `AFR_PHASE_1_PLANNING_ACCEPTANCE = PASS`
- `AFR_PHASE_1_IMPLEMENTATION_AUTHORITY = NONE`
- `AFR_PHASE_2_AUTHORITY = NONE`

Acceptance does not authorize implementation, integration, persistence,
evaluation execution, certificates, deployment, production access, or Phase 2.

## Independent Review Evidence

The unstaged six-file Phase 1 planning package was reviewed as one bounded
candidate.

Review disposition:

- `AFR_PHASE_1_ARCHITECTURE_REVIEW = PASS`
- `AFR_PHASE_1_DETERMINISTIC_SEMANTICS_REVIEW = PASS`
- `AFR_PHASE_1_SECURITY_REVIEW = PASS`
- `AFR_PHASE_1_NEXUS_NON_DUPLICATION_REVIEW = PASS`
- `AFR_PHASE_1_AUTHORITY_LEAKAGE_REVIEW = PASS`
- `AFR_PHASE_1_BLOCKING_FINDINGS = NONE`

Validated properties include:

- exact six-file planning boundary;
- all 45 acceptance criteria satisfied;
- normative but non-executable information contracts;
- deterministic and fail-closed outcome semantics;
- explicit evidence-eligibility and contradiction handling;
- tenant, identity, provenance, integrity, freshness, and time invariants;
- preservation of NEXUS architecture-truth authority;
- preservation of ATA runtime commit authority;
- exclusion of implementation, integration, persistence, certificate,
  deployment, production, and Phase 2 authority.

## Planning-Acceptance Effective Point

Before the effective point:

- Phase 1 status: `PLANNING_REVIEW_ACCEPTED_CANDIDATE`;
- Phase 1 implementation authority: `NONE`;
- Phase 2 authority: `NONE`.

Phase 1 planning acceptance becomes canonical only when:

1. the package remains limited to the authorized six files;
2. the reviewed content and hashes remain unchanged;
3. the package is staged and committed exactly;
4. the branch and pull-request identities are verified;
5. the pull request receives independent acceptance review;
6. all review findings are resolved;
7. the package is merged to canonical `main`;
8. post-merge identity, parentage, tree, and content are verified;
9. the local canonical `main` checkout is synchronized and clean.

Opening, approving, or marking the planning PR ready does not satisfy this
effective point.

Canonical Phase 1 planning acceptance does not authorize implementation,
integration, persistence, evaluation execution, certificates, deployment,
production access, or Phase 2.

## Post-Merge Closure Reconciliation

The Phase 1 planning-acceptance effective point has been verified against:

- planning-package commit:
  `b09b283eb5df28ed2892370efe5f0a1a09a1a703`;
- canonical merge:
  `0368630f8b21cb239885bff0186be5812e21b157`;
- canonical tree:
  `fb20d88e1a4032bf53d20fbf2303f90ef338a6c3`;
- pull request: `#4`;
- exact six-file content hashes;
- clean local and remote canonical synchronization.

All 45 acceptance criteria remain satisfied.

This record is a closure candidate until it is independently reviewed, all
findings are resolved, it is merged to canonical `main`, and its post-merge
identity, parentage, tree, content, and clean synchronization are verified.

Before that effective point:

- `AFR_PHASE_1_STATUS = PLANNING_ACCEPTED_CLOSURE_PENDING`
- `AFR_PHASE_1_PLANNING_AUTHORITY = CONSUMED_PENDING_CLOSURE`
- `AFR_PHASE_1_IMPLEMENTATION_AUTHORITY = NONE`
- `AFR_PHASE_2_AUTHORITY = NONE`

After and only after that effective point:

- `AFR_PHASE_1_STATUS = COMPLETE`
- `AFR_PHASE_1_PLANNING_AUTHORITY = CONSUMED_CLOSED`
- `AFR_PHASE_1_IMPLEMENTATION_AUTHORITY = NONE`
- `AFR_PHASE_2_AUTHORITY = NONE`

Closure acceptance does not authorize implementation or Phase 2.
