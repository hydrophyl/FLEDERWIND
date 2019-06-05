import os, os.path, PIL
from PIL import Image
import numpy as np

#Access all PNG files in directory
imageDir = "RadarbilderProbe/" #specify your path here
image_path_list = [f for f in os.listdir('RadarbilderProbe') if f[-4:] in [".bmp", ".BMP"]]
image_path_list.sort() #sorting the names of pictures

# Asuming all images are the same size, get dimenstions of first image
w,h = Image.open(image_path_list[0]).size
N = len(image_path_list)

#Create a numpy array of floats to store the average (assume RGB images)
arr = np.zeros((h,w,3),np.float)

# Build up average pixel intensities, casting each image as an array of floats
for im in image_path_list:
    imarr=np.array(Image.open(im),dtype=np.float)
    arr=arr+imarr/N
out = Image.fromarray(arr)
print(out)
