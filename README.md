# Trevor — Software Engineering Portfolio

I build software for market information, execution research and automation, with a focus on explicit state, reproducible behavior and operational failure handling.

Full Stack Web Development Live Example: [Blockchain Daily](https://blockchaindaily.org) · Automated Trading Engine: [Python execution sample](https://github.com/blockchaindailyai/trading-engine-sample)

## Selected work

| Project | Engineering focus | Explore |
| --- | --- | --- |
| Blockchain Daily terminal and news pipeline | React/TypeScript, subscription access, cursor-based headlines, worker queues and source provenance | [Case study](case-studies/blockchain-daily.md) |
| NRT client work | TradingView/Pine Script indicators and dashboards | [Public showcases](case-studies/nrt.md) |
| Python execution research | Execution modeling, risk exits and reproducible research | [Case study](case-studies/execution-research.md) · [Runnable sample](trading-engine-sample/README.md) |
| Rackmail MCP | Mail-tool integration | [Public Source](https://github.com/blockchaindailyai/Rackspace-MCP) · [Project overview](case-studies/rackmail.md) |
| BCDAgent | Simulation-first agent prototype; live-chain behavior unverified | [Public source](https://github.com/blockchaindailyai/bcdagent-public) · [Prototype scope and source guide](case-studies/bcd-agent.md) |
| Rust shadow execution | Rust research alongside an authoritative Python engine | [Research subcase](case-studies/rust-shadow.md) |

## Public TradingView showcases

[CORE BEHAVIOR](https://www.tradingview.com/script/lgOiMkb9-Neely-River/) · [EARNINGS](https://www.tradingview.com/script/DqzDGWI6-Neely-River-EARNINGS/) · [TREND Moat](https://www.tradingview.com/script/CgqzZbQa-Neely-River-TREND-Moat/) · [ACCUM/DIST](https://www.tradingview.com/script/s0vXSOP2-Neely-River-ACCUM-DIST/) · [BREAKOUT](https://www.tradingview.com/script/tDr1bslF-Neely-River-BREAKOUT/) · [SPEED](https://www.tradingview.com/script/ojlRNskV-Neely-River-SPEED/)

These published pages showcase client work; client source remains private.

## Run the Python sample

The [runnable sample](trading-engine-sample/README.md) uses the existing public `engine.py` unchanged. Newly written support modules, packaging and a synthetic-data driver make that actual engine excerpt runnable. Tests cover stop-exit behavior, cost/equity reconciliation and input validation.

The demonstration uses fabricated market data and scheduled positions. It illustrates execution accounting rather than strategy performance. The case studies distinguish product work from prototypes and research; private application source and runtime data are not included.
