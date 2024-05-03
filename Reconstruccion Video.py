###################################################################
## CODE TO COMPILE SEGMENTATION 

import cv2
import os

Carpeta = "segmented_images/"
files = os.listdir(Carpeta) # Get a list of all filenames in the folder
files.sort() # Order

# I need the height and width of each frame  
frame = cv2.imread(os.path.join(Carpeta, files[0]))
height, width, channels = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v') # I give you the extension I need
out = cv2.VideoWriter('video_reconstruido.mp4', fourcc, 25, (width, height)) 

for filename in files:
    img_path = os.path.join(Carpeta, filename)
    frame = cv2.imread(img_path)

    out.write(frame) # Add frame to video

out.release()
