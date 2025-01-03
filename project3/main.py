import torch
from pathlib import Path
import cv2
import matplotlib.pyplot as plt

class ObjectDetector:
    def __init__(self, model_name='yolov5s'):
        self.model = torch.hub.load('ultralytics/yolov5', model_name)

    def detect_objects(self, image_path):
        results = self.model(image_path)
        
        annotated_image = results.render()[0]
        
        annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
        return annotated_image, results.pandas().xyxy[0]

detector = ObjectDetector()

image_path = 'C:/Users/Solvo/Desktop/modelsExecution-HuggingFace/project3/images/image.jpg'

annotated_image, detections = detector.detect_objects(image_path)

print("Detecciones:", detections)

plt.imshow(annotated_image)
plt.axis('off')
plt.show()
