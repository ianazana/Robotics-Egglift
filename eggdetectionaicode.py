# NOTE:
# This Python script is a reconstructed version based on the project documentation
# and system description. The original source file was not preserved.
# Components and logic were faithfully replicated from available records.

import cvzone
import cv2
import serial
from cvzone.ClassificationModule import Classifier

cap = cv2.VideoCapture(0)
myClassifier = cvzone.Classifier('MyModel/keras_model.h5','MyModel/labels.txt')
fpsReader = cvzone.FPS

while True:
    _, img = cap.read()
    predictions, index = myClassifier.getPrediction(img)
    print(predictions, index)

    fps = fpsReader.update(img)
    # print(fps)


    cv2.imshow("Image",img)
    cv2.waitKey(1)
