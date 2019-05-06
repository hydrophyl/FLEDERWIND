import os, os.path
import cv2

print (cv2.__version__)

imageDir = "RadarbilderProbe/" #specify your path here
image_path_list = [f for f in os.listdir('RadarbilderProbe')]
image_path_list.sort()

#Read and substract images
for i in range(44):
    pic_1 = cv2.imread('RadarbilderProbe/' + image_path_list[i])
    pic_2 = cv2.imread('RadarbilderProbe/' + image_path_list[i+1])
    dif = cv2.subtract(pic_2,pic_1)
    #Write to files
    cv2.imwrite('translated/' + image_path_list[i] +'.png', dif)
    dif_gs = cv2.imread('translated/' + image_path_list[i] + '.png', 0) 
    cv2.imwrite('translated/' + image_path_list[i] + '_gs.png', dif_gs)