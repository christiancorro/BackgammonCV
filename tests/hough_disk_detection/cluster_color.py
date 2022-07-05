import numpy as np
import cv2 as cv
img = cv.imread('test2.jpg')


def cluster_colors(img, k=2, show=False):
    Z = img.reshape((-1, 3))
    # convert to np.float32
    Z = np.float32(Z)
    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = k
    ret, label, center = cv.kmeans(
        Z, K, None, criteria, 10, cv.KMEANS_RANDOM_CENTERS)
    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    # print(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    if(show):
        cv.imshow('res2', res2)
        # cv.waitKey(0)
        # cv.destroyAllWindows()
    return center


def unique_count_app(a):
    colors, count = np.unique(
        a.reshape(-1, a.shape[-1]), axis=0, return_counts=True)
    return colors[count.argmax()]


def readColors(filename="colors.txt"):
    f = open(filename)
    lines = f.readlines()
    black = np.array(lines[0][1:-2].split(" ")).astype(np.int8)
    print(black)
    white = np.array(lines[1][1:-2].split(" ")).astype(np.int8)
    f.close()
    return black, white


def saveColors(colors, filename="colors.txt"):
    f = open(filename, "w")
    for color in colors:
        f.write(str(color)+"\n")
    f.close()


def BGR_Luminance(BGR):
    return (0.2126*BGR[2] + 0.7152*BGR[1] + 0.0722*BGR[0])


def determineBlackWhite(colors):
    color1 = colors[0]
    color1Lum = BGR_Luminance(color1)

    color2 = colors[1]
    color2Lum = BGR_Luminance(color2)
    if(color1Lum < color2Lum):
        return color1, color2
    else:
        return color2, color1
