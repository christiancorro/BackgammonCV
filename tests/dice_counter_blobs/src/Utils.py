import cv2 as opencv

def read_image(file_location):
    return opencv.imread(file_location, opencv.IMREAD_GRAYSCALE)

def create_window(image, window_name):
    opencv.namedWindow(window_name, opencv.WINDOW_NORMAL)
    opencv.imshow(window_name, image)

def only_exit_on_key_press():
    opencv.waitKey(0)