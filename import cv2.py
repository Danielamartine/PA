
from colorsys import hsv_to_rgb
from ssl import CHANNEL_BINDING_TYPES
import cv2

import cv2
from cv2 import cvtColor

imgText="images"
#Lectura de imagen
img= cv2.imread(imgText+'.jpg')
cv2.imshow('ImagenOriginal',img)

#Imagen escala de grises
imgGrau= cv2.imread(imgText+'.jpg',0)
cv2.imshow('Grises',imgGrau)


#Binarización
ret,tresh=cv2.threshold(imgGrau,120,200,cv2.THRESH_BINARY_INV)
cv2.imshow('Binarizada',tresh)

ret,th3=cv2.threshold(imgGrau,255,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('Otsu',th3)

th1=cv2.adaptiveThreshold(imgGrau,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,40)
th2=cv2.adaptiveThreshold(imgGrau,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,40)
cv2.imshow('Promedio',th1)
cv2.imshow('Gaussiano',th2)

cv2.waitKey(0)
cv2.destroyAllWindows()


