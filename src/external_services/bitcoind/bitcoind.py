import json
import requests

from typing import Dict
from requests.auth import HTTPBasicAuth

from .interface import IBitcoind
from ..base import BaseClient


class BlockHeightOutOfRange(Exception):
    pass


class BlockNotFound(Exception):
    pass


class TransactionNotFound(Exception):
    pass


class Bitcoind(BaseClient, IBitcoind):
    def __init__(
        self, username: str, password: str,
        base_url: str = 'http://localhost:8332',
    ):
        self.base_url = base_url
        self.auth = HTTPBasicAuth(username, password)
        self.headers = {
            'Content-Type': 'application/json',
        }

    def _get_request_payload(self, url: str, payload: Dict = None):
        return {
            'headers': self.headers,
            'auth': self.auth,
            'url': url,
            'data': payload,
        }

    def get_block_hash(self, block_height: int) -> str:
        payload = json.dumps({
            'method': 'getblockhash',
            'params': [block_height],
        })

        response = self.response_handler(
            requests.post,
            self._get_request_payload(self.base_url, payload)
        )

        if response.status_code == 500:
            error = response.json()['error']
            if error['code'] == -8:
                raise BlockHeightOutOfRange(error['message'])

        return response.json()

    def get_block(self, block_hash: str) -> Dict:
        payload = json.dumps({
            'method': 'getblock',
            'params': [block_hash],
        })

        response = self.response_handler(
            requests.post,
            self._get_request_payload(self.base_url, payload)
        )

        if response.status_code == 500:
            error = response.json()['error']
            if error['code'] == -5:
                raise BlockNotFound(error['message'])

        return response.json()

    def get_raw_transaction(
        self, txid: str, block_hash: str
    ) -> Dict:
        payload = json.dumps({
            'method': 'getrawtransaction',
            'params': [txid, True, block_hash],
        })

        response = self.response_handler(
            requests.post,
            self._get_request_payload(self.base_url, payload)
        )

        if response.status_code == 500:
            error = response.json()['error']
            if error['code'] == -5:
                raise TransactionNotFound(error['message'])

        return response.json()
