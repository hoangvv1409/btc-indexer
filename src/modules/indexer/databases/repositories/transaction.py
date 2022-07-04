# from typing import Tuple, List, Any

from ..models import TransactionSchema
from ..interface import ITransactionRepository


class TransactionRepository(ITransactionRepository):
    def __init__(self, session):
        self.session = session
        self.model = TransactionSchema
