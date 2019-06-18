from PIL import Image

#Open image and get all pixel's colors
image = Image.open('png_24bit.png')

loadedPixelMap = image.load()
#image.size[columns,rows]
for i in range(image.size[0]):
    for j in range(image.size[1]):
        if loadedPixelMap[i, j] == (70,70,70) or \
            loadedPixelMap[i, j] == (35,163,163) or \
            loadedPixelMap[i, j] == (0,255,0) or \
            loadedPixelMap[i, j] == (255,170,0) or \
            loadedPixelMap[i, j] == (0,255,255) or \
            loadedPixelMap[i, j] == (255,255,0) or \
            loadedPixelMap[i, j] == (0,157,157) or \
            loadedPixelMap[i, j] == (255,0,0) or \
            loadedPixelMap[i, j] == (255,255,255):
            loadedPixelMap[i, j] = (0,0,0)
image.show()
