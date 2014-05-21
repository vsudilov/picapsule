import os,sys

import cv2
import numpy as np

CASCADE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),'haarcascades')

def getFaces(img):
  face_cascade = cv2.CascadeClassifier(os.path.join(CASCADE_DIR,'haarcascade_frontalface_default.xml'))
  eye_cascade = cv2.CascadeClassifier(os.path.join(CASCADE_DIR,'haarcascade_eye.xml'))

