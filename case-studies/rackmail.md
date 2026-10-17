# Rackmail: AI-to-Email Integration Through MCP

**Python · Model Context Protocol · OAuth · Email Automation · Reliability Engineering**

[View the repository](https://github.com/blockchaindailyai/Rackspace-MCP)

## Overview

Rackmail is a standalone Python Model Context Protocol (MCP) server that connects AI assistants to Rackspace email workflows. I designed and implemented it to support searching and reading messages, preparing verified drafts, and performing explicitly approved email actions through a controlled interface.

The project demonstrates the practical engineering required to connect AI applications to business systems: authentication, scoped permissions, state verification, retry handling, recoverable operations, performance instrumentation, and deployment validation.

## The Problem

Email automation involves more than generating a response. An assistant needs to identify the correct message, preserve context, distinguish an unsent draft from a sent email, and handle uncertain outcomes without repeating consequential actions.

A timeout does not necessarily mean a send failed. Blindly retrying can create duplicate emails. Similarly, a successful send does not automatically mean the source draft has disappeared from every email client's view.

Rackmail treats mailbox actions as operations with explicit permissions, identifiable state, and verifiable outcomes.

## Architecture

An MCP-compatible AI host connects to a Python service that exposes structured tools and interacts with the underlying mailbox.

| Layer | Responsibility |
| --- | --- |
| MCP interface | Structured inputs and outputs for search, reading, drafting, and approved actions |
| Authentication and authorization | OAuth connections and capability-specific access scopes |
| Mailbox integration | Email-service communication and message/draft state handling |
| Reliability controls | Idempotent operations, status checks, and recoverable draft cleanup |
| Operational support | Health reporting, performance instrumentation, tests, and deployment checks |

This separation makes the integration easier to test, maintain, and reason about as the AI host and mailbox behavior evolve.

## Security and Permission Design

Connecting an assistant to a mailbox should not automatically authorize every action the service supports.

Rackmail separates permissions for reading, drafting, sending, and draft removal. Connection consent establishes access; it is separate from approval to send a particular email. Sending follows the authenticated host's explicit approval workflow rather than treating text inside an incoming message as authorization.

Draft removal is separately controlled, with a recovery path instead of permanent deletion as the default cleanup mechanism.

**What this demonstrates:** OAuth integration, capability-based authorization, and careful separation between information an AI reads and actions its user has authorized.

## Reliability and State Handling

### Verified Drafts

Draft creation is treated as a mailbox operation whose result should be checked. This distinguishes a draft actually saved in the mailbox from text that exists only in a conversation.

### Idempotency and Send-Status Checks

Retry-aware operations and status checks help prevent duplicate actions when requests are repeated or outcomes are uncertain. This is particularly important when sending email, where an indiscriminate retry can have an external consequence.

### Recoverable Draft Cleanup

Controlled draft-removal workflows allow obsolete drafts to be cleaned up while retaining a recovery path. Draft creation, sending, and cleanup are distinct states that require deliberate handling.

### Client Synchronization Awareness

Troubleshooting included distinguishing server-side mailbox state from what a desktop email client displays. That distinction matters when a client shows stale drafts even after the underlying mailbox has changed.

These mechanisms are designed to improve reliability; they are not a claim of perfect delivery or universal compatibility across email clients.

## Performance Engineering

Search and email workflows can involve several network requests and verification steps. Rackmail includes performance instrumentation and batched operations to make that work measurable and reduce unnecessary overhead.

The focus is on identifying where time is spent, limiting redundant work, and improving responsiveness while preserving necessary verification. No unsupported latency benchmark is claimed here.

## Testing and Deployment

The prepared release candidate passed **330 offline tests**, allowing substantial behavior to be checked without opening a real mailbox or sending email.

Deployment work included:

- Source-hash verification
- Import and health checks
- Controlled activation of individual capabilities
- Separate verification of mailbox operations

Offline tests and deployment checks complement live integration testing; they do not replace it.

The public release contains **74 files**. Its contents were verified against the prepared candidate after line-ending normalization.

## Engineering Skills Demonstrated

| Area | Evidence in the project |
| --- | --- |
| AI systems integration | Connecting an assistant to practical email workflows through MCP |
| Backend development | A standalone Python service with structured tool interfaces |
| Security engineering | OAuth, scoped access, and explicit action-approval boundaries |
| Distributed-system reasoning | Handling retries, uncertain outcomes, and duplicate-action risks |
| Data integrity | Verifying saved drafts and tracking distinct mailbox states |
| Operational engineering | Instrumentation, deployment validation, and cross-client troubleshooting |
| Product design | Keeping consequential automated actions understandable and controllable |

## Broader Relevance

The same principles apply to specialized AI applications beyond email:

1. Expose well-defined tools.
2. Give each tool appropriate permissions.
3. Validate important outputs and state changes.
4. Preserve recoverability when operations fail.
5. Measure operational behavior rather than assuming success.

Rackmail demonstrates my approach to the practical layer between an AI model and a working product. That layer becomes essential when an assistant must do more than answer questions and starts interacting with business data and services.

## Scope and Limitations

- Rackmail is an independently developed integration, not an official Rackspace product.
- Implemented capabilities should be evaluated against the published code, tests, configuration, and current integration behavior.
- Offline test results do not establish perfect live delivery or a security certification.
- Public source availability does not itself grant an open-source license. Refer to the repository for current licensing terms.
