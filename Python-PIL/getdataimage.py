from PIL import Image

#BMP
im = Image.open('Cuted/bmp24.bmp')
pixel_bmp = list(im.getdata())

#PNG
im1 = Image.open('Cuted/png32.png')
pixel_pnggs_32 = list(im1.getdata())

#PNG
im2 = Image.open('Cuted/png256.png')
pixel_pnggs_256 = list(im1.getdata())

#PNG
im2 = Image.open('Cuted/pngcolor.png')
pixel_png_color = list(im1.getdata())

imcolor = Image.open('Original/bmp0000.bmp').getcolors()
print("Listed Colors in BMPFarben Original: ")

for x in imcolor:
    print(x)

print("\n")
print("Anzahl der Farben im Bild: ")
print(len(imcolor))


# NOTE  Messwerte Cuted Images *nur die Schwarz-Gelb Bereich wird genommen.
#       BMP    Color       32 Farben
#       PNG32  Grayscale   27 Farben ==>>>>>>> !WARNUNG  
#       PNG256 Grayscale   32 Farben
#       PNG    Color       32 Farben
# NOTE  Messwerte Original Images
#       BMP    Color       39 Farben
#       PNG32  Grayscale   33 Farben ==>>>>>>> !WARNUNG  
#       PNG256 Grayscale   39 Farben
#       PNG    Color       39 Farben

""" !TODO 32 von 39 Farben rausnehmen 
-> den Rest ausblenden """
