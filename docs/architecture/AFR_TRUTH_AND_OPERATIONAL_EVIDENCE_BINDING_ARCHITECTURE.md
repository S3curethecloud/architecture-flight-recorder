# AFR Truth and Operational Evidence Binding Architecture

## 1. Architectural purpose

Phase 10 defines a one-way, identity-preserving relationship between qualified
NEXUS architecture truth and operational evidence presented to AFR. The boundary
exists so that operational observations can later be evaluated against a precise
architecture context without allowing observations to rewrite architecture truth
or allowing AFR to acquire NEXUS authority.

## 2. Architectural invariants

- `NEXUS_ARCHITECTURE_TRUTH != AFR_CONFORMANCE_RESULT`
- `AFR_FINDING != NEXUS_ARCHITECTURE_RISK`
- `AFR_CONFORMANCE != NEXUS_ARCHITECTURE_ACCEPTANCE`
- `AFR_READ_AUTHORITY != NEXUS_MUTATION_AUTHORITY`
- `AFR_ACCEPTED_CONFORMANCE_EVIDENCE != PHASE17_RISK_INTERPRETATION`

The qualified NEXUS anchor is immutable for a binding evaluation. The reconciled current
NEXUS `main` at preparation is `bdbc4cf8bf5fcd925c18d49a78ee408773b3ee19`,
which preserves the qualified consumer-contract bytes but does not replace or rebind
`ef1c048ef3c6daaca2f6f1d35fd52341227843b5`. A future newer NEXUS `main` is a
different observed dependency state and must not silently replace the qualified anchor.

## 3. Logical components

### 3.1 QualifiedTruthReference

Planned fields:

- producer repository identity;
- immutable producer commit OID;
- contract ID and contract digest;
- exported architecture subject identity;
- optional architecture-artifact identity/digest where required;
- qualification/evaluation contract version.

### 3.2 EvidenceEnvelope

Planned fields:

- evidence schema/version;
- evidence ID;
- evidence class/source kind;
- producer/source ID;
- subject ID and subject type;
- environment ID;
- tenant/scope ID where applicable;
- observed-at and captured-at semantics;
- sequence/order identity;
- original payload digest;
- canonical payload digest and canonicalization version;
- provenance/custody references;
- classification/sensitivity metadata where needed for safe handling.

The envelope is descriptive input. It grants no authority and is untrusted until
admissibility succeeds.

### 3.3 AdmissibilityDecision

The admissibility layer validates identity, integrity, provenance, chronology,
scope, versions, duplication/replay, staleness, and evidence-set completeness.
The planned output is a deterministic `ADMITTED` or `REJECTED` result plus stable
reason codes and the exact contract versions used.

An `ADMITTED` result means only that the evidence is eligible for later governed
AFR evaluation. It does not mean the system conforms.

### 3.4 TruthEvidenceBindingRecord

The binding record preserves both sides of the relationship rather than collapsing
them. Its planned covered fields include:

- qualified truth reference identity;
- admitted evidence identity or evidence-set identity;
- admissibility decision identity;
- binding contract version;
- canonicalization/version identities;
- deterministic binding digest.

## 4. Deterministic canonicalization

A later implementation must define one versioned canonical serialization for each
hash-covered structure. Canonicalization must specify field ordering, encoding,
number/string/time representation, absent-vs-null handling, list ordering, set
ordering, Unicode treatment, and unknown-field behavior.

No implementation may hash an unspecified in-memory representation or rely on
map/dictionary iteration order.

## 5. Evidence-set model

Where a decision needs more than one evidence object, evidence-set identity must be
computed from explicit member identities under defined ordering rules. Duplicate
members, ambiguous ordering, partial fetches, or conflicting scope identities must
fail closed unless the accepted contract defines an explicit deterministic rule.

## 6. Time and sequence model

`observed_at`, `captured_at`, receipt time, and evaluation time are distinct concepts.
A contract must define which values are producer assertions, which are collector
facts, what clock/precision assumptions apply, what skew is tolerated, and which
chronology relationships are mandatory. Storage order never substitutes for event
sequence.

## 7. Fail-closed boundary

The architecture rejects ambiguity rather than repairing it silently. In particular:

- unknown critical schema/version;
- unknown truth anchor;
- digest mismatch;
- subject/scope mismatch;
- unsupported provenance;
- impossible chronology;
- replay/duplicate not explicitly permitted;
- conflicting evidence without deterministic policy;
- incomplete required evidence set;
- canonicalization disagreement.

## 8. Side-effect boundary

This architecture is planning only. It does not define or authorize a live
collector, provider credential, queue, database, runtime service, deployment,
telemetry subscription, evidence ingestion, finding generation, conformance engine,
NEXUS write path, or Phase 11 runtime.
