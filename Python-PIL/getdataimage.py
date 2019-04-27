""" 4/2019 """

""" Author: Duy Nguyen """
from PIL import Image

#BMP
im = Image.open('18.4 Radarproben/CF_0_333m_f_2_5s_greyscale_25600000000.png')
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

#imcolor = Image.open('18.4 Radarproben/CF_0_333m_f_2_5s_png_24bit00000000.png').getcolors()
#imcolor = Image.open('Original/bmp0000.bmp').getcolors()
imcolor = Image.open('18.4 Radarproben/CF_0_333m_f_2_5s_png_16bit00000000.png').getcolors()
print("Listed Colors in PNG 16 Farben Original: ")

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
