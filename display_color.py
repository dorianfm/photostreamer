#!/home/pi/photostreamer/bin/python

import os
import re
import random

from pathlib import Path
from time import sleep
from PIL import Image
from inky.inky_uc8159 import Inky

import photostreamer

inky = Inky()
tw = 600
th = 448

def show_image(img_path):
    print (img_path)
    img = photostreamer.image_cover(Image.open(img_path), tw, th)
    saturation = 0.5

    inky.set_image(img, saturation=saturation)
    inky.show()

def image_cover(img, tw, th):
    w, h = img.size
    nw = tw
    nh = int((tw/w)*h)
    if (nh < th):
        nh = th
        nw = int((th/h)*w)

    img = img.resize((nw, nh), resample = Image.LANCZOS)
    x = 0
    y = 0
    if (nw > tw):
        x = int(nw-tw/2)
    if (nh > th):
        y = int(nh-th/2)

    box = (x,y , x+tw, y+th)
    box = (0, 0, 600, 448)
    return img.crop(box)

def main():
    images = photostreamer.find_image_files(photostreamer.processed_dir())
    random.shuffle(images)
    for source_path in images:
        show_image(source_path)
        sleep(600)
    main();

main();

