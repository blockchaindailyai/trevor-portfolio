# WilliamsBot and UTBot: trading research and execution engineering

**Python · Historical-data analysis · Backtesting · Paper execution · Risk accounting · Recovery**

[Portfolio](../README.md) · [Runnable Python sample](../trading-engine-sample/README.md) · [Existing public excerpt](https://github.com/blockchaindailyai/trading-engine-sample) · [Rust companion](rust-shadow.md)

## Engineering problem

A strategy signal is only one part of a trading system. Meaningful research also depends on when a signal becomes available, how an order is filled, how costs and position sizes are applied, and whether the system can explain its state after an interruption.

My work on WilliamsBot and UTBot connects strategy research with these execution and data-handling requirements.

## WilliamsBot

The wider WilliamsBot project includes execution simulation, paper order handling, partial fills, volume-weighted fill prices, queue-ahead and latency models, and exchange-integration work. Research tooling includes purged data folds and data hashes for reproducibility.

Operational work includes persistent state, checkpoint recovery, feed continuity, and separating healthy processing from a process that is merely alive. Paper-only operation and shadow execution provide boundaries for validating behavior without treating a test as a live financial result.

## UTBot

UTBot work adapts an ATR trailing-stop strategy with configurable sensitivity and moving-average filtering. The research infrastructure addresses lower-timeframe evaluation of higher-timeframe signals, position sizing, fees, slippage, and fill validation.

The underlying UT Bot strategy is not my invention. My contribution is the surrounding implementation, adaptation, research tooling, and testing.

## Quantitative analysis

The broader research work examines trade-level profit and loss, fees and slippage, position size, exposure, drawdown, win rate, expectancy, profit factor, and risk-adjusted summaries such as Sharpe, Sortino, CAGR, and Calmar. Each metric depends on data quality and its calculation assumptions.

A core design principle is retaining enough information to explain a result: the dataset, signal timing, sizing rule, execution assumptions, and cost model. This supports comparisons and diagnosis rather than relying on a single headline return.

## Inspectable public sample

The public `engine.py` excerpt is preserved unchanged. Minimal support modules, package metadata, and a deterministic synthetic-data driver make it runnable independently; these support modules are sample-specific replacements for omitted dependencies.

| Review path | What to inspect |
| --- | --- |
| [Engine](../trading-engine-sample/engine.py) | Position sizing, execution accounting, and risk exits |
| [Synthetic demo](../trading-engine-sample/demo.py) | A small reproducible input and its resulting accounting |
| [Stop regression tests](../trading-engine-sample/tests/test_stop_exit_drawdown.py) | Long/short stops, gaps, earlier adverse excursions, and explicit intrabar exits |
| [Public demo tests](../trading-engine-sample/tests/test_public_demo.py) | Cost/equity reconciliation, invalid inputs, drawdown, and sizing validation |

The 13-test public suite covers eight stop-exit regression cases and five additional checks. Run it using the [sample instructions](../trading-engine-sample/README.md).

## Important boundaries

The sample uses fabricated market data and scheduled positions. Its results demonstrate execution accounting, not strategy profitability. Private strategy logic, historical datasets, and exchange integrations are not included. Broader modeling features described above are not all implemented in the small public demonstration.

Live-integration development, paper-trading results, and production trading reliability are distinct claims. This portfolio demonstrates engineering work without presenting simulation as verified live performance.
