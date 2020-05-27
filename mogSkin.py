import numpy as np
import cv2
cam = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()
_,lastframe = cam.read()
while(cam.isOpened()):
    _,img = cam.read()
    
    min = np.array([58,34,48])
    max = np.array([230,157,240])
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV_FULL)
    
    mascara = cv2.inRange(hsv, min, max)
    mov = cv2.absdiff(lastframe,img)
    resultado = cv2.bitwise_and(mov, mov, mask = mascara)
    
    fg = fgbg.apply(resultado)

    
    cv2.imshow('Imagem Original', img)
    cv2.imshow('Imagem com MOG', mascara)
    lastframe = resultado
    if cv2.waitKey(33) >= 0:
        break
cam.release()
cv2.destroyAllWindows()