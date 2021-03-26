from typing import List
from abc import ABC, abstractmethod
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    allowed_ext = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        ext = path.split('.')[-1]
        return ext in cls.allowed_ext

    @classmethod
    @abstractmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        pass











