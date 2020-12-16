import os
import re
from pathlib import Path

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
