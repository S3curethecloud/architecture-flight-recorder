# AFR Phase 8 Acceptance Criteria

## 1. Package Boundary

- [ ] Exactly six authorized planning documents exist.
- [ ] No seventh planning document is required.
- [ ] No source, executable schema, test, fixture, dependency, configuration,
      or runtime artifact is part of this candidate.

## 2. Planning Authority

- [ ] Capability is `READ_ONLY_CONSUMER_GATEWAY_FIRST_SLICE_IMPLEMENTATION_PLANNING`.
- [ ] Planning authority is `BOUNDED_READ_ONLY_CONSUMER_GATEWAY_FIRST_SLICE_IMPLEMENTATION_PLANNING_ONLY`.
- [ ] Planning authority is effective and documentation-only.
- [ ] Implementation and runtime authorities remain `NONE`.

## 3. Source Preservation

- [ ] Only already-approved AFR source objects are eligible.
- [ ] Source identity remains exact.
- [ ] Projection cannot repair or replace authoritative source truth.
- [ ] Authoritative outcome cannot be strengthened by projection.
- [ ] Material limitations remain represented.

## 4. Authorization Binding

- [ ] Consumer identity is explicit.
- [ ] Tenant identity is explicit.
- [ ] Subject identity is explicit where applicable.
- [ ] Requested scope is explicit.
- [ ] Policy identifier/version is explicit.
- [ ] Authorization decision and decision identity are explicit.
- [ ] Authorization binds the same source, consumer, tenant, subject, scope,
      and policy version as the request.
- [ ] Missing or denied authorization produces no projection.

## 5. Tenant / Subject Isolation

- [ ] Tenant mismatch fails closed.
- [ ] Cross-tenant substitution fails closed.
- [ ] Unauthorized subject substitution fails closed.
- [ ] No implicit tenant fallback exists.
- [ ] No implicit subject fallback exists.

## 6. Scope and Privilege

- [ ] Requested scope does not exceed source scope.
- [ ] Requested scope does not exceed authorized scope.
- [ ] Scope expansion fails closed.
- [ ] Scope narrowing preserves truthful interpretation.
- [ ] Privilege expansion is prohibited.

## 7. Determinism

- [ ] Identical source and bound authorization context produce the same logical result.
- [ ] Randomness cannot alter entitlement.
- [ ] Ambient state cannot alter entitlement.
- [ ] Generative-model output cannot alter entitlement.

## 8. Read-Only Projection

- [ ] Allowed output is representational only.
- [ ] No AFR state is mutated.
- [ ] No downstream state is mutated.
- [ ] Denial/failure does not alter the source object.

## 9. Integrity / Provenance

- [ ] Existing integrity metadata is preserved.
- [ ] Integrity claims do not exceed source guarantees.
- [ ] Representation remains attributable to the authoritative source.
- [ ] Projection transformation remains distinguishable from authoritative provenance.
- [ ] No signing/key-management implementation is authorized.

## 10. Freshness / Validity

- [ ] Projection cannot refresh stale source state.
- [ ] Projection cannot extend expiry.
- [ ] Projection cannot erase supersession.
- [ ] Invalid source state cannot become valid through projection.

## 11. Fail-Closed Negative Tests

Acceptance fails for:

- unresolved consumer identity;
- authorization absence;
- authorization denial;
- authorization binding mismatch;
- tenant mismatch;
- subject mismatch;
- scope violation;
- policy-version mismatch;
- source identity mismatch;
- source ineligibility;
- integrity mismatch;
- stale/invalid source where current validity is required;
- unsafe projection;
- missing mandatory limitation/provenance context.

## 12. Model / Agent Exclusion

- [ ] Models/agents are non-authoritative for authorization.
- [ ] Models/agents cannot select entitlement.
- [ ] Models/agents cannot widen scope.
- [ ] Models/agents cannot repair source truth.
- [ ] Models/agents cannot suppress required limitations.
- [ ] Models/agents cannot commit consequential actions.

## 13. Prohibited Effects

Acceptance fails if the package requires:

- network/API activation;
- credentials, secrets, tokens, keys, certificates, or service identities;
- persistence or cache;
- event, queue, webhook, feed, or stream activation;
- concrete external integration;
- authoritative AFR mutation;
- downstream mutation;
- runtime delivery;
- deployment;
- enforcement;
- remediation;
- production access.

## 14. Independent Whole-Package Review

Before repository materialization can be proposed:

- [ ] architecture review passes;
- [ ] contract review passes;
- [ ] trust-boundary review passes;
- [ ] authorization-binding review passes;
- [ ] tenant/subject/scope isolation review passes;
- [ ] deterministic-projection review passes;
- [ ] source identity/outcome/limitation preservation review passes;
- [ ] integrity/provenance review passes;
- [ ] fail-closed review passes;
- [ ] predecessor non-drift review passes;
- [ ] authority-leakage review passes;
- [ ] every blocking finding is resolved.

## 15. Lifecycle

Detached preparation does not itself establish planning-package acceptance,
repository materialization authority, closure, implementation authority, or
runtime authority.


## Authority State

`AFR_PHASE_8_CAPABILITY = READ_ONLY_CONSUMER_GATEWAY_FIRST_SLICE_IMPLEMENTATION_PLANNING`

`AFR_PHASE_8_PLANNING_AUTHORITY = BOUNDED_READ_ONLY_CONSUMER_GATEWAY_FIRST_SLICE_IMPLEMENTATION_PLANNING_ONLY`

`AFR_PHASE_8_PLANNING_AUTHORITY_EFFECTIVE = YES`

`AFR_PHASE_8_PLANNING_AUTHORITY_CHARACTER = DOCUMENTATION_ONLY`

`AFR_PHASE_8_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_8_CONSUMER_GATEWAY_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_8_API_AUTHORITY = NONE`

`AFR_PHASE_8_EVENT_AUTHORITY = NONE`

`AFR_PHASE_8_QUEUE_AUTHORITY = NONE`

`AFR_PHASE_8_WEBHOOK_AUTHORITY = NONE`

`AFR_PHASE_8_FEED_AUTHORITY = NONE`

`AFR_PHASE_8_NETWORK_AUTHORITY = NONE`

`AFR_PHASE_8_CREDENTIAL_AUTHORITY = NONE`

`AFR_PHASE_8_PERSISTENCE_AUTHORITY = NONE`

`AFR_PHASE_8_EXTERNAL_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_8_RUNTIME_AUTHORITY = NONE`

`AFR_PHASE_8_DEPLOYMENT_AUTHORITY = NONE`

`AFR_PHASE_8_ENFORCEMENT_AUTHORITY = NONE`

`AFR_PHASE_8_REMEDIATION_AUTHORITY = NONE`

`AFR_PHASE_8_PRODUCTION_ACCESS_AUTHORITY = NONE`
