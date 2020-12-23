import os
import re
from pathlib import Path
from PIL import Image

def source_dir():
    return os.path.dirname(os.path.realpath(__file__))+'/source_images/'

def processed_dir():
    return os.path.dirname(os.path.realpath(__file__))+'/processed_images/'

def find_image_files(directory):
    return find_files(directory,('*.jpg','*.jpeg','*.JPG', '*.PNG','*.png'))

def find_files(directory, types):
    files = []
    for glob in types:
        for path in Path(directory).rglob(glob):
            files.append(path.absolute().as_posix())
    return files

def image_selection(offset, length=100):
    paths = find_image_files(processed_dir())
    return (paths[offset:length], len(paths))

def web_local_path(path):
    return path.replace(processed_dir(),'');

def image_cover(img, tw, th):
    w, h = img.size
    if w == tw and h == th:
        return img
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
