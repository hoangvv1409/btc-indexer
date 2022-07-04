from abc import ABC
# from typing import Tuple, List, Any
from src.databases.repo_base import CRUD

from ..models import TransactionSchema


class ITransactionRepository(ABC, CRUD[TransactionSchema]):
    pass
