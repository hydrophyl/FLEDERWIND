import os, os.path
import cv2

ImageDirectory = "RadarbilderProbe/" #specify your path here
image_path_list = [i for i in ImageDirectory]
image_path_list.sort() #sorting the names of pictures

#1. image
pic_1 = cv2.imread('RadarbilderProbe/' + image_path_list[0])
summe = cv2.imwrite('summe/summe2.png',pic_1)

#Images addition
for i in range(15,35):
    pic_new = cv2.imread('RadarbilderProbe/' + image_path_list[i])
    summe = cv2.add(summe, pic_new)

#write summe_image:
cv2.imwrite('summe/summe2.png',summe)

#Read and substract images
for i in range(44):
    pic_org = cv2.imread('RadarbilderProbe/' + image_path_list[i])
    summe = cv2.imread('summe/summe2.png')
    dif = cv2.subtract(pic_org,summe)
    #Write to files
    cv2.imwrite('translated/' + image_path_list[i] +'.png', dif)
