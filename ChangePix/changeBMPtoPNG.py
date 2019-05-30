import os, os.path, PIL
from PIL import Image

#Access all images files in directory
imageDirectory = "Radarbilder"
imagesNameList = [filename for filename in os.listdir(imageDirectory)]
imagesNameList.sort() #sorting the names of images [0000,0001,0002,0003,...]
analyzedImageDirectory = "PNG_Radarbilder/"

for indexofImage in range(len(imagesNameList)):
    image = Image.open(imageDirectory + "/" + imagesNameList[indexofImage])
    image.save(analyzedImageDirectory + imagesNameList[indexofImage][:len(imagesNameList[indexofImage])-4] + ".png")

print(f"{len(imagesNameList)} images are converted!")
