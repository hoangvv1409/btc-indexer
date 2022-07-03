import os
import concurrent.futures
from src.external_services.bitcoind import Bitcoind

btc = Bitcoind(
    username=os.getenv('RPC_USERNAME'),
    password=os.getenv('RPC_PASSWORD'),
)


def txn_handler(block_hash, height, txid):
    _ = btc.get_raw_transaction(
        txid=txid,
        block_hash=block_hash,
    )
    print(f'{height} | {txid}')


height = 1
while True:
    response = btc.get_block_hash(height)
    block_hash = response['result']
    block_info = btc.get_block(block_hash)
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for txid in block_info['result']['tx']:
            executor.submit(txn_handler, block_hash, height, txid)
    height += 1
