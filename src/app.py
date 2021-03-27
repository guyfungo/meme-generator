import random
import os
import requests

from uuid import uuid4
from flask import Flask, render_template, abort, request
from QuoteEngine import Ingestor
from MemeGenerator import MemeEngine

app = Flask(__name__, static_url_path='/static')
meme = MemeEngine('./static')


def setup():
    """ Load all resources, select random images
    and quotes to generate memes as a default action """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []

    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    path = path[1:]
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme
        3 Inputs expected from the form.  Body, Author and
        Image_Url the latter of which will be saved
        locally while the make_meme function is called
        then cleaned up later.
    """
    path = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    r = requests.get(path)

    if '.png' in path.lower():
        ext = '.png'
    elif 'jpg' in path.lower():
        ext = '.jpg'
    elif 'jpeg' in path.lower():
        ext = '.jpeg'

    print(path)

    tmp = f'./tmp/{uuid4()}{ext}'
    img = open(tmp, 'wb').write(r.content)
    path = meme.make_meme(tmp, body, author)
    new_path = path[1:]
    os.remove(tmp)

    return render_template('meme.html', path=new_path)


if __name__ == "__main__":
    app.run()
