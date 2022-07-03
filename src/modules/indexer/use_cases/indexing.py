from src.external_services.bitcoind import IBitcoind
from ..databases.interface import IBlockRepository, ITransactionRepository


class Indexing():
    def __init__(
        self, client: IBitcoind,
        block_repository: IBlockRepository,
        transaction_repository: ITransactionRepository,
    ):
        self.client = client
        self.block_repo = block_repository
        self.transaction_repo = transaction_repository

    def execute(self, block_height: int):
        self._block_handler(block_height)

    def _txn_handler(self, block_info, txid):
        txn = self.client.get_raw_transaction(
            txid=txid,
            block_hash=block_info['hash'],
        )['result']

        self.transaction_repo.create(**{
            'txid': txn['txid'],
            'hash': txn['hash'],
            'block_hash': txn['blockhash'],
            'time': txn['time'],
            'confirmations': txn['confirmations'],
            'hex': txn['hex'],
            'vin': txn['vin'],
            'vout': txn['vout'],
        })

    def _block_handler(self, height):
        response = self.client.get_block_hash(height)
        block_hash = response['result']
        block_info = self.client.get_block(block_hash)['result']

        self.block_repo.create(**{
            'hash': block_info['hash'],
            'height': block_info['height'],
            'confirmations': block_info['confirmations'],
            'merkle_root': block_info['merkleroot'],
            'time': block_info['time'],
            'nonce': block_info['nonce'],
            'difficulty': block_info['difficulty'],
            'previous_block_hash': block_info['previousblockhash'],
            'next_block_hash': block_info['nextblockhash'],
        })

        for txid in block_info['tx']:
            self._txn_handler(block_info, txid)
