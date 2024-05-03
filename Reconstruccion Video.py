import cv2
import os

Carpeta = "segmented_images/"
files = os.listdir(Carpeta) # Obtener una lista de todos los nombres de archivo en la carpeta
files.sort() # Ordenar

# Necesito la altura y el ancho de cada frame 
frame = cv2.imread(os.path.join(Carpeta, files[0]))
height, width, channels = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Le doy la extension que necesito 
out = cv2.VideoWriter('video_reconstruido.mp4', fourcc, 25, (width, height)) # es 25 fotogramas para la creacion del video

for filename in files:
    img_path = os.path.join(Carpeta, filename)
    frame = cv2.imread(img_path)

    out.write(frame) # Agregar el fotograma al video

out.release()