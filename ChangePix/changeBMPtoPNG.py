import time
import os, os.path, PIL
from PIL import Image

#Access all images files in directory
imageDirectory = "Radarbilder"
imagesNameList = [filename for filename in os.listdir(imageDirectory)]
imagesNameList.sort() #sorting the names of images [0000,0001,0002,0003,...]
analyzedImageDirectory = "PNG_Radarbilder"
os.makedirs(analyzedImageDirectory)

t0 = time.time()
for indexofImage in range(len(imagesNameList)):
    image = Image.open(imageDirectory + "/" + imagesNameList[indexofImage])
    image.save(analyzedImageDirectory + "/" + imagesNameList[indexofImage][:len(imagesNameList[indexofImage])-4] + ".png")
t1 = time.time()
print("Time required: ", t1 - t0)
print(f"{len(imagesNameList)} images are converted!")
