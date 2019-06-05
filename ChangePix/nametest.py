import os, os.path
imDir = "A_LearnData/8"
imNames = [f for f in os.listdir(imDir)]
imNames.sort()

print("="*80)
print("ffmpeg -framerate 24 -i " + imDir + "/" + imNames[0][:4] + "%08d.png " + "speed.mp4")
#os.system("ffmpeg -framerate 24 -i " + imDir + "/" + imNames[0][:4] + "%08d.bmp " + "speed.mp4")
