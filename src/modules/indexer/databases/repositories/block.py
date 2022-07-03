# from typing import Tuple, List, Any

from ..models import BlockSchema
from ..interface import IBlockRepository


class BlockRepository(IBlockRepository):
    def __init__(self, session):
        self.session = session
        self.model = BlockSchema
