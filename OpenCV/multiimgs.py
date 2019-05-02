import cv2
import os, os.path

print (cv2.__version__)

imageDir = "RadarbilderProbe/" #specify your path here
image_path_list = []
valid_image_extensions = [".bmp"] #specify your valid extensions here
valid_image_extensions = [item.lower() for item in valid_image_extensions]

for file in os.listdir(imageDir):
    extension = os.path.splitext(file)[1]
    if extension.lower() not in valid_image_extensions:
        continue
    image_path_list.append(os.path.join(imageDir, file))

for imagePath in image_path_list:
    img = cv2.imread(imagePath)
    if img is None:
        continue

    cv2.imshow(imagePath, img)
    
    key = cv2.waitKey(0) & 0xFF
    if key == 27: # escape
        break

cv2.destroyAllWindows()