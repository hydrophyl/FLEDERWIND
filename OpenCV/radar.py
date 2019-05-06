import numpy as np
import cv2
    
erstes_pic = cv2.imread('RadarbilderProbe/cap_00000001.bmp')
zweite_pic = cv2.imread('RadarbilderProbe/cap_00000002.bmp')

differenz = cv2.subtract(zweite_pic, erstes_pic)

cv2.imshow('Differenz_farbig', differenz)
cv2.imwrite('differenz_farbig_2.png', differenz)

differenz_grayscale = cv2.imread('differenz_farbig.png',0)
cv2.imshow('differenz_grayscale_2.png', differenz_grayscale)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
        