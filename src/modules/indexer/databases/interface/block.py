from abc import ABC
# from typing import Tuple, List, Any
from src.databases.repo_base import CRUD

from ..models import BlockSchema


class IBlockRepository(ABC, CRUD[BlockSchema]):
    pass
