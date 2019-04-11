""" 11/4/2019 """

""" Author: Duy Nguyen """

from PIL import Image
# Import library

#BMP
im = Image.open('Original/bmp0000.bmp')
pixel_bmp = list(im.getdata())
# Get the colors in BMP file

#PNG
im1 = Image.open('Original/png0000.png')
pixel_png_256 = list(im1.getdata())
#Get colors in PNG file

if len(pixel_bmp) == len(pixel_png_256):
    print("True")
# When length of (pixel_bmp) (all the pixel 1280x1024 pixels) equal to length of (pixel_png_256)

for i in range(len(pixel_bmp)):
    if pixel_bmp[i][0] == pixel_png_256[i][0] and pixel_bmp[i][1] == pixel_png_256[i][1] and pixel_bmp[i][2] == pixel_png_256[i][2]:
        break
    else:
        print("Not good!")
print("Alle Pixel sind identisch!")
# for all i from 0 to length(pixel_bmp) 


""" for i in range(100):
    print(pixel_bmp[i][0])
    print(pixel_png_256[i][0])
    print(pixel_bmp[i][1])
    print(pixel_png_256[i][1])
    print(pixel_bmp[i][2])
    print(pixel_png_256[i][2])
    print() """