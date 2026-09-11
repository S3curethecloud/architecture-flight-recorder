# AFR Phase 4 Normalized-Evidence-Bytes Semantic-Amendment Authority Proposal

## 1. Purpose

This document proposes only the bounded documentation authority required to clarify the existing canonical Phase 4 resource term `normalized evidence bytes` after Phase 4 terminal closure.

It does not select the measurement, reopen Phase 4 generally, authorize implementation, or create runtime or cross-program authority.

## 2. Exact Canonical Base

This proposal is bound to exactly:

`REPOSITORY = S3curethecloud/architecture-flight-recorder`

`CANONICAL_BRANCH = main`

`EXPECTED_CANONICAL_BASE_COMMIT = 02f50963a6eaef49283722d6b9000eabe8a04a4c`

`EXPECTED_CANONICAL_BASE_TREE = bf7aed9b874c162294a57857ccfa334dd7eeb261`

`EXPECTED_CANONICAL_BASE_SOT_BLOB = ff8363878f01ac9666f49c68cc4eda280ba4958b`

If canonical `main` moves before this proposal reaches its canonical effective point:

`BASE_MOVED = STOP`

`SILENT_REBASE = PROHIBITED`

`SILENT_BASE_SUBSTITUTION = PROHIBITED`

## 3. Closed Phase 4 State

Phase 4 operational-evidence intake and eligibility planning is canonically complete and terminally closed.

`AFR_PHASE_4_PLANNING_STATUS = COMPLETE`

`AFR_PHASE_4_PLANNING_AUTHORITY = CONSUMED_CLOSED`

`AFR_PHASE_4_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_4_AUTHORITY = NONE`

The bounded capability remains `OPERATIONAL_EVIDENCE_INTAKE_AND_ELIGIBILITY_PLANNING` and its mission remains `DEFINE_BOUNDED_OBSERVATION_TO_ELIGIBLE_EVIDENCE_SEMANTICS`.

## 4. Existing Canonical Resource and Semantic Gap

The canonical Phase 4 deterministic resource surface remains exactly:

1. total ingress bytes;
2. envelope field count;
3. collection cardinality;
4. nesting depth;
5. provenance-chain length;
6. integrity-reference length;
7. normalized evidence bytes;
8. deterministic processing work units.

`NORMALIZED_EVIDENCE_BYTES_CANONICAL_NAME = EXISTING_CANONICAL`

`NORMALIZED_EVIDENCE_BYTES_CANONICAL_MEASUREMENT = NOT_ESTABLISHED`

The canonical rule remains exactly:

`Any violation fails closed before evidence construction.`

## 5. Relationship Neutrality

No equality, inequality, inclusion, exclusion, derivation, or substitution relationship is established between normalized evidence bytes and normalized content identity, normalized content bytes, final eligible-evidence bytes, pre-integrity evidence bytes, eligibility-decision-plus-evidence bytes, Phase 3 canonical bytes, or another representation.

`NORMALIZED_EVIDENCE_BYTES_RELATIONSHIP_SELECTION = NONE`

`NORMALIZED_CONTENT_IDENTITY_TO_NORMALIZED_EVIDENCE_BYTES_RELATIONSHIP = NOT_ESTABLISHED`

`PHASE3_MAXIMUM_CANONICAL_BYTES_TO_NORMALIZED_EVIDENCE_BYTES_RELATIONSHIP = NOT_ESTABLISHED`

## 6. Eligibility and Conformance Non-Drift

Eligibility remains pre-conformance.

The only Phase 4 eligibility classifications remain:

- `ELIGIBLE`
- `INELIGIBLE`
- `QUARANTINED`
- `UNSUPPORTED`
- `PROCESSING_FAILURE`

This proposal does not authorize `CONFORMANT`, `NON_CONFORMANT`, `INCONCLUSIVE`, `STALE`, or another conformance result as an eligibility outcome.

## 7. Security and Trust Non-Expansion

The existing Phase 4 security and trust boundary is not expanded or redesigned by this proposal or by the bounded clarification it may later authorize.

`PHASE_4_SECURITY_TRUST_BOUNDARY_EXPANSION = PROHIBITED`

`EXISTING_PROVENANCE_TRUST_SEMANTICS = PRESERVED`

`EXISTING_INTEGRITY_TRUST_SEMANTICS = PRESERVED`

`EXISTING_TENANT_SUBJECT_ISOLATION = PRESERVED`

`EXISTING_FRESHNESS_TRUST_SEMANTICS = PRESERVED`

The clarification may determine whether integrity material participates in the measured representation only; it cannot alter integrity validation or trust semantics.

## 8. Presence, Type, and Determinism Non-Drift

The canonical distinction among absent optional, explicit null, empty, missing required, unsupported value, unsupported type, and unsupported version remains unchanged.

`PHASE_4_PRESENCE_TYPE_SEMANTICS = UNCHANGED`

`PHASE_4_DETERMINISM_SEMANTICS = UNCHANGED`

`DEFAULTING = PROHIBITED`

`COERCION = PROHIBITED`

`AMBIENT_INFERENCE = PROHIBITED`

`SILENT_REPAIR = PROHIBITED`

Identical governed inputs must continue to produce byte-identical decision records and eligible-evidence representations.

## 9. Phase 3 Non-Drift

Phase 3 independently owns `maximum_canonical_bytes` within its deterministic kernel resource contract.

This proposal does not redefine Phase 3 canonicalization, resource accounting, work-unit accounting, fingerprints, contracts, tests, or vectors.

Primitive reuse cannot establish Phase 4 resource semantics by implication.

## 10. Bounded Governance Path and Requested Authority

The supported path is `BOUNDED_POST_CLOSURE_PHASE_4_SEMANTIC_AMENDMENT`.

`GENERAL_PHASE_4_REOPEN = NO`

The exact authority-proposal canonical boundary is:

1. `docs/SOT.md`
2. `docs/phase-4/PHASE_4_NORMALIZED_EVIDENCE_BYTES_SEMANTIC_AMENDMENT_AUTHORITY_PROPOSAL.md`

No third canonical repository path is authorized.

The requested authority is exactly:

`BOUNDED_NORMALIZED_EVIDENCE_BYTES_SEMANTIC_AMENDMENT_DOCUMENTATION_ONLY`

Before the complete authority-proposal effective point:

`AFR_PHASE_4_NORMALIZED_EVIDENCE_BYTES_SEMANTIC_AMENDMENT_AUTHORITY = NONE`

## 11. Single-Use Authority Lifecycle

`STATE_0 = NONE`

`STATE_1 = BOUNDED_NORMALIZED_EVIDENCE_BYTES_SEMANTIC_AMENDMENT_DOCUMENTATION_ONLY`

`STATE_2 = CONSUMED_PENDING_CLOSURE`

`STATE_3 = CONSUMED_CLOSED`

Only `STATE_0 -> STATE_1 -> STATE_2 -> STATE_3` is permitted. No state implies the next and no state may be skipped.

State 2 may be established only after a separately governed semantic clarification is canonically merged and completely post-merge verified.

State 3 requires separately governed canonical closure after State 2.

`STATE_2_TO_STATE_3_REQUIRES = SEPARATELY_GOVERNED_CANONICAL_CLOSURE`

## 12. State-1 Canonical Effective Point

State 1 becomes effective if and only if every one of these separately governed gates occurs in order:

1. exact two-document boundary and complete future-file preimages established against the exact base;
2. independent integrated adversarial acceptance review of the complete two-object preimage set before freeze;
3. all blocking findings resolved in a fresh exact accepted candidate;
4. exact-content freeze authorization and execution;
5. deterministic serialization-freeze authorization and execution;
6. SHA-256 computation-and-freeze authorization and execution over the exact frozen serialized bytes;
7. post-freeze identity and integrity reverification;
8. exact two-object repository materialization authorization and execution;
9. exact staging authorization and verification;
10. exact commit authorization and commit creation with verified parent, tree, boundary, and frozen identities;
11. exact remote branch publication and identity verification;
12. draft pull-request creation preserving the exact reviewed identity;
13. independent pull-request acceptance review;
14. explicit draft-to-ready transition;
15. explicit merge authorization for the exact Ready identity;
16. exact required two-parent canonical merge;
17. independent post-merge identity, ordered-parent, tree, exact-boundary, and frozen-content verification;
18. local and remote canonical `main` convergence on that merge; and
19. clean canonical worktree and index verification.

No earlier event establishes State 1. Candidate preparation, review, freeze, hash computation, materialization, staging, commit, publication, draft PR, PR review, Ready transition, merge authorization, or merge alone is insufficient.

`MERGE_WITHOUT_PRIOR_READY_TRANSITION = NOT_AUTHORITY_ESTABLISHING`

`MERGE_WITHOUT_EXPLICIT_MERGE_AUTHORIZATION = NOT_AUTHORITY_ESTABLISHING`

`MERGE_WITHOUT_POST_MERGE_VERIFICATION = NOT_AUTHORITY_ESTABLISHING`

After and only after this complete effective point:

`AFR_PHASE_4_NORMALIZED_EVIDENCE_BYTES_SEMANTIC_AMENDMENT_AUTHORITY = BOUNDED_NORMALIZED_EVIDENCE_BYTES_SEMANTIC_AMENDMENT_DOCUMENTATION_ONLY`

## 13. Exact Merge Topology

`FROZEN_BASE = 02f50963a6eaef49283722d6b9000eabe8a04a4c`

Let `VERIFIED_HEAD` be the exact independently reviewed proposal commit and `VERIFIED_HEAD_TREE` its exact tree.

The canonical merge must satisfy:

`MERGE_PARENT_COUNT = 2`

`MERGE_PARENT_1 = FROZEN_BASE`

`MERGE_PARENT_2 = VERIFIED_HEAD`

`MERGE_TREE = VERIFIED_HEAD_TREE`

`SQUASH_MERGE = PROHIBITED`

`REBASE_MERGE = PROHIBITED`

`FAST_FORWARD_SUBSTITUTION = PROHIBITED`

`CHANGED_HEAD = PROHIBITED`

`CHANGED_TREE = PROHIBITED`

A merge with different parent topology, head, tree, moved base, or missing post-merge verification is not authority-establishing.

## 14. Future Semantic-Clarification Boundary

Only if State 1 becomes canonical may a future clarification be prepared within exactly:

1. `docs/SOT.md`
2. `docs/phase-4/PHASE_4_NORMALIZED_EVIDENCE_BYTES_SEMANTIC_CLARIFICATION.md`

No third canonical repository path is authorized.

The future clarification may determine only:

1. the exact object measured by `normalized evidence bytes`;
2. the exact canonical representation whose bytes are counted;
3. the exact lifecycle point at which measurement occurs;
4. whether and how normalized content participates;
5. whether and how eligible-evidence metadata participates;
6. the relationship to the eligibility decision;
7. the relationship to deterministic resource accounting;
8. the relationship to integrity material without altering integrity trust semantics;
9. the relationship to evidence identity;
10. inclusive or exclusive byte-boundary semantics;
11. the exact deterministic pre-construction measurement or admission mechanism;
12. failure ownership within the existing Phase 4 failure taxonomy;
13. the exact resource reference carried by that failure;
14. the relationship to Phase 3 `maximum_canonical_bytes`; and
15. whether a distinct Phase 3 projection bound is necessary without changing Phase 3 semantics.

This proposal answers none of those questions.

## 15. Cross-Program Non-Drift

`DISPOSITION_A = PHASE_4_DOES_NOT_REQUIRE_ARCHITECTURE_TRUTH_CONTRACT_WORK`

`ARCP_WORKING_LABEL = ARCP`

`ARCP_CANONICAL_NAME = UNRESOLVED_PENDING_NEXUS_PHASE_19_GOVERNANCE`

`ARCP_CANONICAL_SEMANTICS = UNRESOLVED_PENDING_NEXUS_PHASE_19_GOVERNANCE`

`NEXUS_PHASE_19_DIRECTION = RESERVED_UPSTREAM_ARCHITECTURE_DIRECTION`

`NEXUS_PHASE_19_CANONICAL_CAPABILITY_NAME = MUST_BE_VERIFIED_FROM_CANONICAL_NEXUS_STATE`

AFR cannot independently define, rename, expand, or canonicalize ARCP or NEXUS Phase 19 through this proposal.

This proposal creates no NEXUS, ARCP, ATA, architecture-truth, integration, or runtime authority.

## 16. Prospective Scope and Historical Preservation

Any future clarification is prospective and limited to normalized-evidence-bytes measurement semantics only.

Historical canonical artifacts remain preserved and are not retroactively rewritten.

No unrelated Phase 4 semantic and no Phase 3 semantic is superseded by implication.

## 17. Implementation Stop and Authority Non-Leakage

`NORMALIZED_EVIDENCE_BYTES_CANONICAL_MEASUREMENT = NOT_ESTABLISHED`

Existing non-canonical implementation-candidate stop conditions remain active.

No older implementation candidate receives retroactive acceptance. After an eventual canonical semantic repair, a fresh implementation candidate must be prepared against the repaired canonical state.

This proposal creates no implementation, integration, live evidence collection, runtime evaluation, persistence, certificate, deployment, production, enforcement, remediation, or subsequent-phase authority.

## 18. Exact Proposed Root SoT Append

The lines between the following two proposal metadata markers are the exact proposed `docs/SOT.md` Section 25 append. The markers themselves belong only to this authority-proposal document and are not part of `docs/SOT.md`.

<!-- AFR_NORMALIZED_EVIDENCE_BYTES_SOT_SECTION_25_BEGIN -->
## 25. Phase 4 Normalized-Evidence-Bytes Semantic-Amendment Authority Proposal

Phase 4 operational-evidence intake and eligibility planning remains canonically complete and terminally closed.

This authority proposal is bound to exactly:

`EXPECTED_CANONICAL_BASE_COMMIT = 02f50963a6eaef49283722d6b9000eabe8a04a4c`

`EXPECTED_CANONICAL_BASE_TREE = bf7aed9b874c162294a57857ccfa334dd7eeb261`

`EXPECTED_CANONICAL_BASE_SOT_BLOB = ff8363878f01ac9666f49c68cc4eda280ba4958b`

If canonical `main` moves before this proposal reaches its canonical effective point:

`BASE_MOVED = STOP`

`SILENT_REBASE = PROHIBITED`

`SILENT_BASE_SUBSTITUTION = PROHIBITED`

The canonical Phase 4 deterministic resource surface remains exactly:

1. total ingress bytes;
2. envelope field count;
3. collection cardinality;
4. nesting depth;
5. provenance-chain length;
6. integrity-reference length;
7. normalized evidence bytes;
8. deterministic processing work units.

`NORMALIZED_EVIDENCE_BYTES_CANONICAL_NAME = EXISTING_CANONICAL`

Canonical Phase 4 does not establish the exact deterministic quantity measured by that resource.

`NORMALIZED_EVIDENCE_BYTES_CANONICAL_MEASUREMENT = NOT_ESTABLISHED`

This proposal establishes no equality, inequality, inclusion, exclusion, derivation, or substitution relationship between normalized evidence bytes and normalized content identity, normalized content bytes, final eligible-evidence bytes, pre-integrity evidence bytes, eligibility-decision-plus-evidence bytes, Phase 3 canonical bytes, or another representation.

`NORMALIZED_EVIDENCE_BYTES_RELATIONSHIP_SELECTION = NONE`

The existing canonical resource-failure rule remains exactly:

`Any violation fails closed before evidence construction.`

Eligibility remains pre-conformance. The only Phase 4 eligibility classifications remain `ELIGIBLE`, `INELIGIBLE`, `QUARANTINED`, `UNSUPPORTED`, and `PROCESSING_FAILURE`. This proposal does not authorize `CONFORMANT`, `NON_CONFORMANT`, `INCONCLUSIVE`, `STALE`, or another conformance result as an eligibility outcome.

The existing Phase 4 security and trust boundary is not expanded or redesigned by this proposal or by the bounded clarification it may later authorize.

`PHASE_4_SECURITY_TRUST_BOUNDARY_EXPANSION = PROHIBITED`

`EXISTING_PROVENANCE_TRUST_SEMANTICS = PRESERVED`

`EXISTING_INTEGRITY_TRUST_SEMANTICS = PRESERVED`

`EXISTING_TENANT_SUBJECT_ISOLATION = PRESERVED`

`EXISTING_FRESHNESS_TRUST_SEMANTICS = PRESERVED`

The existing Phase 4 presence, type, and deterministic-output semantics remain unchanged. Absent optional, explicit null, empty, missing required, unsupported value, unsupported type, and unsupported version remain distinct.

`PHASE_4_PRESENCE_TYPE_SEMANTICS = UNCHANGED`

`PHASE_4_DETERMINISM_SEMANTICS = UNCHANGED`

`DEFAULTING = PROHIBITED`

`COERCION = PROHIBITED`

`AMBIENT_INFERENCE = PROHIBITED`

`SILENT_REPAIR = PROHIBITED`

Identical governed inputs must continue to produce byte-identical decision records and eligible-evidence representations.

Phase 3 continues to own its independent `maximum_canonical_bytes` resource semantic. This proposal does not redefine Phase 3 canonicalization, resource accounting, work-unit accounting, fingerprints, tests, vectors, or contracts.

`PHASE3_MAXIMUM_CANONICAL_BYTES_TO_NORMALIZED_EVIDENCE_BYTES_RELATIONSHIP = NOT_ESTABLISHED`

The supported governance path is a bounded post-closure Phase 4 semantic amendment only.

`GENERAL_PHASE_4_REOPEN = NO`

The exact authority-proposal canonical boundary is:

1. `docs/SOT.md`
2. `docs/phase-4/PHASE_4_NORMALIZED_EVIDENCE_BYTES_SEMANTIC_AMENDMENT_AUTHORITY_PROPOSAL.md`

No third canonical repository path is authorized by this proposal.

Before the complete authority-proposal effective point:

`AFR_PHASE_4_NORMALIZED_EVIDENCE_BYTES_SEMANTIC_AMENDMENT_AUTHORITY = NONE`

The proposal requests exactly:

`BOUNDED_NORMALIZED_EVIDENCE_BYTES_SEMANTIC_AMENDMENT_DOCUMENTATION_ONLY`

If and only if the complete authority-proposal effective point is reached:

`AFR_PHASE_4_NORMALIZED_EVIDENCE_BYTES_SEMANTIC_AMENDMENT_AUTHORITY = BOUNDED_NORMALIZED_EVIDENCE_BYTES_SEMANTIC_AMENDMENT_DOCUMENTATION_ONLY`

The single-use authority lifecycle is exactly:

`STATE_0 = NONE`

`STATE_1 = BOUNDED_NORMALIZED_EVIDENCE_BYTES_SEMANTIC_AMENDMENT_DOCUMENTATION_ONLY`

`STATE_2 = CONSUMED_PENDING_CLOSURE`

`STATE_3 = CONSUMED_CLOSED`

Only `STATE_0 -> STATE_1 -> STATE_2 -> STATE_3` is permitted. No state implies the next and no state may be skipped.

State 1 becomes effective if and only if all of the following occur in order under separately governed gates:

1. the candidate remains limited to the exact two-document canonical boundary and both complete future repository-file preimages are established against the exact frozen base;
2. the complete two-object preimage set passes independent integrated adversarial acceptance review before freeze;
3. every blocking finding is resolved in a fresh exact accepted candidate;
4. exact-content freeze is separately authorized and executed for both complete preimages;
5. deterministic serialization freeze is separately authorized and executed for both complete preimages;
6. SHA-256 computation and freeze is separately authorized and executed over the exact frozen serialized bytes;
7. post-freeze identity and integrity reverification passes without content, serialization, or base drift;
8. repository materialization of exactly the two frozen objects is separately authorized and executed;
9. exact staging is separately authorized and verified against the frozen identities;
10. the exact proposal commit is separately authorized and created with the verified parent, tree, boundary, and frozen identities;
11. the remote proposal branch preserves the exact reviewed commit and tree;
12. a draft pull request into canonical `main` preserves the exact reviewed identity;
13. the pull request receives independent acceptance review at that exact identity;
14. the pull request is explicitly transitioned from draft to ready;
15. explicit merge authorization is granted for that exact ready-state identity;
16. the exact reviewed proposal is merged using the required two-parent topology;
17. post-merge identity, ordered parents, tree, exact two-document boundary, and frozen content identities are independently verified;
18. local and remote canonical `main` converge on the verified merge; and
19. the canonical worktree and index are clean.

No earlier event establishes State 1. Candidate preparation, review, freeze, hash computation, materialization, staging, commit, publication, draft-PR creation, PR review, Ready transition, merge authorization, or merge alone does not establish State 1.

`MERGE_WITHOUT_PRIOR_READY_TRANSITION = NOT_AUTHORITY_ESTABLISHING`

`MERGE_WITHOUT_EXPLICIT_MERGE_AUTHORIZATION = NOT_AUTHORITY_ESTABLISHING`

`MERGE_WITHOUT_POST_MERGE_VERIFICATION = NOT_AUTHORITY_ESTABLISHING`

For the State-1 canonical merge, let:

`FROZEN_BASE = 02f50963a6eaef49283722d6b9000eabe8a04a4c`

Let `VERIFIED_HEAD` be the exact independently reviewed proposal commit and `VERIFIED_HEAD_TREE` its exact tree.

The merge must satisfy:

`MERGE_PARENT_COUNT = 2`

`MERGE_PARENT_1 = FROZEN_BASE`

`MERGE_PARENT_2 = VERIFIED_HEAD`

`MERGE_TREE = VERIFIED_HEAD_TREE`

`SQUASH_MERGE = PROHIBITED`

`REBASE_MERGE = PROHIBITED`

`FAST_FORWARD_SUBSTITUTION = PROHIBITED`

`CHANGED_HEAD = PROHIBITED`

`CHANGED_TREE = PROHIBITED`

A merge with different parent topology, head, tree, moved base, or missing post-merge verification does not establish State 1.

If State 1 is established, the exact future semantic-clarification canonical boundary is:

1. `docs/SOT.md`
2. `docs/phase-4/PHASE_4_NORMALIZED_EVIDENCE_BYTES_SEMANTIC_CLARIFICATION.md`

No third canonical repository path is authorized.

That future clarification may determine only:

1. the exact object measured by `normalized evidence bytes`;
2. the exact canonical representation whose bytes are counted;
3. the exact lifecycle point at which measurement occurs;
4. whether and how normalized content participates;
5. whether and how eligible-evidence metadata participates;
6. the relationship to the eligibility decision;
7. the relationship to deterministic resource accounting;
8. the relationship to integrity material without altering integrity trust semantics;
9. the relationship to evidence identity;
10. inclusive or exclusive byte-boundary semantics;
11. the exact deterministic pre-construction measurement or admission mechanism;
12. failure ownership within the existing Phase 4 failure taxonomy;
13. the exact resource reference carried by that failure;
14. the relationship to Phase 3 `maximum_canonical_bytes`; and
15. whether a distinct Phase 3 projection bound is necessary without changing Phase 3 semantics.

This authority proposal answers none of those fifteen questions.

The controlling cross-program disposition remains:

`DISPOSITION_A = PHASE_4_DOES_NOT_REQUIRE_ARCHITECTURE_TRUTH_CONTRACT_WORK`

`ARCP_WORKING_LABEL = ARCP`

`ARCP_CANONICAL_NAME = UNRESOLVED_PENDING_NEXUS_PHASE_19_GOVERNANCE`

`ARCP_CANONICAL_SEMANTICS = UNRESOLVED_PENDING_NEXUS_PHASE_19_GOVERNANCE`

`NEXUS_PHASE_19_DIRECTION = RESERVED_UPSTREAM_ARCHITECTURE_DIRECTION`

`NEXUS_PHASE_19_CANONICAL_CAPABILITY_NAME = MUST_BE_VERIFIED_FROM_CANONICAL_NEXUS_STATE`

AFR cannot independently define, rename, expand, or canonicalize ARCP or NEXUS Phase 19 through this proposal. This proposal creates no NEXUS, ARCP, ATA, architecture-truth, integration, or runtime authority.

Any future clarification is prospective and limited to normalized-evidence-bytes measurement semantics. Historical canonical artifacts remain preserved and are not retroactively rewritten.

The semantic-amendment authority remains documentation-only throughout State 1.

This authority proposal does not clear any non-canonical implementation-candidate stop condition and creates no implementation, integration, live collection, runtime evaluation, persistence, certificate, deployment, production, enforcement, remediation, or subsequent-phase authority.

State 2 may be established only after a separately governed normalized-evidence-bytes semantic clarification is canonically merged and its complete post-merge verification succeeds.

State 3 may be established only through a separately governed canonical closure after State 2.

`STATE_2_TO_STATE_3_REQUIRES = SEPARATELY_GOVERNED_CANONICAL_CLOSURE`

No gate implies the next.
<!-- AFR_NORMALIZED_EVIDENCE_BYTES_SOT_SECTION_25_END -->

## 19. No Implicit Progression

No gate implies the next.
