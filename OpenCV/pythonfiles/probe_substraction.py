import os, os.path
import cv2

imageDir = "Probe/" #specify your path here
image_path_list = [f for f in os.listdir('Probe')]
image_path_list.sort()

#Read and substract images
pic_1 = cv2.imread('Probe/interstellar.jpg')
pic_2 = cv2.imread('Probe/interstellar_changed.jpg')
dif = cv2.absdiff(pic_2,pic_1)

#Write image
cv2.imwrite('Probe/sustract.png',dif)