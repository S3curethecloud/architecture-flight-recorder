# AFR Phase 11 - Continuous Conformance Evaluation Runtime Acceptance Criteria

A Phase 11 planning package is acceptable only if every required criterion passes.
A planning PASS creates no implementation or runtime authority.

## A. Canonical lineage

1. Phase 10 remains terminally closed and reopen authority is `NONE`.
2. canonical predecessor main is exactly `14a75d02aa7dfa7c254a56bcf66030937ef9e48c`.
3. canonical predecessor tree is exactly `b39815ce431f6502ce4cb7b7a645a1ebbb428d7e`.
4. Phase 10 closure SHA-256 is exactly `4e983e35256030c33ce4bbc3f3e41e2417c39cdc02234c5fe4ef1032bb001383`.
5. accepted Phase 10 package identity and fingerprint are preserved.
6. qualified NEXUS anchor remains `ef1c048ef3c6daaca2f6f1d35fd52341227843b5`.
7. NEXUS contract SHA-256 remains `a6abb49d5536de89d21131abf7d2d717a242f33b1e4c4f9d8966bd48dc465246`.
8. a mutable branch head cannot silently rebind the qualified NEXUS anchor.

## B. Authority separation

9. planning authority is not runtime execution authority.
10. admissibility is not conformance.
11. AFR conformance is not NEXUS architecture acceptance.
12. AFR findings are not NEXUS architecture risk.
13. NEXUS read authority is not NEXUS mutation authority.
14. a Phase 11 result is not a Phase 12 finding or certificate.
15. implementation authority remains `NONE`.
16. runtime authority remains `NONE`.
17. conformance-evaluation execution authority remains `NONE`.
18. operational-evidence ingestion authority remains `NONE`.
19. provider-read authority remains `NONE`.
20. Phase 12 entry authority remains `NONE`.

## C. Evaluation-cycle identity

21. every future evaluation cycle has one immutable cycle identity.
22. cycle identity binds tenant and subject.
23. environment and release are bound when applicable.
24. exact truth identity is bound.
25. exact admitted evidence-binding identity or deterministic evidence-set identity is bound.
26. claim-set identity is bound.
27. evaluation-definition, policy, evaluator, canonicalization, and fingerprint versions are bound.
28. trusted-time context and requested evaluation scope are bound.
29. material input change requires a distinct cycle identity.
30. input arrival order cannot substitute for canonical identity.

## D. Continuous reevaluation semantics

31. reevaluation triggers are explicit and versioned.
32. new admitted evidence may qualify a new cycle but cannot mutate a prior result.
33. new qualified truth may qualify a new cycle but cannot rewrite history.
34. policy or evaluator change requires a distinct cycle when material.
35. freshness expiration can invalidate current assertion without rewriting the old result.
36. duplicate trigger delivery cannot create conflicting authoritative results.
37. trigger detection is distinct from execution admission.
38. scheduler or queue metadata cannot create truth or evidence authority.

## E. Runtime state and concurrency

39. request identity, cycle identity, and attempt identity are distinct.
40. terminal completed results are immutable.
41. retries preserve prior attempt history.
42. concurrency rules prevent conflicting terminal results for one cycle identity.
43. abandoned or timed-out attempts remain explicit.
44. late completion cannot silently overwrite an accepted terminal result.
45. supersession links distinct cycle identities rather than mutating prior results.
46. unknown concurrency state fails closed.

## F. Kernel and evidence boundaries

47. Phase 11 does not redefine canonical evaluation outcomes.
48. Phase 11 does not redefine Phase 10 admissibility.
49. only admitted evidence bindings may enter positive conformance support.
50. raw provider payloads are not automatically eligible evidence.
51. model output cannot select rules or authoritative outcomes.
52. unresolved truth, evidence, policy, or version identity blocks authoritative execution.
53. infrastructure failure cannot produce `CONFORMANT`.
54. cross-tenant and cross-subject substitution fail closed.

## G. Time and freshness

55. observation, capture, admission, evaluation, and validity times remain distinct.
56. trusted-time semantics are explicit.
57. stale evidence cannot support a current conformant assertion.
58. an execution clock does not silently redefine evidence freshness.
59. freshness transitions are deterministic and reproducible.

## H. Result and successor boundary

60. result scope cannot exceed evaluated scope.
61. every result preserves exact truth, evidence, rule, policy, evaluator, and time bindings.
62. completed results preserve limitations and unresolved conditions.
63. Phase 11 does not emit Phase 12 findings.
64. Phase 11 does not issue Phase 12 certificates.
65. Phase 11 does not authorize remediation or deployment.
66. Phase 11 does not mutate NEXUS.
67. Phase 12 remains independently gated.

## I. Package and preparation boundary

68. candidate document count is exactly six.
69. `docs/SOT.md` is an exact canonical copy plus one append-only Phase 11 section.
70. the five new Phase 11 planning paths do not preexist on canonical predecessor main.
71. candidate exists only in the detached preparation root.
72. AFR repository files, index, refs, object database, and worktree registry remain unchanged by preparation.
73. NEXUS repository remains unchanged.
74. no provider access or operational-evidence ingestion occurs during preparation.
75. no repository materialization, staging, commit, push, PR, Ready transition, merge, or branch deletion is authorized.
76. independent whole-package read-only acceptance is required before repository materialization.
77. planning acceptance alone does not authorize implementation.
78. implementation acceptance alone does not automatically authorize runtime execution.
79. runtime qualification remains separately governed.
80. no gate implies the next.
