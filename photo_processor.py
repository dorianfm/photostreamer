#!/bin/env python3
import os
import re
import cv2
import numpy

from pathlib import Path

target_width = 300
target_height = 400;


def source_dir():
    return os.path.dirname(os.path.realpath(__file__))+'/source_images/'

def target_dir():
    return os.path.dirname(os.path.realpath(__file__))+'/processed_images/'

def target_path(source_path, offset):
    path = append_id(source_path, offset)
    path = path.replace(source_dir(), target_dir())
    return path

def append_id(filename, id):
    p = Path(filename)
    r = path.with_name(f"{p.stem}-{id}{p.suffix}").as_posix()
    return r;

def is_processed(path):
    return os.path.exists(source_path+'.processed')

def mark_processed(path):
    Path(path+'.processed').touch()

def find_faces(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml');
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return faces

def process_faces(faces, image, source_path):
    offset = 1
    for face in faces:
        process_face(face, image, source_path, offset)
        offset += 1

def process_face(face, source_image, source_path, offset):
    print(face)
    # widen box
    (x, y, w, h) = calculate_crop(source_image, face)
    print('%d %d %d %d' % (x, y, w, h))
    # crop
    face_image = source_image[y:y+h, x:x+w].copy()
    # scale
    target = target_path(source_path, offset)
    save_target(face_image, target)
    # mark as proccessed
    # mark_processed(source_path)

def save_target(image, file_path):
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path),0o775)
    if image.size != 0:
        print('save => '+ file_path)
        cv2.imwrite(file_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

def calculate_crop(image, face):
    (x, y, w, h) = face
    height, width = image.shape[:2]
    center_x = int(x + w/2)
    center_y = int(y + h/2)

    # how much of the image is a face?

    # at the moment just return a crop of the correct size for the display centered on the face
    # to avoid overthinking shit
    return (int(center_x - target_width/2), int(center_y - target_width/2), target_width, target_height);

def process_image(source_path):
    print(source_path)
    image=cv2.imread(source_path)
    print(image.shape); # width, height, channels
    # find face
    faces = find_faces(image)
    process_faces(faces, image, source_path)

for path in Path(source_dir()).rglob('*.jpg'):
    source_path = path.absolute().as_posix()
    if not is_processed(source_path):
        process_image(source_path)
