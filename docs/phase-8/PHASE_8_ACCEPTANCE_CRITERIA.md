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

## 16. Post-Canonical Closure Reconciliation Candidate R1

The Phase 8 six-document planning package is canonically accepted and has
completed post-merge canonical convergence, but remains closure-pending until
this separately governed documentation-only closure lifecycle reaches its
complete effective point.

The accepted planning-package evidence is exactly:

- planning-package base:
  `ce080591fb65824aeb50f881b053e382c2b7fcf9`;
- planning-package commit:
  `92b3be0a93231c7bb160559deef9df386a6d560e`;
- canonical merge:
  `62c3259f841b50e33e524327888fea05356b79b5`;
- canonical tree:
  `a4a4d6eb8b54fa21a6a6996009d79d2c61ee9343`;
- pull request: `#33`;
- exact six-document identity: `PASS`;
- exact six-path merge boundary: `PASS`;
- canonical convergence acceptance receipt SHA-256:
  `06f18b869a44f46684dbe0d1503a25782285ff0a97246ed75811e3287939b459`;
- canonical closure review receipt SHA-256:
  `b110d08c1e536041beeb652b1a4335f3d4252fed0ed50806a40d9fd85ab64b37`;
- closure preparation specification SHA-256:
  `f0d08673809babf56a9223ffe1e5a7dbaa9cd0d6e43194beff5990d932cd6c36`;
- closure scope manifest SHA-256:
  `043b2a95e65b8631a6841ba5214f4a1a207b2e903cfcaa2c18c1c4d53b032e80`;
- closure preparation authorization receipt SHA-256:
  `9aa75b4164c57601817baea4234cb1c2ae174e10f69ed458bd48cf2180cfd930`.

Closure acceptance is limited exactly to append-only modification of:

1. `docs/SOT.md`
2. `docs/phase-8/PHASE_8_ACCEPTANCE_CRITERIA.md`

No third document is part of the closure scope.

The Phase 8 plan, architecture, contract, and trust-boundary documents remain
byte-identical to their accepted planning-package identities:

- `docs/phase-8/PHASE_8_PLAN.md`:
  `78f68f98d9a62055dc9d55fb7526ab1ddab5b843443bbeee4696a56eaf1a0081`;
- `docs/architecture/AFR_READ_ONLY_CONSUMER_GATEWAY_FIRST_SLICE_ARCHITECTURE.md`:
  `ca23b0d8b553befda0d178743c5d5abf85ad6ad8d707fdcb6a556325812171ca`;
- `docs/contracts/AFR_READ_ONLY_CONSUMER_GATEWAY_FIRST_SLICE_CONTRACT.md`:
  `6aab9336886c18b8138a1821fd999c02a61dc676dfc9974741da838ac013d13a`;
- `docs/security/AFR_PHASE_8_READ_ONLY_CONSUMER_GATEWAY_FIRST_SLICE_TRUST_BOUNDARY.md`:
  `649c56fd0bfbf2c5f3e6b7b001110f60f00c1c6867cf4436f6f2d0411edebf36`.

The closure candidate must preserve every existing Phase 8 planning criterion
and every predecessor boundary.

Closure acceptance requires all of the following:

- the change is append-only;
- exactly the two accepted closure documents change;
- both complete future preimages receive independent content acceptance;
- both accepted complete preimages are frozen by exact identity before
  repository materialization;
- the accepted planning-package base, planning commit, canonical merge,
  canonical tree, exact six-document boundary, exact six-path merge boundary,
  and canonical convergence evidence remain bound exactly;
- the four non-closure Phase 8 planning documents remain byte-identical;
- no predecessor semantic is rewritten;
- no planning architecture, authorization, tenant, subject, scope,
  deterministic-projection, source-truth, outcome, limitation, integrity,
  provenance, validity, freshness, fail-closed, or model-exclusion semantic is
  broadened or replaced;
- no source, executable schema, test, fixture, dependency, configuration, API,
  gateway implementation, event, queue, webhook, feed, credential, network,
  persistence, cache, external integration, runtime execution, runtime
  delivery, deployment, enforcement, remediation, or production authority is
  created;
- repository materialization occurs only under separately granted authority;
- the materialized change is independently verified as exact, append-only, and
  two-document bounded;
- staging occurs only under separately granted authority;
- the staged index is independently verified;
- commit occurs only under separately granted authority;
- push occurs only under separately granted authority;
- an exact Draft pull request preserves the accepted closure identity;
- the Draft pull request receives independent acceptance;
- Draft-to-Ready transition requires explicit separate authorization;
- merge requires explicit separate authorization;
- the exact reviewed closure candidate is merged to canonical `main`;
- post-merge identity, ordered parents, tree, exact two-document boundary, and
  frozen content identities are independently verified;
- local and remote canonical `main` converge on the verified closure merge; and
- the canonical checkout, worktree, and index are clean.

Before every closure-effective-point condition passes:

`AFR_PHASE_8_PLANNING_STATUS = PLANNING_ACCEPTED_CLOSURE_PENDING`

`AFR_PHASE_8_PLANNING_AUTHORITY = BOUNDED_READ_ONLY_CONSUMER_GATEWAY_FIRST_SLICE_IMPLEMENTATION_PLANNING_ONLY`

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

After and only after every closure-effective-point condition passes:

`AFR_PHASE_8_PLANNING_STATUS = COMPLETE`

`AFR_PHASE_8_PLANNING_AUTHORITY = CONSUMED_CLOSED`

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

Terminal planning closure creates no implementation or successor authority.
