import numpy as np
import cv2

cam = cv2.VideoCapture(0)
_,img = cam.read()
cv2.imshow('Teste de Foto', img)
cv2.waitKey(1000)
cam.release()
cv2.destroyAllWindows()