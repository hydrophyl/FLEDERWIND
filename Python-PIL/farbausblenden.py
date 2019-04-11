""" 11/4/2019 """

""" Author: Duy Nguyen """

import xlrd
from PIL import Image
# Export RGB Werte from Excel data
""" loc= ("RGBA Werte.xlsx")

wb= xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)

for i in range(1,33):
    rgb_werte = [sheet.cell_value(i,1),sheet.cell_value(i,2),sheet.cell_value(i,3)]
    print(rgb_werte)

print() """
#Definition useable colors
red = [0,24,28,32,36,40,43,46,49,52,55,58,61,64,76,88,100,105,110,115,120,125,130,140,154,168,230,247,255,255,255,255]
green = [0,24,28,32,36,40,43,46,49,52,55,58,61,64,76,88,100,105,110,115,120,125,130,140,154,168,230,247,255,255,255,255]
blue = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,50,80,110,140]

for i in range(32):
    pallette = [red[i],green[i],blue[i]]

for i in pallette:
    print(i)
""" #Three iterables are passed
redgreenblue = zip(red,green,blue)

# Converting itertor to set
redgreenblueSet = set(redgreenblue)
for a in redgreenblueSet:
    print(a)
# Test getting RGB values in Palette
 """
print()
#PNG
im1 = Image.open('Original/png0000.png')
pixel_png_256 = list(im1.getdata())
#Get colors in PNG file
""" for i in range(100):
    print(pixel_png_256[i]) """
#Test getting pixel colors

#Ausblenden unuseable Pixels
""" for i in pixel_png_256: 
    for a in pallette:
        if i[0] == a[0] and i[1] == a[1] and i[2] == a[2]:
            continue
        else:
            i == [0,0,0] """
    

rgb_from_png_256 = list(dict.fromkeys(pixel_png_256))
# Remove duplicates in pixel_png_256 -> Export as rgb_from_png_256
for i in rgb_from_png_256:
    print(i)

print(set(pallette) & set(rgb_from_png_256))

print("Length of blended unused colors: ", len(rgb_from_png_256))
