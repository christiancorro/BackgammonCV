import numpy as np
from shapely.geometry import Point, Polygon


def imShow(path):
    import cv2
    import matplotlib.pyplot as plt

    image = cv2.imread(path)
    height, width = image.shape[:2]
    resized_image = cv2.resize(image, (3 * width, 3 * height), interpolation=cv2.INTER_CUBIC)

    fig = plt.gcf()
    fig.set_size_inches(18, 10)
    plt.axis("off")
    plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
    plt.show()


def pointInPoly(pt, ply):
    # print(ply)
    ply = np.asarray(ply)
    ply = ply.flatten()
    ply = np.reshape(ply, (4, 2))
    # print(ply.tolist())
    point = Point(pt)
    poly = Polygon(ply)
    return poly.contains(point)
