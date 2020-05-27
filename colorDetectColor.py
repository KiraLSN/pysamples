import cv2
import numpy as np
cam = cv2.VideoCapture(0)

while(cam.isOpened()):
    _,img = cam.read()
    _,img2 = cam.read()
    min = np.array([58,34,48])
    max = np.array([230,157,240])
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV_FULL)
    mascara = cv2.inRange(hsv, min, max)
    resultado = cv2.bitwise_and(img, img, mask = mascara)
    resultado2 = cv2.bitwise_and(img, img2, mask = mascara)
    cv2.imshow("Cor", resultado)
    cv2.imshow("Cor2", img2)
    if cv2.waitKey(33)>=0:
        break
cam.release()
cv2.destroyAllWindows()