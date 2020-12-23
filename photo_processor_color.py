#!/home/pi/photostreamer/bin/python
import os
import re
import cv2
import numpy as np

from PIL import Image
from pathlib import Path

import photostreamer

target_width = 600
target_height = 448;

def target_path(source_path, offset):
    if offset > 0:
        source_path = append_id(source_path, offset)
    source_path = source_path.replace(photostreamer.source_dir(), photostreamer.processed_dir())
    return source_path

def append_id(filename, id):
    p = Path(filename)
    r = p.with_name(f"{p.stem}-{id}{p.suffix}").as_posix()
    return r;

def process_image(source_path):
    if photostreamer.is_processed(source_path):
        return
    print(source_path)
    img = Image.open(source_path)
    img = photostreamer.image_cover(img, target_width, target_height)
    save_target(img, target_path(source_path, 0))
    photostreamer.mark_processed(source_path)
    os.remove(source_path)

def save_target(img, file_path):
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path),0o775)
    print(' => ' + file_path)
    img.save(file_path)


def process_images(directory):
    image_files = photostreamer.find_image_files(directory)
    for source_path in image_files:
        if not photostreamer.is_processed(source_path):
            process_image(source_path)

def find_image_files(directory):
    return find_files(directory,('*.jpg','*.jpeg','*.JPG', '*.PNG','*.png'))

process_images(photostreamer.source_dir())
