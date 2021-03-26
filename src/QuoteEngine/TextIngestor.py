from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """Provides a method for ingesting txt files and
        returns a list of QuoteModel
        """

    allowed_ext = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception.')

        quotes = []

        with open(path, 'r') as file:
            for line in file:
                split = line.split(' - ')
                if len(split) == 2:
                    quotes.append(QuoteModel(split[0], split[1]))

        return quotes
