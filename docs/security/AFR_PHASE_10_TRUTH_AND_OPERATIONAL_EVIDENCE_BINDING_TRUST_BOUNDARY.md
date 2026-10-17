# AFR Phase 10 — Truth and Operational Evidence Binding Trust Boundary

## 1. Trust posture

Operational evidence is external input and is untrusted until an explicit,
deterministic admissibility contract validates it. NEXUS architecture truth is a
qualified read-only dependency. AFR is not authorized to mutate NEXUS.

## 2. Principal boundaries

### NEXUS boundary

Qualified NEXUS anchor OID: `ef1c048ef3c6daaca2f6f1d35fd52341227843b5`.

Trusted only at the exact qualified immutable identity. The reconciled current NEXUS
`main` (`bdbc4cf8bf5fcd925c18d49a78ee408773b3ee19`) is recorded only as a
contract-preserving descendant and does not rebind the qualified anchor. A repository
name, branch, tag, UI status, or newer `main` does not replace the accepted anchor. NEXUS retains
ownership of architecture truth and architecture-risk interpretation.

### Evidence-producer boundary

Evidence producers may supply bytes and metadata but gain no AFR authority. Their
self-asserted subject, time, provenance, tenant, environment, and classification
claims require contract validation or independent corroboration where the accepted
contract requires it.

### AFR boundary

AFR may later evaluate admitted evidence only under separately granted authority.
Admission is not conformance. Conformance is not NEXUS acceptance or risk.

## 3. Threats the contract must address

- architecture-truth substitution through mutable aliases;
- evidence payload tampering;
- digest/canonicalization confusion;
- parser differential and ambiguous serialization;
- producer/source impersonation;
- subject substitution;
- cross-tenant or cross-environment evidence confusion;
- provenance/custody fabrication;
- timestamp forgery and chronology inversion;
- replay and duplicate amplification;
- stale evidence represented as current;
- partial evidence-set truncation;
- evidence-set reordering;
- conflicting evidence hidden by last-write-wins behavior;
- schema/canonicalization downgrade;
- unknown-field smuggling;
- oversized, malformed, recursive, compressed-bomb, or otherwise hostile payloads;
- sensitive-data overcollection;
- secret-bearing evidence persisted or echoed unnecessarily;
- authority laundering from evidence availability into findings, conformance,
  NEXUS mutation, implementation, runtime, or Phase 11 authority.

## 4. Fail-closed doctrine

If required identity, integrity, provenance, chronology, version, scope, or
canonicalization cannot be proved under the accepted contract, the evidence is not
admissible. The system must not repair critical ambiguity by guessing, defaulting
to `latest`, selecting an arbitrary conflicting record, or weakening a required
field to optional at runtime.

## 5. Data minimization

The planned binding model should preserve the minimum evidence required for
reproducibility and audit. Secrets, credentials, bearer tokens, private keys, and
unnecessary personal or regulated data are not part of the planning package and
must not be copied into identity manifests, logs, binding IDs, or review output.

## 6. Side-effect prohibition

During Phase 10 planning and contract preparation:

- provider/API operational reads: NONE for evidence collection;
- provider/API writes: NONE;
- evidence ingestion: NONE;
- runtime collector execution: NONE;
- AFR findings/conformance effect: NONE;
- NEXUS mutation: NONE;
- Phase 11 authority: NONE.

Read-only checks of repository identity and the already-qualified NEXUS consumer
contract are governance verification, not operational-evidence ingestion.
