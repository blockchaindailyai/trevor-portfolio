# Historical Volatility Compression: a published Pine Script indicator

**Pine Script v6 · TradingView · Statistical features · Multi-timeframe timing · Dashboard and alerts**

[Portfolio](../README.md) · [Published TradingView indicator](https://www.tradingview.com/script/KdZS3ETR-Historical-Volatility-Compression/) · [Publicly available source](https://github.com/blockchaindailyai/historical-volatility-compression) · [Pine implementation](https://github.com/blockchaindailyai/historical-volatility-compression/blob/main/VolCompression.pine)

## Engineering problem

How compressed is the current market relative to its own available history, and how long has that condition persisted?

I built a standalone indicator that combines daily realized volatility and total price range into a historical compression percentile. It provides descriptive market context rather than a directional forecast, calibrated breakout probability, or trading strategy.

## Calculation and interface

- **Daily composite:** Annualized standard deviation of daily log returns and the total high-low range as a percentage of its midpoint. The default lookback is 30 daily bars; a negative weighted log composite assigns 40% to realized volatility and 60% to range.
- **Expanding historical percentile:** Rank the composite against accumulated valid daily observations, rather than a fixed rolling ranking window. The default warmup requires 365 observations. Higher readings indicate greater historical compression.
- **Persistence:** Track current and maximum daily streaks at or above the 90th, 95th, and 99th percentile thresholds. A separate persistence score compares the current >=90 streak with its historical maximum.
- **Dashboard:** Expose the component readings, percentile, streaks, persistence, one- and seven-day changes, sample count, and live-versus-completed daily mode.

The implementation has no imported Pine libraries. Inputs allow the lookback, weighting, annualization, warmup, and display options to be adjusted.

## Multi-timeframe timing and alerts

The calculation engine runs in the daily context through `request.security`, including when displayed on intraday charts.

The default live mode uses the developing daily observation with `lookahead_off`. Its values can change intraday and repaint after reload. Optional **Completed Daily Bars Only** uses prior daily inputs and aligns them to the next daily period on intraday charts, accepting a one-day lag. Daily and intraday standard positive-price charts are preferred; charts above daily do not expose every daily observation.

Alert conditions evaluate at chart-bar close. Regime entries include equality at 90, 95, and 99, with releases below the corresponding thresholds. Sharp-release alerts use the requested daily observation's timestamp to avoid repeating the same event across intraday bars during continuous execution. Closing an intraday bar does not make live daily data final.

## Status and verification

The indicator is published on TradingView, with a separate public repository containing its source and documentation.

The [release verification notes](https://github.com/blockchaindailyai/historical-volatility-compression#verification) report successful TradingView compilation and plotting, completed-daily consistency across hourly and daily views, hourly Bar Replay checks, and 100 source-derived behavioral assertions covering thresholds, warmup, repeated values, and release/re-entry handling. These checks were documented for the indicator release; they are not a trading backtest, and live alert delivery was not exercised.

Available chart history, tied observations, feed revisions, and nonstandard charts can affect readings. No profitability, direction, or calibrated probability claims are made. The source is publicly available; no additional license has been assigned in the repository.

## What this demonstrates

The project connects statistical feature construction with explicit data timing, persistent state, alert semantics, and a compact analytical interface. It is distinct from the [private volatility-research prototype](volatility-research.md), which explores additional features and experimental probability displays.
