# Trevor Arnold
## Software engineering for trading, financial data, and AI applications

I turn market methodologies and messy information flows into working software: TradingView indicators, research and execution tools, AI-assisted data pipelines, and subscription web applications. My trading and financial-news background helps me translate domain requirements into software behavior, then work through the data, testing, integration, and operating details.

**Core focus:** Python · Pine Script · TypeScript/React · Rust · SQL · AI tool integration

[Live market-intelligence Terminal](https://blockchaindaily.org) · [Python code sample](trading-engine-sample/README.md) · [Rust code sample](rust-shadow-sample/README.md) · [Contact](mailto:fractuitiontechnologies@gmail.com)

## Selected projects

| Project | My contribution and engineering focus | Explore |
| --- | --- | --- |
| **Neely River / NRT** | Led the TradingView implementation of a client's trading methodology; Pine Script, multi-timeframe behavior, cross-platform validation, and release coordination | [Case study and published indicators](case-studies/nrt.md) |
| **Blockchain Daily + NewsBot** | Built a full-stack market-intelligence product and AI-assisted ingestion/editorial pipeline, with source traceability, subscriptions, and cost-conscious processing | [Case study](case-studies/blockchain-daily.md) · [Live product](https://blockchaindaily.org) |
| **WilliamsBot + UTBot** | Developed trading research, execution simulation, historical-data analysis, and paper-trading infrastructure | [Case study](case-studies/execution-research.md) · [Runnable Python sample](trading-engine-sample/README.md) |
| **Rackmail MCP** | Built an AI-to-email service with scoped OAuth access, verified drafts, retry-aware actions, and recoverable cleanup | [Case study](case-studies/rackmail.md) · [Public source](https://github.com/blockchaindailyai/Rackspace-MCP) |
| **Rust shadow execution** | Explored a Rust execution companion to Python, including crash-safe recovery of an append-only log | [Case study](case-studies/rust-shadow.md) · [Rust implementation](rust-shadow-sample/src/lib.rs) |
| **Market-data tooling** | Built incremental exchange-history ingestion, provider fallback, validation, and TradeStation-compatible output | [Private-project case study](case-studies/market-data.md) |
| **Volatility research** | Developed multi-timeframe compression indicators and experimental breakout-probability displays in Pine Script | [Private research overview](case-studies/volatility-research.md) |
| **BCDAgent** | Prototyped policy-controlled agents, MCP transport, and simulation-first blockchain workflows | [Private-project overview](case-studies/bcd-agent.md) |

## Where engineering and markets meet

- **Methodology to implementation:** Convert specialist rules into indicators, state transitions, multi-timeframe calculations, and testable behavior.
- **Data to research:** Capture and normalize information, preserve timestamps and provenance, and make historical records searchable and reusable.
- **AI to applications:** Connect models to structured data and tools, retain review context, and design for useful output at sustainable operating cost.
- **Research to execution:** Make sizing, costs, fills, stops, and recovery assumptions explicit; separate simulation from live execution.
- **Product to operations:** Build the accounts, subscriptions, databases, integrations, and failure handling behind a customer-facing service.

## Start with the code

### Python: execution accounting and risk exits

The [Python sample](trading-engine-sample/README.md) packages an existing public execution-engine excerpt with a synthetic-data demonstration and regression tests. Review [stop-exit tests](trading-engine-sample/tests/test_stop_exit_drawdown.py) for gap handling and adverse excursion, or [the demo](trading-engine-sample/demo.py) for cost and equity reconciliation.

### Rust: recovery before append

The [Rust sample](rust-shadow-sample/README.md) contains actual recovery logic extracted from the shadow daemon. It validates complete records before repairing a torn final record, with tests for corruption, truncation, and reopening. It has no external crate dependencies.

## Published client work

[CORE BEHAVIOR](https://www.tradingview.com/script/lgOiMkb9-Neely-River/) · [EARNINGS](https://www.tradingview.com/script/DqzDGWI6-Neely-River-EARNINGS/) · [TREND Moat](https://www.tradingview.com/script/CgqzZbQa-Neely-River-TREND-Moat/) · [ACCUM/DIST](https://www.tradingview.com/script/s0vXSOP2-Neely-River-ACCUM-DIST/) · [BREAKOUT](https://www.tradingview.com/script/tDr1bslF-Neely-River-BREAKOUT/) · [SPEED](https://www.tradingview.com/script/ojlRNskV-Neely-River-SPEED/)

The case studies identify what is a live product, client implementation, research system, or unfinished prototype. Client and private application source are not distributed here. Sample results use synthetic data and demonstrate software behavior, not investment performance. Public availability does not change the licensing terms of any linked project.
