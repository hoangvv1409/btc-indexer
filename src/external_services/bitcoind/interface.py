from typing import Dict
from abc import ABC, abstractmethod


class IBitcoind(ABC):
    @abstractmethod
    def get_block_hash(self, block_height: int) -> str:
        pass

    @abstractmethod
    def get_block(self, block_hash: str) -> Dict:
        pass

    @abstractmethod
    def get_raw_transaction(self, txid: str, block_hash: str) -> Dict:
        pass
