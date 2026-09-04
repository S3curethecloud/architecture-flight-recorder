# Phase 2 Acceptance Criteria

## Purpose

These criteria govern the documentation-only Phase 2 deterministic conformance
kernel planning package.

## Authority and File Boundary

- [x] The package contains exactly the six authorized files.
- [x] Every change is documentation-only.
- [x] Phase 2 implementation authority remains `NONE`.
- [x] Runtime and deployment authority remain `NONE`.
- [x] Phase 3 authority remains `NONE`.
- [x] No code, executable schema, test, adapter, or deployment artifact exists.
- [x] The SOT records the verified Phase 2 planning-authority activation.

## Phase 1 Semantic Preservation

- [x] Phase 1 canonical record identities and relationships remain unchanged.
- [x] The four canonical outcomes retain their approved meanings.
- [x] Missing evidence cannot produce `CONFORMANT`.
- [x] Contradictory evidence cannot be silently suppressed.
- [x] Evidence normalization cannot elevate authority.
- [x] Model inference cannot select an authoritative outcome.
- [x] Identical eligible inputs retain deterministic result requirements.

## Kernel Architecture

- [x] Kernel stages have explicit responsibilities and boundaries.
- [x] Gate ordering is deterministic and fail-closed.
- [x] Truth validation precedes evidence evaluation.
- [x] Tenant and subject binding precede claim evaluation.
- [x] Evidence eligibility precedes use as supporting evidence.
- [x] Rule selection is versioned and deterministic.
- [x] Claim evaluation remains distinct from aggregation.
- [x] Result construction remains distinct from enforcement.
- [x] Explanation remains non-authoritative.

## Evaluation Contract

- [x] Invocation prerequisites are explicit.
- [x] Required and optional conceptual inputs are distinguished.
- [x] Invalid-state behavior is explicit.
- [x] Unsupported versions fail closed.
- [x] Canonical ordering requirements are defined.
- [x] Claim-level outcome derivation is traceable.
- [x] Aggregate precedence cannot mask weaker material outcomes.
- [x] Result limitations and validity boundaries are preserved.
- [x] No contract is represented as an executable schema or API.

## Fingerprint and Reproducibility

- [x] Every material deterministic input is fingerprint-bound.
- [x] Truth, claims, evidence, eligibility, rules, and versions are bound.
- [x] Tenant, subject, environment, release, and time context are bound.
- [x] Canonical representation and ordering requirements are explicit.
- [x] Reproduction requires the same preserved inputs and semantics.
- [x] A fingerprint is not represented as execution authority.
- [x] Storage and replay execution remain unauthorized.

## Trust Boundary

- [x] Tenant isolation is maintained across every kernel stage.
- [x] Source and collector identities remain distinct.
- [x] Replay, substitution, impersonation, and downgrade threats are addressed.
- [x] Trusted-time and freshness requirements remain explicit.
- [x] Integrity validation failures cannot produce `CONFORMANT`.
- [x] Rule substitution and outcome suppression are addressed.
- [x] Explanation output cannot mutate authoritative results.
- [x] Cross-evaluation data leakage is addressed.

## Ecosystem Boundaries

- [x] NEXUS remains authoritative for approved architecture truth.
- [x] No NEXUS export or integration is defined or implemented.
- [x] AFR cannot mutate NEXUS state or infer approval.
- [x] ATA retains consequential runtime commit authority.
- [x] AFR results do not authorize execution, deployment, or remediation.
- [x] PAA and Humanize remain non-authoritative consumers.
- [x] Provider collection and live evidence ingestion remain unauthorized.

## Required Exit Evidence

Phase 2 planning acceptance requires:

- exact six-file boundary verification;
- Markdown and whitespace validation;
- cross-document terminology review;
- Phase 1 semantic-preservation review;
- deterministic stage and gate-order review;
- fingerprint and reproducibility review;
- security and tenant-boundary review;
- NEXUS non-duplication review;
- ATA authority-boundary review;
- implementation and Phase 3 authority-leakage review;
- clean staged-object verification;
- independent architecture and acceptance review.

## Exit Gate

Phase 2 planning may be accepted only with:

- `AFR_PHASE_2_PLANNING_ACCEPTANCE = PASS`
- `AFR_PHASE_2_IMPLEMENTATION_AUTHORITY = NONE`
- `AFR_PHASE_3_AUTHORITY = NONE`

Acceptance does not authorize implementation, runtime evaluation, integration,
persistence, certificates, deployment, production access, or Phase 3.

## Independent Review Evidence

The unstaged six-file Phase 2 planning package was reviewed as one bounded
candidate.

Review disposition:

- `AFR_PHASE_2_ARCHITECTURE_REVIEW = PASS`
- `AFR_PHASE_2_DETERMINISTIC_SEMANTICS_REVIEW = PASS`
- `AFR_PHASE_2_EXECUTION_CONTRACT_REVIEW = PASS`
- `AFR_PHASE_2_SECURITY_REVIEW = PASS`
- `AFR_PHASE_2_NEXUS_NON_DUPLICATION_REVIEW = PASS`
- `AFR_PHASE_2_ATA_AUTHORITY_REVIEW = PASS`
- `AFR_PHASE_2_AUTHORITY_LEAKAGE_REVIEW = PASS`
- `AFR_PHASE_2_REVIEW_FINDING_001 = RESOLVED`
- `AFR_PHASE_2_BLOCKING_FINDINGS = NONE`

All 54 acceptance criteria are satisfied.

## Planning-Acceptance Effective Point

Before the effective point:

- `AFR_PHASE_2_STATUS = PLANNING_REVIEW_ACCEPTED_CANDIDATE`
- `AFR_PHASE_2_IMPLEMENTATION_AUTHORITY = NONE`
- `AFR_PHASE_3_AUTHORITY = NONE`

Phase 2 planning acceptance becomes canonical only when:

1. the package remains limited to the authorized six files;
2. the reviewed content and hashes remain unchanged;
3. the exact package is staged and committed;
4. branch and pull-request identities are verified;
5. the pull request receives independent acceptance review;
6. all review findings are resolved;
7. the package is merged to canonical `main`;
8. post-merge identity, parentage, tree, and content are verified;
9. local and remote canonical `main` converge cleanly.

Canonical acceptance does not authorize implementation, integration,
persistence, evaluation execution, certificates, deployment, production
access, remediation, or Phase 3.
