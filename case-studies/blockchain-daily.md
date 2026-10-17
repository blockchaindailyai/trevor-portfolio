# Blockchain Daily — terminal and news pipeline

[Explore Blockchain Daily](https://blockchaindaily.org)

## Engineering problem

A market-information product must deliver fresh headlines to subscribers while handling repeated inputs, interrupted workers and uncertain publishing outcomes.

## Implementation

The terminal combines React and TypeScript with Supabase authentication, Stripe subscriptions and Cloudflare D1 through Drizzle. Cursor-based headline retrieval supports incremental updates. Regression coverage addresses a billing race that can otherwise leave subscription access inconsistent when events arrive at different times.

The companion news pipeline uses SQLite-backed priority queues, worker leases, retries and dead-letter handling. Its uncertain-post reconciliation path distinguishes a failed action from one whose outcome is not yet known. Source provenance and LLM feedback exports support reviewing how content was produced.

## Engineering focus

This work connects a subscriber-facing interface with background processing and explicit failure handling. The portfolio highlights architecture and regression coverage; it makes no quantified throughput, uptime or revenue claims. Application source and operational records remain private.
