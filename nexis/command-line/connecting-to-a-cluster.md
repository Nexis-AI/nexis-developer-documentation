# Connecting to a Cluster

**Connecting to a Cluster**

See Nexis Network Clusters for general information about the available clusters.

**Configure the command-line tool**

You can check what cluster the Nexis Network command-line tool (CLI) is currently targeting by running the following command:

```
Nexis config get
```

Use Nexisnetwork config set command to target a particular cluster. After setting a cluster target, any future subcommands will send/receive information from that cluster.

For example to target the Devnet cluster, run:

```
Nexis config set --url https://rpc-test-1.Nexis.network

```

**Ensure Versions Match**

Though not strictly necessary, the CLI will generally work best when its version matches the software version running on the cluster. To get the locally-installed CLI version, run:

```
Nexis --version
```

To get the cluster version, run:

```
Nexis cluster-version
```

Ensure the local CLI version is greater than or equal to the cluster version.
