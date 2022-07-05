import cv2 as opencv
import numpy as np


def count_blobs(image):
    params = opencv.SimpleBlobDetector_Params()
    params.filterByColor = True
    params.blobColor = 255
    params.minArea = 500
    # Disable the default settings
    params.filterByInertia = False
    params.filterByConvexity = False
    detector = opencv.SimpleBlobDetector_create(params)
    keypoints = detector.detect(image)
    im_with_keypoints = opencv.drawKeypoints(
        image, keypoints, np.array([]), (0, 0, 255),
        opencv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
    )
    return keypoints, im_with_keypoints
