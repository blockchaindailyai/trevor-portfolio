# Python execution and research

[Existing public repository](https://github.com/blockchaindailyai/trading-engine-sample) · [Runnable sample](../trading-engine-sample/README.md)

## Engineering problem

Backtest results depend on execution assumptions as well as signals. The public engine excerpt makes position sizing, costs, order handling and risk exits inspectable. Its stop-exit regression cases check that adverse-excursion calculations respect the actual exit fill, including gaps through stops, while retaining worse excursions from earlier bars.

## Research scope

The broader WilliamsBot research project includes paper order types, partial fills, VWAP, queue-ahead and latency models. Research tooling includes purged folds and data hashes for reproducibility. These are modeling capabilities, not claims of profitable performance or measured live execution quality.

## Runnable public excerpt

The existing public `engine.py` is preserved unchanged. Newly written minimal support modules, package metadata and a deterministic synthetic-data driver make it runnable independently. The support modules replace omitted dependencies for this sample; they are not exports of the private research implementation.

The eight existing stop-exit regression cases now import the real package. Five additional tests cover cost/equity reconciliation, invalid OHLC inputs, summary drawdown and milestone sizing validation. All 13 tests passed in the documented Python preparation environment.

The sample uses fabricated market data and scheduled positions. Private strategy logic, datasets and exchange integrations remain outside its scope.
