import numpy as np 
import cv2
from matplotlib import pyplot as plt 


firstimage = cv2.imread('cap_00000000.bmp')
secondimage = cv2.imread('cap_00000001.bmp')

#subtr = cv2.subtract(img1,img2) #FIXME Not working
#image1 = np.float(firstimage)
#image2 = np.float(secondimage)
#image3 = image2 - image1
#plt.imshow(image3)
#plt.show()

#out_img = cv2.imread(secondimage).astype(np.int8)
#tar_img = cv2.imread(firstimage).astype(np.int8)
#difference = out_img - tar_img

difference = cv2.subtract(firstimage,secondimage) #FIXME FIXED
cv2.imshow('Target',firstimage)
cv2.imshow('Output',secondimage)
cv2.imshow('difference', difference)
#cv2.imwrite('diffence.png', difference)
graydiff = cv2.imread('difference.png',0)
cv2.imshow('differencegray', graydiff)

k = cv2.waitKey(0) & 0xFF
if k == 27:     #wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):     #wait for 's' key to save and exit
    cv2.imwrite('differenzgray.png', graydiff)
    cv2.destroyAllWindows()
