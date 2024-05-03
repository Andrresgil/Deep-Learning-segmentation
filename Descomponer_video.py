#############
## CODE TO DECOMPOSE VIDEO INTO FRAMES  
## I RECOMMEND HAVING THE VIDEO PREVIOUSLY DOWNLOADED TO THE PC.

import cv2 

cap = cv2.VideoCapture('Video_0_Produce.mp4') #RENAME VIDEO

frame_count = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    # If there are no more frames, stop the iteration.
    if not ret:
        break
    cv2.imwrite('Mi Viaje_{}.jpg'.format(frame_count), frame)
    frame_count += 1
    cv2.waitKey(250)

cap.release()
cv2.destroyAllWindows()
