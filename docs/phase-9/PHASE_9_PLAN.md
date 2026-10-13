# AFR Phase 9 — NEXUS Architecture-Truth Compatibility and Consumer-Contract Qualification Plan

## Mission
Phase 9 establishes the AFR-side planning boundary required to consume NEXUS-owned architecture truth through an explicit, versioned, deterministic, read-only, fail-closed contract. It is not a runtime integration phase.

## Frozen identities
AFR predecessor: `323b23d51ec7b4027b00adbb59ea716607ce455e`
NEXUS reference main: `a59327a5d829399048e64c37967b7bc4cb057739`
NEXUS contract ID: `NEXUS_TO_AFR_ARCHITECTURE_TRUTH_CONSUMER_CONTRACT_V1`
NEXUS contract SHA-256: `a6abb49d5536de89d21131abf7d2d717a242f33b1e4c4f9d8966bd48dc465246`
Current contract posture: `DETACHED_FUTURE_CONTRACT_CANDIDATE_R1_NON_CANONICAL`
Current NEXUS AFR integration authority: `NONE`

## Ownership
NEXUS owns architecture identity/version, acceptance identity, package revision/fingerprint, provenance, supersession/currentness, truth-snapshot identity/version, integrity fingerprint, compatibility version, ArchitectureRisk references, and NEXUS conformance-request references.
AFR owns AFR conformance-request identity, AFR execution state, AFR conformance result, AFR finding, and AFR stale-reference evaluation outcome.

## Compatibility dimensions
Phase 9 plans qualification of contract identity/version, truth-snapshot identity/version, acceptance binding, package identity/revision/fingerprints, source version identity, object acceptance, provenance, integrity, supersession/currentness, stale-reference behavior, compatibility version, ArchitectureRisk references, NEXUS conformance-request references, consumer limitations, authority separation, and fail-closed behavior.

## Existing NEXUS interlock reuse
Reuse is partial and limited to semantically equivalent NEXUS-owned acceptance, package, provenance, version, supersession, read-only projection, and NEXUS conformance-reference semantics. The NEXUS conformance-result contract MUST NOT become AFR's conformance-result contract.

## Planned logical result domain
`COMPATIBLE | INCOMPATIBLE | ERROR`

While the producer contract remains non-canonical, documentary planning may classify it only as `SEMANTICALLY_QUALIFIABLE_PENDING_NEXUS_CANONICALIZATION`. That is not runtime compatibility acceptance.

## Canonicalization prerequisite
The canonicalization owner is NEXUS.
AFR Phase 9 implementation authority MUST remain `NONE` while the NEXUS architecture-truth export boundary is not canonically closed.
AFR cannot satisfy this prerequisite by copying the contract, recreating it locally, or declaring structural equivalence.

## Fail-closed minimums
Missing/unsupported contract version, missing snapshot identity/version, missing or invalid acceptance binding, missing package identity/revision/fingerprints, missing provenance, integrity mismatch, ambiguous acceptance, stale-reference ambiguity, supersession ambiguity, unsupported compatibility version, authority ambiguity, attempted NEXUS mutation, attempted AFR-finding promotion to ArchitectureRisk, or attempted AFR-result promotion to NEXUS acceptance all fail closed.

## Phase 17 / ARCP
AFR evidence may later be consumed by Phase 17 only under separately governed authority. `AFR_FINDING != ARCHITECTURE_RISK`.
Phase 9 does not activate Phase 19 or ARCP. Final NEXUS/ARCP compatibility certification is deferred to AFR Phase 14.

## Planned sequence
P9.1 source acquisition and identity qualification.
P9.2 field ownership/preservation mapping.
P9.3 compatibility/version matrix.
P9.4 deterministic fail-closed vectors.
P9.5 acceptance/provenance/integrity/supersession qualification.
P9.6 NEXUS canonical-contract dependency revalidation.
P9.7 implementation-authority proposal only after the NEXUS canonical prerequisite is satisfied.
P9.8 separately governed implementation/acceptance.
P9.9 current-NEXUS compatibility decision and Phase 9 closure.

## Exclusions
No repository mutation, NEXUS canonicalization, connector, API, transport, network, credential, persistence, runtime, deployment, remediation, enforcement, production, or cross-domain mutation authority is created.

`PHASE_9_IMPLEMENTATION_AUTHORITY = NONE`
`AFR_NEXUS_INTEGRATION_AUTHORITY = NONE`
