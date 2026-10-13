# AFR NEXUS Architecture-Truth Consumer Qualification Contract

This AFR-owned qualification contract determines whether a NEXUS-owned truth snapshot is eligible for later AFR conformance processing. It is not the NEXUS producer contract and cannot canonicalize or replace it.

Prospective producer contract: `NEXUS_TO_AFR_ARCHITECTURE_TRUTH_CONSUMER_CONTRACT_V1`.
Frozen candidate SHA-256: `a6abb49d5536de89d21131abf7d2d717a242f33b1e4c4f9d8966bd48dc465246`.
Current source-contract status: `NON_CANONICAL`.

Planned result domain: `COMPATIBLE | INCOMPATIBLE | ERROR`.

`COMPATIBLE` means compatible with AFR's consumer profile and potentially eligible for later AFR conformance, subject to separate evidence and authorization requirements. It does not mean conformant and does not mean NEXUS-accepted beyond the source acceptance state.

`INCOMPATIBLE` means a well-formed source is outside the supported AFR compatibility profile.

`ERROR` means the source cannot be deterministically or safely qualified.

AFR preserves all NEXUS-owned identities, provenance, acceptance state, supersession/currentness, ArchitectureRisk references, and NEXUS conformance-request references without rewriting.

```text
AFR_COMPATIBLE != AFR_CONFORMANT
AFR_CONFORMANT != NEXUS_ACCEPTED
AFR_FINDING != ARCHITECTURE_RISK
AFR_FINDING_REFERENCE != ARCHITECTURE_RISK_MUTATION_AUTHORITY
```

Qualification fails closed on missing/unsupported versions, missing snapshot identity, invalid acceptance binding, missing package identity/revision/fingerprints, missing provenance, integrity mismatch, ambiguous acceptance/supersession/staleness, authority ambiguity, or attempted cross-domain promotion/mutation.

Runtime use is prohibited until the NEXUS producer contract is canonical. Documentary planning may test semantic mapping against the frozen candidate only.

No repository, network, credential, persistence, connector, adapter, API, runtime, deployment, production, NEXUS mutation, ArchitectureRisk mutation, or ARCP authority is granted.
