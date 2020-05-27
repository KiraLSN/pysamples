import numpy as np
import cv2
cam = cv2.VideoCapture(0)
while(cam.isOpened()):
    _,img = cam.read()
    outro = cv2.imread("bingo.jpg")
    cv2.imshow('Imagem', outro)
    if cv2.waitKey(33) >= 0:
        break
cam.release()
cv2.destroyAllWindows()