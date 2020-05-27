import numpy as np
import cv2
cam = cv2.VideoCapture(0)
_,lastframe = cam.read()

while(cam.isOpened()):
    _,img = cam.read()
    mov = cv2.absdiff(lastframe,img)
    min = np.array([58,34,48])
    max = np.array([230,157,240])
    hsv = cv2.cvtColor(mov, cv2.COLOR_RGB2HSV_FULL)
    
    mascara = cv2.inRange(hsv, min, max)
    resultado = cv2.bitwise_and(img, img, mask = mascara)
    mov = cv2.absdiff(resultado,img)
    
    cv2.imshow('Imagem Original', mov)
    cv2.imshow('Imagem Subtraida', img)
    lastframe = img
    if cv2.waitKey(33) >= 0:
        break
cam.release()
cv2.destroyAllWindows()