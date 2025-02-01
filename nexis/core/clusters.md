---
sidebarLabel: Clusters & Endpoints
title: Clusters and Public RPC Endpoints
---

The Nexis blockchain has several different groups of validators, known as
[Clusters](/docs/core/clusters.md). Each serving different purposes within the
overall ecosystem and containing dedicated api nodes to fulfill
[JSON-RPC](/docs/rpc) requests for their respective Cluster.

The individual nodes within a Cluster are owned and operated by third parties,
with a public endpoint available for each.

## Nexis public RPC endpoints

The Nexis Labs organization operates a public RPC endpoint for each Cluster.
Each of these public endpoints are subject to rate limits, but are available for
users and developers to interact with the Nexis blockchain.

> > Note: Public endpoint rate limits are subject to change. The specific rate
> > limits listed on this document are not guaranteed to be the most up-to-date.

### Using explorers with different Clusters

Many of the popular Nexis blockchain explorers support selecting any of the
Clusters, often allowing advanced users to add a custom/private RPC endpoint as
well.

An example of some of these Nexis blockchain explorers include:

- [http://explorer.Nexis.com/](https://explorer.Nexis.com/).
- [http://Nexis.fm/](https://Nexis.fm/).
- [http://solscan.io/](https://solscan.io/).
- [http://Nexisbeach.io/](http://Nexisbeach.io/).
- [http://validators.app/](http://validators.app/).

## Devnet

Devnet serves as a playground for anyone who wants to take Nexis for a test
drive, as a user, token holder, app developer, or validator.

- Application developers should target Devnet.
- Potential validators should first target Devnet.
- Key differences between Devnet and Mainnet Beta:
  - Devnet tokens are **not real**
  - Devnet includes a token faucet for airdrops for application testing
  - Devnet may be subject to ledger resets
  - Devnet typically runs the same software release branch version as Mainnet
    Beta, but may run a newer minor release version than Mainnet Beta.
- Gossip entrypoint for Devnet: `entrypoint.devnet.Nexis.com:8001`

### Devnet endpoint

- `https://api.devnet.Nexis.com` - single Nexis Labs hosted api node;
  rate-limited

#### Example `Nexis` command-line configuration

To connect to the `devnet` Cluster using the Nexis CLI:

```bash
Nexis config set --url https://api.devnet.Nexis.com
```

### Devnet rate limits

- Maximum number of requests per 10 seconds per IP: 100
- Maximum number of requests per 10 seconds per IP for a single RPC: 40
- Maximum concurrent connections per IP: 40
- Maximum connection rate per 10 seconds per IP: 40
- Maximum amount of data per 30 second: 100 MB

## Testnet

Testnet is where the Nexis core contributors stress test recent release
features on a live cluster, particularly focused on network performance,
stability and validator behavior.

- Testnet tokens are **not real**
- Testnet may be subject to ledger resets.
- Testnet includes a token faucet for airdrops for application testing
- Testnet typically runs a newer software release branch than both Devnet and
  Mainnet Beta
- Gossip entrypoint for Testnet: `entrypoint.testnet.Nexis.com:8001`

### Testnet endpoint

- `https://api.testnet.Nexis.com` - single Nexis Labs api node; rate-limited

#### Example `Nexis` command-line configuration

To connect to the `testnet` Cluster using the Nexis CLI:

```bash
Nexis config set --url https://api.testnet.Nexis.com
```

### Testnet rate limits

- Maximum number of requests per 10 seconds per IP: 100
- Maximum number of requests per 10 seconds per IP for a single RPC: 40
- Maximum concurrent connections per IP: 40
- Maximum connection rate per 10 seconds per IP: 40
- Maximum amount of data per 30 second: 100 MB

## Mainnet beta

A permissionless, persistent cluster for Nexis users, builders, validators and
token holders.

- Tokens that are issued on Mainnet Beta are **real** NZT
- Gossip entrypoint for Mainnet Beta: `entrypoint.mainnet-beta.Nexis.com:8001`

### Mainnet beta endpoint

- `https://api.mainnet-beta.Nexis.com` - Nexis Labs hosted api node cluster,
  backed by a load balancer; rate-limited

#### Example `Nexis` command-line configuration

To connect to the `mainnet-beta` Cluster using the Nexis CLI:

```bash
Nexis config set --url https://api.mainnet-beta.Nexis.com
```

### Mainnet beta rate limits

- Maximum number of requests per 10 seconds per IP: 100
- Maximum number of requests per 10 seconds per IP for a single RPC: 40
- Maximum concurrent connections per IP: 40
- Maximum connection rate per 10 seconds per IP: 40
- Maximum amount of data per 30 second: 100 MB

> The public RPC endpoints are not intended for production applications. Please
> use dedicated/private RPC servers when you launch your application, drop NFTs,
> etc. The public services are subject to abuse and rate limits may change
> without prior notice. Likewise, high-traffic websites may be blocked without
> prior notice.

## Common HTTP Error Codes

- 403 -- Your IP address or website has been blocked. It is time to run your own
  RPC server(s) or find a private service.
- 429 -- Your IP address is exceeding the rate limits. Slow down! Use the
  [Retry-After](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After)
  HTTP response header to determine how long to wait before making another
  request.
