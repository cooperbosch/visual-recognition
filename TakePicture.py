import matplotlib.pyplot as plt
from camera import take_picture
import numpy as np
import dlib_models
from dlib_models import download_model, download_predictor, load_dlib_models
download_model()
download_predictor()
from dlib_models import models

def take_pic():
    pic = take_picture()
    load_dlib_models()
    face_detect = models["face detect"]
    face_rec_model = models["face rec"]
    shape_predictor = models["shape predict"]
    shape = shape_predictor(pic, detections[0])
    descriptor = np.array(face_rec_model.compute_face_descriptor(pic, shape))
    return (pic, face_detect, face_rec_model, shape_predictor, descriptor)


def find_rectangles(pic):
    detections = list(face_detect(pic))
    rectangles = []
    for i in range(len(detections)):
        r = []
        r.append(detections[i].left())
        r.append(detections[i].top())
        r.append(detections[i].right() - detections[i].left())
        r.append(detections[i].bottom() - detections[i].top())
        rectangles.append(r)