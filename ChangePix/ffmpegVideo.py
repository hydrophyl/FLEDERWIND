import os, os.path

imageDirectory = "PNGImages" #change here to change the image directory
imagesNameList = [filename for filename in os.listdir(imageDirectory)]
imagesNameList.sort()
os.system("ffmpeg -framerate 10 -i " + imageDirectory + "/" + imagesNameList[0][:-7] + "%03d.png " + "Zusammenfassung.mp4") #when bmp images are used, change png to bmp.

# Example: we have 300 images and these are named as cap_00000001.png to cap_00000300.png
# imagesNameList[0] = cap_00000001.png -> imagesNameList[0][:-7] = cap_00000 -> imagesNameList[0][:-7] + "%03d.png" = cap_00000001.png to cap_00000999.png *just to 300 because of limited files
