# Rust WAL recovery from the shadow execution daemon

[Read the implementation](src/lib.rs) · [Source provenance and changes](PROVENANCE.md) · [Architecture case study](../case-studies/rust-shadow.md)

A crash can leave half a record at the end of an append-only log. Ignoring those bytes during replay is insufficient: the next append would follow the corrupt tail. This excerpt from WilliamsBot's actual Rust execution daemon validates the complete prefix, physically removes the incomplete tail, synchronizes the repair, and only then returns an append handle.

## Run locally

With an installed Rust toolchain and platform linker:

```sh
cd rust-shadow-sample
cargo test --offline
cargo fmt
cargo clippy --offline --all-targets -- -D warnings
```

There are no external crates, downloads, credentials, services or exchange connections. Tests use temporary synthetic files. The crate is a library; the tests are the executable demonstration.

**Verification status:** source inspection completed; executable Rust tests have not run in the preparation environment because no installed Rust compiler/Cargo toolchain was found. No passing test result is claimed yet. The scoped GitHub Actions workflow runs the tests and Clippy on the hosted runner; its outcome will be linked here after verification.

## Exact invariants

- Retained bytes end at the final newline, or at length zero if no newline exists. A syntactically valid but unterminated final record is still discarded.
- Each nonempty complete line is validated in order before any truncation. Blank complete lines are skipped, matching the original implementation.
- A validation error leaves file bytes unchanged, including an incomplete suffix. Validator side effects are the caller's responsibility.
- Successful repair truncates the physical file to the retained length and calls `sync_all` before returning the append handle.
- Later appends begin after the repaired prefix. Reopening the synthetic test log sees both complete records.

| Test | Failure or boundary exercised |
| --- | --- |
| `torn_final_line_is_physically_removed_before_append` | Crash-like partial suffix, physical repair, append, second recovery |
| `complete_corrupt_record_fails_closed` | Complete malformed record rejects recovery without rewriting bytes |
| `corrupt_complete_record_prevents_tail_repair` | Earlier complete corruption blocks truncation of a later torn suffix |
| `empty_complete_and_wholly_torn_files` | Empty log, complete log, no complete record, blank line |

## Limits

This is one recovery boundary, not a complete durable execution engine. The caller must own the file exclusively and supply real record validation; no file lock is acquired here. Recovery reads the entire file into memory. The excerpt does not authenticate records, restore account state, maintain idempotency, create files durably, handle WAL rotation, or test actual power loss. Filesystem and hardware durability behavior is outside these tests.

In the wider shadow system Python remains authoritative. This sample does not establish live execution readiness, production latency, trading performance, or signing/custody guarantees. Rights remain proprietary; see provenance.
