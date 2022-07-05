from Detector import Detector
import numpy as np
import cv2

image = cv2.imread("../data/images/test/test6.jpg")
p_min = 0.3
threshold_nms = 0.3

detector = Detector(p_min, threshold_nms)

detector.detect(image)

# At-least one detection should exists
print(len(detector.results))
image = detector.drawResult()

# WINDOW_NORMAL gives window as resizable.
cv2.namedWindow("Detections", cv2.WINDOW_NORMAL)
cv2.imshow("Detections", image)
cv2.waitKey(0)
cv2.destroyWindow("Detections")
