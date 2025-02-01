# CLI Usage Reference

## CLI Usage Reference

The Nexis-cli crate provides a command-line interface tool for Nexis Network

### Examples

#### Get Pubkey

// Command

$ Nexisnetwork-keygen pubkey

&#x20;

// Return

\<PUBKEY>

#### Airdrop NZT/Lamports

// Command

Nexisnetwork airdrop 2

&#x20;

// Return

"2.00000000 NZT"

#### Get Balance

// Command

Nexisnetwork balance

&#x20;

// Return

"3.00050001 NZT"

#### Confirm Transaction

// Command

Nexisnetwork confirm \<TX\_SIGNATURE>

&#x20;

// Return

"Confirmed" / "Not found" / "Transaction failed with error \<ERR>"

#### Deploy program

// Command

Nexisnetwork deploy \<PATH>

&#x20;

// Return

\<PROGRAM\_ID>

### Usage

### Nexisnetwork-cli

Nexisnetwork-cli 0.3.6 (src:9e42883d; feat:2960423209)

Blockchain, Rebuilt _for_ Scale

&#x20;

USAGE:

&#x20;   Nexisnetwork \[FLAGS] \[OPTIONS] \<SUBCOMMAND>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

SUBCOMMANDS:

&#x20;   account                        Show the contents of an account

&#x20;   address                        Get your public key

&#x20;   airdrop                        Request lamports

&#x20;   authorize-nonce-account        Assign account authority to a new entity

&#x20;   balance                        Get your balance

&#x20;   block                          Get a confirmed block

&#x20;   block-height                   Get current block height

&#x20;   block-production               Show information about block production

&#x20;   block-time                     Get estimated production time of a block

&#x20;   catchup                        Wait for a validator to catch up to the cluster

&#x20;   cluster-date                   Get current cluster date, computed from genesis creation time and network time

&#x20;   cluster-version                Get the version of the cluster entrypoint

&#x20;   config                         Nexisnetwork command-line tool configuration settings

&#x20;   confirm                        Confirm transaction by signature

&#x20;   create-address-with-seed       Generate a derived account address with a seed

&#x20;   create-nonce-account           Create a nonce account

&#x20;   create-stake-account           Create a stake account

&#x20;   create-vote-account            Create a vote account

&#x20;   deactivate-stake               Deactivate the delegated stake from the stake account

&#x20;   decode-transaction             Decode a serialized transaction

&#x20;   delegate-stake                 Delegate stake to a vote account

&#x20;   deploy                         Deploy a program

&#x20;   epoch                          Get current epoch

&#x20;   epoch-info                     Get information about the current epoch

&#x20;   feature                        Runtime feature management

&#x20;   fees                           Display current cluster fees

&#x20;   first-available-block          Get the first available block in the storage

&#x20;   genesis-hash                   Get the genesis hash

&#x20;   gossip                         Show the current gossip network nodes

&#x20;   help                           Prints this message or the help of the given subcommand(s)

&#x20;   inflation                      Show inflation information

&#x20;   largest-accounts               Get addresses of largest cluster accounts

&#x20;   leader-schedule                Display leader schedule

&#x20;   live-slots                     Show information about the current slot progression

&#x20;   logs                           Stream transaction logs

&#x20;   merge-stake                    Merges one stake account into another

&#x20;   new-nonce                      Generate a new nonce, rendering the existing nonce useless

&#x20;   nonce                          Get the current nonce value

&#x20;   nonce-account                  Show the contents of a nonce account

&#x20;   ping                           Submit transactions sequentially

&#x20;   program                        Program management

&#x20;   rent                           Calculate per-epoch and rent-exempt-minimum values for a given account data

&#x20;                                  length.

&#x20;   resolve-signer                 Checks that a signer is valid, and returns its specific path; useful for signers

&#x20;                                  that may be specified generally, eg. usb://ledger

&#x20;   slot                           Get current slot

&#x20;   split-stake                    Duplicate a stake account, splitting the tokens between the two

&#x20;   stake-account                  Show the contents of a stake account

&#x20;   stake-authorize                Authorize a new signing keypair for the given stake account

&#x20;   stake-history                  Show the stake history

&#x20;   stake-set-lockup               Set Lockup for the stake account

&#x20;   stakes                         Show stake account information

&#x20;   supply                         Get information about the cluster supply of NZT

&#x20;   transaction-count              Get current transaction count

&#x20;   transaction-history            Show historical transactions affecting the given address from newest to oldest

&#x20;   transfer                       Transfer funds between system accounts

&#x20;   validator-info                 Publish/get Validator info on Nexisnetwork

&#x20;   validators                     Show summary information about the current validators

&#x20;   vote-account                   Show the contents of a vote account

&#x20;   vote-authorize-voter           Authorize a new vote signing keypair for the given vote account

&#x20;   vote-authorize-withdrawer      Authorize a new withdraw signing keypair for the given vote account

&#x20;   vote-update-commission         Update the vote account's commission

&#x20;   vote-update-validator          Update the vote account's validator identity

&#x20;   wait-for-max-stake             Wait _for_ the max stake of any one node to drop below a percentage of total.

&#x20;   withdraw-from-nonce-account    Withdraw NZT from the nonce account

&#x20;   withdraw-from-vote-account     Withdraw lamports from a vote account into a specified account

&#x20;   withdraw-stake                 Withdraw the unstaked NZT from the stake account

**Nexisnetwork-account**[**#**](https://docs.nexis.network/cli/usage#nexis-account)

Nexisnetwork-account

Show the contents of an account

&#x20;

USAGE:

&#x20;   Nexisnetwork account \[FLAGS] \[OPTIONS] \<ACCOUNT\_ADDRESS>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--lamports                       Display balance _in_ lamports instead of NZT

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork's JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;   \-o, --output-file \<FILEPATH>           Write the account data to this file

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<ACCOUNT\_ADDRESS>    Account key URI. , one of:

&#x20;                          \* a base58-encoded public key

&#x20;                          \* a path to a keypair file

&#x20;                          \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                          \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                          \* a hardware wallet keypair URL (i.e. usb://ledger)

**Nexisnetwork-address**[**#**](https://docs.nexis.network/cli/usage#nexis-address)

Nexisnetwork-address

Get your public key

&#x20;

USAGE:

&#x20;   Nexisnetwork address \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;       \--confirm-key                    Confirm key on device; only relevant _if_ using remote wallet

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-airdrop**[**#**](https://docs.nexis.network/cli/usage#nexis-airdrop)

Nexisnetwork-airdrop

Request lamports

&#x20;

USAGE:

&#x20;   Nexisnetwork airdrop \[FLAGS] \[OPTIONS] \<AMOUNT> \[RECIPIENT\_ADDRESS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;       \--faucet-host \<URL>                Faucet host to use \[default: the --url host]

&#x20;       \--faucet-port \<PORT\_NUMBER>        Faucet port to use \[default: 9900]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork's JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<AMOUNT>               The airdrop amount to request, in NZT    \<RECIPIENT\_ADDRESS>    The account address of airdrop recipient. , one of:

&#x20;                            \* a base58-encoded public key

&#x20;                            \* a path to a keypair file

&#x20;                            \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                            \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                            \* a hardware wallet keypair URL (i.e. usb://ledger)

**Nexisnetwork-authorize-nonce-account**[**#**](https://docs.nexis.network/cli/usage#nexis-authorize-nonce-account)

Nexisnetwork-authorize-nonce-account

Assign account authority to a new entity

&#x20;

USAGE:

&#x20;   Nexis authorize-nonce-account \[FLAGS] \[OPTIONS] \<NONCE\_ACCOUNT\_ADDRESS> \<AUTHORITY\_PUBKEY>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--nonce-authority \<KEYPAIR>        Provide the nonce authority keypair to use when signing a nonced transaction

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<NONCE\_ACCOUNT\_ADDRESS>    Address of the nonce account. , one of:

&#x20;                                \* a base58-encoded public key

&#x20;                                \* a path to a keypair file

&#x20;                                \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;   \<AUTHORITY\_PUBKEY>         Account to be granted authority of the nonce account. , one of:

&#x20;                                \* a base58-encoded public key

&#x20;                                \* a path to a keypair file

&#x20;                                \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                \* a hardware wallet keypair URL (i.e. usb://ledger)

**Nexisnetwork-balance**[**#**](https://docs.nexis.network/cli/usage#nexis-balance)

Nexisnetwork-balance

Get your balance

&#x20;

USAGE:

&#x20;   Nexisnetwork balance \[FLAGS] \[OPTIONS] \[ACCOUNT\_ADDRESS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--lamports                       Display balance _in_ lamports instead of NZT

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<ACCOUNT\_ADDRESS>    The account address of the balance to check. , one of:

&#x20;                          \* a base58-encoded public key

&#x20;                          \* a path to a keypair file

&#x20;                          \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                          \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                          \* a hardware wallet keypair URL (i.e. usb://ledger)

**Nexisnetwork-block**[**#**](https://docs.nexis.network/cli/usage#nexis-block)

Nexisnetwork-block

Get a confirmed block

&#x20;

USAGE:

&#x20;   Nexisnetwork block \[FLAGS] \[OPTIONS] \[SLOT]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<SLOT>

**Nexisnetwork-block-height**[**#**](https://docs.nexis.network/cli/usage#nexis-block-height)

Nexisnetwork-block-height

Get current block height

&#x20;

USAGE:

&#x20;   Nexisnetwork block-height \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-block-production**[**#**](https://docs.nexis.network/cli/usage#nexis-block-production)

Nexisnetwork-block-production

Show information about block production

&#x20;

USAGE:

&#x20;   Nexisnetwork block-production \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;       \--epoch \<epoch>                    Epoch to show block production _for_ \[default: current epoch]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--slot-limit \<slot\_limit>          Limit results to this many slots from the end of the epoch \[default: full

&#x20;                                          epoch]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-block-time**[**#**](https://docs.nexis.network/cli/usage#nexis-block-time)

Nexisnetwork-block-time

Get estimated production time of a block

&#x20;

USAGE:

&#x20;   Nexisnetwork block-time \[FLAGS] \[OPTIONS] \[SLOT]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<SLOT>    Slot number of the block to query

**Nexisnetwork-catchup**[**#**](https://docs.nexis.network/cli/usage#nexis-catchup)

Nexisnetwork-catchup

Wait _for_ a validator to catch up to the cluster

&#x20;

USAGE:

&#x20;   Nexisnetwork catchup \[FLAGS] \[OPTIONS] \[ARGS]

&#x20;

FLAGS:

&#x20;       \--follow                         Continue reporting progress even after the validator has caught up

&#x20;   \-h, --help                           Prints help information

&#x20;       \--log                            Don't update the progress inplace; instead show updates with its own new lines

&#x20;       \--no-address-labels              Do not use address labels in the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this if your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL for Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--our-localhost \<PORT>             Guess Identity pubkey and validator rpc node assuming local (possibly

&#x20;                                          private) validator \[default: 8899]

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<OUR\_VALIDATOR\_PUBKEY>    Identity pubkey of the validator, one of:

&#x20;                               \* a base58-encoded public key

&#x20;                               \* a path to a keypair file

&#x20;                               \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                               \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                               \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;   \<OUR\_URL>                 JSON RPC URL _for_ validator, which is useful _for_ validators with a private RPC service

**Nexisnetwork-cluster-date**[**#**](https://docs.nexis.network/cli/usage#nexis-cluster-date)

Nexisnetwork-cluster-date

Get current cluster date, computed from genesis creation time and network time

&#x20;

USAGE:

&#x20;   Nexisnetwork cluster-date \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-cluster-version**[**#**](https://docs.nexis.network/cli/usage#nexis-cluster-version)

Nexisnetwork -cluster-version

Get the version of the cluster entrypoint

&#x20;

USAGE:

&#x20;   Nexisnetwork cluster-version \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-config**[**#**](https://docs.nexis.network/cli/usage#nexis-config)

Nexisnetwork -config

Nexisnetwork command-line tool configuration settings

&#x20;

USAGE:

&#x20;   Nexisnetwork config \[FLAGS] \[OPTIONS] \<SUBCOMMAND>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

&#x20;

SUBCOMMANDS:

&#x20;   export-address-labels    Export the current address labels

&#x20;   get                      Get current config settings

&#x20;   help                     Prints this message or the help of the given subcommand(s)

&#x20;   import-address-labels    Import a list of address labels

&#x20;   set                      Set a config setting

**Nexisnetwork-confirm**[**#**](https://docs.nexis.network/cli/usage#nexis-confirm)

Nexisnetwork -confirm

Confirm transaction by signature

&#x20;

USAGE:

&#x20;   Nexisnetwork confirm \[FLAGS] \[OPTIONS] \<TRANSACTION\_SIGNATURE>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork's JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<TRANSACTION\_SIGNATURE>    The transaction signature to confirm

&#x20;

Note: This will show more detailed information _for_ finalized transactions with verbose mode (-v/--verbose).

&#x20;

Account modes:

&#x20; |srwx|

&#x20;   s: signed

&#x20;   r: readable (always true)

&#x20;   w: writable

&#x20;   x: program account (inner instructions excluded)

**Nexisnetwork-create-address-with-seed**[**#**](https://docs.nexis.network/cli/usage#nexis-create-address-with-seed)

Nexisnetwork -create-address-with-seed

Generate a derived account address with a seed

&#x20;

USAGE:

&#x20;   Nexisnetwork create-address-with-seed \[FLAGS] \[OPTIONS] \<SEED\_STRING> \<PROGRAM\_ID>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;       \--from \<FROM\_PUBKEY>               From (base) key, \[default: cli config keypair]. , one of:

&#x20;                                            \* a base58-encoded public key

&#x20;                                            \* a path to a keypair file

&#x20;                                            \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                            \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                            \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<SEED\_STRING>    The seed.  Must not take more than 32 bytes to encode as utf-8

&#x20;   \<PROGRAM\_ID>     The program\_id that the address will ultimately be used for,

&#x20;                    or one of NONCE, STAKE, and VOTE keywords

**Nexisnetwork-create-nonce-account**[**#**](https://docs.nexis.network/cli/usage#nexis-create-nonce-account)

Nexisnetwork -create-nonce-account

Create a nonce account

&#x20;

USAGE:

&#x20;   Nexisnetwork create-nonce-account \[FLAGS] \[OPTIONS] \<ACCOUNT\_KEYPAIR> \<AMOUNT>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--nonce-authority \<PUBKEY>         Assign noncing authority to another entity. , one of:

&#x20;                                            \* a base58-encoded public key

&#x20;                                            \* a path to a keypair file

&#x20;                                            \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                            \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                            \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--seed \<STRING>                    Seed _for_ address generation; _if_ specified, the resulting account will be at a

&#x20;                                          derived address of the NONCE\_ACCOUNT pubkey

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<ACCOUNT\_KEYPAIR>    Keypair of the nonce account to fund

&#x20;   \<AMOUNT>             The amount to load the nonce account with, _in_ NZT; accepts keyword ALL

**Nexisnetwork-create-stake-account**[**#**](https://docs.nexis.network/cli/usage#nexis-create-stake-account)

Nexisnetwork -create-stake-account

Create a stake account

&#x20;

USAGE:

&#x20;   Nexisnetwork create-stake-account \[FLAGS] \[OPTIONS] \<STAKE\_ACCOUNT\_KEYPAIR> \<AMOUNT>

&#x20;

FLAGS:

&#x20;       \--dump-transaction-message       Display the base64 encoded binary transaction message _in_ sign-only mode

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--sign-only                      Sign the transaction offline

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--blockhash \<BLOCKHASH>             Use the supplied blockhash

&#x20;       \--commitment \<COMMITMENT\_LEVEL>     Return information at the selected commitment level \[possible values:

&#x20;                                           processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                 Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;       \--custodian \<PUBKEY>                Authority to modify lockups. , one of:

&#x20;                                             \* a base58-encoded public key

&#x20;                                             \* a path to a keypair file

&#x20;                                             \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                             \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                             \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;       \--fee-payer \<KEYPAIR>               Specify the fee-payer account. This may be a keypair file, the ASK keyword

&#x20;                                           or the pubkey of an offline signer, provided an appropriate --signer

&#x20;                                           argument

&#x20;                                           is also passed. Defaults to the client keypair.

&#x20;       \--from \<KEYPAIR>                    Source account of funds \[default: cli config keypair]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>              URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                           testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                 Filepath or URL to a keypair

&#x20;       \--lockup-date \<RFC3339 DATETIME>    The date and time at which this account will be available _for_ withdrawal

&#x20;       \--lockup-epoch \<NUMBER>             The epoch height at which this account will be available _for_ withdrawal

&#x20;       \--nonce \<PUBKEY>                    Provide the nonce account to use when creating a nonced

&#x20;                                           transaction. Nonced transactions are useful when a transaction

&#x20;                                           requires a lengthy signing process. Learn more about nonced

&#x20;                                           transactions at https://docs. Nexisnetwork.com/cli/durable-nonce/

&#x20;       \--nonce-authority \<KEYPAIR>         Provide the nonce authority keypair to use when signing a nonced transaction

&#x20;       \--output \<FORMAT>                   Return information _in_ specified output format \[possible values: json, json-

&#x20;                                           compact]

&#x20;       \--seed \<STRING>                     Seed _for_ address generation; _if_ specified, the resulting account will be at

&#x20;                                           a derived address of the STAKE\_ACCOUNT\_KEYPAIR pubkey

&#x20;       \--signer \<PUBKEY=SIGNATURE>...      Provide a public-key/signature pair _for_ the transaction

&#x20;       \--stake-authority \<PUBKEY>          Authorized staker \[default: cli config keypair]

&#x20;       \--ws \<URL>                          WebSocket URL _for_ the Nexisnetwork cluster

&#x20;       \--withdraw-authority \<PUBKEY>       Authorized withdrawer \[default: cli config keypair]

&#x20;

ARGS:

&#x20;   \<STAKE\_ACCOUNT\_KEYPAIR>    Stake account to create (or base of derived address _if_ --seed is used)

&#x20;   \<AMOUNT>                   The amount to send to the stake account, _in_ NZT; accepts keyword ALL

**Nexisnetwork-create-vote-account**[**#**](https://docs.nexis.network/cli/usage#nexis-create-vote-account)

Nexisnetwork -create-vote-account

Create a vote account

&#x20;

USAGE:

&#x20;   Nexisnetwork create-vote-account \[FLAGS] \[OPTIONS] \<ACCOUNT\_KEYPAIR> \<IDENTITY\_KEYPAIR>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--authorized-voter \<VOTER\_PUBKEY>

&#x20;           Public key of the authorized voter \[default: validator identity pubkey]. , one of:

&#x20;             \* a base58-encoded public key

&#x20;             \* a path to a keypair file

&#x20;             \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;             \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;             \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;       \--authorized-withdrawer \<WITHDRAWER\_PUBKEY>

&#x20;           Public key of the authorized withdrawer \[default: validator identity pubkey]. , one of:

&#x20;             \* a base58-encoded public key

&#x20;             \* a path to a keypair file

&#x20;             \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;             \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;             \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;       \--commission \<PERCENTAGE>                      The commission taken on reward redemption (0-100) \[default: 100]

&#x20;       \--commitment \<COMMITMENT\_LEVEL>

&#x20;           Return information at the selected commitment level \[possible values: processed, confirmed, finalized]

&#x20;

&#x20;   \-C, --config \<FILEPATH>

&#x20;           Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;

&#x20;   \-u, --url \<URL\_OR\_MONIKER>

&#x20;           URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta, testnet, devnet, localhost]

&#x20;

&#x20;   \-k, --keypair \<KEYPAIR>                            Filepath or URL to a keypair

&#x20;       \--with-memo \<MEMO>                             Specify a memo string to include _in_ the transaction.

&#x20;       \--output \<FORMAT>

&#x20;           Return information _in_ specified output format \[possible values: json, json-compact]

&#x20;

&#x20;       \--seed \<STRING>

&#x20;           Seed _for_ address generation; _if_ specified, the resulting account will be at a derived address of the VOTE

&#x20;           ACCOUNT pubkey

&#x20;       \--ws \<URL>                                     WebSocket URL _for_ the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<ACCOUNT\_KEYPAIR>     Vote account keypair to create

&#x20;   \<IDENTITY\_KEYPAIR>    Keypair of validator that will vote with this account

**Nexisnetwork-deactivate-stake**[**#**](https://docs.nexis.network/cli/usage#nexis-deactivate-stake)

Nexisnetwork-deactivate-stake

Deactivate the delegated stake from the stake account

&#x20;

USAGE:

&#x20;   Nexisnetwork deactivate-stake \[FLAGS] \[OPTIONS] \<STAKE\_ACCOUNT\_ADDRESS>

&#x20;

FLAGS:

&#x20;       \--dump-transaction-message       Display the base64 encoded binary transaction message _in_ sign-only mode

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--sign-only                      Sign the transaction offline

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--blockhash \<BLOCKHASH>            Use the supplied blockhash

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;       \--fee-payer \<KEYPAIR>              Specify the fee-payer account. This may be a keypair file, the ASK keyword

&#x20;                                          or the pubkey of an offline signer, provided an appropriate --signer argument

&#x20;                                          is also passed. Defaults to the client keypair.

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--nonce \<PUBKEY>                   Provide the nonce account to use when creating a nonced

&#x20;                                          transaction. Nonced transactions are useful when a transaction

&#x20;                                          requires a lengthy signing process. Learn more about nonced

&#x20;                                          transactions at https://docs.Nexisnetwork.com/cli/durable-nonce/

&#x20;       \--nonce-authority \<KEYPAIR>        Provide the nonce authority keypair to use when signing a nonced transaction

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--seed \<STRING>                    Seed for address generation; if specified, the resulting account will be at a

&#x20;                                          derived address of STAKE\_ACCOUNT\_ADDRESS

&#x20;       \--signer \<PUBKEY=SIGNATURE>...     Provide a public-key/signature pair for the transaction

&#x20;       \--stake-authority \<KEYPAIR>        Authorized staker \[default: cli config keypair]

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<STAKE\_ACCOUNT\_ADDRESS>    Stake account to be deactivated (or base of derived address if --seed is used). , one

&#x20;                              of:

&#x20;                                \* a base58-encoded public key

&#x20;                                \* a path to a keypair file

&#x20;                                \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                \* a hardware wallet keypair URL (i.e. usb://ledger)

**Nexisnetwork-decode-transaction**[**#**](https://docs.nexis.network/cli/usage#nexis-decode-transaction)

Nexisnetwork-decode-transaction

Decode a serialized transaction

&#x20;

USAGE:

&#x20;   Nexisnetwork decode-transaction \[FLAGS] \[OPTIONS] \<TRANSACTION> \<ENCODING>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<TRANSACTION>    transaction to decode

&#x20;   \<ENCODING>       transaction encoding \[default: base58]  \[possible values: base58, base64]

**Nexisnetwork-delegate-stake**[**#**](https://docs.nexis.network/cli/usage#nexis-delegate-stake)

Nexisnetwork-delegate-stake

Delegate stake to a vote account

&#x20;

USAGE:

&#x20;   Nexisnetwork delegate-stake \[FLAGS] \[OPTIONS] \<STAKE\_ACCOUNT\_ADDRESS> \<VOTE\_ACCOUNT\_ADDRESS>

&#x20;

FLAGS:

&#x20;       \--dump-transaction-message       Display the base64 encoded binary transaction message _in_ sign-only mode

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--sign-only                      Sign the transaction offline

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--blockhash \<BLOCKHASH>            Use the supplied blockhash

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;       \--fee-payer \<KEYPAIR>              Specify the fee-payer account. This may be a keypair file, the ASK keyword

&#x20;                                          or the pubkey of an offline signer, provided an appropriate --signer argument

&#x20;                                          is also passed. Defaults to the client keypair.

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--nonce \<PUBKEY>                   Provide the nonce account to use when creating a nonced

&#x20;                                          transaction. Nonced transactions are useful when a transaction

&#x20;                                          requires a lengthy signing process. Learn more about nonced

&#x20;                                          transactions at https://docs.Nexisnetwork.com/cli/durable-nonce/

&#x20;       \--nonce-authority \<KEYPAIR>        Provide the nonce authority keypair to use when signing a nonced transaction

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--signer \<PUBKEY=SIGNATURE>...     Provide a public-key/signature pair for the transaction

&#x20;       \--stake-authority \<KEYPAIR>        Authorized staker \[default: cli config keypair]

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<STAKE\_ACCOUNT\_ADDRESS>    Stake account to delegate, one of:

&#x20;                                \* a base58-encoded public key

&#x20;                                \* a path to a keypair file

&#x20;                                \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;   \<VOTE\_ACCOUNT\_ADDRESS>     The vote account to which the stake will be delegated, one of:

&#x20;                                \* a base58-encoded public key

&#x20;                                \* a path to a keypair file

&#x20;                                \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                \* a hardware wallet keypair URL (i.e. usb://ledger)

**Nexisnetwork-deploy**[**#**](https://docs.nexis.network/cli/usage#nexis-deploy)

Nexisnetwork-deploy

Deploy a program

&#x20;

USAGE:

&#x20;   Nexisnetwork deploy \[FLAGS] \[OPTIONS] \<PROGRAM\_FILEPATH> \[PROGRAM\_ADDRESS\_SIGNER]

&#x20;

FLAGS:

&#x20;       \--allow-excessive-deploy-account-balance

&#x20;           Use the designated program id, even _if_ the account already holds a large balance of NZT

&#x20;

&#x20;   \-h, --help                                      Prints help information

&#x20;       \--no-address-labels                         Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation

&#x20;           Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39 official English word list

&#x20;

&#x20;   \-V, --version                                   Prints version information

&#x20;   \-v, --verbose                                   Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<PROGRAM\_FILEPATH>          /path/to/program.o

&#x20;   \<PROGRAM\_ADDRESS\_SIGNER>    The signer _for_ the desired address of the program \[default: new random address]

**exnonetwork-epoch**[**#**](https://docs.nexis.network/cli/usage#nexis-epoch)

Nexisnetwork -epoch

Get current epoch

&#x20;

USAGE:

&#x20;   Nexisnetwork epoch \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-epoch-info**[**#**](https://docs.nexis.network/cli/usage#nexis-epoch-info)

Nexisnetwork-epoch-info

Get information about the current epoch

&#x20;

USAGE:

&#x20;   Nexisnetwork epoch-info \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-feature**[**#**](https://docs.nexis.network/cli/usage#nexis-feature)

Nexisnetwork-feature

Runtime feature management

&#x20;

USAGE:

&#x20;   Nexisnetwork feature \[FLAGS] \[OPTIONS] \<SUBCOMMAND>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

&#x20;

SUBCOMMANDS:

&#x20;   activate    Activate a runtime feature

&#x20;   help        Prints this message or the help of the given subcommand(s)

&#x20;   status      Query runtime feature status

**Nexisnetwork-fees**[**#**](https://docs.nexis.network/cli/usage#nexis-fees)

Nexisnetwork-fees

Display current cluster fees

&#x20;

USAGE:

&#x20;   Nexisnetwork fees \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--blockhash \<BLOCKHASH>            Query fees _for_ BLOCKHASH instead of the the most recent blockhash

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-first-available-block**[**#**](https://docs.nexis.network/cli/usage#nexis-first-available-block)

Nexisnetwork-first-available-block

Get the first available block _in_ the storage

&#x20;

USAGE:

&#x20;   Nexisnetwork first-available-block \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-genesis-hash**[**#**](https://docs.nexis.network/cli/usage#nexis-genesis-hash)

Nexisnetwork-genesis-hash

Get the genesis hash

&#x20;

USAGE:

&#x20;   Nexisnetwork genesis-hash \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-gossip**[**#**](https://docs.nexis.network/cli/usage#nexis-gossip)

Nexisnetwork-gossip

Show the current gossip network nodes

&#x20;

USAGE:

&#x20;   Nexisnetwork gossip \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-help**[**#**](https://docs.nexis.network/cli/usage#nexis-help)

Nexisnetwork-help

Prints this message or the help of the given subcommand(s)

&#x20;

USAGE:

&#x20;   Nexisnetwork help \[subcommand]...

&#x20;

ARGS:

&#x20;   \<subcommand>...    The subcommand whose help message to display

**Nexisnetwork-inflation**[**#**](https://docs.nexis.network/cli/usage#nexis-inflation)

Nexisnetwork-inflation

Show inflation information

&#x20;

USAGE:

&#x20;   Nexisnetwork inflation \[FLAGS] \[OPTIONS] \[SUBCOMMAND]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

&#x20;

SUBCOMMANDS:

&#x20;   help       Prints this message or the help of the given subcommand(s)

&#x20;   rewards    Show inflation rewards _for_ a set of addresses

**Nexisnetwork-largest-accounts**[**#**](https://docs.nexis.network/cli/usage#nexis-largest-accounts)

Nexisnetwork-largest-accounts

Get addresses of largest cluster accounts

&#x20;

USAGE:

&#x20;   Nexisnetwork largest-accounts \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;       \--circulating                    Filter address list to only circulating accounts

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--non-circulating                Filter address list to only non-circulating accounts

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-leader-schedule**[**#**](https://docs.nexis.network/cli/usage#nexis-leader-schedule)

Nexisnetwork-leader-schedule

Display leader schedule

&#x20;

USAGE:

&#x20;   Nexisnetwork leader-schedule \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;       \--epoch \<EPOCH>                    Epoch to show leader schedule for. (default: current)

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-live-slots**[**#**](https://docs.nexis.network/cli/usage#nexis-live-slots)

Nexisnetwork-live-slots

Show information about the current slot progression

&#x20;

USAGE:

&#x20;   Nexisnetwork live-slots \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-logs**[**#**](https://docs.nexis.network/cli/usage#nexis-logs)

Nexisnetwork-logs

Stream transaction logs

&#x20;

USAGE:

&#x20;   Nexisnetwork logs \[FLAGS] \[OPTIONS] \[ADDRESS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--include-votes                  Include vote transactions when monitoring all transactions

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<ADDRESS>    Account address to monitor \[default: monitor all transactions except for votes] , one of:

&#x20;                  \* a base58-encoded public key

&#x20;                  \* a path to a keypair file

&#x20;                  \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                  \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                  \* a hardware wallet keypair URL (i.e. usb://ledger)

**Nexisnetwork-merge-stake**[**#**](https://docs.nexis.network/cli/usage#nexis-merge-stake)

Nexisnetwork-merge-stake

Merges one stake account into another

&#x20;

USAGE:

&#x20;   Nexisnetwork merge-stake \[FLAGS] \[OPTIONS] \<STAKE\_ACCOUNT\_ADDRESS> \<SOURCE\_STAKE\_ACCOUNT\_ADDRESS>

&#x20;

FLAGS:

&#x20;       \--dump-transaction-message       Display the base64 encoded binary transaction message _in_ sign-only mode

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--sign-only                      Sign the transaction offline

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--blockhash \<BLOCKHASH>            Use the supplied blockhash

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;       \--fee-payer \<KEYPAIR>              Specify the fee-payer account. This may be a keypair file, the ASK keyword

&#x20;                                          or the pubkey of an offline signer, provided an appropriate --signer argument

&#x20;                                          is also passed. Defaults to the client keypair.

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--nonce \<PUBKEY>                   Provide the nonce account to use when creating a nonced

&#x20;                                          transaction. Nonced transactions are useful when a transaction

&#x20;                                          requires a lengthy signing process. Learn more about nonced

&#x20;                                          transactions at https://docs.Nexisnetwork.com/cli/durable-nonce/

&#x20;       \--nonce-authority \<KEYPAIR>        Provide the nonce authority keypair to use when signing a nonced transaction

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--signer \<PUBKEY=SIGNATURE>...     Provide a public-key/signature pair for the transaction

&#x20;       \--stake-authority \<KEYPAIR>        Authorized staker \[default: cli config keypair]

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<STAKE\_ACCOUNT\_ADDRESS>           Stake account to merge into, one of:

&#x20;                                       \* a base58-encoded public key

&#x20;                                       \* a path to a keypair file

&#x20;                                       \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                       \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                       \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;   \<SOURCE\_STAKE\_ACCOUNT\_ADDRESS>    Source stake account for the merge.  If successful, this stake account will no

&#x20;                                     longer exist after the merge, one of:

&#x20;                                       \* a base58-encoded public key

&#x20;                                       \* a path to a keypair file

&#x20;                                       \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                       \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                       \* a hardware wallet keypair URL (i.e. usb://ledger)

**Nexisnetwork-new-nonce**[**#**](https://docs.nexis.network/cli/usage#nexis-new-nonce)

Nexisnetwork-new-nonce

Generate a new nonce, rendering the existing nonce useless

&#x20;

USAGE:

&#x20;   Nexisnetwork new-nonce \[FLAGS] \[OPTIONS] \<NONCE\_ACCOUNT\_ADDRESS>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--nonce-authority \<KEYPAIR>        Provide the nonce authority keypair to use when signing a nonced transaction

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<NONCE\_ACCOUNT\_ADDRESS>    Address of the nonce account. , one of:

&#x20;                                \* a base58-encoded public key

&#x20;                                \* a path to a keypair file

&#x20;                                \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                \* a hardware wallet keypair URL (i.e. usb://ledger)

**Nexisnetwork-nonce**[**#**](https://docs.nexis.network/cli/usage#nexis-nonce)

Nexisnetwork-nonce

Get the current nonce value

&#x20;

USAGE:

&#x20;   Nexisnetwork nonce \[FLAGS] \[OPTIONS] \<NONCE\_ACCOUNT\_ADDRESS>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<NONCE\_ACCOUNT\_ADDRESS>    Address of the nonce account to display. , one of:

&#x20;                                \* a base58-encoded public key

&#x20;                                \* a path to a keypair file

&#x20;                                \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                \* a hardware wallet keypair URL (i.e. usb://ledger)

**Nexisnetwork-nonce-account**[**#**](https://docs.nexis.network/cli/usage#nexis-nonce-account)

Nexisnetwork-nonce-account

Show the contents of a nonce account

&#x20;

USAGE:

&#x20;   Nexisnetwork nonce-account \[FLAGS] \[OPTIONS] \<NONCE\_ACCOUNT\_ADDRESS>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--lamports                       Display balance _in_ lamports instead of NZT

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<NONCE\_ACCOUNT\_ADDRESS>    Address of the nonce account to display. , one of:

&#x20;                                \* a base58-encoded public key

&#x20;                                \* a path to a keypair file

&#x20;                                \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                \* a hardware wallet keypair URL (i.e. usb://ledger)

**Nexisnetwork -ping**[**#**](https://docs.nexis.network/cli/usage#nexis-ping)

Nexisnetwork-ping

Submit transactions sequentially

&#x20;

USAGE:

&#x20;   Nexisnetwork ping \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;   \-D, --print-timestamp                Print timestamp (unix time + microseconds as _in_ gettimeofday) before each line

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--blockhash \<BLOCKHASH>            Use the supplied blockhash

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-c, --count \<NUMBER>                   Stop after submitting count transactions

&#x20;   \-i, --interval \<SECONDS>               Wait interval seconds between submitting the next transaction \[default: 2]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--lamports \<NUMBER>                Number of lamports to transfer _for_ each transaction \[default: 1]

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;   \-t, --timeout \<SECONDS>                Wait up to timeout seconds _for_ transaction confirmation \[default: 15]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-program**[**#**](https://docs.nexis.network/cli/usage#nexis-program)

Nexisnetwork-program

Program management

&#x20;

USAGE:

&#x20;   Nexisnetwork program \[FLAGS] \[OPTIONS] \<SUBCOMMAND>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

&#x20;

SUBCOMMANDS:

&#x20;   close                    Close an acount and withdraw all lamports

&#x20;   deploy                   Deploy a program

&#x20;   dump                     Write the program data to a file

&#x20;   help                     Prints this message or the help of the given subcommand(s)

&#x20;   set-buffer-authority     Set a new buffer authority

&#x20;   set-upgrade-authority    Set a new program authority

&#x20;   show                     Display information about a buffer or program

&#x20;   write-buffer             Writes a program into a buffer account

**Nexisnetwork-rent**[**#**](https://docs.nexis.network/cli/usage#nexis-rent)

Nexisnetwork-rent

Calculate per-epoch and rent-exempt-minimum values _for_ a given account data length.

&#x20;

USAGE:

&#x20;   Nexisnetwork rent \[FLAGS] \[OPTIONS] \<DATA\_LENGTH\_OR\_MONIKER>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--lamports                       Display rent _in_ lamports instead of NZT

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<DATA\_LENGTH\_OR\_MONIKER>    Length of data _in_ the account to calculate rent for, or moniker: \[nonce, stake,

&#x20;                               system, vote]

**Nexisnetwork-resolve-signer**[**#**](https://docs.nexis.network/cli/usage#nexis-resolve-signer)

Nexisnetwork-resolve-signer

Checks that a signer is valid, and returns its specific path; useful _for_ signers that may be specified generally, eg.

usb://ledger

&#x20;

USAGE:

&#x20;   Nexisnetwork resolve-signer \[FLAGS] \[OPTIONS] \<SIGNER\_KEYPAIR>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<SIGNER\_KEYPAIR>    The signer path to resolve

**Nexisnetwork-slot**[**#**](https://docs.nexis.network/cli/usage#nexis-slot)

Nexisnetwork-slot

Get current slot

&#x20;

USAGE:

&#x20;   Nexisnetwork slot \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-split-stake**[**#**](https://docs.nexis.network/cli/usage#nexis-split-stake)

Nexisnetwork-split-stake

Duplicate a stake account, splitting the tokens between the two

&#x20;

USAGE:

&#x20;   Nexisnetwork split-stake \[FLAGS] \[OPTIONS] \<STAKE\_ACCOUNT\_ADDRESS> \<SPLIT\_STAKE\_ACCOUNT> \<AMOUNT>

&#x20;

FLAGS:

&#x20;       \--dump-transaction-message       Display the base64 encoded binary transaction message _in_ sign-only mode

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--sign-only                      Sign the transaction offline

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--blockhash \<BLOCKHASH>            Use the supplied blockhash

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;       \--fee-payer \<KEYPAIR>              Specify the fee-payer account. This may be a keypair file, the ASK keyword

&#x20;                                          or the pubkey of an offline signer, provided an appropriate --signer argument

&#x20;                                          is also passed. Defaults to the client keypair.

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--nonce \<PUBKEY>                   Provide the nonce account to use when creating a nonced

&#x20;                                          transaction. Nonced transactions are useful when a transaction

&#x20;                                          requires a lengthy signing process. Learn more about nonced

&#x20;                                          transactions at https://docs.Nexisnetwork.com/cli/durable-nonce/

&#x20;       \--nonce-authority \<KEYPAIR>        Provide the nonce authority keypair to use when signing a nonced transaction

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--seed \<STRING>                    Seed for address generation; if specified, the resulting account will be at a

&#x20;                                          derived address of SPLIT\_STAKE\_ACCOUNT

&#x20;       \--signer \<PUBKEY=SIGNATURE>...     Provide a public-key/signature pair for the transaction

&#x20;       \--stake-authority \<KEYPAIR>        Authorized staker \[default: cli config keypair]

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<STAKE\_ACCOUNT\_ADDRESS>    Stake account to split (or base of derived address if --seed is used). , one of:

&#x20;                                \* a base58-encoded public key

&#x20;                                \* a path to a keypair file

&#x20;                                \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;   \<SPLIT\_STAKE\_ACCOUNT>      Keypair of the new stake account

&#x20;   \<AMOUNT>                   The amount to move into the new stake account, _in_ NZT

**Nexisnetwork-stake-account**[**#**](https://docs.nexis.network/cli/usage#nexis-stake-account)

Nexisnetwork-stake-account

Show the contents of a stake account

&#x20;

USAGE:

&#x20;   Nexisnetwork stake-account \[FLAGS] \[OPTIONS] \<STAKE\_ACCOUNT\_ADDRESS>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--lamports                       Display balance _in_ lamports instead of NZT

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;       \--with-rewards                   Display inflation rewards

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--num-rewards-epochs \<NUM>         Display rewards for NUM recent epochs, max 10 \[default: latest epoch only]

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<STAKE\_ACCOUNT\_ADDRESS>    The stake account to display. , one of:

&#x20;                                \* a base58-encoded public key

&#x20;                                \* a path to a keypair file

&#x20;                                \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                \* a hardware wallet keypair URL (i.e. usb://ledger)

**Nexisnetwork-stake-authorize**[**#**](https://docs.nexis.network/cli/usage#nexis-stake-authorize)

Nexisnetwork-stake-authorize

Authorize a new signing keypair _for_ the given stake account

&#x20;

USAGE:

&#x20;   Nexisnetwork stake-authorize \[FLAGS] \[OPTIONS] \<STAKE\_ACCOUNT\_ADDRESS> --new-stake-authority \<PUBKEY> --new-withdraw-authority \<PUBKEY>

&#x20;

FLAGS:

&#x20;       \--dump-transaction-message       Display the base64 encoded binary transaction message _in_ sign-only mode

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--sign-only                      Sign the transaction offline

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--blockhash \<BLOCKHASH>              Use the supplied blockhash

&#x20;       \--commitment \<COMMITMENT\_LEVEL>      Return information at the selected commitment level \[possible values:

&#x20;                                            processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                  Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;       \--custodian \<KEYPAIR>                Authority to override account lockup

&#x20;       \--fee-payer \<KEYPAIR>                Specify the fee-payer account. This may be a keypair file, the ASK keyword

&#x20;                                            or the pubkey of an offline signer, provided an appropriate --signer

&#x20;                                            argument

&#x20;                                            is also passed. Defaults to the client keypair.

&#x20;   \-u, --url \<URL\_OR\_MONIKER>               URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-

&#x20;                                            beta, testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                  Filepath or URL to a keypair

&#x20;       \--new-stake-authority \<PUBKEY>       New authorized staker, one of:

&#x20;                                              \* a base58-encoded public key

&#x20;                                              \* a path to a keypair file

&#x20;                                              \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                              \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                              \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;       \--new-withdraw-authority \<PUBKEY>    New authorized withdrawer. , one of:

&#x20;                                              \* a base58-encoded public key

&#x20;                                              \* a path to a keypair file

&#x20;                                              \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                              \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                              \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;       \--nonce \<PUBKEY>                     Provide the nonce account to use when creating a nonced

&#x20;                                            transaction. Nonced transactions are useful when a transaction

&#x20;                                            requires a lengthy signing process. Learn more about nonced

&#x20;                                            transactions at https://docs.Nexisnetwork.com/cli/durable-nonce/

&#x20;       \--nonce-authority \<KEYPAIR>          Provide the nonce authority keypair to use when signing a nonced

&#x20;                                            transaction

&#x20;       \--output \<FORMAT>                    Return information in specified output format \[possible values: json, json-

&#x20;                                            compact]

&#x20;       \--signer \<PUBKEY=SIGNATURE>...       Provide a public-key/signature pair for the transaction

&#x20;       \--stake-authority \<KEYPAIR>          Authorized staker \[default: cli config keypair]

&#x20;       \--ws \<URL>                           WebSocket URL for the Nexisnetwork cluster

&#x20;       \--withdraw-authority \<KEYPAIR>       Authorized withdrawer \[default: cli config keypair]

&#x20;

ARGS:

&#x20;   \<STAKE\_ACCOUNT\_ADDRESS>    Stake account in which to set a new authority. , one of:

&#x20;                                \* a base58-encoded public key

&#x20;                                \* a path to a keypair file

&#x20;                                \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                \* a hardware wallet keypair URL (i.e. usb://ledger)

**Nexisnetwork-stake-history**[**#**](https://docs.nexis.network/cli/usage#nexis-stake-history)

Nexisnetwork-stake-history

Show the stake history

&#x20;

USAGE:

&#x20;   Nexisnetwork stake-history \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--lamports                       Display balance _in_ lamports instead of NZT

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--limit \<NUM>                      Display NUM recent epochs worth of stake history _in_ text mode. 0 _for_ all

&#x20;                                          \[default: 10]

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-stake-set-lockup**[**#**](https://docs.nexis.network/cli/usage#nexis-stake-set-lockup)

Nexisnetwork-stake-set-lockup

Set Lockup _for_ the stake account

&#x20;

USAGE:

&#x20;   Nexisnetwork stake-set-lockup \[FLAGS] \[OPTIONS] \<STAKE\_ACCOUNT\_ADDRESS> <--lockup-epoch \<NUMBER>|--lockup-date \<RFC3339 DATETIME>|--new-custodian \<PUBKEY>>

&#x20;

FLAGS:

&#x20;       \--dump-transaction-message       Display the base64 encoded binary transaction message _in_ sign-only mode

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--sign-only                      Sign the transaction offline

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--blockhash \<BLOCKHASH>             Use the supplied blockhash

&#x20;       \--commitment \<COMMITMENT\_LEVEL>     Return information at the selected commitment level \[possible values:

&#x20;                                           processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                 Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;       \--custodian \<KEYPAIR>               Keypair of the existing custodian \[default: cli config pubkey]

&#x20;       \--fee-payer \<KEYPAIR>               Specify the fee-payer account. This may be a keypair file, the ASK keyword

&#x20;                                           or the pubkey of an offline signer, provided an appropriate --signer

&#x20;                                           argument

&#x20;                                           is also passed. Defaults to the client keypair.

&#x20;   \-u, --url \<URL\_OR\_MONIKER>              URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                           testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                 Filepath or URL to a keypair

&#x20;       \--lockup-date \<RFC3339 DATETIME>    The date and time at which this account will be available for withdrawal

&#x20;       \--lockup-epoch \<NUMBER>             The epoch height at which this account will be available for withdrawal

&#x20;       \--new-custodian \<PUBKEY>            Identity of a new lockup custodian. , one of:

&#x20;                                             \* a base58-encoded public key

&#x20;                                             \* a path to a keypair file

&#x20;                                             \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                             \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                             \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;       \--nonce \<PUBKEY>                    Provide the nonce account to use when creating a nonced

&#x20;                                           transaction. Nonced transactions are useful when a transaction

&#x20;                                           requires a lengthy signing process. Learn more about nonced

&#x20;                                           transactions at https://docs.Nexisnetwork.com/cli/durable-nonce/

&#x20;       \--nonce-authority \<KEYPAIR>         Provide the nonce authority keypair to use when signing a nonced transaction

&#x20;       \--output \<FORMAT>                   Return information in specified output format \[possible values: json, json-

&#x20;                                           compact]

&#x20;       \--signer \<PUBKEY=SIGNATURE>...      Provide a public-key/signature pair for the transaction

&#x20;       \--ws \<URL>                          WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<STAKE\_ACCOUNT\_ADDRESS>    Stake account for which to set lockup parameters. , one of:

&#x20;                                \* a base58-encoded public key

&#x20;                                \* a path to a keypair file

&#x20;                                \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                \* a hardware wallet keypair URL (i.e. usb://ledger)

**Nexisnetwork-stakes**[**#**](https://docs.nexis.network/cli/usage#nexis-stakes)

Nexisnetwork-stakes

Show stake account information

&#x20;

USAGE:

&#x20;   Nexisnetwork stakes \[FLAGS] \[OPTIONS] \[VOTE\_ACCOUNT\_PUBKEYS]...

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--lamports                       Display balance _in_ lamports instead of NZT

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<VOTE\_ACCOUNT\_PUBKEYS>...    Only show stake accounts delegated to the provided vote accounts. , one of:

&#x20;                                  \* a base58-encoded public key

&#x20;                                  \* a path to a keypair file

&#x20;                                  \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                  \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                  \* a hardware wallet keypair URL (i.e. usb://ledger)

**Nexisnetwork-supply**[**#**](https://docs.nexis.network/cli/usage#nexis-supply)

Nexisnetwork-supply

Get information about the cluster supply of NZT

&#x20;

USAGE:

&#x20;   Nexisnetwork supply \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--print-accounts                 Print list of non-circualting account addresses

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-transaction-count**[**#**](https://docs.nexis.network/cli/usage#nexis-transaction-count)

Nexisnetwork-transaction-count

Get current transaction count

&#x20;

USAGE:

&#x20;   Nexisnetwork transaction-count \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-transaction-history**[**#**](https://docs.nexis.network/cli/usage#nexis-transaction-history)

Nexisnetwork-transaction-history

Show historical transactions affecting the given address from newest to oldest

&#x20;

USAGE:

&#x20;   Nexisnetwork transaction-history \[FLAGS] \[OPTIONS] \<ADDRESS>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--show-transactions              Display the full transactions

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--before \<TRANSACTION\_SIGNATURE>    Start with the first signature older than this one

&#x20;       \--commitment \<COMMITMENT\_LEVEL>     Return information at the selected commitment level \[possible values:

&#x20;                                           processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                 Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>              URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                           testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                 Filepath or URL to a keypair

&#x20;       \--limit \<LIMIT>                     Maximum number of transaction signatures to return \[default: 1000]

&#x20;       \--output \<FORMAT>                   Return information in specified output format \[possible values: json, json-

&#x20;                                           compact]

&#x20;       \--ws \<URL>                          WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<ADDRESS>    Account address, one of:

&#x20;                  \* a base58-encoded public key

&#x20;                  \* a path to a keypair file

&#x20;                  \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                  \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                  \* a hardware wallet keypair URL (i.e. usb://ledger)

**Nexisnetwork-transfer**[**#**](https://docs.nexis.network/cli/usage#nexis-transfer)

Nexisnetwork-transfer

Transfer funds between system accounts

&#x20;

USAGE:

&#x20;   Nexisnetwork transfer \[FLAGS] \[OPTIONS] \<RECIPIENT\_ADDRESS> \<AMOUNT>

&#x20;

FLAGS:

&#x20;       \--allow-unfunded-recipient       Complete the transfer even _if_ the recipient address is not funded

&#x20;       \--dump-transaction-message       Display the base64 encoded binary transaction message _in_ sign-only mode

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--no-wait                        Return signature immediately after submitting the transaction, instead of

&#x20;                                        waiting _for_ confirmations

&#x20;       \--sign-only                      Sign the transaction offline

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--blockhash \<BLOCKHASH>            Use the supplied blockhash

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;       \--fee-payer \<KEYPAIR>              Specify the fee-payer account. This may be a keypair file, the ASK keyword

&#x20;                                          or the pubkey of an offline signer, provided an appropriate --signer argument

&#x20;                                          is also passed. Defaults to the client keypair.

&#x20;       \--from \<FROM\_ADDRESS>              Source account of funds (if different from client local account). , one of:

&#x20;                                            \* a base58-encoded public key

&#x20;                                            \* a path to a keypair file

&#x20;                                            \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                            \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                            \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--with-memo \<MEMO>                 Specify a memo string to include in the transaction.

&#x20;       \--nonce \<PUBKEY>                   Provide the nonce account to use when creating a nonced

&#x20;                                          transaction. Nonced transactions are useful when a transaction

&#x20;                                          requires a lengthy signing process. Learn more about nonced

&#x20;                                          transactions at https://docs.Nexisnetwork.com/cli/durable-nonce/

&#x20;       \--nonce-authority \<KEYPAIR>        Provide the nonce authority keypair to use when signing a nonced transaction

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--signer \<PUBKEY=SIGNATURE>...     Provide a public-key/signature pair for the transaction

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<RECIPIENT\_ADDRESS>    The account address of recipient. , one of:

&#x20;                            \* a base58-encoded public key

&#x20;                            \* a path to a keypair file

&#x20;                            \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                            \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                            \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;   \<AMOUNT>               The amount to send, _in_ NZT accepts keyword ALL

**Nexisnetwork-validator-info**[**#**](https://docs.nexis.network/cli/usage#nexis-validator-info)

Nexisnetwork-validator-info

Publish/get Validator info on Nexisnetwork

&#x20;

USAGE:

&#x20;   Nexisnetwork validator-info \[FLAGS] \[OPTIONS] \<SUBCOMMAND>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

&#x20;

SUBCOMMANDS:

&#x20;   get        Get and parse Nexisnetwork Validator info

&#x20;   help       Prints this message or the help of the given subcommand(s)

&#x20;   publish    Publish Validator info on Nexisnetwork

**Nexisnetwork-validators**[**#**](https://docs.nexis.network/cli/usage#nexis-validators)

Nexisnetwork-validators

Show summary information about the current validators

&#x20;

USAGE:

&#x20;   Nexisnetwork validators \[FLAGS] \[OPTIONS]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--lamports                       Display balance _in_ lamports instead of NZT

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;   \-n, --number                         Number the validators

&#x20;   \-r, --reverse                        Reverse order _while_ sorting

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--sort \<sort>                      Sort order (does not affect JSON output) \[default: stake]  \[possible values:

&#x20;                                          delinquent, commission, credits, identity, last-vote, root, skip-rate, stake,

&#x20;                                          vote-account]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

**Nexisnetwork-vote-account**[**#**](https://docs.nexis.network/cli/usage#nexis-vote-account)

Nexisnetwork-vote-account

Show the contents of a vote account

&#x20;

USAGE:

&#x20;   Nexisnetwork vote-account \[FLAGS] \[OPTIONS] \<VOTE\_ACCOUNT\_ADDRESS>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--lamports                       Display balance _in_ lamports instead of NZT

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;       \--with-rewards                   Display inflation rewards

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--num-rewards-epochs \<NUM>         Display rewards for NUM recent epochs, max 10 \[default: latest epoch only]

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<VOTE\_ACCOUNT\_ADDRESS>    Vote account pubkey. , one of:

&#x20;                               \* a base58-encoded public key

&#x20;                               \* a path to a keypair file

&#x20;                               \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                               \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                               \* a hardware wallet keypair URL (i.e. usb://ledger)

**ezonetwork -vote-authorize-voter**[**#**](https://docs.nexis.network/cli/usage#nexis-vote-authorize-voter)

Nexisnetwork-vote-authorize-voter

Authorize a new vote signing keypair _for_ the given vote account

&#x20;

USAGE:

&#x20;   Nexisnetwork vote-authorize-voter \[FLAGS] \[OPTIONS] \<VOTE\_ACCOUNT\_ADDRESS> \<AUTHORIZED\_KEYPAIR> \<NEW\_AUTHORIZED\_PUBKEY>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--with-memo \<MEMO>                 Specify a memo string to include in the transaction.

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<VOTE\_ACCOUNT\_ADDRESS>     Vote account in which to set the authorized voter. , one of:

&#x20;                                \* a base58-encoded public key

&#x20;                                \* a path to a keypair file

&#x20;                                \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;   \<AUTHORIZED\_KEYPAIR>       Current authorized vote signer.

&#x20;   \<NEW\_AUTHORIZED\_PUBKEY>    New authorized vote signer. , one of:

&#x20;                                \* a base58-encoded public key

&#x20;                                \* a path to a keypair file

&#x20;                                \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                \* a hardware wallet keypair URL (i.e. usb://ledger)

**Nexisnetwork-vote-authorize-withdrawer**[**#**](https://docs.nexis.network/cli/usage#nexis-vote-authorize-withdrawer)

Nexisnetwork-vote-authorize-withdrawer

Authorize a new withdraw signing keypair _for_ the given vote account

&#x20;

USAGE:

&#x20;   Nexisnetwork vote-authorize-withdrawer \[FLAGS] \[OPTIONS] \<VOTE\_ACCOUNT\_ADDRESS> \<AUTHORIZED\_KEYPAIR> \<AUTHORIZED\_PUBKEY>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--with-memo \<MEMO>                 Specify a memo string to include in the transaction.

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<VOTE\_ACCOUNT\_ADDRESS>    Vote account in which to set the authorized withdrawer. , one of:

&#x20;                               \* a base58-encoded public key

&#x20;                               \* a path to a keypair file

&#x20;                               \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                               \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                               \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;   \<AUTHORIZED\_KEYPAIR>      Current authorized withdrawer.

&#x20;   \<AUTHORIZED\_PUBKEY>       New authorized withdrawer. , one of:

&#x20;                               \* a base58-encoded public key

&#x20;                               \* a path to a keypair file

&#x20;                               \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                               \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                               \* a hardware wallet keypair URL (i.e. usb://ledger)

**Nexisnetwork-vote-update-commission**[**#**](https://docs.nexis.network/cli/usage#nexis-vote-update-commission)

Nexisnetwork-vote-update-commission

Update the vote account's commission

&#x20;

USAGE:

&#x20;   Nexisnetwork vote-update-commission \[FLAGS] \[OPTIONS] \<VOTE\_ACCOUNT\_ADDRESS> \<PERCENTAGE> \<AUTHORIZED\_KEYPAIR>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels in the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this if your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL for Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--with-memo \<MEMO>                 Specify a memo string to include _in_ the transaction.

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<VOTE\_ACCOUNT\_ADDRESS>    Vote account to update. , one of:

&#x20;                               \* a base58-encoded public key

&#x20;                               \* a path to a keypair file

&#x20;                               \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                               \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                               \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;   \<PERCENTAGE>              The new commission

&#x20;   \<AUTHORIZED\_KEYPAIR>      Authorized withdrawer keypair

**Nexisnetwork-vote-update-validator**[**#**](https://docs.nexis.network/cli/usage#nexis-vote-update-validator)

Nexisnetwork-vote-update-validator

Update the vote account's validator identity

&#x20;

USAGE:

&#x20;   Nexisnetwork vote-update-validator \[FLAGS] \[OPTIONS] \<VOTE\_ACCOUNT\_ADDRESS> \<IDENTITY\_KEYPAIR> \<AUTHORIZED\_KEYPAIR>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels in the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this if your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL for Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--with-memo \<MEMO>                 Specify a memo string to include _in_ the transaction.

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<VOTE\_ACCOUNT\_ADDRESS>    Vote account to update. , one of:

&#x20;                               \* a base58-encoded public key

&#x20;                               \* a path to a keypair file

&#x20;                               \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                               \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                               \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;   \<IDENTITY\_KEYPAIR>        Keypair of new validator that will vote with this account

&#x20;   \<AUTHORIZED\_KEYPAIR>      Authorized withdrawer keypair

**Nexisnetwork-wait-for-max-stake**[**#**](https://docs.nexis.network/cli/usage#nexis-wait-for-max-stake)

Nexisnetwork-wait-for-max-stake

Wait _for_ the max stake of any one node to drop below a percentage of total.

&#x20;

USAGE:

&#x20;   Nexisnetwork wait-for-max-stake \[FLAGS] \[OPTIONS] \[PERCENT]

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--output \<FORMAT>                  Return information _in_ specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL _for_ the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<PERCENT>

**Nexisnetwork-withdraw-from-nonce-account**[**#**](https://docs.nexis.network/cli/usage#nexis-withdraw-from-nonce-account)

Nexisnetwork-withdraw-from-nonce-account

Withdraw NZT from the nonce account

&#x20;

USAGE:

&#x20;   Nexisnetwork withdraw-from-nonce-account \[FLAGS] \[OPTIONS] \<NONCE\_ACCOUNT\_ADDRESS> \<RECIPIENT\_ADDRESS> \<AMOUNT>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--nonce-authority \<KEYPAIR>        Provide the nonce authority keypair to use when signing a nonced transaction

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<NONCE\_ACCOUNT\_ADDRESS>    Nonce account to withdraw from. , one of:

&#x20;                                \* a base58-encoded public key

&#x20;                                \* a path to a keypair file

&#x20;                                \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;   \<RECIPIENT\_ADDRESS>        The account to which the NZT should be transferred. , one of:

&#x20;                                \* a base58-encoded public key

&#x20;                                \* a path to a keypair file

&#x20;                                \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;   \<AMOUNT>                   The amount to withdraw from the nonce account, _in_ NZT

**Nexisnetwork-withdraw-from-vote-account**[**#**](https://docs.nexis.network/cli/usage#nexis-withdraw-from-vote-account)

Nexisnetwork-withdraw-from-vote-account

Withdraw lamports from a vote account into a specified account

&#x20;

USAGE:

&#x20;   Nexisnetwork withdraw-from-vote-account \[FLAGS] \[OPTIONS] \<VOTE\_ACCOUNT\_ADDRESS> \<RECIPIENT\_ADDRESS> \<AMOUNT>

&#x20;

FLAGS:

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--authorized-withdrawer \<AUTHORIZED\_KEYPAIR>    Authorized withdrawer \[default: cli config keypair]

&#x20;       \--commitment \<COMMITMENT\_LEVEL>

&#x20;           Return information at the selected commitment level \[possible values: processed, confirmed, finalized]

&#x20;

&#x20;   \-C, --config \<FILEPATH>

&#x20;           Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;

&#x20;   \-u, --url \<URL\_OR\_MONIKER>

&#x20;           URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta, testnet, devnet, localhost]

&#x20;

&#x20;   \-k, --keypair \<KEYPAIR>                             Filepath or URL to a keypair

&#x20;       \--with-memo \<MEMO>                              Specify a memo string to include in the transaction.

&#x20;       \--output \<FORMAT>

&#x20;           Return information in specified output format \[possible values: json, json-compact]

&#x20;

&#x20;       \--ws \<URL>                                      WebSocket URL for the Nexisnetwork cluster

&#x20;

ARGS:

&#x20;   \<VOTE\_ACCOUNT\_ADDRESS>    Vote account from which to withdraw. , one of:

&#x20;                               \* a base58-encoded public key

&#x20;                               \* a path to a keypair file

&#x20;                               \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                               \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                               \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;   \<RECIPIENT\_ADDRESS>       The recipient of withdrawn NZT. , one of:

&#x20;                               \* a base58-encoded public key

&#x20;                               \* a path to a keypair file

&#x20;                               \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                               \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                               \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;   \<AMOUNT>                  The amount to withdraw, _in_ NZT; accepts keyword ALL

**Nexisnetwork-withdraw-stake**[**#**](https://docs.nexis.network/cli/usage#nexis-withdraw-stake)

Nexisnetwork-withdraw-stake

Withdraw the unstaked NZT from the stake account

&#x20;

USAGE:

&#x20;   Nexisnetwork withdraw-stake \[FLAGS] \[OPTIONS] \<STAKE\_ACCOUNT\_ADDRESS> \<RECIPIENT\_ADDRESS> \<AMOUNT>

&#x20;

FLAGS:

&#x20;       \--dump-transaction-message       Display the base64 encoded binary transaction message _in_ sign-only mode

&#x20;   \-h, --help                           Prints help information

&#x20;       \--no-address-labels              Do not use address labels _in_ the output

&#x20;       \--sign-only                      Sign the transaction offline

&#x20;       \--skip-seed-phrase-validation    Skip validation of seed phrases. Use this _if_ your phrase does not use the BIP39

&#x20;                                        official English word list

&#x20;   \-V, --version                        Prints version information

&#x20;   \-v, --verbose                        Show additional information

&#x20;

OPTIONS:

&#x20;       \--blockhash \<BLOCKHASH>            Use the supplied blockhash

&#x20;       \--commitment \<COMMITMENT\_LEVEL>    Return information at the selected commitment level \[possible values:

&#x20;                                          processed, confirmed, finalized]

&#x20;   \-C, --config \<FILEPATH>                Configuration file to use \[default: \~/.config/Nexisnetwork/cli/config.yml]

&#x20;       \--custodian \<KEYPAIR>              Authority to override account lockup

&#x20;       \--fee-payer \<KEYPAIR>              Specify the fee-payer account. This may be a keypair file, the ASK keyword

&#x20;                                          or the pubkey of an offline signer, provided an appropriate --signer argument

&#x20;                                          is also passed. Defaults to the client keypair.

&#x20;   \-u, --url \<URL\_OR\_MONIKER>             URL _for_ Nexisnetwork’s JSON RPC or moniker (or their first letter): \[mainnet-beta,

&#x20;                                          testnet, devnet, localhost]

&#x20;   \-k, --keypair \<KEYPAIR>                Filepath or URL to a keypair

&#x20;       \--nonce \<PUBKEY>                   Provide the nonce account to use when creating a nonced

&#x20;                                          transaction. Nonced transactions are useful when a transaction

&#x20;                                          requires a lengthy signing process. Learn more about nonced

&#x20;                                          transactions at https://docs.Nexisnetwork.com/cli/durable-nonce/

&#x20;       \--nonce-authority \<KEYPAIR>        Provide the nonce authority keypair to use when signing a nonced transaction

&#x20;       \--output \<FORMAT>                  Return information in specified output format \[possible values: json, json-

&#x20;                                          compact]

&#x20;       \--seed \<STRING>                    Seed for address generation; if specified, the resulting account will be at a

&#x20;                                          derived address of STAKE\_ACCOUNT\_ADDRESS

&#x20;       \--signer \<PUBKEY=SIGNATURE>...     Provide a public-key/signature pair for the transaction

&#x20;       \--ws \<URL>                         WebSocket URL for the Nexisnetwork cluster

&#x20;       \--withdraw-authority \<KEYPAIR>     Authorized withdrawer \[default: cli config keypair]

&#x20;

ARGS:

&#x20;   \<STAKE\_ACCOUNT\_ADDRESS>    Stake account from which to withdraw (or base of derived address if --seed is used).

&#x20;                              , one of:

&#x20;                                \* a base58-encoded public key

&#x20;                                \* a path to a keypair file

&#x20;                                \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;   \<RECIPIENT\_ADDRESS>        Recipient of withdrawn NZT, one of:

&#x20;                                \* a base58-encoded public key

&#x20;                                \* a path to a keypair file

&#x20;                                \* a hyphen; signals a JSON-encoded keypair on stdin

&#x20;                                \* the 'ASK' keyword; to recover a keypair via its seed phrase

&#x20;                                \* a hardware wallet keypair URL (i.e. usb://ledger)

&#x20;   \<AMOUNT>                   The amount to withdraw from the stake account, _in_ NZT; accepts keyword ALL
