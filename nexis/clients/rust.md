---
sidebarLabel: Rust
title: Rust Client for Nexis
sidebarSortOrder: 1
---

Nexis's Rust crates are [published to crates.io][crates.io] and can be found
[on docs.rs with the "Nexis-" prefix][docs.rs].

[crates.io]: https://crates.io/search?q=Nexis-
[docs.rs]: https://docs.rs/releases/search?query=Nexis-

Some important crates:

- [`Nexis-program`] &mdash; Imported by programs running on Nexis, compiled to
  SBF. This crate contains many fundamental data types and is re-exported from
  [`Nexis-sdk`], which cannot be imported from a Nexis program.

- [`Nexis-sdk`] &mdash; The basic off-chain SDK, it re-exports
  [`Nexis-program`] and adds more APIs on top of that. Most Nexis programs
  that do not run on-chain will import this.

- [`Nexis-client`] &mdash; For interacting with a Nexis node via the
  [JSON RPC API](/docs/rpc).

- [`Nexis-cli-config`] &mdash; Loading and saving the Nexis CLI configuration
  file.

- [`Nexis-clap-utils`] &mdash; Routines for setting up a CLI, using [`clap`],
  as used by the main Nexis CLI. Includes functions for loading all types of
  signers supported by the CLI.

[`Nexis-program`]: https://docs.rs/Nexis-program
[`Nexis-sdk`]: https://docs.rs/Nexis-sdk
[`Nexis-client`]: https://docs.rs/Nexis-client
[`Nexis-cli-config`]: https://docs.rs/Nexis-cli-config
[`Nexis-clap-utils`]: https://docs.rs/Nexis-clap-utils
[`clap`]: https://docs.rs/clap
