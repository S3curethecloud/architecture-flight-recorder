# AFR Operational Evidence Admissibility and Truth-Binding Contract

## 1. Contract posture

`CONTRACT_STATUS=DETACHED_PLANNING_CANDIDATE_NONCANONICAL`

This contract candidate defines the semantics required before AFR may later admit
operational evidence for evaluation against qualified NEXUS architecture truth.
It is not an ingestion API, runtime schema implementation, conformance result, or
NEXUS contract replacement.

## 2. Frozen truth anchor

For this Phase 10 planning candidate:

- AFR predecessor: `b18281502501f41928f0585cf72ff4715f2c5414`
- NEXUS qualified main: `ef1c048ef3c6daaca2f6f1d35fd52341227843b5`
- observed contract-preserving NEXUS current head: `bdbc4cf8bf5fcd925c18d49a78ee408773b3ee19`
- qualified-anchor rebind authority: `NONE`
- NEXUS consumer contract ID: `NEXUS_TO_AFR_ARCHITECTURE_TRUTH_CONSUMER_CONTRACT_V1`
- NEXUS consumer contract SHA-256: `a6abb49d5536de89d21131abf7d2d717a242f33b1e4c4f9d8966bd48dc465246`

A mutable branch name such as `main` or an implicit `latest` value is never a
sufficient truth-binding identity.

## 3. Required future evidence envelope semantics

A future canonical contract must classify each field as REQUIRED, CONDITIONALLY
REQUIRED, OPTIONAL, or FORBIDDEN for each evidence class. At minimum the model must
be able to represent:

`evidence_contract_version`  
`evidence_id`  
`evidence_class`  
`producer_id`  
`source_id`  
`subject_type`  
`subject_id`  
`environment_id`  
`tenant_or_scope_id`  
`observed_at`  
`captured_at`  
`sequence_id`  
`original_content_digest_algorithm`  
`original_content_digest`  
`canonicalization_version`  
`canonical_content_digest_algorithm`  
`canonical_content_digest`  
`provenance_reference`  
`custody_reference`  
`classification`

No field may be treated as trustworthy merely because a producer asserts it.

## 4. Admissibility outcome

The planned admissibility result is:

`ADMITTED` or `REJECTED`

with stable reason codes and the exact input/contract identities used. There is no
third state that silently treats unknown or partially validated evidence as usable.

`ADMITTED != CONFORMANT`  
`REJECTED != NONCONFORMANT`  
`ADMITTED != NEXUS_ACCEPTED`  
`REJECTED != NEXUS_RISK`

## 5. Mandatory fail-closed classes

A future verifier must reject, at minimum:

- missing required identity;
- unknown critical contract/schema/canonicalization version;
- truth-anchor mismatch;
- subject mismatch;
- applicable tenant/scope mismatch;
- applicable environment mismatch;
- original or canonical digest mismatch;
- canonicalization disagreement;
- unsupported provenance/custody requirement;
- impossible required chronology;
- disallowed duplicate or replay;
- stale evidence outside explicit policy;
- incomplete required evidence set;
- cross-subject evidence substitution;
- evidence-set membership or ordering ambiguity;
- conflicting evidence without an explicit deterministic conflict rule.

## 6. Deterministic binding identity

The later implementation contract must define a canonical binding preimage that
covers, at minimum:

1. binding-contract version;
2. exact qualified truth reference identity;
3. exact admissibility-decision identity;
4. exact admitted evidence identity or deterministic evidence-set identity;
5. canonicalization/version identities required to reproduce the result.

The binding digest algorithm and byte preimage must be explicit. The digest must
not be computed over a mutable alias, display label, filesystem path, database row
number, or transport URL as the sole identity.

## 7. Provenance preservation

Normalization may create canonical bytes for deterministic evaluation but must not
destroy the identity of the originally received evidence. The contract therefore
preserves both original-content identity and canonical-content identity whenever a
transformation occurs.

Any transformation that materially changes semantics rather than representation is
outside canonicalization and requires a separately named processing step with its
own version and evidence identity.

## 8. Replay and duplicate semantics

Duplicate and replay classification must be based on explicit identities and policy,
not arrival order alone. A later contract must distinguish benign duplicate receipt,
replay attack, legitimate repeated observation, and correction/supersession without
silently overwriting prior evidence history.

## 9. Conflict semantics

When two otherwise admissible evidence objects conflict, admissibility does not
silently choose whichever arrived last. The future contract must either define a
deterministic resolution policy for that evidence class or emit a stable conflict
condition for later governed handling.

## 10. Authority boundary

This candidate grants no authority to ingest evidence, query a provider, create a
collector credential, deploy code, persist runtime evidence, issue AFR findings,
produce conformance judgments, mutate NEXUS, reinterpret NEXUS architecture risk,
or enter Phase 11.
