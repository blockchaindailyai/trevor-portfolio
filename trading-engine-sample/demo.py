"""Deterministic synthetic OHLC simulation. Run python -m trading_engine_sample.demo."""
import json
import pandas as pd
from .engine import BacktestConfig, BacktestEngine


def synthetic_bars():
    return pd.DataFrame(
        {"open": [100., 100., 101., 103., 102., 104.],
         "high": [101., 102., 104., 104., 105., 105.],
         "low": [99., 99., 100., 101., 101., 103.],
         "close": [100., 101., 103., 102., 104., 104.],
         "volume": [10., 12., 11., 15., 14., 10.]},
        index=pd.date_range("2026-01-01", periods=6, freq="h", tz="UTC"),
    )


class DemoStrategy:
    use_generic_trade_labels = True

    def generate_signals(self, data):
        # Scheduled synthetic positions, deliberately not an investment strategy.
        return pd.Series([0, 1, 1, 0, 0, 0], index=data.index)


def run_demo():
    return BacktestEngine(BacktestConfig(trade_size_mode="units", trade_size_value=1.0)).run(
        synthetic_bars(), DemoStrategy())


if __name__ == "__main__":
    result = run_demo()
    print(json.dumps({"dataset": "synthetic", "stats": result.stats,
                      "fees": result.total_fees_paid,
                      "final_equity": float(result.equity_curve.iloc[-1])}, indent=2))
