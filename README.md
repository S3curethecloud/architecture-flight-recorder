# Architecture Flight Recorder

Architecture Flight Recorder (AFR) is a continuous architecture-conformance
verification platform.

AFR compares approved architecture truth from an authoritative architecture
system such as NEXUS with time-bound operational evidence from deployed
environments. It detects unsupported claims, contradictory evidence, stale
evidence, and architecture drift.

AFR does not create architecture truth, grant execution authority, or replace
runtime enforcement systems.

## Product Boundary

```text
NEXUS     = defines and approves architecture truth
AFR       = verifies deployed reality against approved truth
ATA       = governs consequential runtime commit authority
PAA       = initiates work and coordinates human-facing remediation
Humanize  = presents approved evidence and conformance narratives
```

## Current Status

The Phase 0 doctrine and system-boundary package was reviewed, amended, and
merged through PR #1.

Canonical package identity:

- merge commit: `5d453729fa2505ef09ddb8ef30daa6e1303c05e9`;
- merge tree: `229a2694d5fc093e1cfaf4a266efa3c6df0e7398`;
- initial package commit: `b1bb95b04db0b2d9d17276e64d80af6df9afce32`;
- review-amendment commit: `dc885d1632af8b2777974ce90233c6c8f82b8106`.

Phase 0 becomes canonically complete only when the bounded post-merge closure
reconciliation is independently reviewed, merged to canonical `main`, and its
identity and integrity are verified.

No runtime, provider integration, evidence collection, conformance evaluation,
certificate generation, persistence, deployment, production, or Phase 1
authority has been granted.

The canonical program status is maintained in [`docs/SOT.md`](docs/SOT.md).
