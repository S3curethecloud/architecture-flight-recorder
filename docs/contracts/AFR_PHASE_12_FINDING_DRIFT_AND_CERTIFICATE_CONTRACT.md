# AFR Phase 12 Finding, Drift, and Conformance Certificate Contract

## 1. Contract posture

`CONTRACT_STATUS=DETACHED_PLANNING_CANDIDATE_NONCANONICAL`

This candidate defines future deterministic Phase 12 finding, drift, and certificate
representation semantics. It grants no implementation, issuance, signing, runtime,
or delivery authority.

## 2. Predecessor binding

- AFR predecessor main: `6e3789ff6f972bfffb5ea04031b874b419730dc2`
- AFR predecessor tree: `8ca430c260f9171424d0329ed28ca128e76fbfc3`
- Phase 11 closure SHA-256: `95ac664def50bb0e785ea7df7ddded1f6c91c28ec5f406fbb99ecdb7a667a3bb`

## 3. Finding contract principle

A Phase 12 finding is valid only when its derivation is deterministically traceable
to accepted Phase 11 evaluation state and all mandatory scope, identity, version,
time, provenance, and authority conditions are resolved.

## 4. Required future finding fields

A future executable contract must classify exact required fields. At minimum it
must support:

`finding_contract_version`
`finding_id`
`finding_state`
`tenant_id`
`subject_id`
`environment_id`
`release_id`
`architecture_truth_reference_id`
`claim_id`
`source_evaluation_cycle_id`
`source_evaluation_result_id`
`evidence_binding_or_set_id`
`finding_derivation_policy_id`
`finding_derivation_policy_version`
`evaluator_id`
`evaluator_version`
`canonicalization_version`
`fingerprint_version`
`trusted_time_context_id`
`finding_valid_from`
`finding_valid_until`
`limitations`
`unresolved_conditions`
`finding_fingerprint`
`supersedes_finding_id`

No presentation identifier may substitute for a missing authoritative field.

## 5. Finding-state domain

The only planned Phase 12 finding states are:

- `SUPPORTED`
- `CONTRADICTED`
- `STALE`
- `INCONCLUSIVE`
- `EVIDENCE_UNAVAILABLE`

A future executable mapping must be explicit and versioned.

## 6. Deterministic derivation

Finding derivation must use exact accepted source fields. Model inference cannot:

- invent evidence;
- repair missing truth;
- waive stale state;
- select a more favorable state;
- suppress limitations;
- alter tenant or subject scope.

## 7. Supported finding contract

`SUPPORTED` requires a source state that deterministically supports the bounded
claim under current required evidence, scope, policy, version, and time semantics.

Availability or lack of an error is not sufficient.

## 8. Contradicted finding contract

`CONTRADICTED` records deterministic conflict with approved architecture truth for
the bounded claim. It does not itself become a NEXUS ArchitectureRisk or authorize
remediation.

## 9. Stale finding contract

`STALE` preserves that a prior result or required evidence is outside the accepted
current validity/freshness boundary. Stale is not supported.

## 10. Inconclusive finding contract

`INCONCLUSIVE` preserves unresolved evaluation semantics where evidence exists but
does not deterministically establish support or contradiction.

## 11. Evidence-unavailable contract

`EVIDENCE_UNAVAILABLE` preserves that required current evidence cannot be qualified
for the bounded claim. It is distinct from `INCONCLUSIVE`, `STALE`, and `SUPPORTED`.

## 12. Finding immutability and supersession

An accepted finding is immutable. New material inputs create a distinct finding.
The later finding may reference the earlier one through `supersedes_finding_id`.

Historical findings cannot be rewritten to erase prior state.

## 13. Drift record contract

A planned drift record must support:

`drift_contract_version`
`drift_id`
`tenant_id`
`subject_id`
`claim_id`
`prior_finding_id`
`current_finding_id`
`drift_class`
`material_change_identity_set`
`detected_at_trusted_time`
`drift_fingerprint`
`limitations`

A drift record is only valid when prior and current findings are scope-compatible.

## 14. No-drift contract

Equivalent canonical material state must not generate a new drift record solely
because of delivery time, polling order, UI refresh, transport identity, or storage
location.

## 15. Certificate representation contract

A planned certificate representation must support:

`certificate_contract_version`
`certificate_content_id`
`tenant_id`
`subject_id`
`scope_id`
`architecture_truth_reference_id`
`finding_set_id`
`source_evaluation_set_id`
`evidence_set_id`
`conformance_policy_id`
`conformance_policy_version`
`canonicalization_version`
`fingerprint_version`
`valid_from`
`valid_until`
`limitations`
`unresolved_conditions`
`certificate_content_fingerprint`
`issuance_authority_state`

## 16. Certificate scope contract

Certificate scope cannot exceed the intersection of:

- accepted finding scope;
- evaluated claim scope;
- qualified architecture-truth scope;
- admitted evidence scope;
- tenant and subject scope;
- validity policy.

## 17. Certificate issuance separation

Certificate content composition is distinct from:

- signing;
- issuance;
- publication;
- delivery;
- revocation;
- external trust.

Phase 12 planning authorizes none of those effects.

## 18. Expiration and supersession

A historical certificate representation remains immutable. Expiration, later
evidence, or changed truth produces later state; it does not rewrite the historical
content.

## 19. Architecture Conformance Score contract

An optional score representation must support:

`score_contract_version`
`score_formula_id`
`score_formula_version`
`finding_set_id`
`eligible_finding_count`
`supported_count`
`contradicted_count`
`stale_count`
`inconclusive_count`
`evidence_unavailable_count`
`excluded_count`
`score_value_or_unavailable`
`score_fingerprint`
`limitations`

A score cannot hide unresolved states in the denominator or imply certainty that
the findings do not support.

## 20. Cross-scope isolation

Cross-tenant, cross-subject, incompatible environment/release, or incompatible
claim-set aggregation fails closed unless a separately accepted contract explicitly
defines the aggregate scope.

## 21. Failure contract

Failure to derive a finding, drift record, certificate representation, or score is
explicit state. Failure cannot default to `SUPPORTED`.

## 22. Provenance contract

Every authoritative representation preserves exact source identities and derivation
contract version sufficient for deterministic replay.

## 23. NEXUS boundary

Phase 12 reads qualified architecture truth indirectly through accepted upstream
bindings. It cannot create, edit, supersede, or approve NEXUS architecture truth.

## 24. Planning authority

`PHASE_12_IMPLEMENTATION_AUTHORITY=NONE`

`PHASE_12_RUNTIME_AUTHORITY=NONE`

`PHASE_12_FINDING_ISSUANCE_RUNTIME_AUTHORITY=NONE`

`PHASE_12_CERTIFICATE_ISSUANCE_RUNTIME_AUTHORITY=NONE`

`PHASE_13_ENTRY_AUTHORITY=NONE`

`PHASE_14_ENTRY_AUTHORITY=NONE`
