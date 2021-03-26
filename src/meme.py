import os
import random
import sys
import argparse
import PIL

from QuoteEngine import Ingestor, QuoteModel
from MemeGenerator import MemeEngine

"""Provides methods to generate a random captioned image.
    Also provides CLI options with three optional arguments:
    A string quote body, A string quote author, An image path.

    If any argument is not defined, a random selection is used.

    The program returns a path to a generated image.
    """


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """

    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]
        print(img)

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                                    description="Meme generator CLI Arguments")
    parser.add_argument('--body', type=str)
    parser.add_argument('--author', type=str)
    parser.add_argument('--path', type=str)

    args = parser.parse_args()
    cli_path = None

    if args.path:
        cli_path = []
        cli_path.append(args.path)

    print(generate_meme(cli_path, args.body, args.author))
