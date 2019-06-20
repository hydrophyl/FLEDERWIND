import os, os.path

imageDirectory = "PNGImages" #change here to change the image directory
imagesNameList = [filename for filename in os.listdir(imageDirectory)]
imagesNameList.sort()
os.system("ffmpeg -framerate 5 -i " + imageDirectory + "/" + imagesNameList[0][:-7] + "%03d.png " + "ffmpeg20fps.mp4") #when bmp images are used, change png to bmp.

