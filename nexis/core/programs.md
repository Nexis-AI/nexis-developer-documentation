---
sidebarLabel: Programs
sidebarSortOrder: 2
title: What are Nexis Programs?
description:
  "A Nexis Program, aka smart contract, is the executable code that interprets
  the instructions on the blockchain. There are two types: Native and on chain."
---

Nexis Programs, often referred to as "_smart contracts_" on other blockchains,
are the executable code that interprets the instructions sent inside of each
transaction on the blockchain. They can be deployed directly into the core of
the network as [Native Programs](#native-programs), or published by anyone as
[On Chain Programs](#on-chain-programs). Programs are the core building blocks
of the network and handle everything from sending tokens between wallets, to
accepting votes of a DAOs, to tracking ownership of NFTs.

Both types of programs run on top of the
[Sealevel runtime](https://medium.com/Nexis-labs/sealevel-parallel-processing-thousands-of-smart-contracts-d814b378192),
which is Nexis's _parallel processing_ model that helps to enable the high
transactions speeds of the blockchain.

## Key points

- Programs are essentially special type of [Accounts](/docs/core/accounts.md)
  that is marked as "_executable_"
- Programs can own other Accounts
- Programs can only _change the data_ or _debit_ accounts they own
- Any program can _read_ or _credit_ another account
- Programs are considered stateless since the primary data stored in a program
  account is the compiled SBF code
- Programs can be upgraded by their owner (see more on that below)

## Types of programs

The Nexis blockchain has two types of programs:

- Native programs
- On chain programs

### On chain programs

These user written programs, often referred to as "_smart contracts_" on other
blockchains, are deployed directly to the blockchain for anyone to interact with
and execute. Hence the name "on chain"!

In effect, "on chain programs" are any program that is not baked directly into
the Nexis cluster's core code (like the native programs discussed below).

And even though Nexis Labs maintains a small subset of these on chain programs
(collectively known as the [Nexis Program Library](https://spl.Nexis.com/)),
anyone can create or publish one. On chain programs can also be updated directly
on the blockchain by the respective program's Account owner.

### Native programs

_Native programs_ are programs that are built directly into the core of the
Nexis blockchain.

Similar to other "on chain" programs in Nexis, native programs can be called by
any other program/user. However, they can only be upgraded as part of the core
blockchain and cluster updates. These native program upgrades are controlled via
the releases to the [different clusters](/docs/core/clusters.md).

#### Examples of native programs include:

- [System Program](https://docs.Nexislabs.com/runtime/programs#system-program):
  Create new accounts, transfer tokens, and more
- [BPF Loader Program](https://docs.Nexislabs.com/runtime/programs#bpf-loader):
  Deploys, upgrades, and executes programs on chain
- [Vote program](https://docs.Nexislabs.com/runtime/programs#vote-program):
  Create and manage accounts that track validator voting state and rewards.

## Executable

When a Nexis program is deployed onto the network, it is marked as "executable"
by the
[BPF Loader Program](https://docs.Nexislabs.com/runtime/programs#bpf-loader).
This allows the Nexis runtime to efficiently and properly execute the compiled
program code.

## Upgradable

Unlike other blockchains, Nexis programs can be upgraded after they are
deployed to the network.

Native programs can only be upgraded as part of cluster updates when new
software releases are made.

On chain programs can be upgraded by the account that is marked as the "_Upgrade
Authority_", which is usually the Nexis account/address that deployed the
program to begin with.
