# AFR Phase 5 Evidence Acquisition Trust Boundary

## 1. Purpose

This document defines the security and trust constraints for planned
provider-neutral, least-privilege, read-only acquisition of attributable
operational observations for Phase 4 ingress.

It is documentation-only and creates no implementation, credential, live
collection, network, persistence, integration, runtime, certificate,
deployment, enforcement, or remediation authority.

## 2. Trust Posture

Every source response, source assertion, identifier, timestamp, scope claim,
continuation token, representation, version declaration, collector assertion,
and transformation claim is untrusted until explicitly attributed and
validated under the planned boundary.

Source authority over source state does not make every response field valid
for every AFR purpose.

## 3. Boundary Position

The trust boundary lies between approved provider or enterprise sources and
the supplied operational observation handed to Phase 4.

It ends before evidence eligibility and conformance.

## 4. Protected Assets

Protected assets include:

- tenant and subject isolation;
- collector identity;
- source identity;
- collection-request identity;
- response identity;
- collection-result identity;
- environment and scope binding;
- authorization-context attribution;
- source-native time;
- collection times;
- scope and completeness accounting;
- raw-response identity;
- transformation metadata;
- failure records;
- Phase 4 eligibility authority;
- canonical AFR phase boundaries.

## 5. Trust Inputs

Only explicit, attributable, version-bound inputs may influence the planned
collection result.

Ambient credentials, process identity, filesystem paths, host placement,
provider account presence, network state, model output, randomness, or
operator convenience are non-authoritative.

## 6. Threat Actors and Conditions

The boundary assumes malicious, accidental, stale, malformed, oversized,
partial, throttled, duplicated, replayed, reordered, substituted,
cross-tenant, cross-subject, cross-environment, cross-scope, ambiguously timed,
unsupported, or misleading source responses may occur.

It also assumes collector configuration or source metadata may be incorrect or
overbroad unless explicitly bounded.

## 7. Least-Privilege Read-Only Identity

A future collector must use the minimum source-read authority needed for the
explicit operation and scope.

Planning must prevent authority confusion between:

- read and write;
- observation and remediation;
- source access and architecture truth;
- source access and evidence eligibility;
- source access and runtime commit authority.

No credential issuance or live use is authorized.

## 8. Tenant and Subject Isolation

Tenant, subject, environment, source, and scope must be explicit and mutually
consistent.

Cross-tenant, cross-subject, cross-environment, and cross-scope substitution
must fail closed in any future implementation.

Ambient identity inference is prohibited.

## 9. Source Authenticity

Planning must define source authenticity inputs sufficient to attribute a
response to the intended source boundary without relying on presentation
labels alone.

Ambiguous or conflicting source identity cannot support a complete collection
result.

## 10. Authorization-Context Safety

Authorization context must be represented by bounded, non-secret references
and operation/scope claims.

Credentials, tokens, keys, passwords, or secret material must not be persisted
in collection identities, results, failure records, or handoff metadata.

## 11. Scope-Minimization Boundary

Collection scope must be the minimum explicitly governed scope required for
the request.

A future collector must not expand scope because broader access is available.

Observed scope beyond the request must not silently become authorized scope.

## 12. Source-Response Integrity

Planning must preserve inputs needed to determine whether a response belongs
to the intended source and request, including source identity, request
identity, response identity, representation/version, scope, temporal metadata,
and any source-native integrity material where available.

Phase 5 does not redefine Phase 4 evidence integrity.

## 13. Temporal Trust

Request, collection, source-observation, source-response, result-construction,
and handoff times remain distinct.

Missing or ambiguous source-native time remains explicit.

Phase 5 cannot promote collector wall-clock time into source-native time or
Phase 4 trusted time.

## 14. Pagination and Continuation Safety

Continuation tokens and page or segment identifiers are untrusted inputs.

Planning must address token substitution, replay, duplication, omission,
unexpected scope expansion, source-version changes, and termination ambiguity.

Partial pagination cannot become a complete result.

## 15. Partial and Failed Collection Safety

Partial, failed, unsupported, cancelled, and resource-bounded collection
states remain explicit.

Unknown state cannot become absence.

Collection failure cannot become evidence or conformance.

## 16. Raw Response and Sensitive Data

Raw source responses may contain secrets, personal data, security-sensitive
configuration, identifiers, or unrelated fields.

Planning must require minimization, bounded exposure, policy-governed
preservation, redaction or exclusion where necessary, and clear distinction
between raw and derived representations.

No persistence mechanism is authorized.

## 17. Failure Safety

Failures must be structured, bounded, attributable, and audit-safe.

Failure records include stable class, semantic location, request/result
identity, scope impact, relevant version, and bounded safe context.

They exclude credentials, secrets, unnecessary payloads, stack traces, and
unbounded provider internals.

## 18. Resource-Exhaustion Controls

Planning must define conceptual future bounds for:

- response bytes;
- page or segment count;
- item count;
- nesting depth;
- metadata cardinality;
- failure count;
- local transformation work.

Bound exhaustion cannot preserve an unqualified complete result.

## 19. Transformation Safety

Parsing, redaction, minimization, normalization, or other future
transformations must preserve representation identity and transformation
metadata.

A transformed representation must not be mislabeled as source-native bytes.

Transformation cannot create missing source attribution, time, scope, or
authority.

## 20. Phase 4 Handoff Trust Boundary

The Phase 4 handoff must preserve collection provenance, identities, scope,
times, outcome, partial state, failures, versions, and representation
distinctions.

Phase 4 applies its own validation and evidence-eligibility rules.

Phase 5 cannot pre-approve eligibility.

## 21. Provider Adapter and Supply-Chain Boundary

Provider-specific adapters are not authorized.

A future adapter must not:

- define canonical AFR acquisition semantics;
- expand source or tenant scope;
- convert read authority to write authority;
- suppress source failures;
- fabricate completeness;
- determine Phase 4 eligibility;
- invoke conformance evaluation;
- import ungoverned dependencies or remote code.

## 22. Cross-Program Non-Drift

Provider sources remain authoritative for their own bounded operational state.

NEXUS remains authoritative for approved architecture truth where applicable.

Phase 4 retains evidence-eligibility authority.

AFR deterministic evaluation retains conformance authority.

ATA retains consequential runtime commit authority where applicable.

No collection boundary may collapse those authorities.

## 23. Abuse and Misuse Cases

The planned controls must address:

- collector identity spoofing;
- source identity spoofing;
- tenant or subject substitution;
- overbroad source scope;
- unauthorized write-capable identity use;
- continuation-token substitution;
- stale or replayed responses;
- response truncation;
- false completeness;
- malformed or adversarial payloads;
- source-version downgrade;
- raw-response sensitive-data leakage;
- failure suppression;
- transformation mislabeling;
- authority escalation into Phase 4 or runtime domains.

## 24. Prohibited Effects and Stop Conditions

This boundary authorizes no source, tests, executable schema, dependency,
configuration, provider adapter, live source access, credential, filesystem,
network, persistence, model, Phase 4 eligibility implementation, kernel
invocation, NEXUS/ARCP/ATA integration, certificate, deployment, enforcement,
remediation, or implementation.

Planning stops if any is required or if accepted Phase 0 through Phase 4
semantics need amendment.

## 25. Review Evidence

Acceptance requires exact six-document and hash verification, semantic
convergence, acquisition-architecture review, contract review, threat and
trust review, scope/completeness review, temporal review, failure review,
bounded-resource review, provider-neutrality review, Phase 4 non-drift review,
NEXUS/ARCP/ATA authority review, authority-leakage review, independent
whole-package review, staged-object verification, commit and remote
verification, explicit readiness and merge authorization, canonical
post-merge verification, and separately governed closure.

No gate implies the next.

## 26. Authority State

`AFR_PHASE_5_PLANNING_AUTHORITY =
BOUNDED_EVIDENCE_ACQUISITION_AND_COLLECTION_BOUNDARY_PLANNING_ONLY`

`AFR_PHASE_5_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_5_LIVE_COLLECTION_AUTHORITY = NONE`

`AFR_PHASE_5_PROVIDER_ADAPTER_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_5_CREDENTIAL_AUTHORITY = NONE`

`AFR_PHASE_5_NETWORK_AUTHORITY = NONE`

`AFR_PHASE_5_PERSISTENCE_AUTHORITY = NONE`

`AFR_PHASE_5_NEXUS_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_5_ARCP_AUTHORITY = NONE`

`AFR_PHASE_5_ATA_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_5_RUNTIME_AUTHORITY = NONE`

`AFR_PHASE_5_CERTIFICATE_AUTHORITY = NONE`

`AFR_PHASE_5_DEPLOYMENT_AUTHORITY = NONE`

`AFR_PHASE_5_ENFORCEMENT_AUTHORITY = NONE`

`AFR_PHASE_5_REMEDIATION_AUTHORITY = NONE`
