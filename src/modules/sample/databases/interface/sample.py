from abc import ABC, abstractmethod
from typing import Tuple, List, Any
from src.databases.repo_base import CRUD

from ..models import SampleSchema


class ISampleRepository(ABC, CRUD[SampleSchema]):
    @abstractmethod
    def get_full_sample(
        self, page: int = None, page_size: int = None,
        **conditions: Any,
    ) -> Tuple[int, int, List[SampleSchema]]:
        pass
