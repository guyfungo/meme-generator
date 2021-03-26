# Meme Generator Project (Udacity - Intermediate Python Nano Degree)

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)

## About <a name = "about"></a>

The purpose of this project is to generate meme images given a body, author
and image as input (or provided statically in some cases).

## Getting Started <a name = "getting_started"></a>

### Prerequisites

Python 3.8 and the following libraries installed:

```
Flask==1.1.2
pandas==1.2.3
Pillow==8.1.2
python-docx==0.8.10
requests==2.25.1

(see requirements.txt or use pip for install)

ex: pip install -r requirements.txt

```

Further instead of using a library, this project illustrates the use of subprocesses. 
Therefore the xpdf CLI packages must be installed and path set in PDFIngestor.py.  The
xpdf CLI package has been included in the ./xpdf directory for your convenience.



## Usage <a name = "usage"></a>

This project is designed to be used in multiple ways with either meme.py or app.py.   If meme.py is run by itself without any arguments it will generate a random meme image with a pairing of a quote/author from data found in the _data directory.  Optionally it can be run with the following arguments:
 
    --body     (a string quote body)
    --author   (a string quote author)
    --path     (an image path for input)

    ex: python3 meme.py --body "Bears Beats BSG" --author Jim --path "./tmp/myimage.jpg"

    All images created from this this application are places in the ./tmp folder by default. 

 If app.py is run, it will use functions within the meme.py to generate the meme but stands up a Flask web server to automatically generate a meme or allow user input to generate a custom meme.  The web pages being served are located in the ./templates directory.

Further, both meme.py and app.py make use of two packages.   The QuoteEngine package includes the ability to ingest quote/author pairs from CSV, PDF, DOCX, or TEXT and further process those pairs into a QuoteModel which expects the pair as an argument. As multiple file types are processed in this package, it depends on external libraries include pandas, and python-docx.  Further as noted in the prequisites xpdf command line utlity most be installed as well to be made use of via python subprocesses.

The MemeGenerator package takes QuoteModel objects and images as input to properly size the image and place the quote and author onto the image before outputting the new meme in an output directory.  

### Project File Hierachy

_data
    DogQuotes   
       DogQuotesCSV.csv
       DogQuotesDOCX.docx
       DogQuotesPDF.pdf
       DOGQuotesTXT.txt
    photos
       dogs
           xander_1.jpg
           xander_2.jpg
           xander_3.jpg
           xander_4.jpg
MemeGenerator
    __init__.py
    MemeEngine.py
QuoteEngine
    __init__.py
    CSVIngestor.py
    DocxIngestor.py
    Ingestor.py
    IngestorInterface.py
    PDFIngestor.py
    QuoteModel.py
    TextIngestor.py
static
templates
    base.html
    meme.html
    meme_form.html
tmp
xpdf
app.py
meme.py
README.md
requirements.txt


### Contact

Mike @ htmlforms@gmail.com 