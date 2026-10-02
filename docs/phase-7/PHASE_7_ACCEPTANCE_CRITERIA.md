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

## 33. Post-Canonical Closure Reconciliation Candidate R1

The Phase 7 planning package is canonically accepted but remains closure-pending until this separately governed documentation-only closure lifecycle completes.

The accepted planning-package evidence is:

- planning-package base: `ea48c34edd9b0684a620fe0ee012a567cde1f445`;
- planning-package commit: `8367312e210cf4a556a0243ba2082dc20c03a5ba`;
- canonical merge: `d679c6595692bbaaaf7b6a39dca19c1c6f4c68d0`;
- canonical tree: `746457591595b06affc1ebb7211286e9889bf7e3`;
- pull request: `#30`;
- exact six-document boundary: `PASS`;
- `docs/SOT.md` SHA-256: `16b3c7edef21a08c53df3ab1755a9fbfe4c785d5525354b1ef6adc3a335209a3`;
- `docs/phase-7/PHASE_7_PLAN.md` SHA-256: `67a43dceb5f90e76e0b718d0367b5e651df3a5668aa64821b9aad7460b3c20f0`;
- `docs/phase-7/PHASE_7_ACCEPTANCE_CRITERIA.md` SHA-256: `40a524be48f224c40f16e68bebe3f7325031ea6d4e55b5c9985efb248605f35d`;
- `docs/architecture/AFR_DELIVERY_AND_INTEGRATION_ARCHITECTURE.md` SHA-256: `55c08d7947580da6a7b64d03e059902e078b26938393d113afb248e855140d97`;
- `docs/contracts/AFR_DELIVERY_AND_INTEGRATION_CONTRACT.md` SHA-256: `afc1730d190eb9597db8f32b3726a85ecc37f8798470d7ef322e164ff5d73775`;
- `docs/security/AFR_PHASE_7_DELIVERY_AND_INTEGRATION_TRUST_BOUNDARY.md` SHA-256: `4fba7fdc02ea2684a3a8a7ac78986aed27a7282babff18931a6fea013b7a46dd`;
- accepted closure-scope manifest SHA-256: `1cf637fe1793677f8a071f46dc80f063f352f92f4a3f3cda3039160ac57e6815`;
- canonical convergence acceptance: `PASS`.

Closure acceptance is limited exactly to append-only modification of:

1. `docs/SOT.md`
2. `docs/phase-7/PHASE_7_ACCEPTANCE_CRITERIA.md`

No third document is part of the accepted closure scope.

The Phase 7 plan, delivery and integration architecture, delivery and integration contract, and Phase 7 trust-boundary document remain byte-identical to their accepted planning-package identities.

The closure candidate must preserve all existing Phase 7 acceptance criteria.

The following reconciled review-harness defects are non-substantive and have no canonical semantic effect:

1. a remote source-head parser false negative caused by literal single quotes embedded in the expected ref target;
2. a closure-precedent checker failure caused by omission of the `grep --` end-of-options delimiter for a dash-prefixed search pattern.

Corrected read-only reconciliation proved the underlying repository and precedent states were exact.

Closure acceptance requires all of the following:

- the closure remains append-only;
- exactly the two accepted closure documents change;
- both complete future preimages match independently accepted frozen identities;
- the accepted Phase 7 planning-package base, commit, canonical merge, ordered parents, tree, exact six-document boundary, and content identities remain bound exactly;
- the canonical planning acceptance and convergence evidence remains preserved;
- all reconciled checker defects remain classified as non-substantive review-harness defects only;
- no source, executable schema, test, fixture, dependency, configuration, API, gateway, event, queue, webhook, feed, credential, network, provider integration, persistence, cache, runtime evaluation, runtime execution, delivery execution, deployment, enforcement, remediation, production access, or Phase 8 authority is created;
- independent closure-content acceptance passes;
- exact candidate identities are frozen before materialization;
- repository materialization occurs only under separately granted authority;
- staging occurs only under separately granted authority;
- the staged index is independently verified;
- commit occurs only under separately granted authority;
- push occurs only under separately granted authority;
- an exact Draft pull request is independently verified;
- Draft-to-Ready transition requires explicit separate authorization;
- merge requires explicit separate authorization;
- the exact reviewed closure is merged to canonical `main`;
- post-merge identity, ordered parents, tree, exact two-document boundary, frozen content identities, local and remote convergence, canonical checkout, worktree cleanliness, and index cleanliness all pass.

Before every closure-effective-point condition passes:

`AFR_PHASE_7_PLANNING_STATUS = PLANNING_ACCEPTED_CLOSURE_PENDING`

`AFR_PHASE_7_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_7_DELIVERY_AUTHORITY = NONE`

`AFR_PHASE_7_RUNTIME_AUTHORITY = NONE`

`PHASE_8_AUTHORITY = NONE`

After and only after every closure-effective-point condition passes:

`AFR_PHASE_7_PLANNING_STATUS = COMPLETE`

`AFR_PHASE_7_PLANNING_AUTHORITY = CONSUMED_CLOSED`

`AFR_PHASE_7_IMPLEMENTATION_AUTHORITY = NONE`

`AFR_PHASE_7_DELIVERY_AUTHORITY = NONE`

`AFR_PHASE_7_CONSUMER_GATEWAY_AUTHORITY = NONE`

`AFR_PHASE_7_API_AUTHORITY = NONE`

`AFR_PHASE_7_EVENT_AUTHORITY = NONE`

`AFR_PHASE_7_QUEUE_AUTHORITY = NONE`

`AFR_PHASE_7_WEBHOOK_AUTHORITY = NONE`

`AFR_PHASE_7_FEED_AUTHORITY = NONE`

`AFR_PHASE_7_NETWORK_AUTHORITY = NONE`

`AFR_PHASE_7_CREDENTIAL_AUTHORITY = NONE`

`AFR_PHASE_7_PROVIDER_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_7_NEXUS_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_7_ARCP_AUTHORITY = NONE`

`AFR_PHASE_7_ATA_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_7_PAA_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_7_HUMANIZE_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_7_CICD_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_7_RELEASE_GOVERNANCE_INTEGRATION_AUTHORITY = NONE`

`AFR_PHASE_7_PERSISTENCE_AUTHORITY = NONE`

`AFR_PHASE_7_CACHE_AUTHORITY = NONE`

`AFR_PHASE_7_RUNTIME_EVALUATION_AUTHORITY = NONE`

`AFR_PHASE_7_RUNTIME_AUTHORITY = NONE`

`AFR_PHASE_7_DEPLOYMENT_AUTHORITY = NONE`

`AFR_PHASE_7_ENFORCEMENT_AUTHORITY = NONE`

`AFR_PHASE_7_REMEDIATION_AUTHORITY = NONE`

`AFR_PHASE_7_PRODUCTION_ACCESS_AUTHORITY = NONE`

`PHASE_8_AUTHORITY = NONE`

Closure acceptance does not authorize implementation or begin Phase 8.
