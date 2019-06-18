import os, os.path, PIL
from PIL import Image

#Access all images files in directory
imageDirectory = "PNG_Radarbilder"
imagesNameList = [filename for filename in os.listdir(imageDirectory)]
imagesNameList.sort() #sorting the names of images [0000,0001,0002,0003,...]
analyzedImageDirectory = "Analyzed/"

for indexofImage in range(len(imagesNameList)):
    #Load pixels of an image and go though all pixels
    image = Image.open(imageDirectory + "/" + imagesNameList[indexofImage])
    loadedPixelMap = image.load()
    #image.size[columns, rows]
    #delete all not interested colors
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            if  loadedPixelMap[i, j] == (70,70,70) or \
                loadedPixelMap[i, j] == (35,163,163) or \
                loadedPixelMap[i, j] == (0,255,0) or \
                loadedPixelMap[i, j] == (255,170,0) or \
                loadedPixelMap[i, j] == (0,255,255) or \
                loadedPixelMap[i, j] == (255,255,0) or \
                loadedPixelMap[i, j] == (0,157,157) or \
                loadedPixelMap[i, j] == (255,0,0) or \
                loadedPixelMap[i, j] == (24,24,0) or \
                loadedPixelMap[i, j] == (28,28,0) or \
                loadedPixelMap[i, j] == (32,32,0) or \
                loadedPixelMap[i, j] == (36,36,0) or \
                loadedPixelMap[i, j] == (40,40,0) or \
                loadedPixelMap[i, j] == (43,43,0) or \
                loadedPixelMap[i, j] == (46,46,0) or \
                loadedPixelMap[i, j] == (49,49,0) or \
                loadedPixelMap[i, j] == (255,255,255):
                loadedPixelMap[i, j] = (0,0,0)
    image.save(analyzedImageDirectory + imagesNameList[indexofImage])

print(f"{len(imagesNameList)} images are converted! Congratulations!")

#!NOTE not interested color list
# color: (R,G,B)
# lightblue1(coordinates) : (35,163,163)
# lightblue2(coordinates) : (0,255,255)
# darkblue(radar's lines) : (0,157,157)
# green(data numbers) :     (0,255,0)
# trueyellow(numbers) :     (255,255,0)
# orangeyellow(numbers) :   (255,170,0)
# red(time) :               (255,0,0)
# gray(background) :        (70,70,70)
# white(cursor) :           (255,255,255)
