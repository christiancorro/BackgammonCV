import cv2
import numpy as np

img = cv2.imread("images/template.jpg")
blur = cv2.GaussianBlur(img, (5, 5), 0)
values = [30, 40, 50, 60, 70, 80, 90]
gray_image = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
for i in values:
    ret, threshold = cv2.threshold(gray_image, i, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    area = sorted(contours, key=cv2.contourArea, reverse=True)
    for j in range(1, len(area)):
        contour = area[j]
        size = cv2.contourArea(contour)
        if 1000 < float(size) < 140000:
            cv2.drawContours(img, [contour], -1, (0, 255, 0), 2)
cv2.imshow("img", img)
cv2.waitKey()
