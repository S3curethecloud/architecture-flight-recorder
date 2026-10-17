# AFR Phase 10 — Truth and Operational Evidence Binding Plan

## 1. Status and authority

- Phase: 10 — Truth and Operational Evidence Binding
- Artifact posture: DETACHED PLANNING CANDIDATE — NONCANONICAL
- Authority: planning and contract preparation only
- Implementation authority: NONE
- Runtime authority: NONE
- Operational-evidence ingestion authority: NONE
- AFR findings effect: NONE
- AFR conformance effect: NONE
- NEXUS mutation authority: NONE
- Phase 11 entry authority: NONE

## 2. Frozen predecessor and dependency identities

Phase 10 planning is anchored to the terminal Phase 9 canonical state and to the
qualified NEXUS architecture-truth consumer boundary. No floating `latest`, branch
name, mutable tag, timestamp-only reference, or repository display state may
replace these immutable identities in a later qualification decision.

- AFR canonical predecessor main OID: `b18281502501f41928f0585cf72ff4715f2c5414`
- AFR canonical predecessor tree: `f4c61f45a0dae6a4d8ac3d59c1718e6567d7d386`
- Phase 9 closure record SHA-256: `7db297f661daca9a2e8e2b9473c7f315ee6a25db09d02d440e440a8ca5446de7`
- qualified NEXUS main OID: `ef1c048ef3c6daaca2f6f1d35fd52341227843b5`
- observed contract-preserving current NEXUS main OID: `bdbc4cf8bf5fcd925c18d49a78ee408773b3ee19`
- qualified-anchor rebind authority: `NONE`
- NEXUS contract ID: `NEXUS_TO_AFR_ARCHITECTURE_TRUTH_CONSUMER_CONTRACT_V1`
- NEXUS contract SHA-256: `a6abb49d5536de89d21131abf7d2d717a242f33b1e4c4f9d8966bd48dc465246`

## 3. Objective

Define the deterministic contract by which qualified NEXUS architecture truth can
be bound to independently identifiable operational evidence without allowing the
evidence channel to redefine architecture truth, mutate NEXUS, silently widen AFR
authority, or produce a conformance conclusion before later implementation and
runtime gates explicitly authorize those effects.

## 4. Planned model

The planned Phase 10 model contains four logical layers:

1. **Qualified truth reference** — immutable NEXUS repository, commit, contract,
   exported subject, and applicable contract-version identity.
2. **Evidence identity and provenance envelope** — immutable producer/source,
   subject, environment, tenant/scope where applicable, capture/observation time,
   sequence, content digest, normalization/canonicalization version, and custody
   metadata sufficient to distinguish one evidence object from every substitute.
3. **Admissibility decision** — deterministic validation of identity, integrity,
   chronology, completeness, provenance, scope, duplication/replay, and contract
   compatibility, with stable fail-closed rejection semantics.
4. **Truth-to-evidence binding record** — deterministic binding of one qualified
   truth identity to one admitted evidence identity or declared evidence set,
   preserving both source identities and the exact policy/contract versions used.

## 5. Required deterministic properties

A later implementation plan must preserve these requirements:

- canonical serialization is versioned and byte-reproducible;
- all digests state algorithm and covered bytes;
- mutable aliases never substitute for immutable source identities;
- normalization cannot erase source identity or original-content digest;
- ordering and chronology are explicit rather than inferred from file order;
- duplicate, replayed, stale, cross-subject, cross-tenant, and cross-environment
  evidence is rejected unless a later contract explicitly defines a safe case;
- a missing required identity or provenance field fails closed;
- evidence-set membership and ordering are deterministic;
- admissibility does not equal conformance;
- conformance does not equal NEXUS architecture acceptance or risk interpretation;
- every accepted binding is reproducible from preserved inputs and contract versions.

## 6. Planned validation campaign

Before any implementation authority can be considered, an independently accepted
Phase 10 contract must define positive and negative fixtures for at least:

- exact qualified truth anchor;
- stale or unknown truth anchor;
- altered NEXUS contract identity;
- correct evidence identity and digest;
- payload tampering;
- missing or ambiguous subject identity;
- source/provenance substitution;
- environment or tenant mismatch;
- chronology inversion and impossible time relationships;
- duplicate and replayed evidence;
- conflicting evidence objects;
- evidence-set ordering ambiguity;
- canonicalization/version mismatch;
- incomplete custody chain where custody is required;
- unknown critical field/version;
- partial evidence-set failure;
- deterministic re-evaluation of the same preserved inputs.

## 7. Sequencing

1. detached planning package preparation;
2. independent whole-package read-only acceptance;
3. separately authorized repository materialization and publication lifecycle;
4. canonical planning effective point and later terminal planning closure;
5. separately governed implementation-readiness review;
6. only then, if explicitly authorized, bounded implementation and offline fixtures;
7. separately governed runtime/evidence-ingestion qualification;
8. separately governed conformance-effect authority.

No earlier step implies a later one.

## 8. Non-goals

This plan does not ingest evidence, collect telemetry, call providers, deploy
collectors, issue findings, calculate conformance, mutate NEXUS, reinterpret NEXUS
risk, authorize Phase 17 actions, create implementation authority, or activate
Phase 11.
