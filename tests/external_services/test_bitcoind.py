import os
import pytest

from src.external_services.bitcoind import (
    Bitcoind, BlockHeightOutOfRange, BlockNotFound,
    TransactionNotFound,
)

client = Bitcoind(
    username=os.getenv('RPC_USERNAME'),
    password=os.getenv('RPC_PASSWORD'),
)


class TestMoralis:
    def test_get_block_hash(self):
        height = 1
        response = client.get_block_hash(height)

        assert response['error'] is None
        assert response['id'] is None
        assert isinstance(response['result'], str)

    def test_get_block_hash_with_invalid_height(self):
        height = -1
        with pytest.raises(BlockHeightOutOfRange):
            client.get_block_hash(height)

    def test_get_block_with_valid_block_hash(self):
        block_hash =\
            '00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048'
        response = client.get_block(block_hash)

        assert response['error'] is None
        assert response['id'] is None
        assert response['result']['hash'] == block_hash
        assert response['result']['height'] == 1

    def test_get_block_with_non_exist_block_hash(self):
        invalid_block_hash =\
            '00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18efa01b'

        with pytest.raises(BlockNotFound):
            client.get_block(invalid_block_hash)

    def test_get_raw_transaction(self):
        block_hash =\
            '00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048'
        txid = \
            '0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098'
        response = client.get_raw_transaction(txid, block_hash)

        assert response['error'] is None
        assert response['id'] is None
        assert response['result']['txid'] == txid
        assert response['result']['blockhash'] == block_hash

    def test_get_raw_transaction_with_invalid_txid(self):
        block_hash =\
            '00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048'
        invalid_txid = \
            '0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512097'

        with pytest.raises(TransactionNotFound):
            client.get_raw_transaction(invalid_txid, block_hash)
