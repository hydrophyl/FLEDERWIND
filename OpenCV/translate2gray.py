import cv2
import numpy as np 

img = cv2.imread('differenzsubtract.png',0)
cv2.imshow('diff',img)

k = cv2.waitKey(0) & 0xFF

if k == 27:     #wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'):     #wait for 's' key to save and exit
    cv2.imwrite('diffgray.png', img)
    cv2.destroyAllWindows()
