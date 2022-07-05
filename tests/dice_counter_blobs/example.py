from src import BlobDetector
from src import Segmentation
from src import Utils

image = Utils.read_image("./resources/multipledice_21.jpg")
Utils.create_window(image, "Original Image")
threshold_image = Segmentation.threshold(image, 245)
Utils.create_window(threshold_image, "Threshold Image")
blobs, kp_image = BlobDetector.count_blobs(threshold_image)
Utils.create_window(kp_image, "Keypoint image")
print("Number of Pips: " + str(len(blobs)))
Utils.only_exit_on_key_press()
