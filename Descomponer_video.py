#############
## Codigo para descomponer el video en frames 

import cv2

cap = cv2.VideoCapture('Video_0_Produce.mp4')

frame_count = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    # Si no hay más fotogramas, detén la iteración
    if not ret:
        break
    cv2.imwrite('Mi Viaje_{}.jpg'.format(frame_count), frame)
    frame_count += 1
    cv2.waitKey(250)

cap.release()
cv2.destroyAllWindows()
