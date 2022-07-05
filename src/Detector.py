import numpy as np
import cv2

from Constants import CLASS_COLORS


class Detector:
    def __init__(self, p_min=0.5, threshold_nms=0.3):
        self.p_min = p_min
        self.threshold_nms = threshold_nms
        self.image = 0
        self.blob = 0
        self.height = 0
        self.width = 0
        self.labels = 0
        self.colors = CLASS_COLORS
        self.network = 0
        self.layers = 0
        self.network_output = 0
        self.results = 0
        self.bounding_boxes = []
        self.confidences = []
        self.class_numbers = []
        self.centers = []

        self.image_size = (608, 608)

        self.__load()

    def __load(self):
        self.__loadLabels()
        # self.__loadColors()
        self.__loadNetwork()

    def __loadLabels(self):
        with open("../data/cfg/coco.names") as f:
            self.labels = [line.strip() for line in f]
        # time.sleep(2)

    # def __loadColors(self):
    # colors = np.random.randint(0, 255, size=(len(self.labels), 3), dtype="uint8")
    # self.colors = colors

    def __loadNetwork(self):
        self.network = cv2.dnn.readNetFromDarknet("../data/cfg/yolov4.cfg", "../data/cfg/yolov4.weights")
        self.layers = self.network.getLayerNames()
        self.layers = [self.layers[i - 1] for i in self.network.getUnconnectedOutLayers()]

    def loadImage(self, image):
        self.image = image
        self.height, self.width = self.image.shape[:2]
        self.blob = cv2.dnn.blobFromImage(self.image, 1 / 255.0, self.image_size, swapRB=True, crop=False)

    def detect(self, image):
        # print("Detecting...")
        self.loadImage(image)
        self.network.setInput(self.blob)
        self.network_output = self.network.forward(self.layers)

        temp_class_numbers = []
        temp_confidences = []
        temp_bounding_boxes = []
        self.centers = []

        temp_class_numbers = []

        # Going through all output layers after feed forward pass
        for result in self.network_output:
            for detected_objects in result:
                scores = detected_objects[5:]
                class_current = np.argmax(scores)
                confidence_current = scores[class_current]

                if confidence_current > self.p_min:
                    box_current = detected_objects[0:4] * np.array([self.width, self.height, self.width, self.height])

                    x_center, y_center, box_width, box_height = box_current
                    x_min = int(x_center - (box_width / 2))
                    y_min = int(y_center - (box_height / 2))

                    # Adding results into prepared lists
                    temp_bounding_boxes.append([x_min, y_min, int(box_width), int(box_height)])
                    temp_confidences.append(float(confidence_current))
                    temp_class_numbers.append(class_current)

        self.results = cv2.dnn.NMSBoxes(temp_bounding_boxes, temp_confidences, self.p_min, self.threshold_nms)

        if len(self.results) > 0:

            self.class_numbers = []
            self.bounding_boxes = []
            self.confidences = []

            for i in self.results.flatten():

                x_min, y_min = temp_bounding_boxes[i][0], temp_bounding_boxes[i][1]
                box_width, box_height = temp_bounding_boxes[i][2], temp_bounding_boxes[i][3]
                x_center = x_min + box_width // 2
                y_center = y_min + box_height // 2

                self.centers.append((x_center, y_center))
                self.class_numbers.append(temp_class_numbers[i])
                self.bounding_boxes.append(temp_bounding_boxes[i])
                self.confidences.append(temp_confidences[i])

        # print("Detection complete\n")

        return self.results, self.class_numbers, self.confidences, self.bounding_boxes, self.centers

    def drawResult(self):
        image = self.image.copy()
        if len(self.results) > 0:
            for i in range(len(self.bounding_boxes)):

                # Getting current bounding box coordinates, its width and height
                # x_center, y_center = centers[i]
                # print(centers[i])
                x_min, y_min = self.bounding_boxes[i][0], self.bounding_boxes[i][1]
                box_width, box_height = self.bounding_boxes[i][2], self.bounding_boxes[i][3]
                x_center, y_center = self.centers[i]

                # Preparing colour for current bounding box
                colour_box_current = self.colors[self.class_numbers[i]].tolist()

                # Drawing bounding box on the original image
                cv2.rectangle(image, (x_min, y_min), (x_min + box_width, y_min + box_height), colour_box_current, 1)
                if self.class_numbers[i] >= 6:
                    cv2.circle(image, (x_center, y_center), 2, (255, 255, 255), 2)

                # Preparing text with label and confidence for current bounding box
                text_box_current = "{}: {:.2f}".format(self.labels[int(self.class_numbers[i])], self.confidences[i])

                # Putting text with label and confidence on the original image
                cv2.putText(image, text_box_current, (x_min, y_min - 5), cv2.FONT_HERSHEY_DUPLEX, 0.4, colour_box_current, 1, cv2.LINE_AA)
        return image

    def drawBboxs(self):
        image = np.zeros((self.height, self.width, 3), np.uint8)
        if len(self.results) > 0:
            for i in range(len(self.bounding_boxes)):

                # Getting current bounding box coordinates, its width and height
                # x_center, y_center = centers[i]
                # print(centers[i])
                x_min, y_min = self.bounding_boxes[i][0], self.bounding_boxes[i][1]
                box_width, box_height = self.bounding_boxes[i][2], self.bounding_boxes[i][3]
                x_center, y_center = self.centers[i]

                # Preparing colour for current bounding box
                colour_box_current = self.colors[self.class_numbers[i]].tolist()

                # Drawing bounding box on the original image
                cv2.rectangle(image, (x_min, y_min), (x_min + box_width, y_min + box_height), colour_box_current, 1)
                if self.class_numbers[i] >= 6:
                    cv2.circle(image, (x_center, y_center), 2, (255, 255, 255), 2)

                # Preparing text with label and confidence for current bounding box
                text_box_current = "{}: {:.2f}".format(self.labels[int(self.class_numbers[i])], self.confidences[i])

                # Putting text with label and confidence on the original image
                cv2.putText(image, text_box_current, (x_min, y_min - 5), cv2.FONT_HERSHEY_DUPLEX, 0.4, colour_box_current, 1, cv2.LINE_AA)
        return image
