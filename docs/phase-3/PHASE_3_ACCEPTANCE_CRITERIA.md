# Phase 3 Acceptance Criteria

## Purpose

These criteria govern the documentation-only Phase 3 deterministic-kernel
implementation-readiness planning package.

## Authority and File Boundary

- [x] The package contains exactly the six authorized documentation files.
- [x] Every change is documentation-only.
- [x] Phase 3 planning authority remains within its activated boundary.
- [x] Phase 3 implementation authority remains `NONE`.
- [x] Runtime-evaluation authority remains `NONE`.
- [x] Integration and persistence authority remain `NONE`.
- [x] Phase 4 authority remains `NONE`.
- [x] No executable artifact or dependency is introduced.

## Canonical Semantic Preservation

- [x] NEXUS remains authoritative for approved architecture truth.
- [x] Observations remain distinct from architecture truth.
- [x] Evidence requires an explicit eligibility decision before evaluation.
- [x] Missing required evidence cannot produce `CONFORMANT`.
- [x] Contradictory evidence cannot be silently suppressed.
- [x] The four canonical outcomes retain their approved meanings.
- [x] Model inference cannot select an authoritative outcome.
- [x] ATA retains consequential runtime commit authority.

## Kernel Implementation Blueprint

- [x] Kernel modules have bounded single responsibilities.
- [x] Invocation validation is represented explicitly.
- [x] Truth-authority validation precedes evidence evaluation.
- [x] Tenant and subject binding precede claim evaluation.
- [x] Evidence eligibility precedes evidence use.
- [x] Rule selection is versioned and deterministic.
- [x] Claim evaluation remains distinct from aggregation.
- [x] Result construction remains distinct from explanation.
- [x] Enforcement remains outside the kernel boundary.

## Contract Mapping

- [x] Every canonical input concept has a future representation mapping.
- [x] Required, optional, derived, and prohibited fields are distinguished.
- [x] Invalid states remain distinct from conformance outcomes.
- [x] Unsupported versions fail closed.
- [x] Canonical identifiers and versions remain stable.
- [x] Mapping does not select an implementation language.
- [x] Mapping does not create an executable schema.
- [x] Provider representations cannot become canonical records directly.

## Canonicalization and Fingerprinting

- [x] Canonical field-inclusion rules are defined.
- [x] Null, absence, and duplicate handling are defined.
- [x] Collection-ordering rules are deterministic.
- [x] Timestamp, text, identifier, and numeric boundaries are defined.
- [x] Canonicalization failures fail closed.
- [x] Every material deterministic input is fingerprint-bound.
- [x] Fingerprint algorithms and versions are identifiable.
- [x] Fingerprints are not represented as execution authority.

## Verification Design

- [x] Deterministic replay requirements are defined.
- [x] Canonicalization-equivalence requirements are defined.
- [x] Tenant-isolation failure cases are defined.
- [x] Truth-authority and evidence-eligibility failure cases are defined.
- [x] Missing, contradictory, and stale evidence cases are defined.
- [x] Unsupported-version and integrity-failure cases are defined.
- [x] Aggregate-outcome precedence cases are defined.
- [x] Explanation non-authority is verifiable.

## Security and Supply Chain

- [x] Dependency minimization and pinning requirements are defined.
- [x] Dependency provenance and integrity requirements are defined.
- [x] Vulnerability and SBOM expectations are defined.
- [x] Secret exclusion requirements are defined.
- [x] Untrusted-input handling requirements are defined.
- [x] Cross-tenant substitution is prohibited.
- [x] Resource-boundary and failure-containment requirements are defined.
- [x] Rollback and abandonment conditions are defined.

## Proposed First Implementation Slice

- [x] The proposed slice is pure and side-effect-free.
- [x] Its future source and test boundaries must be exact.
- [x] Its permitted and prohibited behaviors must be explicit.
- [x] Its deterministic acceptance vectors must be defined.
- [x] Providers, integrations, persistence, and deployment remain excluded.
- [x] The proposed slice requires separate implementation authority.

## Exit Gate

Phase 3 planning may be accepted only with:

- `AFR_PHASE_3_PLANNING_ACCEPTANCE = PASS`
- `AFR_PHASE_3_IMPLEMENTATION_AUTHORITY = NONE`
- `AFR_PHASE_4_AUTHORITY = NONE`

Acceptance does not authorize code, executable schemas, tests, dependencies,
integration, persistence, runtime evaluation, certificates, deployment,
production access, enforcement, remediation, or Phase 4.

All criteria remain pending until the complete six-document package is
materialized and independently reviewed.

## Independent Review Evidence

The complete unstaged six-document Phase 3 planning package was independently
reviewed at its frozen content identities.

Review disposition:

- `AFR_PHASE_3_ARCHITECTURE_REVIEW = PASS`
- `AFR_PHASE_3_CANONICAL_SEMANTIC_PRESERVATION_REVIEW = PASS`
- `AFR_PHASE_3_DETERMINISTIC_CANONICALIZATION_REVIEW = PASS`
- `AFR_PHASE_3_FINGERPRINT_REQUIREMENTS_REVIEW = PASS`
- `AFR_PHASE_3_CONTRACT_MAPPING_REVIEW = PASS`
- `AFR_PHASE_3_SECURITY_REVIEW = PASS`
- `AFR_PHASE_3_TENANT_ISOLATION_REVIEW = PASS`
- `AFR_PHASE_3_SUPPLY_CHAIN_REVIEW = PASS`
- `AFR_PHASE_3_FIRST_SLICE_BOUNDARY_REVIEW = PASS`
- `AFR_PHASE_3_NEXUS_NON_DUPLICATION_REVIEW = PASS`
- `AFR_PHASE_3_ATA_AUTHORITY_REVIEW = PASS`
- `AFR_PHASE_3_AUTHORITY_LEAKAGE_REVIEW = PASS`
- `AFR_PHASE_3_REVIEW_FINDING_001 = RESOLVED`
- `AFR_PHASE_3_BLOCKING_FINDINGS = NONE`

All 63 acceptance criteria are satisfied by the reviewed candidate.

## Planning-Acceptance Effective Point

Before the effective point:

- `AFR_PHASE_3_STATUS = PLANNING_REVIEW_ACCEPTED_CANDIDATE`
- `AFR_PHASE_3_PLANNING_AUTHORITY =
  BOUNDED_KERNEL_IMPLEMENTATION_READINESS_PLANNING_ONLY`
- `AFR_PHASE_3_IMPLEMENTATION_AUTHORITY = NONE`
- `AFR_PHASE_4_AUTHORITY = NONE`

Phase 3 planning acceptance becomes canonical only when:

1. the package remains limited to the authorized six documents;
2. the reviewed content and hashes remain unchanged;
3. the exact package is staged and committed;
4. branch and pull-request identities are verified;
5. the pull request receives independent acceptance review;
6. all review findings remain resolved;
7. explicit merge authorization is granted;
8. the package is merged to canonical `main`;
9. post-merge identity, parentage, tree, file boundary, and content are
   verified;
10. local and remote canonical `main` converge cleanly.

After and only after that effective point:

- `AFR_PHASE_3_STATUS = PLANNING_ACCEPTED_CLOSURE_PENDING`
- `AFR_PHASE_3_PLANNING_AUTHORITY = CONSUMED_PENDING_CLOSURE`
- `AFR_PHASE_3_IMPLEMENTATION_AUTHORITY = NONE`
- `AFR_PHASE_4_AUTHORITY = NONE`

Terminal Phase 3 completion requires a separately governed post-merge closure
reconciliation.

Acceptance and closure do not authorize implementation, integration,
persistence, runtime evaluation, certificates, deployment, production access,
enforcement, remediation, or Phase 4.

## Post-Merge Closure Reconciliation

The Phase 3 planning-acceptance effective point has been verified against:

- planning-package commit:
  `7bd9b3b387606765202a8ba8a7c0fe22c5759e2d`;
- canonical merge:
  `45512c2d4ea2c6d6fd46f33ac312f6624513cdb9`;
- canonical tree:
  `65c5be068614ab3724becb86df8ea4e29c9e7244`;
- pull request: `#10`;
- exact six-document content hashes;
- exact six-document merge boundary;
- clean local and remote canonical synchronization.

All 63 Phase 3 acceptance criteria remain satisfied, and
`AFR_PHASE_3_REVIEW_FINDING_001` remains resolved.

This record remains a closure candidate until it is independently reviewed,
all findings are resolved, it is committed and pushed exactly, its pull
request is verified and explicitly authorized for merge, it is merged to
canonical `main`, and its post-merge identity, parentage, tree, file boundary,
content, and clean synchronization are verified.

Before that effective point:

- `AFR_PHASE_3_STATUS = PLANNING_ACCEPTED_CLOSURE_PENDING`
- `AFR_PHASE_3_PLANNING_AUTHORITY = CONSUMED_PENDING_CLOSURE`
- `AFR_PHASE_3_IMPLEMENTATION_AUTHORITY = NONE`
- `AFR_PHASE_4_AUTHORITY = NONE`

After and only after that effective point:

- `AFR_PHASE_3_STATUS = COMPLETE`
- `AFR_PHASE_3_PLANNING_AUTHORITY = CONSUMED_CLOSED`
- `AFR_PHASE_3_IMPLEMENTATION_AUTHORITY = NONE`
- `AFR_PHASE_4_AUTHORITY = NONE`

Closure acceptance does not authorize code, executable schemas, tests,
fixtures, dependencies, integration, persistence, runtime evaluation,
certificates, deployment, production access, enforcement, remediation, or
Phase 4. The proposed first implementation slice remains inactive.
