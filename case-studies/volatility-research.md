# Volatility compression: multi-timeframe research in Pine Script

**Pine Script v6 · Statistical features · Multi-timeframe analysis · Research visualization**

[Portfolio](../README.md)

## Research question

How can a chart make an unusually compressed market easier to identify and compare across timeframes, while separating a descriptive observation from a prediction?

I developed Pine Script research indicators combining realized volatility, range compression, volume, and price-structure features into multi-timeframe visualizations and experimental breakout-probability estimates.

## Implemented approach

- Rank realized-volatility and range-compression conditions to provide context beyond an absolute volatility number.
- Combine multiple market features in a chart-based research workflow.
- Display experimental logistic-model estimates for non-directional breakout events over 24-hour and three-day horizons.
- Support configurable pooled and TRX-specific calibration choices.
- Handle missing volume information and expose the analysis through dashboards and alerts.

## Engineering distinction

A compression measure describes a market condition. A probability estimate makes an additional statistical claim and requires calibration and out-of-sample evaluation. A likely increase in movement also does not specify which direction price will take.

Keeping those distinctions visible is part of designing a useful analytical interface. It prevents a descriptive ranking from being presented as a complete trading strategy.

## Status and evidence

This is a private research prototype, not a verified forecasting service. The source implements the features and probability display described above. Historical validation has not been independently reproduced for this portfolio, and no accuracy or return figures are claimed. Reproducible training and holdout evaluation, calibration checks, and lookahead/repainting review are required before stronger conclusions.

## What this demonstrates

The project brings together Pine implementation, market-domain understanding, feature engineering, model-output interpretation, and user-facing research tools. It complements the [execution research](execution-research.md), where timing and fill assumptions determine how a signal would be evaluated in a trading simulation.
