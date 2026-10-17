"""Minimal strategy contract written for the standalone public demo."""
from typing import Protocol
import pandas as pd


class Strategy(Protocol):
    def generate_signals(self, data: pd.DataFrame) -> pd.Series:
        """Return aligned desired positions: -1 short, 0 flat, +1 long."""
        ...
