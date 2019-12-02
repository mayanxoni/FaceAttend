import os

import cv2
import numpy as np
from PIL import Image


def assure_path_exists(path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)


classifier_path = "classifier.xml"
recognizer = cv2.face.LBPHFaceRecognizer_create()  # Local Binary Patterns Histograms Algorithm
detector = cv2.CascadeClassifier(classifier_path)


def images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    list_face_samples = []
    list_id = []
    for image_path in image_paths:
        img_pil = Image.open(image_path).convert('L')
        img_numpy = np.array(img_pil, 'uint8')
        image_id = int(os.path.split(image_path)[-1].split(".")[0])
        print(image_path)
        faces_in_images = detector.detectMultiScale(img_numpy)
        for (x, y, w, h) in faces_in_images:
            list_face_samples.append(img_numpy[y:y + h, x:x + w])
            list_id.append(image_id)
    return list_face_samples, list_id


faces, ids = images_and_labels("dataset")
recognizer.train(faces, np.array(ids))
assure_path_exists("trainer/")
recognizer.save("trainer/trainer.yml")
