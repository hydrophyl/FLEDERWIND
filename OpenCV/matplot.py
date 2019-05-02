import numpy as np 
import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('difference.png',0)
plt.imshow(img, cmap='gray',interpolation='bicubic')
#plt.xticks([]), plt.yticks([])  #Hide tick values on X and Y axis
plt.show()
