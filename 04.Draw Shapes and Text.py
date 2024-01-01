import cv2
import numpy as np

img = np.ones((512,512,3), dtype=np.uint8)

cv2.line(img, (0,0), (512,512), (0,100,0), thickness=3)
    
cv2.rectangle(img, (100,200),(400, 500), color=(0,0,189), thickness=-3)

cv2.circle(img, (100,200), 50, color=(123,0,0), thickness=cv2.FILLED)

cv2.putText(img, "Qandaydir tekst", (100,350), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(0,150,0))

cv2.imshow("First blank image", img)

cv2.waitKey(0)
