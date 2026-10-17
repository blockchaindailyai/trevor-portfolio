# BCDAgent — simulation-first prototype

[Public repository and setup](https://github.com/blockchaindailyai/bcdagent-public) · [Offline demo](https://github.com/blockchaindailyai/bcdagent-public/blob/main/examples/offline_policy_demo.py) · [Release provenance](https://github.com/blockchaindailyai/bcdagent-public/blob/main/docs/PROVENANCE.md)

BCDAgent is an agent prototype that defaults to simulation. Testnet broadcasting requires explicit opt-in, keeping simulated behavior distinct from actions submitted to a network.

The public release contains sanitized first-party implementation code spanning Python policy and execution planning, a TRON MCP service, an intelligence API/worker, a React/TypeScript interface, ingestion tools and Solidity treasury contracts. Deployment addresses and configuration have been replaced with synthetic fixtures or placeholders; private history, runtime data and audit evidence are excluded.

## Source guide

| Component | Entry point |
| --- | --- |
| Governance routing and policy decisions | [Governance](https://github.com/blockchaindailyai/bcdagent-public/blob/main/openclaw_agent/capabilities/governance.py) · [Policy controls](https://github.com/blockchaindailyai/bcdagent-public/blob/main/openclaw_agent/capabilities/policy_controls.py) |
| Agent execution orchestration | [Runtime](https://github.com/blockchaindailyai/bcdagent-public/blob/main/openclaw_agent/turnkey/runtime.py) |
| TRON MCP transport | [Server](https://github.com/blockchaindailyai/bcdagent-public/blob/main/mcp-server-tron/src/server.js) |
| Intelligence pipeline | [Worker](https://github.com/blockchaindailyai/bcdagent-public/blob/main/bcd-intel-api/worker.js) |
| User interface and treasury contracts | [Frontend](https://github.com/blockchaindailyai/bcdagent-public/tree/main/bcd-treasury-frontend/src) · [Contracts](https://github.com/blockchaindailyai/bcdagent-public/tree/main/contracts) |

## Validation and limits

The released candidate passed 321 Python tests and 35 subtests with network and subprocess access blocked, plus 14 Node tests using mocked or local fixtures. The TypeScript/Vite frontend build passed. The preparation machine used Node 20.11.1 and emitted an engine-version warning; the documented setup requires Node 22.12+.

The project is unfinished. Its current scope is prototype exploration, rather than production autonomy or a mainnet service. Simulated results do not establish successful chain execution, trading performance or custody guarantees.

Live-chain integrations, signer and broadcast behavior remain unverified. Solidity contracts were not compiled or audited during release preparation. The offline demo exercises actual policy modules with synthetic inputs and does not broadcast transactions.
