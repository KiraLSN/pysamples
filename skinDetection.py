import numpy as np
import cv2
cam = cv2.VideoCapture(0)
min = np.array([0, 133, 77])
max = np.array([255, 150, 127])
while(cam.isOpened()):
    _,img= cam.read()
    ycbcr = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    skin = cv2.inRange(ycbcr, min, max)
    contour,_=cv2.findContours(skin, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow('Pele', skin)
    if cv2.waitKey(33)>= 0:
        break
cam.release()
cv2.destroyAllWindows()