//! WAL framing and tail repair extracted from WilliamsBot executiond.
//! Proprietary. See ../PROVENANCE.md for source and isolation changes.
use std::fs::{File, OpenOptions};
use std::io::{self, Read};
use std::path::Path;

/// Validate complete nonempty records, then remove an unterminated tail.
///
/// The caller must exclusively own this file and supply the domain validator.
/// A validator error leaves the file unchanged. The returned handle appends only
/// after recovery succeeds. This is the framing layer, not a complete WAL.
pub fn recover_for_append(
    path: &Path,
    mut validate: impl FnMut(&[u8]) -> io::Result<()>,
) -> io::Result<File> {
    // Existing files only: creation and parent-directory durability remain the
    // owning daemon's responsibility.
    let file = OpenOptions::new().append(true).read(true).open(path)?;
    let mut bytes = Vec::new();
    File::open(path)?.read_to_end(&mut bytes)?;
    // Verbatim boundary calculation from load_recovery.
    let valid_len = if bytes.is_empty() || bytes.ends_with(b"\n") {
        bytes.len()
    } else if let Some(last_newline) = bytes.iter().rposition(|byte| *byte == b'\n') {
        last_newline + 1
    } else {
        0
    };
    bytes.truncate(valid_len);

    for raw_line in bytes.split(|byte| *byte == b'\n') {
        if raw_line.is_empty() {
            continue;
        }
        validate(raw_line)?;
    }
    // Physical repair from WalStore::open, after all complete records validate.
    let valid_len = valid_len as u64;
    let actual_len = file.metadata()?.len();
    if valid_len < actual_len {
        // The only discardable corruption is an unterminated final record:
        // every acknowledged record was flushed, newline-terminated and
        // fsynced. Remove the bytes physically before appending again.
        file.set_len(valid_len)?;
        file.sync_all()?;
    }
    Ok(file)
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::fs;
    use std::io::Write;
    use std::path::PathBuf;
    use std::sync::atomic::{AtomicU64, Ordering};

    // New harness: no tempfile dependency or runtime data.
    struct Fixture(PathBuf);
    impl Fixture {
        fn new(bytes: &[u8]) -> Self {
            static NEXT: AtomicU64 = AtomicU64::new(0);
            let path = std::env::temp_dir().join(format!(
                "executiond-excerpt-{}-{}.wal", std::process::id(),
                NEXT.fetch_add(1, Ordering::Relaxed)
            ));
            let mut file = OpenOptions::new().write(true).create_new(true).open(&path).unwrap();
            file.write_all(bytes).unwrap();
            file.sync_all().unwrap();
            Self(path)
        }
    }
    impl Drop for Fixture {
        fn drop(&mut self) { let _ = fs::remove_file(&self.0); }
    }
    // Synthetic validator deliberately accepts only two fixture records. The
    // original JSON/schema/hash/snapshot validator is outside this excerpt.
    fn validate(line: &[u8]) -> io::Result<()> {
        if line == b"{\"index\":1}" || line == b"{\"index\":2}" { Ok(()) }
        else { Err(io::Error::new(io::ErrorKind::InvalidData, "invalid fixture record")) }
    }

    // Adapted from the identically named upstream test.
    #[test]
    fn torn_final_line_is_physically_removed_before_append() {
        let fixture = Fixture::new(b"{\"index\":1}\n");
        let valid_len = fs::metadata(&fixture.0).unwrap().len();
        {
            let mut file = OpenOptions::new().append(true).open(&fixture.0).unwrap();
            file.write_all(b"{\"schema_version\":3").unwrap();
            file.sync_all().unwrap();
        }
        let mut wal = recover_for_append(&fixture.0, validate).unwrap();
        assert_eq!(fs::metadata(&fixture.0).unwrap().len(), valid_len);
        wal.write_all(b"{\"index\":2}\n").unwrap();
        wal.sync_all().unwrap();
        drop(wal);
        let mut count = 0;
        let wal = recover_for_append(&fixture.0, |line| { validate(line)?; count += 1; Ok(()) }).unwrap();
        drop(wal);
        assert_eq!(count, 2);
        assert_eq!(fs::read(&fixture.0).unwrap(), b"{\"index\":1}\n{\"index\":2}\n");
    }

    // Adapted from the identically named upstream test; adds no-mutation check.
    #[test]
    fn complete_corrupt_record_fails_closed() {
        let fixture = Fixture::new(b"not-json\n");
        assert!(recover_for_append(&fixture.0, validate).is_err());
        assert_eq!(fs::read(&fixture.0).unwrap(), b"not-json\n");
    }

    #[test]
    fn corrupt_complete_record_prevents_tail_repair() {
        let original = b"{\"index\":1}\nnot-json\npartial";
        let fixture = Fixture::new(original);
        assert!(recover_for_append(&fixture.0, validate).is_err());
        assert_eq!(fs::read(&fixture.0).unwrap(), original);
    }

    #[test]
    fn empty_complete_and_wholly_torn_files() {
        for (input, expected) in [(&b""[..], &b""[..]), (b"partial", b""),
            (b"{\"index\":1}\n", b"{\"index\":1}\n"), (b"\n", b"\n")] {
            let fixture = Fixture::new(input);
            drop(recover_for_append(&fixture.0, validate).unwrap());
            assert_eq!(fs::read(&fixture.0).unwrap(), expected);
        }
    }
}
