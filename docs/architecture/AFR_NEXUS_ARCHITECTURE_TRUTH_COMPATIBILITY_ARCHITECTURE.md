# AFR ↔ NEXUS Architecture-Truth Compatibility Architecture

NEXUS is the authoritative producer of accepted architecture truth. AFR is a read-only consumer of that truth and the authoritative producer of AFR conformance results.

```text
NEXUS canonical architecture truth
        |
        | immutable/versioned truth snapshot
        v
AFR NEXUS-truth compatibility boundary
        |
        | verified read-only projection
        v
AFR evidence binding and conformance evaluation
        |
        | AFR-owned findings/results
        v
authorized downstream consumers
```

The reverse path does not exist as mutation authority.

Ownership invariants:
`NEXUS_ARCHITECTURE_TRUTH != AFR_CONFORMANCE_RESULT`
`AFR_FINDING != ARCHITECTURE_RISK`
`AFR_CONFORMANCE != NEXUS_ARCHITECTURE_ACCEPTANCE`
`AFR_READ_AUTHORITY != NEXUS_MUTATION_AUTHORITY`

The current NEXUS target is `NEXUS_TO_AFR_ARCHITECTURE_TRUTH_CONSUMER_CONTRACT_V1`, presently non-canonical. Phase 9 may plan against its frozen semantics but cannot activate runtime consumption until NEXUS establishes the contract as canonical.

The future compatibility boundary is deterministic, provider-neutral, and fail closed. Same logical snapshot + same supported compatibility profile => same logical result and issue ordering. Wall-clock time, randomness, model output, provider ordering, UI state, and ambient repository state do not control compatibility.

NEXUS owns current/superseded truth. AFR may classify the snapshot used in an AFR evaluation as stale, but cannot refresh, supersede, or repair NEXUS truth under Phase 9 planning authority.

The existing NEXUS architecture-review interlock is reused only where semantics are compatible. AFR conformance results remain AFR-owned.

AFR may reference existing ArchitectureRisk identities but cannot create or mutate authoritative ArchitectureRisk.

Phase 17 may consume AFR conformance evidence under later authority and interpret architecture risk. It does not import AFR authority.

Phase 9 does not activate ARCP. Final NEXUS/ARCP compatibility certification remains Phase 14 work.

No implementation path is authorized by this planning candidate. A later implementation-authority proposal requires canonical AFR planning acceptance, canonical NEXUS producer contract, exact reacquisition of that canonical contract, rebinding of compatibility requirements, and separate implementation authority.
