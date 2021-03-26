import subprocess
import os
from typing import List
from uuid import uuid4

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Provides a method for ingesting PDF files and
        returns a list of QuoteModel
        """

    allowed_ext = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest exception.')

        quotes = []        
        tmp_file = f'./tmp/{uuid4()}.txt'
        cmd = r"""{} -layout "{}" "{}" """.format(
            r'./xpdf/bin64/pdftotext.exe', path, tmp_file)
        result_code = subprocess.call(cmd, shell=True)

        if result_code == 0:
            with open(tmp_file, 'r') as file:
                for line in file:
                    split = line.split(' - ')
                    if len(split) == 2:
                        quotes.append(QuoteModel(split[0], split[1]))

        return quotes
