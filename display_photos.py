#!/home/dorian/bwframe/bin/python

import os
import re
from pathlib import Path

from PIL import Image
from inky import InkyWHAT
import random
from time import sleep
import photostreamer

inky_display = InkyWHAT('black')
inky_display.set_border(inky_display.WHITE)

def show_image(img_file):
    print('show => '+img_file)
    img = Image.open(img_file)
    w, h = img.size

    img = img.rotate(90, expand=True)

    w, h = img.size

    h_new = 300
    w_new = int((float(w) / h) * h_new)
    w_cropped = 400

    img = img.resize((w_new, h_new), resample=Image.LANCZOS)

    x0 = (w_new - w_cropped) / 2
    x1 = x0 + w_cropped
    y0 = 0
    y1 = h_new

    # Crop image
    cropped_img = img.crop((x0, y0, x1, y1)).convert("LA")

    # Convert the image to use a white / black colour palette
    pal_img = Image.new("P", (1, 1))
    pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 252)

    bw_img = cropped_img.convert("RGB").quantize(palette=pal_img)
    # Display the final image on Inky wHAT
    inky_display.set_image(bw_img)
    inky_display.show()
    img.close()
    cropped_img.close()
    pal_img.close()
    bw_img.close()


def main():
    images = photostreamer.find_image_files(photostreamer.processed_dir())
    random.shuffle(images)
    for source_path in images:
        show_image(source_path)
        sleep(600)
    main();

main();

