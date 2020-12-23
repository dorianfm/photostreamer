#!/home/pi/photostreamer/bin/python
import os
import re
import cv2
import numpy
import photostreamer

from pathlib import Path

target_width = 300
target_height = 400;

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
    # print(face)
    # widen box
    (x, y, w, h) = calculate_crop(source_image, face)
    #print('%d %d %d %d' % (x, y, w, h))
    # crop
    face_image = source_image[y:y+h, x:x+w].copy()
    # scale
    target = photostreamer.target_path(source_path, offset)
    save_target(face_image, target)

def save_target(image, file_path):
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path),0o775)
    if image.size != 0:
        print(' => ' + file_path)
        cv2.imwrite(file_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), 90])

def calculate_crop(image, face):
    (x, y, w, h) = face
    if (w > target_width and h > target_height):
        return (x, y, w, h);

    height, width = image.shape[:2]
    center_x = int(x + w/2)
    center_y = int(y + h/2)

    # how much of the image is a face?

    # at the moment just return a crop of the correct size for the display centered on the face
    # to avoid overthinking shit
    return (int(center_x - target_width/2), int(center_y - target_width/2), target_width, target_height);

def process_image(source_path):
    if photostreamer.is_processed(source_path):
        return
    print(source_path)
    #print(source_path)
    image=cv2.imread(source_path)
    # print(image.shape); # width, height, channels
    # find face
    faces = find_faces(image)
    process_faces(faces, image, source_path)
    photostreamer.mark_processed(source_path)


def process_images(directory):
    image_files = photostreamer.find_image_files(directory)
    for source_path in image_files:
        if not photostreamer.is_processed(source_path):
            process_image(source_path)

process_images(photostreamer.source_dir())
