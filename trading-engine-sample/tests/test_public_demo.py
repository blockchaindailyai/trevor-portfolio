import unittest
import numpy as np
from trading_engine_sample.demo import run_demo, synthetic_bars, DemoStrategy
from trading_engine_sample.engine import BacktestConfig, BacktestEngine, parse_trade_size_equity_milestones
from trading_engine_sample.stats import compute_performance_stats
import pandas as pd


class PublicDemoTests(unittest.TestCase):
    def test_demo_reconciles_costs_and_equity(self):
        result = run_demo()
        self.assertEqual(len(result.trades), 1)
        trade = result.trades[0]
        self.assertGreater(result.total_fees_paid, 0)
        self.assertAlmostEqual(trade.pnl, trade.gross_pnl - trade.entry_fee - trade.exit_fee - trade.financing_cost)
        self.assertAlmostEqual(result.equity_curve.iloc[-1], 10000 + trade.pnl)
        self.assertTrue(result.data_quality["valid_ohlc"])

    def test_invalid_prices_and_timestamps_are_rejected(self):
        for bad in (np.nan, np.inf, -1):
            data = synthetic_bars()
            data.iloc[2, 0] = bad
            with self.assertRaises(ValueError):
                BacktestEngine(BacktestConfig()).run(data, DemoStrategy())
        data = synthetic_bars()
        data.index = [data.index[0]] * len(data)
        with self.assertRaises(ValueError):
            BacktestEngine(BacktestConfig()).run(data, DemoStrategy())

    def test_impossible_high_is_rejected(self):
        data = synthetic_bars()
        data.loc[data.index[1], "high"] = 1
        with self.assertRaises(ValueError):
            BacktestEngine(BacktestConfig()).run(data, DemoStrategy())

    def test_summary_drawdown(self):
        stats = compute_performance_stats(equity_curve=pd.Series([100., 120., 90.]), returns=None,
                                          trades=[], periods_per_year=252, positions=None)
        self.assertAlmostEqual(stats["max_drawdown"], -.25)
        self.assertAlmostEqual(stats["total_return"], -.1)

    def test_milestone_validation(self):
        self.assertEqual(parse_trade_size_equity_milestones("200:20,100:10"), ((100., 10.), (200., 20.)))
        for spec in ("100:1,100:2", "nan:2", "0:2", "100:-1", "bad"):
            with self.assertRaises(ValueError):
                parse_trade_size_equity_milestones(spec)
