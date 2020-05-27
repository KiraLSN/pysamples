#!/usr/bin/env python
import numpy as np
import cv2 


img1 = cv2.imread ('dire.jpg')

print('Largura em pixels: ', end='')
print(img1.shape[1]) #largura da imagem
print('Altura em pixels: ', end='')
print(img1.shape[1]) #altura da imagem
#print('Qtde de canais: ', end='')
#print(imagem.shape[2]) 
cv2.imshow('original', img1)
(r,g,b) = img1[1,1]
#Pegar cor de um pixel
print("Verde é %d, vermelho é %d e azul é %d" %(g,r,b))
#Converter para cinza
#cinza = cv2.cvcolor(img1, color_rgb2gray)

#cinza = cv2.cvcolor(img1, color_rgb2gray)
#cv2.imshow('cinza', cinza)
#Mudando valor de um pixel
img1[0,0] = (10,200,30)
#recortar imagem
fatia = img1[10:100,30:200]
cv2.waitKeyEx()