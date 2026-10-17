# Trading engine sample

An offline execution-simulation excerpt with a runnable synthetic example. The existing engine models positions, fills, costs and risk exits. This package adds a small strategy contract, OHLC validation and basic summary statistics so the public excerpt can run independently.

## Quick start

Requires Python 3.10+. From this directory:

```sh
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\python -m pip install -e .
.venv\Scripts\python -m trading_engine_sample.demo
.venv\Scripts\python -m unittest discover -s tests -v
```

On macOS/Linux use `.venv/bin/python` in place of `.venv\Scripts\python`. Dependencies and package metadata are in `pyproject.toml`.

The deterministic six-bar dataset produces one closed trade. With the demo configuration, final equity is approximately `10000.8579001` from initial `10000`, with fees `0.1014999`. These values test accounting on fabricated data; they are not measured strategy returns.

## Review the implementation

- `engine.py`: existing public simulation engine, preserved without changes.
- `demo.py`: synthetic OHLCV bars and scheduled target positions; no proprietary signal logic.
- `quality.py`, `stats.py`, `strategy.py`: newly written minimal public support modules, not private-system exports.
- `tests/test_stop_exit_drawdown.py`: existing regression cases now import the real installed package instead of stub support modules.
- `tests/test_public_demo.py`: cost/equity reconciliation, invalid-data rejection, drawdown and sizing-parser checks.

The regression suite checks long/short stops, gaps through stops, earlier adverse excursions, explicit intrabar exits and ordinary exits. Passing these checks does not validate every engine option. Summary statistics expose fractional total return and drawdown plus closed-trade count. Annualization inference assumes continuous calendar time and is not a market-calendar implementation.

## Limits

No exchange connection, live orders, external market data or performance claims. Bar data does not reveal the true intrabar price path; fills depend on simulation assumptions. The demonstration strategy uses synthetic scheduled positions, with the engine's default next-bar execution. The wider system's integrations and research features are outside this sample.

Source: [existing public repository](https://github.com/blockchaindailyai/trading-engine-sample).
