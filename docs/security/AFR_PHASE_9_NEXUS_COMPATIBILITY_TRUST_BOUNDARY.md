# AFR Phase 9 — NEXUS Compatibility Trust Boundary

Reachability is not trust. File presence, branch presence, commit reachability, UI labels, provider metadata, model output, copied contract text, local fingerprint repair, and structural similarity do not establish NEXUS acceptance or AFR compatibility.

NEXUS is authoritative for architecture truth, acceptance, truth-snapshot identity/version, source acceptance, package identity/revision/fingerprints, provenance, integrity, supersession/currentness, compatibility version, ArchitectureRisk references, and NEXUS conformance-request references.

AFR is authoritative only for AFR conformance request identity, AFR execution, AFR result, AFR finding, and AFR stale-reference evaluation outcome.

AFR may verify NEXUS integrity material but cannot repair a mismatch and promote the repaired value to authoritative truth. Integrity mismatch fails closed.

AFR may retain/cite NEXUS provenance references but cannot rewrite them into new NEXUS truth.

Only NEXUS establishes current or superseded NEXUS truth. AFR may identify staleness but cannot refresh, supersede, or reclassify NEXUS truth under Phase 9 planning authority.

```text
AFR_READ_AUTHORITY != NEXUS_MUTATION_AUTHORITY
AFR_FINDING != ARCHITECTURE_RISK
AFR_CONFORMANCE != NEXUS_ARCHITECTURE_ACCEPTANCE
NEXUS_ARCHITECTURE_TRUTH != AFR_CONFORMANCE_RESULT
```

The frozen NEXUS producer contract is presently non-canonical. No AFR implementation or runtime decision may treat it as canonical before NEXUS establishes its own effective point.

Phase 9 planning authorizes no network integration, credentials, polling, webhook, stream, API, provider invocation, persistence, deployment, remediation, enforcement, or production access.

Final NEXUS/ARCP compatibility certification remains reserved for AFR Phase 14.
