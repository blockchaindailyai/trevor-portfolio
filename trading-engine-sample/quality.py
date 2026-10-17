"""Small public-demo input validator, not the private system's implementation."""
import numpy as np
import pandas as pd


def generate_data_quality_report(data: pd.DataFrame) -> dict[str, float | bool]:
    if not isinstance(data.index, pd.DatetimeIndex):
        raise ValueError("OHLC data requires a DatetimeIndex")
    if data.index.hasnans or not data.index.is_unique or not data.index.is_monotonic_increasing:
        raise ValueError("Timestamps must be valid, unique and increasing")
    prices = data[["open", "high", "low", "close"]].to_numpy(dtype=float)
    if not np.isfinite(prices).all() or (prices <= 0).any():
        raise ValueError("OHLC prices must be finite and positive")
    if ((data.high < data[["open", "close", "low"]].max(axis=1)) |
            (data.low > data[["open", "close", "high"]].min(axis=1))).any():
        raise ValueError("OHLC high/low bounds are inconsistent")
    return {"bars": float(len(data)), "valid_ohlc": True, "unique_timestamps": True}
