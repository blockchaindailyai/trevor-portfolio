# Neely River: implementing a trading methodology in TradingView

**Pine Script · TradingView · Financial-domain engineering · Multi-timeframe analysis · Project leadership**

[Portfolio](../README.md) · [CORE BEHAVIOR showcase](https://www.tradingview.com/script/lgOiMkb9-Neely-River/)

## My role

I led Neely River's TradingView implementation, translating Glenn Neely's methodology into Pine Script indicators and dashboard components. My responsibilities included clarifying requirements, coordinating client and developer feedback, investigating platform differences, guiding validation and releases, and supporting user onboarding.

The methodology belongs to Glenn Neely. My contribution is its software implementation and the work required to make that implementation usable and consistent with the intended behavior.

## Engineering problem

A trading methodology contains more than formulas. Its implementation must resolve how state changes over time, which timeframe controls an interpretation, how gaps affect reference prices, and how charts communicate the result. Small choices can produce visible differences between platforms even when both implementations look plausible.

The work therefore combines market knowledge with specification, implementation, and comparison against reference behavior.

## Implementation areas

| Area | Engineering work |
| --- | --- |
| Core behavior | Price, time, and bias state; trend changes; stops; chart annotations and dashboards |
| Multi-timeframe behavior | Higher-timeframe context, control selection, intrabar information, and consistency across chart resolutions |
| Supporting indicators | Earnings, trend, accumulation/distribution, breakout, and speed displays |
| Cross-platform comparison | Investigating differences between TradingView and TradeStation calculations, inputs, scaling, and chart behavior |
| Product usability | Clear titles, defaults, settings, labels, colors, and shared-chart onboarding |
| Delivery | Requirements clarification, feedback triage, regression checks, and release coordination |

## How I approach validation

A useful comparison starts with the same symbol, timeframe, source data, and settings. From there, I isolate whether a mismatch comes from the data, a calculation rule, a state transition, or the display layer.

Examples from the work include gap treatment in bias-stop calculations, channel reference-point interpretation, log versus linear scaling, and differences in volume-based displays. These are separate problems; making two screenshots look similar is not sufficient evidence that the implementations agree.

This process makes trading knowledge practical: understanding what the indicator is intended to represent helps identify the correct questions and turn client feedback into testable changes.

## Published indicators

- [Neely River CORE BEHAVIOR](https://www.tradingview.com/script/lgOiMkb9-Neely-River/)
- [Neely River EARNINGS](https://www.tradingview.com/script/DqzDGWI6-Neely-River-EARNINGS/)
- [Neely River TREND Moat](https://www.tradingview.com/script/CgqzZbQa-Neely-River-TREND-Moat/)
- [Neely River ACCUM/DIST](https://www.tradingview.com/script/s0vXSOP2-Neely-River-ACCUM-DIST/)
- [Neely River BREAKOUT](https://www.tradingview.com/script/tDr1bslF-Neely-River-BREAKOUT/)
- [Neely River SPEED](https://www.tradingview.com/script/ojlRNskV-Neely-River-SPEED/)

These pages provide a public view of client work. Access to use an indicator may be restricted. Client source and proprietary rules remain private; the showcases do not imply a completed v1.0 launch or establish trading returns.

## What this demonstrates

The project shows my ability to work with a domain expert, own a specialized implementation, investigate ambiguous behavior, and connect engineering decisions to the user's analytical workflow.
