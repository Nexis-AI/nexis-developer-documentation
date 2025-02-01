# Offline Transaction Signing

## Offline Transaction Signing

Some security models require keeping signing keys, and thus the signing process, separated from transaction creation and network broadcast. Examples include:

* Collecting signatures from geographically disparate signers in a multi-signature scheme
* Signing transactions using an airgapped signing device

This document describes using Nexis Network CLI to separately sign and submit a transaction.

### Commands Supporting Offline Signing

At present, the following commands support offline signing:

* [`create-stake-account`](https://docs.nexis.network/cli/usage#nexis-create-stake-account)
* [`deactivate-stake`](https://docs.nexis.network/cli/usage#nexis-deactivate-stake)
* [`delegate-stake`](https://docs.nexis.network/cli/usage#nexis-delegate-stake)
* [`split-stake`](https://docs.nexis.network/cli/usage#nexis-split-stake)
* [`stake-authorize`](https://docs.nexis.network/cli/usage#nexis-stake-authorize)
* [`stake-set-lockup`](https://docs.nexis.network/cli/usage#nexis-stake-set-lockup)
* [`transfer`](https://docs.nexis.network/cli/usage#nexis-transfer)
* [`withdraw-stake`](https://docs.nexis.network/cli/usage#nexis-withdraw-stake)

### Signing Transactions Offline

To sign a transaction offline, pass the following arguments on the command line

1. `--sign-only`, prevents the client from submitting the signed transaction to the network. Instead, the pubkey/signature pairs are printed to stdout.
2. `--blockhash BASE58_HASH`, allows the caller to specify the value used to fill the transaction's `recent_blockhash` field. This serves a number of purposes, namely: _Eliminates the need to connect to the network and query a recent blockhash via RPC_ Enables the signers to coordinate the blockhash in a multiple-signature scheme

#### Example: Offline Signing a Payment

Command

Nexisnetwork@offline$ Nexisnetwork transfer --sign-only --blockhash 5Tx8F3jgSHx21CbtjwmdaKPLM5tWmreWAnPrbqHomSJF \\

&#x20;   recipient-keypair.json 1

Output

&#x20;

Blockhash: 5Tx8F3jgSHx21CbtjwmdaKPLM5tWmreWAnPrbqHomSJF

Signers (Pubkey=Signature):

&#x20; FhtzLVsmcV7S5XqGD79ErgoseCLhZYmEZnz9kQg1Rp7j=4vC38p4bz7XyiXrk6HtaooUqwxTWKocf45cstASGtmrD398biNJnmTcUCVEojE7wVQvgdYbjHJqRFZPpzfCQpmUN

&#x20;

{"blockhash":"5Tx8F3jgSHx21CbtjwmdaKPLM5tWmreWAnPrbqHomSJF","signers":\["FhtzLVsmcV7S5XqGD79ErgoseCLhZYmEZnz9kQg1Rp7j=4vC38p4bz7XyiXrk6HtaooUqwxTWKocf45cstASGtmrD398biNJnmTcUCVEojE7wVQvgdYbjHJqRFZPpzfCQpmUN"]}'

### Submitting Offline Signed Transactions to the Network

To submit a transaction that has been signed offline to the network, pass the following arguments on the command line

1. `--blockhash BASE58_HASH`, must be the same blockhash as was used to sign
2. `--signer BASE58_PUBKEY=BASE58_SIGNATURE`, one for each offline signer. This includes the pubkey/signature pairs directly in the transaction rather than signing it with any local keypair(s)

#### Example: Submitting an Offline Signed Payment

Command

Nexisnetwork@online$ Nexisnetwork transfer --blockhash 5Tx8F3jgSHx21CbtjwmdaKPLM5tWmreWAnPrbqHomSJF \\

&#x20;   \--signer FhtzLVsmcV7S5XqGD79ErgoseCLhZYmEZnz9kQg1Rp7j=4vC38p4bz7XyiXrk6HtaooUqwxTWKocf45cstASGtmrD398biNJnmTcUCVEojE7wVQvgdYbjHJqRFZPpzfCQpmUN

&#x20;   recipient-keypair.json 1

Output

4vC38p4bz7XyiXrk6HtaooUqwxTWKocf45cstASGtmrD398biNJnmTcUCVEojE7wVQvgdYbjHJqRFZPpzfCQpmUN

### Offline Signing Over Multiple Sessions

Offline signing can also take place over multiple sessions. In this scenario, pass the absent signer's public key for each role. All pubkeys that were specified, but no signature was generated for will be listed as absent in the offline signing output

#### Example: Transfer with Two Offline Signing Sessions

Command (Offline Session #1)

Nexisnetwork@offline1 Nexisnetwork transfer Fdri24WUGtrCXZ55nXiewAj6RM18hRHPGAjZk3o6vBut 10 \\

&#x20;   \--blockhash 7ALDjLv56a8f6sH6upAZALQKkXyjAwwENH9GomyM8Dbc \\

&#x20;   \--sign-only \\

&#x20;   \--keypair fee\_payer.json \\

&#x20;   \--from 674RgFMgdqdRoVtMqSBg7mHFbrrNm1h1r721H1ZMquHL

Output (Offline Session #1)

Blockhash: 7ALDjLv56a8f6sH6upAZALQKkXyjAwwENH9GomyM8Dbc

Signers (Pubkey=Signature):

&#x20; 3bo5YiRagwmRikuH6H1d2gkKef5nFZXE3gJeoHxJbPjy=ohGKvpRC46jAduwU9NW8tP91JkCT5r8Mo67Ysnid4zc76tiiV1Ho6jv3BKFSbBcr2NcPPCarmfTLSkTHsJCtdYi

Absent Signers (Pubkey):

&#x20; 674RgFMgdqdRoVtMqSBg7mHFbrrNm1h1r721H1ZMquHL

Command (Offline Session #2)

Nexisnetwork@offline2 Nexisnetwork transfer Fdri24WUGtrCXZ55nXiewAj6RM18hRHPGAjZk3o6vBut 10 \\

&#x20;   \--blockhash 7ALDjLv56a8f6sH6upAZALQKkXyjAwwENH9GomyM8Dbc \\

&#x20;   \--sign-only \\

&#x20;   \--keypair from.json \\

&#x20;   \--fee-payer 3bo5YiRagwmRikuH6H1d2gkKef5nFZXE3gJeoHxJbPjy

Output (Offline Session #2)

Blockhash: 7ALDjLv56a8f6sH6upAZALQKkXyjAwwENH9GomyM8Dbc

Signers (Pubkey=Signature):

&#x20; 674RgFMgdqdRoVtMqSBg7mHFbrrNm1h1r721H1ZMquHL=3vJtnba4dKQmEAieAekC1rJnPUndBcpvqRPRMoPWqhLEMCty2SdUxt2yvC1wQW6wVUa5putZMt6kdwCaTv8gk7sQ

Absent Signers (Pubkey):

&#x20; 3bo5YiRagwmRikuH6H1d2gkKef5nFZXE3gJeoHxJbPjy

Command (Online Submission)

Nexisnetwork@online Nexisnetwork transfer Fdri24WUGtrCXZ55nXiewAj6RM18hRHPGAjZk3o6vBut 10 \\

&#x20;   \--blockhash 7ALDjLv56a8f6sH6upAZALQKkXyjAwwENH9GomyM8Dbc \\

&#x20;   \--from 674RgFMgdqdRoVtMqSBg7mHFbrrNm1h1r721H1ZMquHL \\

&#x20;   \--signer 674RgFMgdqdRoVtMqSBg7mHFbrrNm1h1r721H1ZMquHL=3vJtnba4dKQmEAieAekC1rJnPUndBcpvqRPRMoPWqhLEMCty2SdUxt2yvC1wQW6wVUa5putZMt6kdwCaTv8gk7sQ \\

&#x20;   \--fee-payer 3bo5YiRagwmRikuH6H1d2gkKef5nFZXE3gJeoHxJbPjy \\

&#x20;   \--signer 3bo5YiRagwmRikuH6H1d2gkKef5nFZXE3gJeoHxJbPjy=ohGKvpRC46jAduwU9NW8tP91JkCT5r8Mo67Ysnid4zc76tiiV1Ho6jv3BKFSbBcr2NcPPCarmfTLSkTHsJCtdYi

Output (Online Submission)

ohGKvpRC46jAduwU9NW8tP91JkCT5r8Mo67Ysnid4zc76tiiV1Ho6jv3BKFSbBcr2NcPPCarmfTLSkTHsJCtdYi

### Buying More Time to Sign

Typically a Nexis Network transaction must be signed and accepted by the network within a number of slots from the blockhash in its `recent_blockhash` field (\~2min at the time of this writing). If your signing procedure takes longer than this, a Durable Transaction Nonce can give you the extra time you need.

&#x20;
