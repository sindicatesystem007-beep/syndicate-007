# Syndicate 007

## AI Business OS

**Intelligence. Automation. Growth.**

Syndicate 007 is an owner-controlled AI system designed around one business
operating loop:

**Goal → Action → Measurement → Learning → Money**

It connects opportunity discovery, evidence-bound analysis, governed internal
execution, result measurement and learning. The aim is to turn isolated AI tasks
into a measurable workflow while keeping the owner in control of risk.

**Public Source-Visible Preview:** this repository contains architecture documents,
synthetic contract examples and an offline demo. It is **not the full production
runtime**. The private implementation is under active development and local pilot
use. No guaranteed revenue, autonomous sales or unrestricted external execution
is claimed.

**Start here:** open `demo.html` for the walkthrough, or run `python demo_runner.py`
with existing Python 3.10+. No package installation, credentials or network needed.

## What Syndicate 007 does

- Opportunity discovery and business / buyer intake.
- Evidence-bound decision support and owner priorities.
- Governed internal execution of approved capabilities.
- MEDIA planning, production packages, measurement and learning.
- Cost / revenue truth boundaries and next-action projection.
- Head Manager / owner intelligence across connected sources.

These describe the private implementation. This public package illustrates its
contracts and boundaries; it does not execute the private capabilities.

## Why an operating loop?

Many AI tools handle an individual task. A business workflow also needs evidence,
permissions, a recorded result and a way to learn from it. Syndicate 007 is designed
to connect those steps: intelligence understands a possibility, Head Manager
identifies a priority, governance bounds the risk, authorized execution performs
internal work, measurement records the result, and learning informs the next cycle.
Money is a measured outcome when supported by evidence, not an assumed consequence.

## Current capability map

“Available” below means implemented in the private local runtime, not bundled here.

| Capability | Status / public boundary |
|---|---|
| Opportunity discovery | Available privately; synthetic public walkthrough |
| Business / buyer intake | Available privately; request is not a client |
| Head Manager | Available privately; advisory architecture overview here |
| Governed internal execution | Available privately for approved internal capabilities |
| MEDIA operations | Available privately; owner-controlled publication |
| Result / revenue evidence | Recording contracts available; revenue remains unknown without evidence |
| Learning / next actions | Evidence-based proposals; no causal guarantee |
| External contact | Explicit owner authorization required |
| Payments | No autonomous payment capability enabled |
| Production ChatGPT / OpenAI provider | Not included or configured by this snapshot; no active production integration claim |

## Head Manager

Head Manager combines bounded owner context into priorities, blockers and evidence
gaps. It can identify safe internal action candidates from existing approved
capabilities. Deterministic reasoning is the fallback; optional bounded adapters
select existing evidence and actions rather than inventing execution authority.

Recommendations cannot bypass governance, approve spending or authorize external
contact/publication. Unknown source coverage remains unknown. The Head Manager
runtime and its Telegram/cockpit integration stay private.

## Architecture at a glance

```text
Evidence / Sources
        ↓
Owner Context
        ↓
Head Manager
        ↓
Governance / Execution Gate ──→ Owner Approval ──→ Authorized External Action
        ↓
Internal Execution
        ↓
Result / Revenue Evidence
        ↓
Learning ──→ next Goal / Action
```

This is a conceptual overview, not a map of active workers or a public executor.
See [ARCHITECTURE.md](ARCHITECTURE.md). Cross-store persistence has a known
non-atomic boundary; no global transaction or production recovery guarantee is claimed.

## Bounded use cases

| Use case | What it supports | Boundary |
|---|---|---|
| AI Media Operator | Plan content, prepare/review packages, ingest measurements, propose the next experiment | Approval is not publication; no automatic publishing |
| Opportunity-to-Income | Public demand → intake → analysis → plan → commercial review → result/revenue evidence | Request is not a deal; draft is not sent; no guaranteed income |
| AI Business Automation | Approved safe internal capabilities through governance | Unknown cost and missing authorization fail closed |
| Owner Intelligence | CEO brief, priorities, blockers, missing information | Connected sources only; no invented system-wide telemetry |

## What is public — and what stays private

The public package is a **curated, history-free, source-visible snapshot**: readable
architecture, contract projections, synthetic examples, passive HTML and a stdlib
replay runner. This is an intentional product boundary, not an incomplete installer.

The full runtime, production credentials, private execution configuration, databases,
runtime state, customer data, operational history, unpublished assets and full
development Git history are excluded. Provider integrations and commercial
orchestration remain private. See [OPEN_CORE.md](OPEN_CORE.md) and [ROADMAP.md](ROADMAP.md).
Future public interfaces are a roadmap decision, not a current open-source grant.

## Offline demo

1. Read this overview and the architecture notes.
2. Open `demo.html` directly for the eight-step synthetic walkthrough.
3. Optionally, with existing Python 3.10+, run `python demo_runner.py`.
4. Compare the output with `demo_fixture.json`; all scenario values are synthetic.

The runner uses the standard library, reads its adjacent fixed fixture and writes
nothing. No server, packages, network, credentials, database or elevated shell is
required. It validates demonstration boundaries, not production execution.
The full runtime requires private configuration and is not installable from this
snapshot. See [DEMO.md](DEMO.md) and [INSTALL.md](INSTALL.md).

## Governance and data truth

- Evidence-bound decisions: a model response is not proof of execution.
- Unknown ≠ zero; registered ≠ active; estimated ≠ recorded.
- Price ≠ revenue; potential ≠ revenue; revenue ≠ profit.
- Technical execution ≠ business result; approval ≠ sending/publication.
- External/high-risk actions require explicit authorization.
- Secrets, private runtime state and customer evidence are excluded from this package.

## Status and license

**Public Source-Visible Preview.** Private runtime is under active development and
local pilot use. This preview is not a production application/SDK or a hosted SaaS
offer. Primary development / owner interface supports RU/EN.

**Source-visible / All Rights Reserved.** See [LICENSE](LICENSE), [NOTICE](NOTICE)
and [LICENSE_SCOPE.md](LICENSE_SCOPE.md). Copying, redistribution, modification,
sublicensing and commercial use require permission. No trademark rights are granted.
Third-party components remain under their own terms. This is not open source.

The exact curated file/hash inventory is `RELEASE_MANIFEST.json`; build boundaries
are recorded in `PUBLIC_SNAPSHOT_PROVENANCE.md`.
