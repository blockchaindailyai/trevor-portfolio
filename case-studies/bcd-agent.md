# BCDAgent: simulation-first agent architecture

**Python · TypeScript/React · MCP · Policy controls · Blockchain integration**

[Portfolio](../README.md) · [Public source](https://github.com/blockchaindailyai/bcdagent-public) · [Offline policy demo](https://github.com/blockchaindailyai/bcdagent-public/blob/main/examples/offline_policy_demo.py)

## Overview

BCDAgent is a source-available prototype exploring policy-controlled agents and blockchain workflows. I built across its Python policy layer, tool transport, intelligence pipeline, and web interface to examine how an agent can propose and evaluate actions within explicit application constraints.

The public release makes the implementation inspectable and includes an offline demonstration using actual governance and policy modules with synthetic inputs. It remains an unfinished prototype, with simulation as its default mode.

## Architecture and engineering decisions

The project combines Python policy and execution planning, a TRON MCP service, an intelligence API and worker, a React/TypeScript interface, ingestion tools, and experimental Solidity treasury contracts.

Its organizing principle is separating a proposed action from permission to perform it. Simulation provides a place to inspect policy decisions and planned behavior before considering network submission. Interfaces between planning, policy evaluation, transport, and reconciliation make those responsibilities easier to test individually.

| Component | Purpose |
| --- | --- |
| Python policy and governance | Represent constraints, evaluate proposed actions, and model approval decisions |
| Execution planning and reconciliation | Track planned behavior and inspect resulting application state |
| TRON MCP transport | Expose structured tools and local indexing/search to an AI host |
| Intelligence API and ingestion | Gather source information, normalize records, and support downstream queries |
| React/TypeScript interface | Present application state and controls |
| Solidity contract experiments | Explore treasury, budget, strategy, subscription, and identity components |

## Inspectable code and validation

Start with the [offline policy demo](https://github.com/blockchaindailyai/bcdagent-public/blob/main/examples/offline_policy_demo.py). It reports an approval decision and reconciliation status without invoking a signer, broadcaster, or external service. The [offline test runner](https://github.com/blockchaindailyai/bcdagent-public/blob/main/tools/test_offline.py) removes runtime credentials from the test environment and blocks network connections and child processes.

The release README records **321 Python tests plus 35 subtests** and **14 Node tests** passing during preparation. These use synthetic, mocked, in-process, or loopback fixtures. It also records a successful frontend build; Node 22.12+ is recommended for the supported frontend setup. Reproduction commands and component-specific requirements are provided in the public repository.

## What this showcases

- Designing boundaries between AI reasoning, application policy, tools, and consequential operations
- Building connected backend, frontend, ingestion, and blockchain-facing components
- Making a prototype reproducible through an offline demonstration and isolated tests
- Separating application-level validation from live integration and deployment claims

## Scope and provenance

Network execution remains experimental and requires explicit configuration and opt-in. Offline tests and a frontend build do not establish wallet behavior, live chain execution, or contract security; Solidity compilation and security auditing are outside the release's validation. See the repository's [provenance and changes](https://github.com/blockchaindailyai/bcdagent-public/blob/main/docs/PROVENANCE.md) for extraction details and retained licensing declarations.
