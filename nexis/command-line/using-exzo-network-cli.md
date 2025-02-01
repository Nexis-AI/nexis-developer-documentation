# Using Nexis Network CLI

## Using Nexis Network CLI

Before running any Nexis Network CLI commands, let's go over some conventions that you will see across all commands. First, the Nexis Network CLI is actually a collection of different commands for each action you might want to take. You can view the list of all possible commands by running:

```
Nexis --help
```

To zoom in on how to use a particular command, run:

```
Nexis <COMMAND> --help
```

where you replace the text `<COMMAND>` with the name of the command you want to learn more about.

The command's usage message will typically contain words such as `<AMOUNT>`, `<ACCOUNT_ADDRESS>` or `<KEYPAIR>`. Each word is a placeholder for the _type_ of text you can execute the command with. For example, you can replace `<AMOUNT>` with a number such as `42` or `100.42`. You can replace `<ACCOUNT_ADDRESS>` with the base58 encoding of your public key, such as `9grmKMwTiZwUHSExjtbFzHLPTdWoXgcg1bZkhvwTrTww`.

### Keypair conventions

Many commands using the CLI tools require a value for a `<KEYPAIR>`. The value you should use for the keypair depend on what type of command line wallet you created.

For example, the way to display any wallet's address (also known as the keypair's pubkey), the CLI help document shows:

```
Nexis-keygen pubkey <KEYPAIR>
```

Below, we show how to resolve what you should put in `<KEYPAIR>` depending on your wallet type.

**Paper Wallet**

In a paper wallet, the keypair is securely derived from the seed words and optional passphrase you entered when the wallet was create. To use a paper wallet keypair anywhere the `<KEYPAIR>` text is shown in examples or help documents, enter the word `ASK` and the program will prompt you to enter your seed words when you run the command.

To display the wallet address of a Paper Wallet:

```
Nexis-keygen pubkey ASK
```

**File System Wallet**

With a file system wallet, the keypair is stored in a file on your computer. Replace `<KEYPAIR>` with the complete file path to the keypair file.

For example, if the file system keypair file location is `/home/Nexis/my_wallet.json`, to display the address, do:

Copy

```
Nexis-keygen pubkey /home/Nexis/my_wallet.json
```
