import os, numpy , PIL
from PIL import Image

# Access all BMP files in directory
imageDir = "RadarbilderProbe/" #specify your path here
allfiles=os.listdir("RadarbilderProbe/")
imlist=[filename for filename in allfiles if  filename[-4:] in [".bmp",".BMP"]]

# Assuming all images are the same size, get dimensions of first image
img = Image.open(imageDir + imlist[0])
h = img.height
w = img.width
N=len(imlist)

# Create a numpy array of floats to store the average (assume RGB images)
arr=numpy.zeros((h,w,3),numpy.float)

# Build up average pixel intensities, casting each image as an array of floats
for img in imlist:
    imarr=numpy.array(Image.open(imageDir + img),dtype=numpy.float)
    arr=arr+imarr/N

# Round values in array and cast as 8-bit integer
arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)

# Generate, save and preview final image
out=Image.fromarray(arr,mode="RGB")
out.save("Average.png")
out.show()