## 1. Setup and run full node

[https://github.com/bitcoin/bitcoin/blob/master/doc](https://github.com/bitcoin/bitcoin/blob/master/doc)

## 2. Iterate through the entire block chain using RPC

[https://developer.bitcoin.org/reference/rpc/index.html](https://developer.bitcoin.org/reference/rpc/index.html)

1. [getblockhash](https://developer.bitcoin.org/reference/rpc/getblockhash.html) 1
2. [getblock](https://developer.bitcoin.org/reference/rpc/getblock.html) (input of #1 here)
3. Iterate through each transaction with [getrawtransaction](https://developer.bitcoin.org/reference/rpc/getrawtransaction.html) (input of tx field here)
4. After getting all transactions, call [getblockhash](https://developer.bitcoin.org/reference/rpc/getblockhash.html) 2 (or goto nextblockhash in block)
