---
title: 'JSON RPC API'
description: 'Complete guide to interacting with the Nexis Network blockchain through JSON-RPC API'
---

import { Tabs, Tab } from 'nextra/components'
import { Callout } from 'nextra/components'

# JSON RPC API

The Nexis Network provides a JSON-RPC API that allows developers to interact with the blockchain through HTTP requests. This documentation covers the available methods, their parameters, and includes example usage.

## Network Details

### Available Networks

<CardGroup cols={2}>
  <Card title="Testnet" icon="flask">
    - RPC Endpoint: `https://evm-testnet.nexscan.io/rpc`
    - Chain ID: `22222`
    - Network Name: Nexis Network Testnet
    - Currency Symbol: NZT
    - Block Time: ~2 seconds
    - Gas Token: Nexis
  </Card>
</CardGroup>

### Network Parameters

<Properties>
  <Property name="Gas Price" type="Dynamic">
    Use `eth_gasPrice` to get current price
  </Property>
  <Property name="Block Gas Limit" type="number">
    30,000,000
  </Property>
  <Property name="Minimum Gas Price" type="number">
    1 Gwei
  </Property>
  <Property name="Consensus" type="string">
    Proof of Stake (PoS)
  </Property>
  <Property name="EVM Compatibility" type="string">
    Full Ethereum Virtual Machine compatibility
  </Property>
</Properties>

## Connection

### HTTP Connection

To connect to the Nexis Network RPC endpoint, you can use any HTTP client that supports JSON-RPC 2.0.

<Tabs items={['cURL', 'Python', 'Node.js']}>
  <Tab>
    ```bash
    curl -X POST https://evm-testnet.nexscan.io/rpc \
      -H "Content-Type: application/json" \
      --data '{
        "jsonrpc":"2.0",
        "method":"eth_blockNumber",
        "params":[],
        "id":1
      }'
    ```
  </Tab>
  <Tab>
    ```python
    from web3 import Web3

    # Connect to Nexis Network
    web3 = Web3(Web3.HTTPProvider('https://evm-testnet.nexscan.io/rpc'))

    # Check connection
    print(f"Connected: {web3.is_connected()}")
    print(f"Current block: {web3.eth.block_number}")
    ```
  </Tab>
  <Tab>
    ```javascript
    const axios = require('axios');

    async function makeRPCCall(method, params = []) {
      const response = await axios.post('https://evm-testnet.nexscan.io/rpc', {
        jsonrpc: '2.0',
        method: method,
        params: params,
        id: 1
      });
      return response.data;
    }

    // Usage example
    makeRPCCall('eth_blockNumber')
      .then(result => console.log(result))
      .catch(error => console.error(error));
    ```
  </Tab>
</Tabs>

## Available Methods

### Network State

<ResponseField name="eth_blockNumber" type="method">
  Returns the current block number.

  <Expandable title="Parameters">
    None
  </Expandable>

  <Expandable title="Returns">
    Hex string of the current block number
  </Expandable>

  <CodeGroup>
    ```json Request
    {
      "jsonrpc": "2.0",
      "method": "eth_blockNumber",
      "params": [],
      "id": 1
    }
    ```

    ```json Response
    {
      "jsonrpc": "2.0",
      "id": 1,
      "result": "0x1234" // Block number in hexadecimal
    }
    ```
  </CodeGroup>
</ResponseField>

<ResponseField name="eth_getBalance" type="method">
  Returns the balance of a given account address.

  <Expandable title="Parameters">
    1. `address`: 20-byte address to check for balance
    2. `block`: Block number in hex, or "latest", "earliest" or "pending"
  </Expandable>

  <CodeGroup>
    ```json Request
    {
      "jsonrpc": "2.0",
      "method": "eth_getBalance",
      "params": [
        "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
        "latest"
      ],
      "id": 1
    }
    ```

    ```json Response
    {
      "jsonrpc": "2.0",
      "id": 1,
      "result": "0x1234567890" // Balance in wei (hexadecimal)
    }
    ```
  </CodeGroup>
</ResponseField>

<ResponseField name="eth_gasPrice" type="method">
  Returns the current gas price in wei.

  <CodeGroup>
    ```json Request
    {
      "jsonrpc": "2.0",
      "method": "eth_gasPrice",
      "params": [],
      "id": 1
    }
    ```

    ```json Response
    {
      "jsonrpc": "2.0",
      "id": 1,
      "result": "0x4a817c800" // Gas price in wei (hexadecimal)
    }
    ```
  </CodeGroup>
</ResponseField>

### Transaction Operations

<ResponseField name="eth_sendRawTransaction" type="method">
  Submits a signed transaction to the network.

  <Expandable title="Parameters">
    1. `data`: The signed transaction data
  </Expandable>

  <Expandable title="Transaction Fields">
    - `nonce`: Number of transactions sent by the account
    - `gasPrice`: Gas price in wei
    - `gasLimit`: Maximum gas allowed
    - `to`: Recipient address
    - `value`: Amount of NEXIS to transfer
    - `data`: Contract data or empty string
    - `v, r, s`: Transaction signature values
  </Expandable>

  <CodeGroup>
    ```json Request
    {
      "jsonrpc": "2.0",
      "method": "eth_sendRawTransaction",
      "params": [
        "0xf86c0185746a528800825208947b0379b43951d4e8803c6b70f25f7c8a96bf2b1487038d7ea4c68000802ba06e16cf1bc8b8c85c53cd8c2d42c580a9bb3c3b31f32ab...."
      ],
      "id": 1
    }
    ```

    ```json Response
    {
      "jsonrpc": "2.0",
      "id": 1,
      "result": "0x..." // Transaction hash
    }
    ```
  </CodeGroup>
</ResponseField>

<ResponseField name="eth_getTransactionByHash" type="method">
  Returns transaction details by transaction hash.

  <Expandable title="Parameters">
    1. `hash`: Transaction hash
  </Expandable>

  <Expandable title="Response Fields">
    - `blockHash`: Hash of the block containing the transaction
    - `blockNumber`: Block number containing the transaction
    - `from`: Address of the sender
    - `gas`: Gas provided by the sender
    - `gasPrice`: Gas price provided by the sender in wei
    - `hash`: Transaction hash
    - `input`: Data sent along with the transaction
    - `nonce`: Number of transactions sent by the sender
    - `to`: Address of the receiver
    - `transactionIndex`: Integer of the transaction's index position in the block
    - `value`: Value transferred in wei
    - `v, r, s`: Transaction signature values
  </Expandable>

  <CodeGroup>
    ```json Request
    {
      "jsonrpc": "2.0",
      "method": "eth_getTransactionByHash",
      "params": [
        "0x88df016429689c079f3b2f6ad39fa052532c56795b733da78a91ebe6a713944b"
      ],
      "id": 1
    }
    ```

    ```json Response
    {
      "jsonrpc": "2.0",
      "id": 1,
      "result": {
        "blockHash": "0x1d59ff54b1eb26b013ce3cb5fc9dab3705b415a67127a003c3e61eb445bb8df2",
        "blockNumber": "0x5daf3b",
        "from": "0xa7d9ddbe1f17865597fbd27ec712455208b6b76d",
        "gas": "0xc350",
        "gasPrice": "0x4a817c800",
        "hash": "0x88df016429689c079f3b2f6ad39fa052532c56795b733da78a91ebe6a713944b",
        "input": "0x68656c6c6f21",
        "nonce": "0x15",
        "to": "0xf02c1c8e6114b1dbe8937a39260b5b0a374432bb",
        "transactionIndex": "0x41",
        "value": "0xf3dbb76162000",
        "v": "0x25",
        "r": "0x1b5e176d927f8e9ab405058b2d2457392da3e20f328b16ddabcebc33eaac5fea",
        "s": "0x4ba69724e8f69de52f0125ad8b3c5c2cef33019bac3249e2c0a2192766d1721c"
      }
    }
    ```
  </CodeGroup>
</ResponseField>

### Smart Contract Interaction

<ResponseField name="eth_call" type="method">
  Executes a new message call immediately without creating a transaction on the blockchain.

  <Expandable title="Parameters">
    1. `transaction`: Transaction call object
       - `from`: (optional) Address the call is made from
       - `to`: Address the call is made to
       - `gas`: (optional) Gas provided for the call
       - `gasPrice`: (optional) Gas price in wei
       - `value`: (optional) Value sent in wei
       - `data`: (optional) Hash of the method signature and encoded parameters
    2. `block`: Block number or "latest", "earliest" or "pending"
  </Expandable>

  <CodeGroup>
    ```json Request
    {
      "jsonrpc": "2.0",
      "method": "eth_call",
      "params": [
        {
          "to": "0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
          "data": "0x70a08231000000000000000000000000e16c1623c1aa7d919cd2241d8b36d9e79c1be2a2"
        },
        "latest"
      ],
      "id": 1
    }
    ```

    ```json Response
    {
      "jsonrpc": "2.0",
      "id": 1,
      "result": "0x0000000000000000000000000000000000000000000000000de0b6b3a7640000"
    }
    ```
  </CodeGroup>
</ResponseField>

## JavaScript Integration

<CodeGroup>

```javascript Web3.js
const Web3 = require('web3');
const web3 = new Web3('https://evm-testnet.nexscan.io/rpc');

// Utility function to convert wei to NEXIS
function weiToNexis(wei) {
  return web3.utils.fromWei(wei, 'ether');
}

// Utility function to convert NEXIS to wei
function nexisToWei(nexis) {
  return web3.utils.toWei(nexis.toString(), 'ether');
}

// Get network information
async function getNetworkInfo() {
  const [blockNumber, gasPrice, chainId] = await Promise.all([
    web3.eth.getBlockNumber(),
    web3.eth.getGasPrice(),
    web3.eth.getChainId()
  ]);
  
  console.log('Current block:', blockNumber);
  console.log('Gas price:', weiToNexis(gasPrice), 'NEXIS');
  console.log('Chain ID:', chainId);
}
```

```javascript Contract Interaction
// Smart contract interaction example
async function interactWithContract(contractAddress, abi) {
  const contract = new web3.eth.Contract(abi, contractAddress);
  
  // Read contract data
  async function readContract() {
    const result = await contract.methods.someMethod().call();
    console.log('Contract read result:', result);
    return result;
  }
  
  // Write to contract
  async function writeContract(from, privateKey) {
    const gasPrice = await web3.eth.getGasPrice();
    const gasEstimate = await contract.methods.someMethod()
      .estimateGas({ from: from });
      
    const tx = {
      from: from,
      to: contractAddress,
      gas: Math.round(gasEstimate * 1.1), // Add 10% buffer
      gasPrice: gasPrice,
      data: contract.methods.someMethod().encodeABI()
    };
    
    const signedTx = await web3.eth.accounts.signTransaction(tx, privateKey);
    const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
    console.log('Contract transaction successful:', receipt.transactionHash);
    return receipt;
  }
  
  return { readContract, writeContract };
}
```

```javascript Event Handling
// Event listening example
function listenToEvents(contractAddress, abi) {
  const contract = new web3.eth.Contract(abi, contractAddress);
  
  // Listen to all events
  contract.events.allEvents()
    .on('data', event => console.log('Event received:', event))
    .on('error', error => console.error('Event error:', error));
    
  // Listen to specific event
  contract.events.SpecificEvent()
    .on('data', event => console.log('Specific event received:', event))
    .on('error', error => console.error('Specific event error:', error));
}
```

</CodeGroup>

## Error Handling

<Callout type="warning">
The API returns standard JSON-RPC 2.0 errors that should be properly handled in your application.
</Callout>

<ResponseField name="Error Response Format" type="object">
  ```json
  {
    "jsonrpc": "2.0",
    "id": 1,
    "error": {
      "code": -32602,
      "message": "Invalid parameter value"
    }
  }
  ```
</ResponseField>

### Common Error Codes

<Properties>
  <Property name="-32700" type="Parse Error">
    Invalid JSON was received. Validate JSON before sending.
  </Property>
  <Property name="-32600" type="Invalid Request">
    JSON is not a valid Request object. Ensure request follows JSON-RPC 2.0 specification.
  </Property>
  <Property name="-32601" type="Method Not Found">
    Method does not exist. Check method name and available methods.
  </Property>
  <Property name="-32602" type="Invalid Params">
    Invalid method parameters. Validate parameter types and values.
  </Property>
  <Property name="-32603" type="Internal Error">
    Internal JSON-RPC error. Implement retry mechanism with exponential backoff.
  </Property>
</Properties>

## Best Practices

### Rate Limiting

<CodeGroup>
```javascript Rate Limiter
class RateLimiter {
  constructor(maxRequests, timeWindow) {
    this.maxRequests = maxRequests;
    this.timeWindow = timeWindow;
    this.requests = [];
  }
  
  async throttle() {
    const now = Date.now();
    this.requests = this.requests.filter(time => now - time < this.timeWindow);
    
    if (this.requests.length >= this.maxRequests) {
      const oldestRequest = this.requests[0];
      const waitTime = this.timeWindow - (now - oldestRequest);
      await new Promise(resolve => setTimeout(resolve, waitTime));
    }
    
    this.requests.push(now);
  }
}

// Usage
const rateLimiter = new RateLimiter(10, 1000); // 10 requests per second
```
</CodeGroup>

### Security Considerations

<CardGroup cols={2}>
  <Card title="Private Key Management" icon="key">
    Never store private keys in code. Use environment variables or a secure key management service.
  </Card>
  <Card title="Input Validation" icon="shield-check">
    Always validate addresses, amounts, and other parameters before sending transactions.
  </Card>
  <Card title="Transaction Security" icon="lock">
    Implement proper gas estimation and balance checks before sending transactions.
  </Card>
  <Card title="Network Validation" icon="network-wired">
    Verify the correct network/chain ID before performing operations.
  </Card>
</CardGroup>

<Callout type="info">
For more detailed information and updates, visit the [Nexis Network Documentation](https://docs.nexis.network).
</Callout>

