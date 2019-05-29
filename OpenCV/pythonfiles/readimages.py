import numpy as np 
import cv2
#load an color image

img = cv2.imread('1542505298935.jpg',0)
#firstimg = cv2.imread('cap_00000000.bmp')
#secondimg = cv2.imread('cap_00000001.bmp')
""" cv2.imshow('image',firstimg)
cv2.imshow('image',secondimg) """
cv2.imshow('test',img)

k = cv2.waitKey(0) & 0xFF

if k == 27:     #wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):     #wait for 's' key to save and exit
    cv2.imwrite('test.png', img)
    cv2.destroyAllWindows()
