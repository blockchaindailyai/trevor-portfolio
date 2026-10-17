"""Deliberately limited summary statistics for the public example."""
import pandas as pd


def infer_periods_per_year(index: pd.Index, default: float = 252) -> float:
    if not isinstance(index, pd.DatetimeIndex) or len(index) < 2:
        return float(default)
    deltas = index.to_series().diff().dropna().dt.total_seconds()
    if (deltas <= 0).any():
        return float(default)
    return float(365.25 * 24 * 3600 / deltas.median())


def compute_performance_stats(*, equity_curve, returns, trades, periods_per_year, positions):
    """Ratios are fractions, not percentages. No Sharpe/annual-return claim."""
    return {
        "total_return": float(equity_curve.iloc[-1] / equity_curve.iloc[0] - 1),
        "max_drawdown": float((equity_curve / equity_curve.cummax() - 1).min()),
        "closed_trades": float(len(trades)),
    }
