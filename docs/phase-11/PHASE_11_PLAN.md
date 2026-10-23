# AFR Phase 11 - Continuous Conformance Evaluation Runtime Plan

## 1. Status and authority

- Phase: 11 - Continuous Conformance Evaluation Runtime
- Artifact posture: DETACHED PLANNING CANDIDATE - NONCANONICAL
- Authority: planning and contract preparation only
- Implementation authority: NONE
- Runtime authority: NONE
- Conformance-evaluation execution authority: NONE
- Operational-evidence ingestion authority: NONE
- Provider-read authority: NONE
- Findings effect: NONE
- Certificate effect: NONE
- NEXUS mutation authority: NONE
- Phase 12 entry authority: NONE

## 2. Frozen predecessor and dependency identities

Phase 11 planning is anchored to terminal Phase 10 and the qualified NEXUS
consumer boundary.

- AFR canonical predecessor main OID: `14a75d02aa7dfa7c254a56bcf66030937ef9e48c`
- AFR canonical predecessor tree: `b39815ce431f6502ce4cb7b7a645a1ebbb428d7e`
- Phase 10 closure record SHA-256: `4e983e35256030c33ce4bbc3f3e41e2417c39cdc02234c5fe4ef1032bb001383`
- accepted Phase 10 package identity SHA-256: `abf2068133fa572cd2b4d2da064aae69f80d9f652be0a583bf86aaa50467ed22`
- accepted Phase 10 package fingerprint SHA-256: `13107091c7e0d72a8b5ab14e1124c8f13c3157d083988dd51a63d452151f6e83`
- qualified NEXUS anchor OID: `ef1c048ef3c6daaca2f6f1d35fd52341227843b5`
- Phase 10 closure-preparation NEXUS head: `2c30cbf50aef35f5e5855c24795316128955a2c1`
- NEXUS contract ID: `NEXUS_TO_AFR_ARCHITECTURE_TRUTH_CONSUMER_CONTRACT_V1`
- NEXUS contract SHA-256: `a6abb49d5536de89d21131abf7d2d717a242f33b1e4c4f9d8966bd48dc465246`

A live NEXUS head may be observed for compatibility, but it does not silently
replace the qualified immutable anchor.

## 3. Objective

Define the deterministic runtime contract by which AFR may later execute repeated
bounded conformance evaluations using qualified architecture truth and already
admitted, identity-preserving operational evidence bindings without collapsing
admissibility into conformance, converting AFR results into NEXUS architecture
acceptance, or creating Phase 12 findings and certificate authority.

## 4. Runtime planning model

The planned runtime contains these logical responsibilities:

1. evaluation-request admission;
2. immutable evaluation-cycle identity construction;
3. truth and evidence-binding qualification;
4. version and policy compatibility resolution;
5. deterministic kernel invocation;
6. result integrity and scope validation;
7. freshness and validity-window tracking;
8. repeat-evaluation trigger qualification;
9. attempt, retry, and concurrency control;
10. immutable result and supersession linkage;
11. non-authoritative observability and audit projection.

These are planning responsibilities, not implemented services.

## 5. Evaluation-cycle identity

Every future runtime cycle must bind, at minimum:

- tenant and subject;
- environment and release where applicable;
- qualified truth identity;
- admitted truth-to-evidence binding identity or set identity;
- evaluated claim set;
- evaluation-definition identity and version;
- conformance-policy identity and version;
- evaluator version;
- trusted-time context;
- canonicalization and fingerprint versions;
- requested evaluation scope;
- one immutable evaluation-cycle identity.

Material input changes require a new evaluation-cycle identity.

## 6. Continuous reevaluation triggers

A later runtime may qualify a reevaluation when an explicitly governed material
condition changes, including:

- a new admitted evidence binding;
- a new qualified architecture-truth snapshot;
- policy or evaluation-definition revision;
- evaluator or canonicalization version change;
- freshness or validity-window expiration;
- explicit bounded operator request.

Trigger observation alone does not authorize execution. A future implementation
must separate trigger detection, execution admission, and evaluation execution.

## 7. Deterministic runtime state

The planning contract must distinguish at least:

- request identity;
- evaluation-cycle identity;
- execution-attempt identity;
- current cycle state;
- terminal result identity when completed;
- blocked/failure state when evaluation cannot proceed;
- supersession linkage for a later distinct cycle.

Retries cannot rewrite a prior completed result. Duplicate delivery of the same
request cannot create conflicting authoritative results for one cycle identity.

## 8. Kernel boundary

Phase 11 does not redefine Phase 1 evaluation semantics or the Phase 2 kernel
contract. A later runtime must invoke only an independently accepted deterministic
kernel implementation under exact version and scope bindings.

The runtime cannot use model inference to select rules, repair evidence, select an
outcome, or manufacture a missing truth or evidence input.

## 9. Evidence boundary

Phase 11 planning consumes Phase 10 admissibility and truth-binding semantics. It
must not treat raw provider responses, transport payloads, filesystem location, or
arrival order as automatically eligible evaluation evidence.

Provider collection and operational-evidence ingestion remain separately governed.

## 10. Time and freshness boundary

Continuous evaluation requires explicit trusted-time semantics. A later runtime
must distinguish observation time, capture time, admission time, evaluation time,
validity window, and freshness deadline where applicable.

A scheduler clock or queue timestamp alone cannot silently establish evidence
freshness or truth currentness.

## 11. Retry and concurrency boundary

A later implementation must define deterministic rules for duplicate requests,
concurrent attempts, retries after failure, abandoned attempts, timeout, and late
completion. The contract must prevent two conflicting terminal results from being
accepted for the same evaluation-cycle identity.

No distributed-lock, queue, database, or consensus technology is selected here.

## 12. Result boundary

A completed Phase 11 evaluation result may represent bounded conformance under the
canonical evaluation semantics. It remains distinct from:

- a Phase 12 drift finding;
- a Phase 12 certificate;
- NEXUS architecture acceptance or risk interpretation;
- ATA consequential runtime authority;
- remediation or deployment authority.

## 13. Failure and fail-closed rules

The runtime must fail closed for unresolved mandatory identity, authority, scope,
version, evidence, rule, time, canonicalization, fingerprint, or concurrency
conditions. Runtime infrastructure failure cannot be translated into `CONFORMANT`.

## 14. Planned validation campaign

Before implementation authority can be considered, the accepted Phase 11 package
must support future positive and negative fixtures for at least:

- exact deterministic repeated evaluation;
- duplicate request deduplication;
- conflicting concurrent attempt suppression;
- stale evidence transition;
- changed truth snapshot;
- changed evidence binding;
- changed policy/evaluator version;
- invalid or unsupported version;
- missing mandatory evidence binding;
- cross-tenant and cross-subject substitution;
- retry after transient execution failure;
- terminal-result immutability;
- supersession by a distinct later cycle;
- model-output non-authority;
- Phase 12 effect remaining absent.

## 15. Sequencing

1. detached Phase 11 planning-package preparation;
2. independent whole-package read-only acceptance;
3. separately authorized repository materialization and publication lifecycle;
4. canonical Phase 11 planning effective point and terminal planning closure;
5. separately governed implementation-readiness review;
6. only then, if explicitly authorized, bounded implementation and offline tests;
7. separately governed runtime qualification;
8. only then, if explicitly authorized, bounded runtime execution;
9. Phase 12 remains independently gated.

No earlier step implies a later one.

## 16. Non-goals

This plan does not authorize source code, executable schemas, provider reads,
operational-evidence ingestion, queues, schedulers, databases, deployment,
continuous execution, findings, certificates, remediation, enforcement, NEXUS
mutation, or Phase 12 entry.
