# AFR Phase 12 - Drift, Findings, Conformance Certificates, and Command Center Acceptance Criteria

A Phase 12 planning package is acceptable only if every required criterion passes.
A planning PASS creates no implementation, runtime, deployment, or production authority.

## A. Canonical lineage

1. Phase 11 remains terminally closed and reopen authority is `NONE`.
2. canonical predecessor main is exactly `6e3789ff6f972bfffb5ea04031b874b419730dc2`.
3. canonical predecessor tree is exactly `8ca430c260f9171424d0329ed28ca128e76fbfc3`.
4. Phase 11 closure SHA-256 is exactly `95ac664def50bb0e785ea7df7ddded1f6c91c28ec5f406fbb99ecdb7a667a3bb`.
5. Phase 11 evaluation-result semantics remain upstream and unchanged.
6. the accepted roadmap keeps Phase 12, Phase 13, and Phase 14 in that order.
7. `AFR_V1_COMPLETION_TARGET=PHASE_14`.
8. Phase 13 is not treated as the terminal AFR V1 phase.

## B. Authority separation

9. planning authority is not implementation authority.
10. implementation authority is not runtime authority.
11. Command Center presentation is not execution authority.
12. Command Center visibility is not provider mutation authority.
13. certificate display is not certificate issuance authority.
14. AFR conformance is not NEXUS architecture acceptance.
15. AFR findings are not NEXUS architecture risk.
16. NEXUS read authority is not NEXUS mutation authority.
17. Phase 13 integration does not authorize Phase 12 finding reinterpretation.
18. Phase 14 hardening does not authorize Phase 12 semantic redefinition.
19. Phase 12 implementation authority remains `NONE`.
20. Phase 12 runtime authority remains `NONE`.
21. Command Center implementation authority remains `NONE`.
22. Command Center runtime authority remains `NONE`.
23. Phase 13 entry authority remains `NONE`.
24. Phase 14 entry authority remains `NONE`.

## C. Finding semantics

25. finding states are exactly `SUPPORTED`, `CONTRADICTED`, `STALE`, `INCONCLUSIVE`, and `EVIDENCE_UNAVAILABLE`.
26. each finding binds one exact source evaluation result or deterministic source set.
27. each finding binds tenant and subject scope.
28. each finding binds architecture truth identity.
29. each finding binds claim identity.
30. each finding binds evidence identity or explicit evidence-unavailable state.
31. each finding binds policy/evaluator/version identity.
32. each finding binds trusted-time context.
33. `EVIDENCE_UNAVAILABLE` cannot become `SUPPORTED`.
34. `INCONCLUSIVE` cannot collapse to `SUPPORTED`.
35. infrastructure failure cannot become `SUPPORTED`.
36. finding derivation is deterministic and model inference is non-authoritative.
37. accepted findings are immutable.
38. changed material inputs create a later finding linked by supersession.

## D. Drift semantics

39. drift requires a deterministic material change.
40. drift binds prior and current finding identity.
41. drift identifies the affected architecture claim.
42. drift identifies the exact material change class.
43. drift preserves prior and current source identities.
44. drift cannot modify NEXUS architecture truth.
45. absence of comparable prior state is not silently labeled drift.
46. repeated equivalent input cannot fabricate drift.
47. cross-tenant comparison fails closed.
48. cross-subject comparison fails closed.

## E. Certificate semantics

49. a certificate representation binds an exact finding set.
50. certificate scope cannot exceed evaluated and accepted finding scope.
51. certificate representation binds truth, evaluation, evidence, policy, and version identities.
52. certificate validity interval is explicit.
53. limitations and unresolved conditions are preserved.
54. certificate-content fingerprint is deterministic.
55. stale or expired required state cannot support a current certificate assertion.
56. certificate planning creates no signing authority.
57. certificate planning creates no issuance authority.
58. display of a certificate does not prove issuance.
59. later revocation or supersession cannot rewrite historical certificate content.
60. certificate authority state is visible in the Command Center.

## F. Architecture Conformance Score

61. a score is optional.
62. any score has a formula identity and version.
63. score denominator and exclusions are explicit.
64. score links to the exact finding set.
65. unresolved mandatory state may make the score unavailable.
66. `STALE`, `INCONCLUSIVE`, and `EVIDENCE_UNAVAILABLE` cannot be hidden as success.
67. score display cannot replace canonical finding states.
68. score computation cannot create architecture authority.

## G. Command Center durable shell

69. the Command Center is provider neutral.
70. the Command Center is read oriented in Phase 12.
71. the shell is stable across successor phases unless a separately governed breaking change is approved.
72. semantic surfaces are independent from route/page count.
73. all ten required semantic surfaces are represented.
74. authority state is visible.
75. evidence provenance is visible.
76. freshness and `as_of` state are visible.
77. limitations and warnings are visible.
78. unknown or unavailable state fails closed.
79. provider-specific payloads do not define shell contracts.
80. Command Center presentation cannot mutate authoritative results.

## H. Read-model and extension contracts

81. every read model has an explicit contract version.
82. every read model carries scope.
83. every read model carries source identity or fingerprint.
84. every read model carries authority state.
85. every read model carries freshness state.
86. capability registration has a stable capability ID.
87. capability registration declares read/write posture.
88. capability registration declares required authority.
89. capability presence does not inherit authority.
90. adapters are isolated from canonical finding semantics.
91. extension compatibility is explicit.
92. breaking changes require explicit versioning and governance.

## I. Phase 13 and Phase 14 continuity

93. Phase 13 extension points are frozen as additive adapter seams.
94. Phase 13 does not require routine shell replacement.
95. Phase 13 cannot silently add provider mutation authority.
96. Phase 14 hardening hooks are frozen for security, reliability, performance, observability, E2E, and compatibility.
97. Phase 14 does not require routine shell replacement.
98. Phase 14 hardening cannot redefine accepted finding states.
99. later phases may extend through stable or explicitly versioned contracts.
100. no successor phase inherits authority merely because a capability exists.

## J. Package and preparation boundary

101. candidate document count is exactly seven.
102. `docs/SOT.md` is an exact canonical copy plus one append-only Phase 12 section.
103. the six new Phase 12 planning paths do not preexist on canonical predecessor main.
104. candidate exists only in the detached preparation root.
105. AFR repository files, indexes, refs, objects, and worktree registry remain unchanged by preparation.
106. no provider access or operational-evidence ingestion occurs during preparation.
107. no finding or certificate runtime effect occurs during preparation.
108. no Command Center implementation occurs during preparation.
109. no repository materialization, staging, commit, push, PR, merge, or branch deletion is authorized.
110. independent whole-package read-only acceptance is required before repository materialization.
111. planning acceptance alone does not authorize implementation.
112. implementation acceptance alone does not authorize runtime.
113. runtime qualification remains separately governed.
114. Phase 13 remains independently gated.
115. Phase 14 remains independently gated.
116. no gate implies the next.
