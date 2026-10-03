# AFR Read-Only Consumer Gateway First-Slice Contract
1. Purpose
This planning contract defines the deterministic first-slice semantic
requirements. It defines no executable schema or implementation.
2. Normative Rules
1. Only an already-approved AFR source output MAY be consumed.
2. Exact source identity MUST be bound.
3. An attributable consumer identity MUST be bound.
4. Tenant identity MUST be explicit.
5. Subject identity MUST be explicit where applicable.
6. Requested read scope MUST be explicit.
7. Policy identifier/version MUST be explicit.
8. An explicit authorization decision and decision identity MUST be supplied.
9. Authorization MUST bind the same source, consumer, tenant, subject, scope,
   and policy version as the request.
10. Missing, denied, ambiguous, or mismatched authorization MUST fail closed.
11. Requested scope MUST NOT exceed source scope.
12. Requested scope MUST NOT exceed authorized scope.
13. Scope MAY narrow only when resulting meaning remains truthful.
14. Scope and privilege MUST NOT expand.
15. Projection MUST be read-only and representational.
16. Projection MUST NOT create or change a conformance outcome.
17. Material limitations MUST remain represented where omission would
    strengthen apparent meaning.
18. Existing source integrity/provenance metadata MUST remain attributable.
19. Integrity claims MUST NOT exceed source guarantees.
20. Projection MUST NOT refresh stale state, extend expiry, or erase
    supersession.
21. Identical source and bound context MUST produce the same logical decision.
22. Ambient state, randomness, and generative-model output MUST NOT change
    authoritative entitlement.
23. Denial and failure MUST NOT alter authoritative AFR state.
24. A prior representation MUST NOT establish entitlement outside its original
    bound source/consumer/tenant/subject/scope/policy/validity context.
25. Models and agents MUST NOT authoritatively determine authorization,
    entitlement, scope expansion, source eligibility, integrity, conformance
    outcome, limitation suppression, or consequential action.
3. Logical Result Contract
Exactly one logical result class applies:
- READ_ONLY_PROJECTION_ALLOWED
- READ_ONLY_PROJECTION_DENIED
- READ_ONLY_PROJECTION_FAIL_CLOSED
Only the allowed class may carry bounded source content.
4. Fail-Closed Contract
Fail closed on unresolved identity, authorization absence/denial/mismatch,
tenant mismatch, subject mismatch, scope violation, policy mismatch, source
mismatch/ineligibility, integrity mismatch, invalid/stale state where current
validity is required, unsafe projection, or missing mandatory source context.
5. Prohibited Implementation Effects
This contract MUST NOT authorize or require:
- network/API activation;
- credentials or service identities;
- signing keys or certificates;
- persistence or cache;
- event/queue/webhook/feed/stream activation;
- concrete external integration;
- authoritative AFR mutation;
- downstream mutation;
- runtime delivery;
- deployment;
- enforcement;
- remediation;
- production access.
6. Lifecycle Rule
Independent whole-package acceptance must precede any separately governed
repository materialization proposal.

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
