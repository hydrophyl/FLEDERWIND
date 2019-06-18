import os, os.path, PIL
import numpy
from PIL import Image

#Access all images files in directory
imageDirectory = "Analyzed"
imagesNameList = [filename for filename in os.listdir(imageDirectory)]
imagesNameList.sort() #sorting the names of images [0000,0001,0002,0003,...]
analyzedImageDirectory = "NoiseReducedImages/"

#Assuming all image files in directory, get dimensions of first image
imageModel = Image.open(imageDirectory + "/" + imagesNameList[0])
rows = imageModel.height #number of rows of pixels
columns = imageModel.width   #number of columns of pixels

#Create a 2D array of integer to store the counter of color's appear
#Assume that all elements of matrix has the value 0
counterMatrix = numpy.zeros((rows, columns), dtype = int)

#TODO Count the number when a pixel appear colors
for indexofImage in range(len(imagesNameList)):
    #Load pixels of an image and go though all pixels
    image = Image.open(imageDirectory + "/" + imagesNameList[indexofImage])
    loadedPixelMap = image.load()
    #NOTE image.size[columns, rows] -> loadedPixelMap[col, row] == counterMatrix[row,col] (probably with tranverse matrix calculate)
    for column in range(columns): #for all columns
        for row in range(rows): #for all rows
            if loadedPixelMap[column, row] != (0,0,0):
                counterMatrix[row, column] = counterMatrix[row, column] + 1

#Read the Matrix and analyse
#Go through all images and delete the Noise
for indexofImage in range(len(imagesNameList)):
    image = Image.open(imageDirectory + "/" + imagesNameList[indexofImage])
    loadedPixelMap = image.load()
    for column in range(columns): #for all columns
        for row in range(rows): #for all rows
            if counterMatrix[row, column] > 1:
                #loadedPixelMap[column, row] = (122,122,190)
                loadedPixelMap[column, row] = (0,0,0)
    image.save(analyzedImageDirectory + imagesNameList[indexofImage])


#TODO define range intensity of bat's signal color
#TODO compare RGB datas of loadedPixelMap[i,j] with yellow niveaus
