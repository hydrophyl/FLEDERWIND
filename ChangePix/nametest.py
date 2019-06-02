import os, os.path
imDir = "Radarbilder"
imNames = [f for f in os.listdir(imDir)]
imNames.sort()

print("ffmpeg -framerate 24 -i " + imDir + "/" + imNames[0][:4] + "%08d.png " + "speed.mp4")
os.system("ffmpeg -framerate 24 -i " + imDir + "/" + imNames[0][:4] + "%08d.bmp " + "speed.mp4")
