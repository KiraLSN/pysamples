import numpy as np
import cv2
cam = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()
while(cam.isOpened()):
    _,frame = cam.read()
    fg = fgbg.apply(frame)
    cv2.imshow('Imagem Original', frame)
    cv2.imshow('Imagem com MOG', fg)
    
    if cv2.waitKey(33) >= 0:
        break
cam.release()
cv2.destroyAllWindows()