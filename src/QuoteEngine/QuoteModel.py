class QuoteModel:
    """ A Quote model expects a body and an author both of
    type str().   A str and repr override is included to output
    the following string example:

    "Cubs win!" - Mike

    QuoteModel(body=”Cubs win!”, author="Mike")
    """

    body = None
    author = None

    def __init__(self, body: str, author: str):
        self.body = str(body.strip('" '))
        self.author = str(author.strip('" '))

    def __str__(self):
        return f'"{self.body}" - {self.author}'

    def __repr__(self):
        return f'QuoteModel(body=”{self.body}”, author="{self.author}")'
