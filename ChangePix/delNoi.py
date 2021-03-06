import time
import os, os.path, PIL
import numpy
from PIL import Image

#Start time counter
t0 = time.time()
print("="*80)
print("Welcome to the Noise Reduction Program! All radar images in the Directory in the python file are going to be converted!")

#Access all images files in directory
imageDirectory = "PNGImages" #change here to change the image directory
#create a list of filenames in imagesDirectory
imagesNameList = [filename for filename in os.listdir(imageDirectory)]
imagesNameList.sort() #sorting namelist a-z

#Assuming all image files in directory have the same size, get dimensions of first image
imageModel = Image.open(imageDirectory + "/" + imagesNameList[0])
rows = imageModel.height #number of rows of pixels
columns = imageModel.width   #number of columns of pixels

#Create a 2D array of integer to store the counter of color's appear
#Assume that all elements of matrix has the value 0
counterMatrix = numpy.zeros((rows, columns), dtype = int)

#Change this value to change how much images are analyzed to count the noise
counter = 100
for indexofImage in range(counter): # the first "counter" images is taken to analyse the noise (noise appear in the same spot > 1 times in 100 images)
    image = Image.open(imageDirectory + "/" + imagesNameList[indexofImage])
    loadedPixelMap = image.load() #loading the (R,G,B) array of all pixel
    #for every columns and rows of matrix
    for column in range(columns):
        for row in range(rows):
            if loadedPixelMap[column, row] != (0,0,0): #if pixel is not black -> (!signal) -> add one to counterMatrix on the spot of this pixel
                counterMatrix[row, column] = counterMatrix[row, column] + 1

t1 = time.time()
print("="*80)
print("Time required: ",t1 - t0)
print("End of noise counter!")
print()

for indexofImage in range(len(imagesNameList)): #analyze all images in folders and delete the unused colors
    #Load pixels of an image and go though all pixels
    image = Image.open(imageDirectory + "/" + imagesNameList[indexofImage])
    loadedPixelMap = image.load()
    #image.size[columns, rows]
    #delete all not interested colors
    for column in range(columns):
        for row in range(rows):
            if  loadedPixelMap[column, row] == (70,70,70) or \
                loadedPixelMap[column, row] == (35,163,163) or \
                loadedPixelMap[column, row] == (0,255,0) or \
                loadedPixelMap[column, row] == (255,170,0) or \
                loadedPixelMap[column, row] == (0,255,255) or \
                loadedPixelMap[column, row] == (255,255,0) or \
                loadedPixelMap[column, row] == (0,157,157) or \
                loadedPixelMap[column, row] == (255,0,0) or \
                loadedPixelMap[column, row] == (255,255,255):
                loadedPixelMap[column, row] = (0,0,0)
    image.save(imageDirectory + "/" + imagesNameList[indexofImage])

t2 = time.time()
print("="*80)
print("Time required to convert full radar images to yellow signal images: ",t2-t1)
print(f"{len(imagesNameList)} images are converted! Congratulations!")
print()

#NOTE not interested color list
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
#Read the Matrix and analyse
#Go through all images and delete the Noise
for indexofImage in range(len(imagesNameList)):
    image = Image.open(imageDirectory + "/" + imagesNameList[indexofImage])
    loadedPixelMap = image.load()
    for column in range(columns): #for all columns
        for row in range(rows): #for all rows
            if counterMatrix[row, column] > 1:
                #loadedPixelMap[column, row] = (122,122,190) #toggle this line and comment the next line to see the noise
                loadedPixelMap[column, row] = (0,0,0)
    image.save(imageDirectory + "/" + imagesNameList[indexofImage])

t3 = time.time()
print("="*80)
print("Time required to delete noises to all radar images: ",t3 - t2)
print("="*80)
print()
print("="*80)
os.system("ffmpeg -framerate 10 -i " + imageDirectory + "/" + imagesNameList[0][:-7] + "%03d.png " + "Zusammenfassung.mp4") #when bmp images are used, change png to bmp with the script changetoBMP.py
print("All the noise reduced radar images is saved in video ffmpeg.mp4 in 10fps!")
# Example: we have 300 images and these are named as cap_00000001.png to cap_00000300.png
# imagesNameList[0] = cap_00000001.png -> imagesNameList[0][:-7] = cap_00000 -> imagesNameList[0][:-7] + "%03d.png" = cap_00000001.png to cap_00000999.png *just to 300 because of limited files

# End time counter
t4 = time.time()
print("="*80)
print()
print("Time required for all processes: ", t4 - t0)
print("Vielen Dank fuer Ihre Geduld!")
