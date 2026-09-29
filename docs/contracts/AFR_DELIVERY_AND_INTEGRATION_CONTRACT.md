# AFR Delivery and Integration Contract

## 1. Purpose

This contract defines deterministic Phase 7 planning requirements for bounded read-only delivery of approved AFR outputs.

## 2. Contract Boundary

This is a planning contract only.

It defines no executable API, schema, protocol, credential, network behavior, persistence mechanism, or runtime service.

## 3. Source Object Rule

A delivery representation MUST originate from an already-approved AFR output valid under canonical predecessor semantics.

A delivery layer MUST NOT create or repair authoritative source truth.

## 4. Source Identity Rule

Every delivered representation MUST retain an immutable reference to the authoritative source output identity.

## 5. Outcome Preservation Rule

A delivered representation MUST preserve the authoritative conformance outcome and MUST NOT substitute a more favorable outcome.

## 6. Evidence Non-Mutation Rule

Delivery MUST NOT fabricate, suppress, replace, or reinterpret evidence in a way that changes authoritative meaning.

## 7. Limitation Preservation Rule

Material limitations MUST remain represented whenever omission would strengthen, broaden, or otherwise mischaracterize the source result.

## 8. Consumer Identity Rule

Every request MUST bind an attributable consumer identity.

Unresolved identity MUST fail closed.

## 9. Consumer Role Rule

Authorization MUST bind the consumer's approved role independently of source-object visibility.

Possession MUST NOT imply role authority.

## 10. Tenant Binding Rule

Source tenant, request tenant, authorization tenant, and representation tenant MUST agree under an approved contract.

Cross-tenant mismatch MUST fail closed.

## 11. Subject Binding Rule

Subject identity MUST be preserved or explicitly authorized by a future canonical relationship.

Unauthorized substitution MUST fail closed.

## 12. Action Binding Rule

The requested action MUST be explicit and MUST be constrained to read-only semantics under this Phase 7 plan.

## 13. Scope Rule

Delivered scope MUST NOT exceed authoritative source scope or authorized consumer scope.

Scope expansion MUST fail closed.

## 14. Policy-Version Rule

Every authorization decision MUST bind an approved policy identifier/version.

Policy ambiguity MUST fail closed.

## 15. Deny-by-Default Rule

Absence of an explicit allow decision MUST produce denial.

## 16. Determinism Rule

Given identical authoritative source identity, consumer identity, tenant, subject, requested action, scope, policy version, and applicable validity context, the authorization and representation decision MUST be deterministic.

## 17. Projection Rule

Projection MAY remove fields only under explicit policy and MUST preserve semantic truth.

Projection MUST NOT become reevaluation.

## 18. Redaction Rule

Redaction MUST be policy-bound and MUST preserve required limitations, outcome, scope, and validity semantics.

## 19. Integrity Rule

Delivered integrity metadata MUST NOT claim stronger guarantees than the source object provides.

## 20. Provenance Rule

Representation provenance MUST identify the source AFR output and material projection transformation where applicable.

## 21. Freshness Rule

A stale or expired source MUST NOT be represented as current solely because delivery occurred later.

## 22. Supersession Rule

Supersession relationships MUST remain visible where needed to avoid presenting obsolete output as current.

## 23. Audit Correlation Rule

Each access decision MUST be correlatable to consumer, tenant, source, action, scope, policy version, decision, and relevant time context.

## 24. Read-Only Rule

`READ_ACCESS != WRITE_AUTHORITY`

The delivery contract MUST NOT create a mutation path to AFR or downstream systems.

## 25. Downstream Authority Rule

Receipt of an AFR output MUST NOT grant remediation, deployment, enforcement, policy mutation, architecture mutation, or runtime commit authority.

## 26. Consumer-Class Rule

A named consumer class MUST NOT be treated as an active integration.

Concrete integration requires separate future authority.

## 27. Failure Classification Rule

Identity, authorization, tenant, subject, scope, source, integrity, validity, policy, projection, audit, and future transport failures MUST remain non-conformance-neutral delivery failures rather than replacement conformance outcomes.

## 28. Partial Response Rule

A partial response MUST fail closed if required semantic constraints cannot be preserved.

## 29. Replay Rule

A representation replayed outside its authorized tenant, subject, scope, identity, policy, or validity context MUST fail closed.

## 30. Model-Exclusion Rule

A model MUST NOT authoritatively determine access, entitlement, tenant/subject binding, source eligibility, conformance outcome, integrity, policy selection, scope expansion, limitation suppression, or consequential action.

## 31. Provider-Neutrality Rule

No provider-specific API, cloud service, queue, event bus, webhook product, cache, database, identity provider, or gateway technology is normative in Phase 7 planning.

## 32. Security Rule

Least privilege, deny-by-default authorization, tenant isolation, subject/scope binding, data minimization, integrity, provenance, and audit correlation are mandatory planning properties.

## 33. Non-Implementation Rule

This contract MUST NOT be interpreted as authorization to implement APIs, gateways, credentials, network calls, persistence, queues, events, webhooks, feeds, caches, audit sinks, or runtime services.

## 34. Stop Rule

Planning MUST stop if compliance requires predecessor amendment, concrete integration activation, write authority, credentials, network access, persistence, executable API/event/queue/webhook/feed semantics, runtime action, model authority, deployment, enforcement, remediation, production access, a seventh document, or Phase 8 definition.

## 35. Lifecycle Rule

Independent whole-package review, exact-content freeze, repository materialization, staging, commit, publication, PR acceptance, Ready transition, merge authorization, canonical merge, post-merge verification, convergence, and closure are separately governed.

No earlier gate implies a later gate.

## 36. Authority State

`AFR_PHASE_7_PLANNING_AUTHORITY = BOUNDED_DELIVERY_AND_INTEGRATION_BOUNDARY_PLANNING_ONLY`

`IMPLEMENTATION_AUTHORITY = NONE`

`DELIVERY_AUTHORITY = NONE`

`CONSUMER_GATEWAY_AUTHORITY = NONE`

`API_AUTHORITY = NONE`

`EVENT_AUTHORITY = NONE`

`QUEUE_AUTHORITY = NONE`

`WEBHOOK_AUTHORITY = NONE`

`FEED_AUTHORITY = NONE`

`NETWORK_AUTHORITY = NONE`

`PERSISTENCE_AUTHORITY = NONE`

`RUNTIME_AUTHORITY = NONE`
