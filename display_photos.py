#!/home/pi/photostreamer/bin/python

from PIL import Image
from inky import InkyWHAT
import os
import re
from pathlib import Path
from time import sleep


def source_dir():
    return os.path.dirname(os.path.realpath(__file__))+'/processed_images/'
    sleep(5)

def show_image(img_file):
    print('show => '+img_file)

    inky_display = InkyWHAT('black')
    inky_display.set_border(inky_display.WHITE)


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
    img = img.crop((x0, y0, x1, y1))

    # Convert the image to use a white / black colour palette
    pal_img = Image.new("P", (1, 1))
    pal_img.putpalette((255, 255, 255, 0, 0, 0, 255, 0, 0) + (0, 0, 0) * 252)

    img = img.convert("RGB").quantize(palette=pal_img)

    # Display the final image on Inky wHAT
    inky_display.set_image(img)
    inky_display.show()
    img.close()

def find_image_files(directory):
    return find_files(directory,('*.jpg','*.jpeg','*.JPG', '*.PNG','*.png'))

def find_files(directory, types):
    files = []
    for glob in types:
        for path in Path(directory).rglob(glob):
            files.append(path.absolute().as_posix())
    return files

def main():
    for source_path in find_image_files(source_dir()):
        show_image(source_path)
        sleep(1)
    main();

main();

