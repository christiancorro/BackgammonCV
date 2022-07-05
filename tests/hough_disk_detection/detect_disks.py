import cv2
import numpy as np

from cluster_color import BGR_Luminance, cluster_colors, determineBlackWhite, readColors, saveColors

offset = 20

img = cv2.imread("test6.jpg", 0)
img = cv2.medianBlur(img, 5)
imgColor = cv2.imread("test6.jpg")
hsvImg = cv2.cvtColor(imgColor, cv2.COLOR_BGR2HSV)

# multiple by a factor to change the saturation
hsvImg[..., 1] = hsvImg[..., 1] * 2

# multiple by a factor of less than 1 to reduce the brightness
# hsvImg[..., 2] = hsvImg[..., 2]*0.6

imgColor = cv2.cvtColor(hsvImg, cv2.COLOR_HSV2BGR)

cimg = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, param1=50, param2=12, minRadius=24, maxRadius=25)

circles = np.uint16(np.around(circles))
images = []
count = 0
offset = circles[0, 1][2]
for i in circles[0, :]:
    count += 1
    # draw the outer circle
    cv2.circle(imgColor, (i[0], i[1]), i[2], (0, 255, 0), 1)
    # draw the center of the circle
    # cv2.circle(imgColor, (i[0], i[1]), 2, (0, 0, 255), 2)
    # Using cv2.putText() method
    # imgColor = cv2.putText(imgColor, str(
    #     count), (i[0], i[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
    images.append(imgColor[i[1] - offset : i[1] + offset, i[0] - offset : i[0] + offset])


allDisks = np.concatenate(images, axis=1)

cv2.imshow("detected circles 2", allDisks)
colors = cluster_colors(allDisks, show=True)

# saveColors(colors)

# white, black = readColors()
black, white = determineBlackWhite(colors)
# white = colors[0]
# black = colors[1]

black_lum = BGR_Luminance(black)
white_lum = BGR_Luminance(white)

print("Black Lum: " + str(black_lum))
print("White Lum: " + str(white_lum))

images = []
for i in circles[0, :]:
    image = imgColor[i[1] - offset : i[1] + offset, i[0] - offset : i[0] + offset]
    color = cluster_colors(image, k=1)
    print(color[0])
    color_lum = BGR_Luminance(color[0])
    print("lum " + str(color_lum))
    balck_distance = abs(color_lum - black_lum)
    white_distance = abs(color_lum - white_lum)
    # With kernel size depending upon image size
    if balck_distance > white_distance:
        print("white")
        imgColor = cv2.putText(imgColor, "w", (i[0], i[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
    else:
        print("black")
        imgColor = cv2.putText(imgColor, "b", (i[0], i[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    images.append(image)


allDisks = np.concatenate(images, axis=1)
cv2.imshow("detected circles 3", allDisks)

cv2.imshow("detected circles", imgColor)
cv2.waitKey(0)
cv2.destroyAllWindows()
