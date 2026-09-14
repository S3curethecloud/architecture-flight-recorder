# AFR Future Roadmap — Non-Authorizing Product Direction

## Status

`FUTURE_ROADMAP_STATUS = NON_AUTHORIZING_PRODUCT_DIRECTION_ONLY`

This document records approved future AFR product direction after the completed
Phase 4 first-slice terminal implementation closure.

It does not reopen Phase 4, activate Phase 5, grant another implementation
slice, authorize integration, authorize runtime evaluation, authorize provider
or NEXUS access, authorize ARCP implementation, authorize ATA use, authorize
PAA or Humanize integration, authorize persistence or deployment, or create any
other execution authority.

The current canonical authority boundary remains:

`AFR_PHASE_4_FIRST_SLICE_IMPLEMENTATION_STATUS = COMPLETE`

`AFR_PHASE_4_IMPLEMENTATION_AUTHORITY = CONSUMED_CLOSED`

`AFR_PHASE_4_ADDITIONAL_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_4_NEXUS_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_4_ARCP_AUTHORITY = NONE`

`AFR_PHASE_4_ATA_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_4_RUNTIME_EVALUATION_AUTHORITY = NONE`

`PHASE_5_START_AUTHORITY = NONE`

No future capability listed below is assigned a canonical phase number by this
roadmap. Any phase assignment, planning authority, implementation authority,
integration authority, runtime authority, or production authority requires a
separately governed future authority lifecycle.

## Completed Foundation

```text
Phase 0  Doctrine & Boundary
   COMPLETE

Phase 1  Contracts & Evaluation Semantics
   COMPLETE

Phase 2  Deterministic Conformance Kernel
   COMPLETE

Phase 3  Kernel Implementation Readiness
         + First Kernel Slice
   COMPLETE

Phase 4  Operational Evidence Intake & Eligibility
         + normalized-evidence semantics
         + first implementation slice
   COMPLETE FOR THE GOVERNED FIRST SLICE

-------------------- CURRENT BOUNDARY --------------------
```

## Future Capability Progression

The approved future product direction is:

1. complete additional bounded operational-evidence intake capability only
   through separately governed future implementation authority;
2. establish a read-only NEXUS architecture-truth ingestion boundary;
3. establish executable-architecture-contract verification integration if and
   only if NEXUS later canonically establishes the relevant Phase 19 contract
   name, schema, semantics, versioning, and producer authority;
4. bind approved architecture claims to eligible operational evidence without
   changing NEXUS architecture truth or Phase 4 evidence-eligibility semantics;
5. execute deterministic claim-to-evidence conformance evaluation through the
   AFR kernel;
6. support continuous conformance and architecture-drift detection;
7. govern findings freshness, validity, expiry, contradiction, re-evaluation,
   and lifecycle state;
8. produce cryptographically bound conformance certificates and reproducible
   evidence packages;
9. expose bounded conformance signals to ATA without granting AFR runtime
   commit authority;
10. expose bounded findings and remediation context to PAA without granting PAA
    authority to alter AFR findings or NEXUS architecture truth;
11. expose approved AFR evidence and conformance artifacts to Humanize for
    presentation without making Humanize a conformance or architecture source
    of truth; and
12. establish production persistence, deployment, observability, operational
    APIs, and hardening only under separately governed future authority.

The directional pipeline is:

```text
NEXUS approved architecture truth
        |
        +---- future executable architecture contract / ARCP-equivalent
        |     only after NEXUS canonical governance establishes it
        |
        v
AFR read-only architecture-contract ingestion
        |
        |
External operational observations
        |
        v
AFR evidence intake + eligibility
        |
        v
Eligible operational evidence
        |
        +------------------+
                           v
                  claim/evidence binding
                           |
                           v
                  deterministic AFR kernel
                           |
                           v
                    conformance result
                           |
             +-------------+-------------+
             |             |             |
             v             v             v
          findings     certificates    drift events
             |             |             |
             +-------------+-------------+
                           |
              +------------+------------+
              |            |            |
              v            v            v
             PAA        Humanize        ATA
       remediation/     governed     runtime-policy
       coordination    presentation      input
```

## Cross-Program Ownership Boundary

### NEXUS

NEXUS remains authoritative for approved architecture truth and architecture
decisions.

If NEXUS later canonically establishes an executable architecture-contract
capability, NEXUS remains the producer/owner of that contract truth. AFR may
consume such contracts only through a separately governed, immutable,
versioned, read-only consumer boundary.

AFR must not author, silently enrich, reinterpret, supersede, or mutate NEXUS
architecture truth.

### ARCP Working Direction

`ARCP_WORKING_LABEL = ARCP`

The working architectural direction is:

`NEXUS -> ARCP_OR_CANONICAL_EQUIVALENT -> AFR -> ATA`

This roadmap does not canonicalize the ARCP name or semantics.

`ARCP_CANONICAL_NAME = UNRESOLVED_PENDING_NEXUS_PHASE_19_GOVERNANCE`

`ARCP_CANONICAL_SEMANTICS = UNRESOLVED_PENDING_NEXUS_PHASE_19_GOVERNANCE`

AFR's future role is verification of operational reality against an approved
contract, not authorship of the architecture contract and not runtime
enforcement.

### ATA

ATA remains consequential runtime transaction-assurance and commit authority.
AFR may eventually provide deterministic conformance signals or certificates as
inputs to ATA policy evaluation. An AFR result must never independently grant
runtime authority.

### Personal Architect Agent

PAA may eventually consume immutable AFR findings, evidence references,
conformance state, and remediation context to explain findings, initiate review,
and coordinate proposed remediation.

PAA must not alter AFR findings, fabricate conformance state, modify NEXUS
architecture truth, or convert an AFR finding directly into execution
authority.

### Humanize

Humanize may eventually consume approved AFR findings, evidence, certificates,
and provenance for executive, client, audit, and delivery presentation.

Humanize remains presentation and delivery authority only. Presentation must
not become architecture truth, AFR conformance truth, or runtime authority.

## Reserved Future Contract Sequence

The directional contract sequence is reserved as follows. These names are
working descriptions only and create no active contract or integration
authority.

1. `NEXUS_TO_AFR_ARCHITECTURE_TRUTH_AND_EXECUTABLE_CONTRACT_CONSUMER_CONTRACT`
   - first cross-program contract dependency;
   - producer: NEXUS;
   - consumer: AFR;
   - read-only, immutable, versioned, provenance-aware;
   - must wait for canonical NEXUS Phase 19 naming and semantics where the
     executable architecture-contract capability is involved.

2. `AFR_TO_ATA_CONFORMANCE_SIGNAL_CONTRACT`
   - consumes stable AFR conformance results/certificates;
   - does not transfer runtime commit authority to AFR.

3. `AFR_TO_PAA_FINDINGS_AND_REMEDIATION_COORDINATION_CONTRACT`
   - consumes stable AFR findings and evidence references;
   - supports explanation, review initiation, and proposed remediation;
   - creates no authority to alter findings or execute remediation.

4. `AFR_TO_HUMANIZE_CONFORMANCE_EVIDENCE_PRESENTATION_CONTRACT`
   - consumes approved AFR evidence/findings/certificates;
   - read-only and provenance-preserving;
   - supports governed client, executive, audit, and delivery presentation;
   - Humanize remains downstream and non-authoritative for conformance.

The first contract should be the NEXUS-to-AFR consumer contract because AFR
requires authoritative architecture truth before downstream systems can safely
consume AFR-derived conformance findings. PAA and Humanize contracts should be
designed only after the AFR finding/certificate surfaces they consume are
canonically stable.

## Non-Drift Rules

`ROADMAP_DIRECTION != PLANNING_AUTHORITY`

`ROADMAP_DIRECTION != IMPLEMENTATION_AUTHORITY`

`DEPENDENCY_RECOGNITION != INTEGRATION_PLANNING_AUTHORITY`

`INTEGRATION_PLANNING_AUTHORITY != INTEGRATION_IMPLEMENTATION_AUTHORITY`

`INTEGRATION_IMPLEMENTATION_AUTHORITY != RUNTIME_AUTHORITY`

`CONFORMANCE_SIGNAL != RUNTIME_COMMIT_AUTHORITY`

`PRESENTATION != EVIDENCE_AUTHORITY`

`REMEDIATION_COORDINATION != REMEDIATION_EXECUTION`

`PHASE_5_START_AUTHORITY = NONE`

No item in this future roadmap may be represented as implemented, active,
authorized, canonical phase assignment, or runtime capability unless a later
separately governed canonical authority lifecycle establishes that state.
