# Nexis Network Clusters

```
```

## Nexis Network Clusters

Nexis Network maintains several different clusters with different purposes.

Before you begin make sure you have first installed the Nexis Network command line tools

Explorers:

* http://native.Nexisnetwork.com/ Native explorer.
* http://evmexplorer.Nexisnetwork.com/ EVM mainnet explorer.
* http://evmexplorer.testnet.Nexisnetwork.com/ EVM testnet explorer.

### Testnet

|                |                                                                                                 |
| -------------- | ----------------------------------------------------------------------------------------------- |
| Space          | **Native**                                                                                      |
| RPC            | `https://api.testnet.Nexis.network`                                                              |
| Websocket      | `wss://api.testnet.Nexis.network`                                                                |
| Block Explorer | `https://native.Nexis.network?cluster=testnet`                                                   |
| Faucet CLI     | `Nexis airdrop 1 -u https://api.testnet.Nexis.network --faucet-host airdrop.testnet.Nexis.network` |

&#x20;

|                |                                                                                          |
| -------------- | ---------------------------------------------------------------------------------------- |
| Space          | **EVM**                                                                                  |
| chainId        | `2370`                                                                                   |
| ETH RPC        | `https://evm.testnet.Nexisscan.io/rpc`                                                    |
| ETH Websocket  | `wss://api.testnet.Nexisscan.io/`                                                         |
| Block Explorer | `https://evmexplorer.testnet.Nexisscan.io`                                                |
| Block Explorer | <p><code>https://explorer.testnet.Nexisscan.io</code><br>(V-encoded Legacy addresses)</p> |
| Faucet bot     | `https://t.me/Nexis_network_faucet_bot`                                                   |

* Testnet serves as a playground for anyone who wants to take Nexis Network for a test drive, as a user, token holder, app developer, or validator.
* Application developers should target Testnet.
* Potential validators should first target Testnet.
* Key differences between Testnet and Mainnet:
*
  * Testnet tokens are **not real**
  * Testnet includes a token faucet for airdrops for application testing
  * Testnet may be subject to ledger resets
  * Testnet typically runs a newer software version than Mainnet Beta
* Gossip entrypoint for Testnet: `bootstrap.testnet.Nexisnetwork.com:8001`

### Mainnet

|                |                                                |
| -------------- | ---------------------------------------------- |
| Space          | **Native**                                     |
| RPC            | `https://api.Nexisscan.io`                      |
| Websocket      | `wss://api.Nexisscan.io`                        |
| Block Explorer | `https://native.Nexisscan.io`                   |
| Shred version  | 17211                                          |
| Genesis hash   | `EsZtukC1MYxB2tohUTdigaUdy1k6kCU8HKS8LEK99iJY` |

&#x20;

|                |                                                                                       |
| -------------- | ------------------------------------------------------------------------------------- |
| Space          | **EVM**                                                                               |
| chainId        | 1229                                                                                  |
| ETH RPC        | `https://evm-explorer.Nexisscan.io/rpc`                                                |
| ETH Websocket  | `wss://api.Nexisscan.io/`                                                              |
| Block Explorer | `https://evm.Nexisscan.io`                                                             |
| Block Explorer | <p><code>https://evm-explorer.Nexisscan.io/</code><br>(V-encoded Legacy addresses)</p> |

* Gossip entrypoint for Mainnet: `bootstrap.Nexisscan.io:8001`
* Shred version: 17211
* Some of the popular nodes:&#x20;
* `78rvyxYJAUXGaZHJWyz7Yx81ribpAYvwupVuF9CugGws`, `FSZbHLPerYngGGwgWbXHtqTLRvLmgKVeUZCKwbFttWng`, `Eydu1kJNyPQNKtYrH4dqJJRxrxHuHtbXJCjgo6pSGSjf`, `QnQHuNAYMd7jaUJ61Pchi9bD7NbaZ4jxZ4cbdEaYMWF`, `Fxb6TgvScYJxjHjSpTr6a4xgLULLQSh8uhAexG5tzFJ6`

**Example `Nexis` command-line configuration**

Nexisconfig set --url https://api.Nexisscan.io

**Example `Nexis-validator` command-line**

$ Nexis-validator \\

&#x20;   \--identity \~/validator-keypair.json \\

&#x20;   \--vote-account \~/vote-account-keypair.json \\

&#x20;   \--no-untrusted-rpc \\

&#x20;   \--ledger \~/validator-ledger \\

&#x20;   \--rpc-port 8899 \\

&#x20;   \--enable-rpc-transaction-history \\

&#x20;   \--trusted-validator 78rvyxYJAUXGaZHJWyz7Yx81ribpAYvwupVuF9CugGws \\

&#x20;   \--trusted-validator FSZbHLPerYngGGwgWbXHtqTLRvLmgKVeUZCKwbFttWng \\

&#x20;   \--dynamic-port-range 8000-8010 \\

&#x20;   \--entrypoint bootstrap.Nexisscan.io:8001 \\

&#x20;   \--limit-ledger-size

The `--trusted-validator`s is operated by Nexis Network
