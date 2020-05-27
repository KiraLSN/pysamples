import numpy as np
import cv2
cam = cv2.VideoCapture(0)
_,lastframe = cam.read()
fonte = cv2.FONT_HERSHEY_COMPLEX_SMALL
while(cam.isOpened()):
    _,firstframe = cam.read()
    mov = cv2.absdiff(lastframe,firstframe)
    cv2.putText(mov, "Luciano", (50,100), fonte, 2.0, (255,255,255), 1)
    cv2.imshow('Imagem Original', firstframe)
    cv2.imshow('Imagem Subtraida', mov)
    lastframe = firstframe
    if cv2.waitKey(33) >= 0:
        break
cam.release()
cv2.destroyAllWindows()