#!/bin/env python3
import os
import re
import cv2

from pathlib import Path

def source_dir():
    return os.path.dirname(os.path.realpath(__file__))+'/source_images/'

def target_dir():
    return os.path.dirname(os.path.realpath(__file__))+'/processed_image/'

def target_path(source_path):
    return source_path.replace(source_dir(), target_dir())

def save_target(image, source_path):
    # save as bitmap image not jpeg, to reduce noise.
    pass

def is_processed(path):
    return os.path.exists(source_path+'.processed')

def mark_processed(path):
    Path(path+'.processed').touch()

def find_faces(image)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return faces

def process_faces(faces, source_path)
    for face in faces:
        process_face(face, source_path)

def process_face(face, source_path)


def process_image(source_path):
    print(source_path)
    image=cv2.imread(source_path)
    print(image.shape);
    # find face
    faces = find_faces(image)
    process_faces(faces, source_path)
    # widen box
    # crop
    # convert to grayscale
    # scale
    # dither
    # save
    save(image, source_path)
    # mark as proccessed
    # mark_processed(source_path)


for path in Path(source_dir()).rglob('*.jpg'):
    source_path = path.absolute().as_posix()
    if not is_processed(source_path):
        process_image(source_path)
