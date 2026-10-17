# Source provenance and rights

This is an owner-authorized public excerpt of **WilliamsBot executiond**, with isolation changes documented below. The original crate is marked `license = "Proprietary"` and `publish = false`; those declarations are retained. Public visibility does not introduce an open-source license or grant additional rights. No new license is applied.

- Repository: `blockchaindailyai/WilliamsBot`
- Pinned source commit: `76928aa31a446c12d97fa18d6c661ca21ef0f994`
- Source: [`executiond/src/wal.rs`](https://github.com/blockchaindailyai/WilliamsBot/blob/76928aa31a446c12d97fa18d6c661ca21ef0f994/executiond/src/wal.rs)
- Source Git blob: `d4a3ec9e76e509945391378a47a2e40c9b3681ed`
- Manifest: `executiond/Cargo.toml`, Git blob `c20d2f4afc3845ce592775edf0f59a5821ce409b`, package `williams-executiond` version `0.2.1`, edition 2021, original minimum Rust 1.98.

The source repository may require access. No private history is copied here. The source file contained no file-level copyright or license header; its crate-level proprietary designation is preserved above and in the sample manifest.

## Exact extraction boundary

`src/lib.rs::recover_for_append` combines the newline-prefix calculation in `load_recovery` (source lines 159–167) and physical tail truncation in `WalStore::open` (lines 75–83). The calculation and truncation operations are retained. The source comment explaining the acknowledged-record assumption is retained verbatim.

The original tests `torn_final_line_is_physically_removed_before_append` (lines 419–441) and `complete_corrupt_record_fails_closed` (lines 444–448) supply the recovery scenarios. Their setup and assertions are adapted to the isolated API, not represented as unchanged full-daemon tests.

## Isolation changes

1. Introduced the public `recover_for_append` wrapper and returned an append-capable file handle. The file must already exist; creation, parent-directory synchronization, process locking and daemon ownership are outside this boundary.
2. Replaced JSON decoding, schema/index/hash-chain validation, engine snapshot restoration and response-cache reconstruction with a caller-supplied fallible record validator. Validation still precedes physical repair. The test validator only recognizes two synthetic fixture byte strings; it is not a production validator.
3. Used `io::Result` instead of the daemon's `WalError`. Removed all daemon, engine, protocol and third-party dependencies. The isolated package has a new name/version; it does not inherit the full daemon's minimum-version requirement as a tested compatibility claim.
4. Replaced `tempfile` and engine snapshots in the test setup with exclusive-create temporary files and synthetic index records. Retained the original torn suffix bytes and corrupt complete-record fixture. Added byte-for-byte preservation checks, a corruption-plus-tail test, and empty/complete/wholly-torn/blank-line cases.
5. Added this documentation, case study, crate manifest and harness. No strategy, exchange adapter, credential, market dataset, production snapshot or operational history is included.

The extraction preserves a real recovery algorithm, while deliberately making no claim that it reproduces the complete execution daemon.
