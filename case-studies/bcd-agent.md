# BCDAgent: simulation-first agent architecture

**Python · TypeScript/React · MCP · Policy controls · Blockchain integration**

[Portfolio](../README.md)

## Project status

BCDAgent is an unfinished private prototype exploring policy-controlled agents and blockchain workflows. This page describes the architecture at a high level; source access is not currently offered through this portfolio.

## Engineering focus

The project combines Python policy and execution planning, a TRON MCP service, an intelligence API and worker, a React/TypeScript interface, ingestion tools, and experimental Solidity treasury contracts.

Its organizing principle is separating a proposed action from permission to perform it. Simulation provides a place to inspect policy decisions and planned behavior before considering any network submission.

| Component | Purpose |
| --- | --- |
| Policy and governance routing | Represent constraints and evaluate proposed actions |
| Agent orchestration | Coordinate decisions and execution planning |
| MCP transport | Expose structured tools to an AI host |
| Intelligence pipeline | Gather and process information used by the application |
| Web interface | Present application state and controls |
| Treasury-contract experiments | Explore on-chain components separately from the agent interface |

## What this work contributes to my portfolio

BCDAgent adds experience designing the boundaries between AI reasoning, application policy, tools, and consequential actions. It also demonstrates work across backend services, a frontend, and blockchain interfaces within one prototype.

## Scope

The project is not presented as a production autonomous agent or a live mainnet service. Simulated behavior does not establish chain execution, custody safety, contract security, or trading performance. Contract compilation and security auditing are outside this portfolio's validation claims.
