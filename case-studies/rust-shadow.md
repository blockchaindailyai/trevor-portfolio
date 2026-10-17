# Rust shadow execution — research subcase

The Rust work explores shadow execution alongside an authoritative Python engine. Python retains execution authority; the Rust component is a research subcase rather than a production replacement.

The project includes a KMS v2 implementation, while deployment canary work and signing isolation remain incomplete. That scope does not establish deployed custody infrastructure or production signing guarantees.

This case study describes the research boundary. Private execution logic, signing material and runtime configuration remain excluded.
