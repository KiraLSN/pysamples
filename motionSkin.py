import numpy as np
import cv2
cam = cv2.VideoCapture(0)
_,lastframe = cam.read()

while(cam.isOpened()):
    _,img = cam.read()
    min = np.array([30,50,67])
    max = np.array([90,50,67])
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV_FULL)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    mascara = cv2.inRange(hsv, min, max)
    resultado = cv2.bitwise_and(img, img, mask = mascara)
    mov = cv2.absdiff(resultado,img)
    
    cv2.imshow('Imagem Original', resultado)
    cv2.imshow('Imagem Subtraida', img)
    lastframe = img
    if cv2.waitKey(33) >= 0:
        break
cam.release()
cv2.destroyAllWindows()