# Manage Stake Accounts

## Manage Stake Accounts

If you want to delegate stake to many different validators, you will need to create a separate stake account for each. If you follow the convention of creating the first stake account at seed "0", the second at "1", the third at "2", and so on, then the `Nexisnetwork-stake-accounts` tool will allow you to operate on all accounts with single invocations. You can use it to sum up the balances of all accounts, move accounts to a new wallet, or set new authorities.

### Usage

#### Create a stake account

Create and fund a derived stake account at the stake authority public key:

Nexisnetwork-stake-accounts new \<FUNDING\_KEYPAIR> \<BASE\_KEYPAIR> \<AMOUNT> \\

&#x20;   \--stake-authority \<PUBKEY> --withdraw-authority \<PUBKEY> \\

&#x20;   \--fee-payer \<KEYPAIR>

#### Count accounts

Count the number of derived accounts:

Nexisnetwork-stake-accounts count \<BASE\_PUBKEY>

#### Get stake account balances

Sum the balance of derived stake accounts:

Nexisnetwork-stake-accounts balance \<BASE\_PUBKEY> --num-accounts \<NUMBER>

#### Get stake account addresses

List the address of each stake account derived from the given public key:

Nexisnetwork-stake-accounts addresses \<BASE\_PUBKEY> --num-accounts \<NUMBER>

#### Set new authorities

Set new authorities on each derived stake account:

Nexisnetwork-stake-accounts authorize \<BASE\_PUBKEY> \\

&#x20;   \--stake-authority \<KEYPAIR> --withdraw-authority \<KEYPAIR> \\

&#x20;   \--new-stake-authority \<PUBKEY> --new-withdraw-authority \<PUBKEY> \\

&#x20;   \--num-accounts \<NUMBER> --fee-payer \<KEYPAIR>

#### Relocate stake accounts

Relocate stake accounts:

Nexisnetwork-stake-accounts rebase \<BASE\_PUBKEY> \<NEW\_BASE\_KEYPAIR> \\

&#x20;   \--stake-authority \<KEYPAIR> --num-accounts \<NUMBER> \\

&#x20;   \--fee-payer \<KEYPAIR>

To atomically rebase and authorize each stake account, use the 'move' command:

Nexisnetwork-stake-accounts move \<BASE\_PUBKEY> \<NEW\_BASE\_KEYPAIR> \\

&#x20;   \--stake-authority \<KEYPAIR> --withdraw-authority \<KEYPAIR> \\

&#x20;   \--new-stake-authority \<PUBKEY> --new-withdraw-authority \<PUBKEY> \\

&#x20;   \--num-accounts \<NUMBER> --fee-payer \<KEYPAIR>
