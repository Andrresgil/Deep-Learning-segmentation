###########################################################3
## Codigo para segmentar imagenes 

import cv2
import os

#creo la carpeta 
if not os.path.exists('segmented_images'):
    os.makedirs('segmented_images')

for filename in os.listdir():
    if filename.endswith('.jpg'): 
        
        imgColor = cv2.imread(filename)
        imgColor = cv2.cvtColor(imgColor, cv2.COLOR_BGR2RGB)

        uhr = 200
        ulr = 180

        uhg = 200
        ulg = 180

        uhb = 200
        ulb = 180

        img_Color_Seg = cv2.inRange(imgColor, (ulr, ulg, ulb), (uhr, uhg, uhb))
        cv2.imwrite('segmented_images/' + filename, img_Color_Seg)



