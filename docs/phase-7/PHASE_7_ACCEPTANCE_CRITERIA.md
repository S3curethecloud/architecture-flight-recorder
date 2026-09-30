# AFR Phase 7 Acceptance Criteria

## 1. Exact Package Boundary

- [ ] Exactly six authorized planning documents are present.
- [ ] No seventh planning document is required.
- [ ] No source, test, schema, dependency, configuration, or runtime artifact is part of the candidate.

## 2. Canonical Baseline

- [ ] Canonical baseline is `ea48c34edd9b0684a620fe0ee012a567cde1f445`.
- [ ] Canonical tree is `78a573501ee86de69528b1d029823363a4caea3e`.
- [ ] Phase 7 planning authority is `BOUNDED_DELIVERY_AND_INTEGRATION_BOUNDARY_PLANNING_ONLY`.

## 3. Mission Acceptance

- [ ] The package plans tenant-aware authorized read-only delivery of already-approved AFR outputs.
- [ ] It does not plan mutation of AFR results or downstream systems.

## 4. Predecessor Preservation

- [ ] NEXUS architecture-truth authority remains preserved.
- [ ] AFR evidence-eligibility semantics remain preserved.
- [ ] AFR deterministic evaluation semantics remain preserved.
- [ ] Phase 6 finding/certificate semantics remain preserved.
- [ ] ATA runtime commit authority remains preserved.

## 5. Approved-Output Boundary

- [ ] Only already-approved AFR outputs are deliverable inputs.
- [ ] Missing mandatory identity, integrity, provenance, scope, policy, tenant, subject, validity, or freshness context fails closed.

## 6. Outcome Preservation

- [ ] Delivery cannot create a conformance outcome.
- [ ] Delivery cannot upgrade `NON_CONFORMANT`, `INCONCLUSIVE`, or `STALE` to `CONFORMANT`.
- [ ] Delivery cannot suppress or reinterpret evidence to alter outcome meaning.

## 7. Limitation Preservation

- [ ] Material limitations remain visible or explicitly represented in any safe projection.
- [ ] Redaction cannot materially strengthen the apparent result.

## 8. Consumer Identity

- [ ] Every interaction requires an attributable consumer identity.
- [ ] Consumer identity is bound to tenant, role, action, scope, policy version, and audit correlation identity.
- [ ] Anonymous or authority-ambiguous access fails closed.

## 9. Authorization

- [ ] Authorization is deny by default.
- [ ] Authorization decisions are deterministic under an approved policy boundary.
- [ ] Object possession does not imply entitlement.
- [ ] A consumer cannot self-expand permission.

## 10. Tenant Isolation

- [ ] Cross-tenant exposure is prohibited without separately canonical authority.
- [ ] Confused-deputy and tenant-substitution cases fail closed.

## 11. Subject and Scope Isolation

- [ ] Subject identity is preserved.
- [ ] Scope expansion is prohibited.
- [ ] Scope narrowing cannot misrepresent the source result.

## 12. Consumer Gateway Boundary

- [ ] The planned Consumer Gateway is read-only with respect to authoritative AFR state.
- [ ] The planned Consumer Gateway is read-only with respect to downstream systems.
- [ ] No implicit write, remediation, deployment, or policy-mutation path exists.

## 13. Projection Semantics

- [ ] Projection rules are deterministic and policy-bound.
- [ ] Filtering and pagination cannot alter authoritative semantics.
- [ ] Sensitive-field minimization preserves semantic truth.

## 14. Integrity and Provenance

- [ ] Delivery retains source output identity.
- [ ] Provenance remains attributable.
- [ ] Delivered integrity claims do not exceed source integrity.
- [ ] Delivery representation cannot invent stronger validity or authority.

## 15. Freshness and Validity

- [ ] Upstream freshness and validity semantics are preserved.
- [ ] Stale, expired, superseded, or invalid outputs are not represented as current valid conformance.

## 16. Auditability

- [ ] Access decisions are correlatable to consumer, tenant, source object, action, scope, policy version, decision, and relevant time context.
- [ ] Planning does not create logging infrastructure or an audit sink.

## 17. Consumer-Class Separation

- [ ] Human reviewers may be represented as a consumer class without integration authority.
- [ ] Audit/assurance systems may be represented without integration authority.
- [ ] PAA, Humanize, CI/CD, release governance, and ATA may be represented only as prospective bounded consumers.

## 18. Cross-Program Non-Drift

- [ ] Naming a consumer does not activate integration.
- [ ] Concrete integration requires separate future authority.
- [ ] Phase 7 does not redefine NEXUS, ARCP, ATA, PAA, Humanize, CI/CD, or release-governance semantics.

## 19. Downstream Non-Mutation

- [ ] Consumers cannot mutate authoritative AFR outputs.
- [ ] Delivery does not authorize remediation.
- [ ] Delivery does not authorize deployment.
- [ ] Delivery does not authorize enforcement.

## 20. Failure Taxonomy

- [ ] Identity, authorization, tenant, subject, scope, source, integrity, staleness, policy-version, projection, audit-correlation, and future transport failures are distinct from conformance outcomes.
- [ ] Failure handling cannot manufacture `CONFORMANT`.

## 21. Partial Response Safety

- [ ] Partial responses cannot silently remove material limitations.
- [ ] Semantically unsafe partial responses fail closed.

## 22. Replay and Reuse Safety

- [ ] Replay outside bound tenant, subject, scope, policy, identity, or validity context fails closed.
- [ ] Cached or repeated representations cannot silently exceed source validity.

## 23. Model Exclusion

- [ ] Models are non-authoritative for authorization, entitlement, identity binding, source eligibility, conformance outcome, integrity, policy selection, limitation suppression, permission expansion, or consequential action.

## 24. Determinism

- [ ] Identical authoritative inputs and authorization context produce identical planning decisions.
- [ ] Ambient state, randomness, or model output cannot alter authoritative delivery entitlement.

## 25. Security and Privacy

- [ ] Least privilege is required.
- [ ] Data minimization is required.
- [ ] Sensitive-field projection is explicit and policy-bound.
- [ ] Read access is separated from consequential-action authority.

## 26. Implementation Exclusion

Acceptance fails if the package creates authority for source code, executable schemas, tests, APIs, gateways, queues, events, webhooks, feeds, credentials, network access, storage, cache, runtime services, deployment, or production access.

## 27. Stop Conditions

Acceptance fails if Phase 7 planning requires predecessor amendment, a seventh document, concrete integration activation, credentials, network access, persistence, API/event/queue/webhook/feed implementation, write authority, model authority, runtime action, deployment, enforcement, remediation, production behavior, or Phase 8 definition.

## 28. Whole-Package Review

Before planning-package acceptance:

- [ ] architecture review passes;
- [ ] contract review passes;
- [ ] security review passes;
- [ ] identity and authorization review passes;
- [ ] tenant/subject/scope isolation review passes;
- [ ] projection and limitation-preservation review passes;
- [ ] downstream non-mutation review passes;
- [ ] model-exclusion review passes;
- [ ] predecessor non-drift review passes;
- [ ] authority-leakage review passes;
- [ ] every blocking finding is resolved.

## 29. Exact-Identity Lifecycle

- [ ] All six document hashes are frozen after review.
- [ ] Repository materialization requires separate authority.
- [ ] Staging requires separate authority.
- [ ] Commit requires separate authority.
- [ ] Push requires separate authority.
- [ ] Draft PR creation requires separate authority.
- [ ] Ready transition requires separate authority.
- [ ] Merge requires explicit separate authority.

## 30. Canonical Planning Acceptance

Canonical planning acceptance requires exact six-document identity through repository lifecycle, canonical merge, independent post-merge identity/tree/parent/content verification, local/remote canonical-main convergence, and clean canonical checkout.

Merge alone does not establish acceptance.

## 31. Closure Acceptance

Terminal Phase 7 completion additionally requires a separately governed documentation-only closure candidate, independent closure review, exact repository lifecycle, explicit closure merge authorization, canonical closure merge, post-merge verification, canonical convergence, and clean checkout.

## 32. Required Current State

A successful detached planning-package review may establish only:

`AFR_PHASE_7_PLANNING_PACKAGE = REVIEWED_CANDIDATE`

`AFR_PHASE_7_PLANNING_AUTHORITY = BOUNDED_DELIVERY_AND_INTEGRATION_BOUNDARY_PLANNING_ONLY`

`AFR_PHASE_7_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_7_DELIVERY_AUTHORITY = NONE`

`AFR_PHASE_7_RUNTIME_AUTHORITY = NONE`

`PHASE_8_AUTHORITY = NONE`
