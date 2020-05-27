import cv2
import numpy as np

img = cv2.imread('dire.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 35, 200, apertureSize=3)
minLineLenght = 100
maxLineGap = 20
lines = cv2.HoughLinesP(edges,1,np.pi/100,100,minLineLenght,maxLineGap)
for x1, y1, x2, y2 in lines[0]:
    cv2.line(img,(x1,x2),(x2,y2), (0,255,0),2)
    cv2.imwrite('bingo.jpg',img)
    k = cv2.waitKey(10) 