# agentic-swarm-guardrails

Guardrail enforcers for self-evolving agent swarms, built as a starting point for Navy SBIR topic **DON27BZ02-NV012, Self-Replicating Evolutionary Agentic SI Swarming Force with Autonomous Embedded SI Guardrail Enforcers** (DoW FY27 Release 2).

> The public topic states the technology is restricted under ITAR/EAR. This public repository holds only general, unclassified design work drawn from the public topic text. Keep any controlled technical data out of it.

## The problem

The topic asks for a swarm of AI agents that can replicate and evolve on its own, and for embedded guardrail agents that keep that evolving swarm inside fixed safety, security and policy boundaries. The hard-fail metrics are zero safety violations, zero boundary violations, zero uncontrolled replication and zero drift from policy.

## Approach in plain terms

Treat every agent action as a request that must pass an enforcer before it runs. The enforcer checks the action against a policy that the agents cannot edit: which actions are allowed, how many replicas may exist, which resources may be used. Every decision is logged. The swarm can evolve its behavior, but only through actions the enforcer approves.

## Phase I scope

A feasibility study built around a challenge problem (a cross-domain littoral anti-access scenario), a preliminary architecture, a risk assessment and a Phase II plan. Simulation-only is acceptable; hardware in the loop is preferred. See [docs/topic-summary.md](docs/topic-summary.md).

## Status

Skeleton only. The first vertical slice (toy agents, one enforcer, one policy, a replication budget) is sketched in [docs/architecture.md](docs/architecture.md) and stubbed in `src/`.

## How to run

```bash
python -m unittest discover -s tests -v
```

## Documentation

- [docs/topic-summary.md](docs/topic-summary.md): what the public topic asks for
- [docs/topic-qa.md](docs/topic-qa.md): posted topic Q&A, summarized
- [docs/references.md](docs/references.md): the topic's references
- [docs/submission-requirements.md](docs/submission-requirements.md): dates, award size, official instructions
- [docs/architecture.md](docs/architecture.md): first vertical slice and design decisions
