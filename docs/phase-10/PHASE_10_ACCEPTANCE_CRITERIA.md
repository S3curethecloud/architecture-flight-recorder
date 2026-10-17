# AFR Phase 10 — Truth and Operational Evidence Binding Acceptance Criteria

A Phase 10 planning package is acceptable only if every criterion below passes.
Failure or ambiguity in any required criterion is a NONPASS and grants no successor
implementation, runtime, ingestion, conformance, NEXUS-mutation, or Phase 11 authority.

## A. Canonical lineage

1. Phase 9 remains terminally closed and is not reopened.
2. AFR predecessor OID is exactly `b18281502501f41928f0585cf72ff4715f2c5414`.
3. AFR predecessor tree is exactly `f4c61f45a0dae6a4d8ac3d59c1718e6567d7d386`.
4. Phase 9 closure SHA-256 is exactly `7db297f661daca9a2e8e2b9473c7f315ee6a25db09d02d440e440a8ca5446de7`.
5. qualified NEXUS OID is exactly `ef1c048ef3c6daaca2f6f1d35fd52341227843b5`.
6. NEXUS contract SHA-256 is exactly `a6abb49d5536de89d21131abf7d2d717a242f33b1e4c4f9d8966bd48dc465246`.
7. no mutable alias is treated as sufficient qualification identity.

Reconciled dependency observation: current NEXUS `main` is `bdbc4cf8bf5fcd925c18d49a78ee408773b3ee19`, exactly two commits ahead of the qualified anchor with the consumer-contract bytes preserved. This observation does not rebind criterion 5.

## B. Authority separation

8. NEXUS architecture truth is not represented as an AFR conformance result.
9. AFR findings are not represented as NEXUS architecture risk.
10. AFR conformance is not represented as NEXUS architecture acceptance.
11. AFR read authority is not represented as NEXUS mutation authority.
12. AFR evidence output does not claim Phase 17 risk-interpretation authority.
13. implementation authority remains NONE.
14. runtime authority remains NONE.
15. evidence-ingestion authority remains NONE.
16. findings/conformance effect remains NONE.
17. NEXUS mutation authority remains NONE.
18. Phase 11 entry authority remains NONE.

## C. Evidence identity and provenance

19. every evidence object has a contract/version identity.
20. every evidence object has an immutable evidence identity or deterministic derivation.
21. source/producer identity is explicit.
22. subject identity is explicit and cannot be inferred only from transport location.
23. environment identity is explicit when environment affects interpretation.
24. tenant/scope identity is explicit when multi-tenant or scoped evidence is possible.
25. original content digest is preserved when normalization occurs.
26. normalized/canonical content digest states its canonicalization version.
27. digest algorithm and covered bytes are unambiguous.
28. observation and capture timestamps have defined semantics.
29. sequence/order semantics are defined independently of storage enumeration order.
30. provenance/custody requirements are explicit for each evidence class.

## D. Deterministic admissibility

31. missing required fields fail closed.
32. unknown critical versions fail closed.
33. truth-anchor mismatch fails closed.
34. subject mismatch fails closed.
35. tenant/scope mismatch fails closed where applicable.
36. environment mismatch fails closed where applicable.
37. content-integrity mismatch fails closed.
38. chronology violation fails closed.
39. unsupported source/provenance fails closed.
40. duplicate/replay policy is deterministic.
41. stale-evidence policy is deterministic.
42. conflicting-evidence handling is deterministic and cannot silently choose a winner.
43. partial evidence-set failure cannot silently produce an admitted complete set.
44. evidence-set membership and ordering are deterministic.
45. the same preserved inputs and contract versions reproduce the same admissibility result.

## E. Truth-to-evidence binding

46. a binding record preserves the exact qualified truth identity.
47. a binding record preserves the exact admitted evidence identity or evidence-set identity.
48. a binding record preserves applicable contract/policy/canonicalization versions.
49. binding identity is deterministic from canonical covered fields.
50. binding cannot substitute evidence from another subject, tenant, environment, or truth anchor.
51. binding cannot erase rejected evidence history where later evidence is accepted.
52. admissibility result remains distinct from conformance result.

## F. Security and trust boundary

53. external operational evidence is untrusted until explicitly admitted.
54. evidence producers do not gain AFR authority by providing evidence.
55. evidence cannot grant NEXUS mutation or acceptance authority.
56. parser/canonicalization ambiguity is treated as a security failure.
57. oversized/malformed/hostile evidence handling is planned fail-closed.
58. secret material and unnecessary sensitive payloads are excluded from planning artifacts.
59. provenance metadata cannot be trusted solely because it is self-asserted by the producer.
60. replay, substitution, cross-scope confusion, and downgrade attacks are explicitly covered.

## G. Package and successor boundary

61. exact candidate document count is six.
62. candidate exists only in the detached preparation root.
63. AFR repository/index/refs/object database remain unchanged by preparation.
64. NEXUS repository remains unchanged.
65. no real operational evidence is ingested during planning.
66. no staging, commit, push, PR, Ready transition, merge, or branch deletion is authorized.
67. independent whole-package read-only acceptance is required before materialization.
68. planning acceptance alone does not authorize implementation.
69. implementation acceptance alone would not automatically authorize runtime ingestion.
70. Phase 11 remains independently gated.
