import os, os.path
import cv2

imageDir = "RadarbilderProbe/" #specify your path here
image_path_list = [f for f in os.listdir('RadarbilderProbe')]
image_path_list.sort()

#Read and substract imageqs
for i in range(44):
    pic_1 = cv2.imread('RadarbilderProbe/' + image_path_list[i])
    summe = cv2.imread('summe/summe.png') 
    dif = cv2.subtract(pic_1,summe)
    #Write to files
    cv2.imwrite('translated/' + image_path_list[i] +'.png', dif)
 