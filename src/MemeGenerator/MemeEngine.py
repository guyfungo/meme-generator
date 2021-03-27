import os
import random
from typing import List
from PIL import Image, ImageDraw, ImageFont
from uuid import uuid4


class MemeEngine:
    """The Meme Engine Module is responsible for
    manipulating and drawing text onto images """

    def __init__(self, output_path: str):
        self.output_path = output_path
        pass

    def make_meme(self, img, body: str, author: str, width=500):
        self.img = img
        self.body = body
        self.author = author
        self.width = int(width)

        try:
            im = Image.open(img)
            size = self.width, self.width
            im.thumbnail(size, Image.ANTIALIAS)

            # Because the image may not be 500px find the actual w+h
            # to be used later in the random location to draw text
            im_width, im_height = im.size

            # randomize location (within constraints) .5w, .5h
            r_width = random.randint(0, im_width / 2)
            r_height = random.randint(0, im_height / 2)

            draw = ImageDraw.Draw(im)
            body_font = ImageFont.truetype("./fonts/impact.ttf", size=22)
            author_font = ImageFont.truetype("./fonts/impact.ttf", size=18)
            draw.text((r_width, r_height),
                      self.body, font=body_font, fill='white')
            draw.text((r_width, r_height+36),
                      self.author, font=author_font, fill='white')

            file_name = f'{self.output_path}/{uuid4()}.jpg'

            try:
                im.save(file_name)
                return file_name
            except:
                print('Unable to create Image: Output Path Invalid')
                pass

        except:
            print('Unable to open Image: Path Invalid')
