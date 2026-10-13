# AFR Phase 9 — Acceptance Criteria

1. Phase 8 remains canonically closed; reopen authority is `NONE`.
2. AFR predecessor is exactly `323b23d51ec7b4027b00adbb59ea716607ce455e`.
3. NEXUS reference main is exactly `a59327a5d829399048e64c37967b7bc4cb057739`.
4. Contract path and ID are exact.
5. Frozen NEXUS contract SHA-256 is `a6abb49d5536de89d21131abf7d2d717a242f33b1e4c4f9d8966bd48dc465246`.
6. The target is treated as non-canonical until NEXUS separately closes canonicalization.
7. NEXUS architecture truth remains distinct from AFR conformance result.
8. AFR finding remains distinct from ArchitectureRisk.
9. AFR conformance remains distinct from NEXUS architecture acceptance.
10. AFR read authority remains distinct from NEXUS mutation authority.
11. Required snapshot identity/version, acceptance, package, provenance, integrity, compatibility, supersession/currentness, risk-reference, conformance-reference, and consumer-limitation fields are explicit.
12. Unsupported contract/compatibility versions fail closed.
13. Missing provenance fails closed.
14. Integrity mismatch fails closed.
15. Non-accepted source architecture fails closed.
16. Stale-reference and supersession ambiguity fail closed.
17. Authority-domain ambiguity fails closed.
18. Structural similarity alone never establishes compatibility.
19. Phase 9 implementation authority remains `NONE` until NEXUS makes the architecture-truth export contract canonical through its own governed effective point.
20. AFR cannot satisfy that prerequisite by copying/recreating the candidate or by local equivalence.
21. AFR provides conformance evidence; NEXUS Phase 17 interprets architecture risk.
22. ARCP contract validation is not AFR operational conformance.
23. ARCP consumer compatibility is not AFR evidence eligibility.
24. Final NEXUS/ARCP certification remains deferred to AFR Phase 14.
25. The detached candidate contains exactly six documents, all mode 0644, all identity-frozen.
26. Preparation mutates neither AFR nor NEXUS repositories.
27. Preparation grants no repository materialization, implementation, runtime, deployment, production, network, credential, persistence, or integration authority.
28. Independent read-only acceptance is required before repository materialization can even be proposed.
29. Intermediate classification is `SEMANTICALLY_QUALIFIABLE_PENDING_NEXUS_CANONICALIZATION`.
30. Final current-NEXUS compatibility later resolves explicitly to `PASS` or `NONPASS`.
