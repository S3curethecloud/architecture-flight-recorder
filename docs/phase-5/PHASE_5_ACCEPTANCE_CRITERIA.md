# AFR Phase 5 Acceptance Criteria

## 1. Purpose

These criteria govern acceptance of the documentation-only Phase 5 planning
package for:

`EVIDENCE_ACQUISITION_AND_COLLECTION_BOUNDARY_PLANNING`

They determine whether the package defines a coherent, provider-neutral,
least-privilege, fail-closed acquisition boundary that can produce attributable
supplied operational observations for Phase 4 without performing Phase 4
evidence eligibility or AFR conformance.

Satisfying these criteria does not authorize implementation, live collection,
provider integration, credentials, network access, persistence, NEXUS, ARCP,
ATA, runtime evaluation, certificates, deployment, enforcement, remediation,
or production use.

## 2. Canonical Baseline Acceptance

Planning is acceptable only if:

- canonical `main` remains based on
  `d19e0c7b0d3b8812bb5e23d01ba01c28d2b5b589`;
- the activation tree remains
  `ee8120180c663bef3d13d6d5ada8acf6284e4421`;
- the Phase 5 planning-authority effective point remains complete;
- Phase 4 planning remains `COMPLETE`;
- Phase 4 planning authority remains `CONSUMED_CLOSED`;
- Phase 4 implementation authority remains `CONSUMED_CLOSED`;
- Phase 4 additional implementation authority remains `NONE`;
- no accepted Phase 0 through Phase 4 semantic is silently reopened.

## 3. Exact Planning-Package Boundary

The complete Phase 5 planning candidate must contain changes to exactly:

1. `docs/SOT.md`
2. `docs/phase-5/PHASE_5_PLAN.md`
3. `docs/phase-5/PHASE_5_ACCEPTANCE_CRITERIA.md`
4. `docs/architecture/AFR_EVIDENCE_ACQUISITION_ARCHITECTURE.md`
5. `docs/contracts/AFR_OBSERVATION_ACQUISITION_CONTRACT.md`
6. `docs/security/AFR_PHASE_5_EVIDENCE_ACQUISITION_TRUST_BOUNDARY.md`

Acceptance fails if a seventh document or any source, test, vector, fixture,
executable schema, dependency, configuration, migration, build artifact, or
provider-specific adapter is introduced.

## 4. Document Convergence

All six documents must converge on:

- one capability identity;
- one acquisition lifecycle;
- one collector and source identity model;
- one collection-scope and completeness model;
- one temporal model;
- one collection-outcome model;
- one failure model;
- one raw-response boundary;
- one Phase 4 handoff boundary;
- one security and trust boundary;
- one provider-neutrality position;
- one authority boundary.

Contradictory definitions or document-specific semantic variants are blocking
findings.

## 5. Collector-Identity Acceptance

The package must explicitly define collector identity without relying on
ambient process state.

Collector identity must bind, as applicable:

- collector identifier;
- collector version;
- collector class;
- tenant authorization context;
- subject or target context;
- environment context;
- approved source class;
- approved operation class;
- authorization-policy reference;
- collection-request identity.

A future collector cannot self-assert expanded authority.

## 6. Source-Identity Acceptance

The package must define source identity and source class explicitly.

Source identity planning must distinguish provider or enterprise source
reference, source-native account or project boundary where applicable,
endpoint identity where applicable, and source representation or API version.

Credentials, DNS, hostnames, local configuration, environment variables, or
deployment placement cannot implicitly establish source identity.

## 7. Tenant, Subject, Environment, and Scope Acceptance

Every planned request and result must bind:

- tenant;
- subject and subject type;
- environment;
- source;
- collector;
- requested scope;
- applicable versions.

Cross-tenant, cross-subject, cross-environment, and cross-scope substitution
must fail closed in any future implementation.

## 8. Collection-Request Identity Acceptance

The request identity must bind all material governed request inputs without
including secret or credential material.

Material request changes must produce a different request identity.

The package must prohibit identity derived only from arrival order, process
memory address, random identifiers without bound context, or provider-specific
ambient state.

## 9. Collection-Result Identity Acceptance

Result identity must bind:

- request identity;
- source identity;
- source-response identity or explicit absence;
- observed scope;
- successful scope;
- failed scope;
- unsupported scope;
- omitted scope;
- collection outcome;
- source-native observation time where available;
- collection start and completion times;
- representation and version;
- bounded transformation metadata.

Material changes must change result identity.

## 10. Time-Semantics Acceptance

The package must distinguish:

- request time;
- collection start time;
- collection completion time;
- provider or source observation time where available;
- source response time where meaningful;
- result construction time;
- handoff time.

Missing source-native time must remain missing or unknown.

Phase 5 must not invent trusted time or redefine Phase 4 freshness policy.

## 11. Collection-Scope Acceptance

The package must distinguish:

- requested scope;
- source-accepted scope;
- observed scope;
- successful scope;
- failed scope;
- unsupported scope;
- omitted scope;
- filtered scope;
- paginated or segmented scope.

A completeness claim must be explicitly relative to a bounded request and must
not exceed successfully observed scope.

Unknown state cannot be converted to absence.

## 12. Pagination and Segmentation Acceptance

Planning must define behavior for:

- page or segment identity;
- continuation-token presence;
- duplicate pages or segments;
- missing pages or segments;
- continuation failure;
- source-reported totals where available;
- collector-observed totals;
- bounded page and item limits;
- partial completion.

A failed or omitted page cannot coexist with an unqualified complete result.

## 13. Collection-Outcome Acceptance

The package must distinguish the collection-only classes:

- `COLLECTION_COMPLETE`;
- `COLLECTION_PARTIAL`;
- `COLLECTION_FAILED`;
- `COLLECTION_UNSUPPORTED`;
- `COLLECTION_CANCELLED`.

They must remain distinct from Phase 4 evidence-eligibility and AFR
conformance outcomes.

No collection outcome may directly imply `ELIGIBLE`, `INELIGIBLE`,
`QUARANTINED`, `CONFORMANT`, `NON_CONFORMANT`, `INCONCLUSIVE`, or `STALE`.

## 14. Source-Failure Acceptance

The package must define explicit structured handling for:

- authorization denial;
- source access failure;
- timeout;
- throttling;
- partial response;
- pagination or segmentation failure;
- unsupported endpoint or operation;
- malformed source response;
- ambiguous source identity;
- inconsistent scope;
- source-version mismatch;
- bounded-resource exhaustion;
- cancellation;
- collector internal failure.

Failure must not be converted into positive evidence, negative evidence,
absence, eligibility, or conformance.

## 15. Raw-Response Acceptance

The package must distinguish source-native response bytes from:

- response identity;
- response metadata;
- redacted representations;
- minimized representations;
- parsed representations;
- collector-generated metadata;
- transformation metadata;
- Phase 4 handoff representation.

Any preservation requirement must remain conditional on security, privacy,
contractual, and provider constraints.

Planning must create no persistence or retention authority.

## 16. Least-Privilege Read-Only Acceptance

The package must require future collection operations to be:

- explicitly bounded;
- read-only;
- least privilege;
- attributable;
- scope minimized;
- fail-closed on authority ambiguity.

The package must prohibit write, mutation, remediation, acknowledgement,
deletion, tagging, annotation, quarantine, deployment, or policy-change
authority.

Planning creates no credentials and performs no live source call.

## 17. Provider-Neutrality Acceptance

The acquisition semantics must remain independent of specific clouds, cluster
managers, CI/CD systems, observability vendors, security products, SaaS
products, data warehouses, model gateways, MCP systems, SDKs, and APIs.

A future provider adapter may translate a source response into the governed
collection model, but it cannot:

- define AFR semantics;
- expand its own authority;
- determine Phase 4 eligibility;
- emit conformance;
- bypass tenant or scope binding;
- weaken failure behavior;
- create write authority.

## 18. Phase 4 Handoff Acceptance

The planned handoff must preserve:

- collector and source identity;
- tenant, subject, environment, and scope;
- request and result identity;
- source-response identity or explicit absence;
- collection and source-observation times;
- collection outcome;
- partial-collection state;
- successful, failed, unsupported, omitted, and filtered scope;
- representation and version;
- bounded transformation metadata;
- structured source failures;
- raw-response identity or reference where permitted.

Phase 4 must remain solely responsible for observation-to-evidence eligibility.

## 19. Security and Privacy Acceptance

The package must address:

- untrusted source responses;
- least-privilege read-only identity;
- tenant and subject isolation;
- source authenticity;
- request and result attribution;
- response-integrity inputs;
- credential and secret non-persistence;
- sensitive-data minimization;
- collection-scope minimization;
- bounded response processing;
- audit-safe failure records;
- provenance continuity;
- supply-chain independence;
- safe cancellation;
- bounded resource use.

No live credential, network, filesystem, persistence, plugin, subprocess,
remote-code, or production access is permitted.

## 20. Bounded-Resource Acceptance

Planning must define conceptual versioned bounds for future acquisition,
including as applicable:

- maximum source-response bytes;
- maximum page or segment count;
- maximum collected item count;
- maximum nesting depth;
- maximum metadata cardinality;
- maximum failure-record count;
- maximum transformation work units.

A future implementation must fail closed or produce an explicit partial or
failed collection result when a bound is reached.

Bounds cannot silently truncate while preserving a complete result.

## 21. Audit and Provenance Acceptance

Every collection result must be attributable to:

- collector identity;
- source identity;
- request identity;
- authorization-context reference;
- scope;
- relevant times;
- representation and version;
- result identity;
- structured failure state where applicable.

Audit records must minimize sensitive payload exposure and must not include
credentials or secrets.

## 22. Phase and Cross-Program Non-Drift Acceptance

The package must preserve:

- provider or enterprise source authority over its own bounded state;
- NEXUS architecture-truth authority where applicable;
- Phase 4 evidence-eligibility authority;
- AFR deterministic conformance authority;
- ATA consequential runtime commit authority where applicable.

It must preserve:

`DEPENDENCY_RECOGNITION != INTEGRATION_PLANNING_AUTHORITY`

`INTEGRATION_PLANNING_AUTHORITY != INTEGRATION_IMPLEMENTATION_AUTHORITY`

`INTEGRATION_IMPLEMENTATION_AUTHORITY != RUNTIME_AUTHORITY`

## 23. Prohibited-Scope Acceptance

Acceptance fails if the planning package creates authority for:

- source or tests;
- executable schemas;
- dependencies or configuration;
- live collection;
- provider adapters;
- credentials or secrets;
- network or filesystem behavior;
- persistence;
- NEXUS, ARCP, or ATA integration;
- Phase 4 eligibility implementation or amendment;
- deterministic-kernel invocation;
- runtime conformance evaluation;
- model calls or model-based repair;
- certificates;
- deployment;
- enforcement;
- remediation;
- production access;
- Phase 5 implementation.

## 24. Stop-Condition Acceptance

Planning must stop and require separate authority if:

- architecture-truth export semantics become necessary;
- NEXUS or ARCP semantics must be defined;
- provider-specific behavior becomes normative;
- live source access becomes necessary;
- credentials or secrets become necessary;
- network access becomes necessary;
- persistence becomes necessary;
- accepted Phase 4 eligibility semantics require amendment;
- accepted Phase 0 through Phase 4 semantics require amendment;
- executable schemas, source, tests, dependencies, or configuration become
  necessary;
- the exact six-document package becomes insufficient;
- implementation or runtime behavior becomes necessary.

A stop condition cannot be waived for implementation convenience.

## 25. Review and Evidence Acceptance

The exact six-document package must pass:

- exact path-boundary verification;
- frozen content-hash verification;
- architecture review;
- contract and semantic review;
- collection-scope and completeness review;
- temporal-semantics review;
- failure-model review;
- bounded-resource review;
- security and privacy review;
- provider-neutrality review;
- Phase 4 handoff non-drift review;
- NEXUS, ARCP, and ATA authority non-drift review;
- authority-leakage review;
- independent whole-package re-review;
- repository materialization review;
- staged-object verification;
- commit and tree verification;
- remote branch and pull-request verification;
- explicit readiness transition;
- explicit merge authorization;
- post-merge canonical verification;
- separately governed planning closure reconciliation.

No review gate implies or authorizes a later gate.

## 26. Completion and Authority Acceptance

Phase 5 planning is complete only after the exact reviewed package is merged
to canonical `main`, independently verified locally and remotely, and
reconciled through a separately governed closure.

Planning completion does not create implementation authority.

The authority state remains:

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

## 27. Post-Merge Closure Reconciliation

The Phase 5 evidence-acquisition and collection-boundary planning package is
canonically accepted through PR #25 at merge commit
`034c1c5103d0fa868f589e2c7ee801dd17820cc3`, tree
`9de2827915baac58178853ad28caa4fae78536c7`, with ordered parents
`d19e0c7b0d3b8812bb5e23d01ba01c28d2b5b589` and
`c478b14bcf0f7512e402bcfca60f45d1e1ceac36`.

The exact accepted six-document package is:

1. `docs/SOT.md`
   - Git blob: `a8c81e3ce2b77385ec5c2f9165a200de92d8309c`
   - SHA-256: `ed4c706c207794b4f8e6c818f4338a94aca8fc2e680cb0d09da7f19e0ddf740f`
2. `docs/phase-5/PHASE_5_PLAN.md`
   - Git blob: `d186b9664d287860b046a161a8a59f97e964969a`
   - SHA-256: `53392f870c9486d453e2ff7717c97707e07991f1999a2f683ac8b482fd6494a7`
3. `docs/phase-5/PHASE_5_ACCEPTANCE_CRITERIA.md`
   - Git blob: `441db1a6067af740ddf399b6cb61deface076b0b`
   - SHA-256: `e08ac23ad479b46887baab54b289983196fcea3547f995fe3a68260ce6868d12`
4. `docs/architecture/AFR_EVIDENCE_ACQUISITION_ARCHITECTURE.md`
   - Git blob: `aac799d0ead2da3800c9336a9d458bec824f1794`
   - SHA-256: `781632a5c600c638dd327733e24d797f9621cbe158ec11c0d793fd41bffcb82e`
5. `docs/contracts/AFR_OBSERVATION_ACQUISITION_CONTRACT.md`
   - Git blob: `07236ea44126e06066625d331c5b8f67f2b9ab97`
   - SHA-256: `4564da35179d72d9497186f786ea7153dfca7d6fead7dcb8131c3b218f3b22a4`
6. `docs/security/AFR_PHASE_5_EVIDENCE_ACQUISITION_TRUST_BOUNDARY.md`
   - Git blob: `10dcc012d58cec073a5e092f31fd9f485396ca2b`
   - SHA-256: `ea1a5cafede059914a8be13cd0859510aded0d30596d4a2c681eb830a6d875f2`

Closure acceptance requires all of the following:

- the closure is append-only and limited exactly to `docs/SOT.md` and this
  acceptance-criteria document;
- both complete closure documents match their independently reviewed frozen
  content identities;
- PR #25's canonical merge identity, ordered parents, tree, exact six-document
  boundary, and six canonical content identities are recorded exactly;
- the independent package, pull-request, post-merge, and canonical-convergence
  acceptance evidence is preserved;
- the historical review-harness failures are recorded only as reconciled,
  non-substantive control-harness defects with no canonical effect;
- the closure creates no source, executable schema, test, fixture, dependency,
  configuration, live collection, provider adapter, credential, network,
  persistence, NEXUS, ARCP, ATA, runtime, certificate, deployment,
  enforcement, remediation, production, or subsequent-phase authority;
- closure activation remains conditional and fail-closed;
- the reviewed closure commit, tree, exact two-document boundary, and frozen
  content identities are preserved through its remote branch and pull request;
- independent closure PR acceptance, explicit Draft-to-Ready transition, and
  explicit merge authorization occur as separate gates;
- the reviewed closure is merged to canonical `main`;
- post-merge identity, ordered parents, tree, exact boundary, frozen content
  identities, local and remote convergence, canonical checkout, worktree
  cleanliness, and index cleanliness all pass; and
- all Phase 5 implementation and runtime-adjacent authorities remain `NONE`.

Before every closure condition passes:

`AFR_PHASE_5_PLANNING_STATUS =
CANONICALLY_ACCEPTED_CLOSURE_PENDING`

`AFR_PHASE_5_PLANNING_AUTHORITY = CONSUMED_PENDING_CLOSURE`

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

After and only after every closure condition passes:

`AFR_PHASE_5_PLANNING_STATUS = COMPLETE`

`AFR_PHASE_5_PLANNING_AUTHORITY = CONSUMED_CLOSED`

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

Closure completion creates no implementation, collection, integration,
runtime, persistence, certificate, deployment, enforcement, remediation,
production-access, or subsequent-phase authority.
