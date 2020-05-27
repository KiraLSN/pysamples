import numpy as np
import cv2
cam = cv2.VideoCapture(0)
while(cam.isOpened()):
    _,img= cam.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    min = np.array([161, 155, 84])
    max = np.array([179, 255, 255])
    red_mask = cv2.inRange(hsv, min, max)
    red = cv2.bitwise_and(img, img, mask = red_mask)
    cv2.imshow('Imagem Vermelha', red)
    if cv2.waitKey(33)>= 0:
        break
cam.release()
cv2.destroyAllWindows()