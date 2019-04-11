
""" 11/4/2019 """

""" Author: Duy Nguyen """

from PIL import Image
#NOTE Definition useable colors
red = [0,24,28,32,36,40,43,46,49,52,55,58,61,64,76,88,100,105,110,115,120,125,130,140,154,168,230,247,255,255,255,255]
green = [0,24,28,32,36,40,43,46,49,52,55,58,61,64,76,88,100,105,110,115,120,125,130,140,154,168,230,247,255,255,255,255]
blue = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,50,80,110,140]

#NOTE Get colors in PNG file
im1 = Image.open('Original/png0000.png')
data_png_256 = list(im1.getdata())
#print()
#NOTE compare two list
""" print(red)
print(green)
for i in red:
    if i in red and i in green:
        print(i)
    else:
        print("no") """

#print()
#NOTE This function makes the same values in one list disappear too !!!!
#ANCHOR  print(set(red) & set(green)) 

#NOTE Make tuple palette with zip function
palette = zip(red,green,blue)
for i in palette:
    print(i)
#NOTE Now palette hat the same structur as exported RGB values from images 

#NOTE Now compare two lists: color from pixels and palette.
""" for i in data_png_256:
    if i not in data_png_256 and i not in palette:
        i = [0,0,0]
    else:
        pass
print(data_png_256) """
#FIXME  It takes a lot of time to print and to stay with this loop

#TODO Manually take the 39-32=7 unuseable color and convert to [0,0,0]
#NOTE Define the unuseable colors
un_color_1 = [255,255,0]
un_color_2 = [255,255,255]
un_color_3 = [0,255,0]
un_color_4 = [255,170,0]
un_color_5 = [70,70,70]
un_color_6 = [0,255,255]
un_color_7 = [16,16,16]

for i in data_png_256:
    if i == un_color_1 or i == un_color_2 or i == un_color_3 or i == un_color_4 or i == un_color_5 or i == un_color_6 or i == un_color_7:
        i = [0,0,0]
    else:
        pass

#print(data_png_256)
#REVIEW It take not litte but good amount of time to do this loop and print
#REVIEW With no print data much faster :v
print()
#TODO Test the output
#NOTE remove duplicates to test the amount of colors in data
rgb_from_png_256 = list(dict.fromkeys(data_png_256))
for i in rgb_from_png_256:
    print(i)

#FIXME Not working.. Scheisse