# Send and Receive Tokens

## Send and Receive Tokens

This page decribes how to receive and send NZT tokens using the command line tools with a command line wallet such as a paper wallet, and a file system wallet. Before you begin, make sure you have created a wallet and have access to its address (pubkey) and the signing keypair. Check out our conventions for entering keypairs for different wallet types.

### Testing your Wallet

Before sharing your public key with others, you may want to first ensure the key is valid and that you indeed hold the corresponding private key.

In this example, we will create a second wallet in addition to your first wallet, and then transfer some tokens to it. This will confirm that you can send and receive tokens on your wallet type of choice.

This test example uses our Developer Testnet, called devnet. Tokens issued on devnet have **no** value, so don't worry if you lose them.



**Airdrop some tokens to get started**

First, _airdrop_ yourself some play tokens on the devnet.

```
Nexis airdrop 10 <RECIPIENT_ACCOUNT_ADDRESS> --url https://rpc-test-1.Nexis.network
```

where you replace the text `<RECIPIENT_ACCOUNT_ADDRESS>` with your base58-encoded public key/wallet address.



**Check your balance**

Confirm the airdrop was successful by checking the account's balance. It should output `10 NZT`:

```
Nexis balance <ACCOUNT_ADDRESS> --url https://rpc-test-1.Nexis.network
```



**Create a second wallet address**

We will need a new address to receive our tokens. Create a second keypair and record its pubkey:

```
Nexis -keygen new --no-passphrase --no-outfile
```

The output will contain the address after the text `pubkey:`.&#x20;



Copy the address. We will use it in the next step.

```
pubkey: GKvqsuNcnwWqPzzuhLmGi4rzzh55FhJtGizkhHaEJqiV
```

You can also create a second (or more) wallet of any type: paper, file system.



**Transfer tokens from your first wallet to the second address**

Next, prove that you own the airdropped tokens by transferring them. The Nexis Network cluster will only accept the transfer if you sign the transaction with the private keypair corresponding to the sender's public key in the transaction.

```
Nexis transfer --from <KEYPAIR> <RECIPIENT_ACCOUNT_ADDRESS> 5 --url https://rpc-test-1.Nexis.network --fee-payer <KEYPAIR>
```

where you replace `<KEYPAIR>` with the path to a keypair in your first wallet, and replace `<RECIPIENT_ACCOUNT_ADDRESS>` with the address of your second wallet.

Confirm the updated balances with `Nexis balance`:

Nexisnetwork balance \<ACCOUNT\_ADDRESS> --url  https://rpc-test-1.Nexis.network

where `<ACCOUNT_ADDRESS>` is either the public key from your keypair or the recipient's public key.



**Full example of test transfer**

```
$ Nexis --keygen new --outfile my_Nexis_wallet.json   # Creating my first wallet, a file system wallet
Generating a new keypair
For added security, enter a passphrase (empty for no passphrase):
Wrote new keypair to my_Nexis_wallet.json
==========================================================================
pubkey: DYw8jCTfwHNRJhhmFcbXvVDTqWMEVFBX6ZKUmG5CNSKK                          # Here is the address of the first wallet
==========================================================================
Save this seed phrase to recover your new keypair:
width enhance concert vacant ketchup eternal spy craft spy guard tag punch    # If this was a real wallet, never share these words on the internet like this!
==========================================================================
```

&#x20;

```
$ Nexis airdrop 10 DYw8jCTfwHNRJhhmFcbXvVDTqWMEVFBX6ZKUmG5CNSKK --url https://rpc-test-1.Nexis.network  # Airdropping 10 NZT to my wallet's address/pubkey
Requesting airdrop of 10 NZT from https://rpc-test-1.Nexis.network
10 NZT
```

&#x20;

```
$ Nexis balance DYw8jCTfwHNRJhhmFcbXvVDTqWMEVFBX6ZKUmG5CNSKK --url https://rpc-test-1.Nexis.network # Check the address's balance
10 NZT
```

&#x20;

```
$ Nexis-keygen new --no-outfile  # Creating a second wallet, a paper wallet
Generating a new keypair
For added security, enter a passphrase (empty for no passphrase):
====================================================================
pubkey: 7S3P4HxJpyyigGzodYwHtCxZyUQe9JiBMHyRWXArAaKv                   # Here is the address of the second, paper, wallet.
====================================================================
Save this seed phrase to recover your new keypair:
clump panic cousin hurt coast charge engage fall eager urge win love   # If this was a real wallet, never share these words on the internet like this!
====================================================================
```

&#x20;

```
$ Nexis transfer --from my_Nexis_wallet.json 7S3P4HxJpyyigGzodYwHtCxZyUQe9JiBMHyRWXArAaKv 5 --url https://rpc-test-1.Nexis.network --fee-payer my_Nexisnetwork_wallet.json  # Transferring tokens to the public address of the paper wallet

3gmXvykAd1nCQQ7MjosaHLf69Xyaqyq1qw2eu1mgPyYXd5G4v1rihhg1CiRw35b9fHzcftGKKEu4mbUeXY2pEX2z  # This is the transaction signature
```

&#x20;

```
$ Nexis balance DYw8jCTfwHNRJhhmFcbXvVDTqWMEVFBX6ZKUmG5CNSKK --url https://rpc-test-1.Nexis.network

4.999995 NZT  # The sending account has slightly less than 5 NZT remaining due to the 0.000005 NZT transaction fee payment
```

&#x20;

```
$ Nexis balance 7S3P4HxJpyyigGzodYwHtCxZyUQe9JiBMHyRWXArAaKv --url https://rpc-test-1.Nexis.network
5 NZT  # The second wallet has now received the 5 NZT transfer from the first wallet
```

&#x20;

### Receive Tokens

To receive tokens, you will need an address for others to send tokens to. In Nexis Network, the wallet address is the public key of a keypair. There are a variety of techniques for generating keypairs. The method you choose will depend on how you choose to store keypairs. Keypairs are stored in wallets. Before receiving tokens, you will need to create a wallet. Once completed, you should have a public key for each keypair you generated. The public key is a long string of base58 characters. Its length varies from 32 to 44 characters.

### Send Tokens

If you already hold NZT and want to send tokens to someone, you will need a path to your keypair, their base58-encoded public key, and a number of tokens to transfer. Once you have that collected, you can transfer tokens with the `Nexis transfer` command:

```
Nexis transfer --from <KEYPAIR> <RECIPIENT_ACCOUNT_ADDRESS> <AMOUNT> --fee-payer <KEYPAIR>
```

Confirm the updated balances with `Nexisnetwork balance`:

Copy

```
Nexis balance <ACCOUNT_ADDRESS>
```
