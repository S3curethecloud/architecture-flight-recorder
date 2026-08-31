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

Phase 0 — Doctrine and System Boundary is in planning.

No runtime, provider integration, evidence collection, conformance evaluation,
certificate generation, persistence, deployment, or production authority has
been granted.

The canonical program status will be maintained in [`docs/SOT.md`](docs/SOT.md).
