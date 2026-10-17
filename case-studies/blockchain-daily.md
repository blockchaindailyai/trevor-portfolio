# Blockchain Daily: AI-Powered Market Intelligence

**Full-Stack Engineering · AI Systems · Financial Data · Automation · Cost Optimization**

[Explore the live Terminal](https://blockchaindaily.org)

## Overview

I co-founded Blockchain Daily and developed its market-intelligence software: a web-based Terminal supported by NewsBot, an AI-assisted data ingestion, editorial review, and publishing backend.

The project combines my experience in trading and financial news with software engineering. It brings market information, research tools, and AI workflows into a usable product while addressing the less visible requirements behind it: data capture, source tracking, duplicate detection, subscriptions, databases, and operational reliability.

A major design priority is keeping operating costs low enough for a small business to sustain the product.

## The Problem

Financial information arrives through many sources, in inconsistent formats, with substantial repetition and varying levels of relevance.

An effective system needs to do more than summarize headlines. It needs to preserve where information came from, distinguish genuinely new developments from repeated coverage, organize information for retrieval, and present it in a form that supports research and decision-making.

It also needs a workable business model. Processing everything with the most expensive model or tool can make a useful product uneconomical.

## System Architecture

The product consists of two complementary systems:

### Blockchain Daily Terminal

The user-facing web application provides a workspace for market news, charts, asset discovery, research, and AI-assisted interaction.

Its stack includes:

- **TypeScript and React/Vinext** for the application interface
- **Cloudflare D1 and Drizzle** for application data storage and database access
- **Supabase authentication** for user accounts
- **Stripe** for subscription and payment integration
- **Market-data and exchange integrations** for connected financial tools

### NewsBot

The Python backend captures and processes source material, applies editorial logic, and supports publishing and downstream retrieval.

Its implementation includes:

- Source ingestion through feeds and browser-based collection where needed
- LLM-assisted classification, summarization, and editorial checks
- Duplicate detection and publication-state handling
- SQLite storage and full-text search
- Source revisions, timestamps, and structured records
- Worker coordination, retries, and recovery workflows

Together, these systems connect data acquisition and AI processing to a subscriber-facing product.

## Data Capture and Machine-Readable Research

A central part of the engineering work is turning incoming information into reusable, structured data.

NewsBot's retrieval and feedback infrastructure includes source revisions, temporal queries, full-text indexing, versioned prompts, model decisions, and human corrections. These records make it possible to trace an output back to the material and processing context that produced it.

This matters beyond publishing a single news item. Structured records can support:

- Searching historical information by topic and time
- Comparing source material with generated outputs
- Investigating incorrect or inconsistent classifications
- Reusing captured information in research tools
- Preparing reproducible datasets for future model development

The broader capability is converting a growing archive into a searchable and machine-readable resource. That is a foundation for specialized research applications and potential new products; it is not, by itself, evidence of profitable trading signals or successful model training.

## AI Systems Engineering

### Source-Grounded Workflows

The system connects AI processing to captured source material and retrieval tools. This gives generated outputs a concrete information base and makes their provenance easier to inspect.

### Structured Processing

Classification, summarization, editorial review, and publication are distinct responsibilities. Separating them makes it easier to examine decisions, identify failures, and improve individual stages.

### Human Feedback and Traceability

An append-only decision ledger links model decisions with source revisions, prompt versions, and human corrections. This supports investigation and iterative improvement rather than treating each model response as an isolated result.

### Tool Integration

LLM tool workflows and MCP access connect AI assistants to news and market data. This demonstrates experience building the interface between models, retrieval systems, and application functions.

### Model-Development Foundations

Reproducible training-data exports and structured feedback create a basis for future specialized model work. The demonstrated experience is in data preparation and application architecture; it should not be confused with a claim that a proprietary foundation model has been trained.

## Cost-Conscious Engineering

I designed the system around a practical constraint: useful AI functionality must be affordable to operate.

My approximate reported operating figure is **about $3 per day**, reflecting extensive cost-optimization work. This is an indicative figure for my operating setup, not an audited total-cost-of-ownership benchmark or a guarantee at every workload. Model usage, external data services, hosting, and other charges can vary.

The engineering approach emphasizes:

- Matching model and tool choices to the task
- Reducing unnecessary repeated processing
- Reusing structured information through retrieval
- Detecting duplication before it creates additional downstream work
- Keeping workflows inspectable so cost and quality problems can be investigated
- Evaluating whether additional complexity or inference expense produces useful improvement

The objective is to reduce costs without giving up more quality than the application can tolerate. Quality and cost remain separate things to assess; low expenditure alone does not prove accuracy.

## Reliability and Operational Design

The backend includes worker leases, retries, dead-letter handling, and uncertain-post reconciliation to address interrupted or ambiguous publishing operations.

These mechanisms support several important behaviors:

- Coordinating background work without assuming every worker finishes successfully
- Retaining failed work for investigation or controlled retry
- Distinguishing an uncertain publication result from a confirmed failure
- Preserving enough state to investigate processing and data-integrity issues

This work demonstrates practical experience with asynchronous processing and external-service failure modes. It does not imply that every integration is failure-free or that production reliability has been independently certified.

## Web and Business Systems

The Terminal also demonstrates the supporting engineering needed to turn a technical project into a commercial application:

- User accounts and authentication
- Subscription and payment integration
- Access controls for product features
- Database-backed application state
- Market-data integration and presentation
- Deployment configuration and operational monitoring
- User-facing interface development

These capabilities connect product development with the everyday needs of a subscription business.

## Product and Domain Experience

My role spans software implementation, market-intelligence requirements, editorial judgment, and product direction.

Trading and financial-news experience help me identify which information is useful, understand timing and market context, and translate research needs into application behavior.

The Blockchain Daily news brand also reached a historical audience of **55,000+ followers**. That is evidence of audience-building experience, not a claim about current active reach, paying users, or software revenue.

## What This Project Showcases

| Capability | Demonstrated work |
| --- | --- |
| Full-stack development | A market-intelligence interface connected to databases, accounts, subscriptions, and external services |
| AI application architecture | Source-grounded processing, structured workflows, model-tool integration, and human feedback |
| Data engineering | Capture, normalization, revision tracking, temporal retrieval, and reusable datasets |
| Financial-domain translation | Turning market research and editorial requirements into software behavior |
| Reliability engineering | Worker coordination, retries, failed-work handling, and publication reconciliation |
| Cost optimization | Designing AI workflows around sustainable operating expenditure |
| Product development | Connecting technical capabilities to a usable subscription product |

## Broader Applications

The same architecture can support other specialist information products: searchable research archives, educational assistants, expert-review workflows, and domain-specific analytical applications.

The transferable skill is designing the full path from raw material to structured data, AI-assisted interpretation, and a usable customer experience.

## Scope and Evidence

The live Terminal provides a user-facing demonstration. Public portfolio material can explain the architecture and selected implementation details, while private repositories and credentials remain private.

The project demonstrates substantial application and infrastructure work. It does not claim independently verified trading performance, guaranteed factual accuracy, or a particular level of commercial success.
