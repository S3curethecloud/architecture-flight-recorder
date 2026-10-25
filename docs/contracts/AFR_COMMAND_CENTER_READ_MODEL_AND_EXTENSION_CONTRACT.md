# AFR Command Center Read Model and Extension Contract

## 1. Contract posture

`CONTRACT_STATUS=DETACHED_PLANNING_CANDIDATE_NONCANONICAL`

This candidate defines the durable provider-neutral read-model and extension
boundary for the AFR Command Center. It creates no UI implementation, runtime,
provider, deployment, production, remediation, or mutation authority.

## 2. Product role

The AFR Command Center is the human-facing conformance operations and investigation
plane.

It may observe, explain, correlate, filter, and present accepted AFR state.

It may not silently mutate infrastructure or become architecture authority.

## 3. Durable shell principle

The Phase 12 shell is designed to survive Phase 13 operational-delivery extensions
and Phase 14 production hardening without routine replacement.

`ROUTINE_SHELL_REBUILD=PROHIBITED`

`SUCCESSOR_EVOLUTION=ADDITIVE_OR_EXPLICITLY_VERSIONED`

A future breaking change requires separate architecture governance.

## 4. Core semantic surfaces

Stable surface IDs are planned as:

`executive_status`
`live_findings`
`architecture_drift`
`evidence_health`
`evaluation_runs`
`conformance_certificates`
`system_scope`
`critical_alerts`
`flight_recorder_timeline`
`governance_audit`

A surface ID is a semantic contract identifier, not a required URL or page.

## 5. Common read-model envelope

Every future core read model must carry at least:

`read_model_contract_version`
`surface_id`
`tenant_id`
`subject_id_or_scope`
`workspace_or_system_scope`
`as_of_trusted_time`
`freshness_state`
`source_identity_set`
`source_fingerprint`
`authority_state`
`availability_state`
`limitations`
`warnings`
`data`

Exact null/absence semantics must be frozen before implementation.

## 6. Availability-state domain

The shell must distinguish at least:

- `AVAILABLE`
- `PARTIAL`
- `STALE`
- `UNAVAILABLE`
- `UNCONFIGURED`
- `UNAUTHORIZED`
- `INCONCLUSIVE`
- `BLOCKED`

An unavailable capability must not render as an empty successful result.

## 7. Authority-state presentation

A read model must not imply that presentation authority equals execution authority.

Where material, authority state must make distinctions such as:

- planned;
- accepted;
- implementation authorized/not authorized;
- runtime qualified/not qualified;
- provider access authorized/not authorized;
- certificate issuance authorized/not authorized;
- remediation authorized/not authorized.

## 8. Executive status read model

The executive surface may summarize:

- overall traceable conformance state;
- optional Architecture Conformance Score;
- critical contradiction count;
- stale/inconclusive/evidence-unavailable counts;
- certificate validity status;
- highest-priority drift;
- evidence health;
- evaluation freshness.

Every summary links back to exact source state.

## 9. Findings read model

The findings surface exposes finding identity, state, scope, affected claim,
source evaluation, evidence state, validity, limitations, and supersession.

## 10. Drift read model

The drift surface exposes prior/current finding identity, drift class, affected
claim, material change identity, trusted time, and deterministic rationale.

## 11. Evidence health read model

Evidence health exposes admissibility/freshness/provenance state without turning a
collection or transport success into evidence eligibility.

## 12. Evaluation runs read model

Evaluation runs expose Phase 11 cycle/result identity, attempt history where
permitted, versions, scope, terminal state, and limitations.

The surface cannot rewrite Phase 11 results.

## 13. Certificate read model

Certificate surfaces distinguish:

- certificate representation composed;
- signing authority absent/present;
- issuance state;
- validity;
- expiration;
- supersession/revocation state where later authorized.

Display alone is not issuance proof.

## 14. System and scope read model

System scope exposes tenant, subject, environment, release, architecture scope,
claim scope, and relevant capability context.

Cross-tenant aggregation fails closed unless separately accepted.

## 15. Critical alerts read model

Alerting is a projection over accepted state. Planned alert conditions may include
new contradiction, certificate expiration, evidence unavailability, stale critical
claim, or evaluation freshness breach.

Phase 12 planning creates no notification-delivery authority.

## 16. Flight Recorder timeline read model

The timeline preserves ordered historical projections for truth reference changes,
evidence changes, evaluations, findings, drift, certificates, authority changes,
and supersession.

Timeline presentation cannot mutate historical evidence.

## 17. Governance and audit read model

Governance/audit exposes:

- immutable identities;
- derivation versions;
- source provenance;
- authority boundaries;
- acceptance state;
- limitations;
- historical dispositions.

## 18. Capability registry contract

A capability registration must support:

`capability_id`
`capability_contract_version`
`supported_surface_ids`
`source_class`
`adapter_class`
`read_write_posture`
`required_authority_classes`
`freshness_contract`
`failure_contract`
`provenance_contract`
`compatibility_min_version`
`compatibility_max_version`
`lifecycle_state`

Registration does not grant authority.

## 19. Adapter boundary

Adapters translate provider/downstream-specific representations to or from stable
AFR extension contracts.

An adapter cannot:

- redefine finding states;
- redefine certificate semantics;
- bypass tenant/subject scope;
- invent evidence;
- suppress limitations;
- inherit provider mutation authority from registration.

## 20. Phase 12 adapter posture

`PHASE_12_ADAPTER_POSTURE=DECLARATIVE_EXTENSION_SEAMS_ONLY`

No live downstream adapter is activated by this planning contract.

## 21. Phase 13 extension points

Phase 13 may separately govern capabilities such as:

- downstream consumer delivery;
- notifications;
- external read projections;
- approved consumer APIs/feeds;
- integration-health projections.

Phase 13 modules plug into the capability registry and adapter boundary.

Phase 13 must not require routine replacement of the Phase 12 shell.

## 22. Phase 14 hardening hooks

The shell and read-model envelope reserve explicit support for:

- component health;
- SLO status;
- latency/performance evidence;
- capacity state;
- security posture;
- compatibility state;
- E2E test evidence;
- deployment version;
- rollback/upgrade state;
- final NEXUS/ARCP compatibility evidence.

These are hardening projections, not semantic overrides.

## 23. Compatibility policy

Additive fields may be introduced only under an accepted compatibility policy.
Breaking semantic changes require a new major contract version and separate
governance.

Unknown fields cannot silently become authority.

## 24. Provider neutrality

The core shell and core read models cannot require a specific cloud provider,
database, queue, identity provider, frontend framework, telemetry vendor, or
certificate-signing service.

## 25. Security and privacy

Read models must minimize exposed sensitive data. Secrets, tokens, raw credentials,
and unnecessary provider-native payloads are prohibited from Command Center
presentation contracts.

## 26. Failure behavior

Module failure degrades the affected module when isolation is safe. Failure of a
shared critical authority, identity, scope, provenance, or integrity boundary fails
closed for the affected authoritative presentation.

## 27. Planning authority

`PHASE_12_COMMAND_CENTER_IMPLEMENTATION_AUTHORITY=NONE`

`PHASE_12_COMMAND_CENTER_RUNTIME_AUTHORITY=NONE`

`PHASE_12_COMMAND_CENTER_DEPLOYMENT_AUTHORITY=NONE`

`PHASE_12_COMMAND_CENTER_PRODUCTION_AUTHORITY=NONE`

`PHASE_13_ENTRY_AUTHORITY=NONE`

`PHASE_14_ENTRY_AUTHORITY=NONE`
