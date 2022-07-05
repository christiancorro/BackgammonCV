import cv2 as opencv
import numpy

def threshold(img_in, value):
    img_out = img_in.copy()
    map, img_out = opencv.threshold(img_out, value, 255, opencv.THRESH_BINARY)
    return img_out
