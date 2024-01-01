
import cv2
import numpy as np

img1 = cv2.resize(cv2.imread('images/mountain.webp'), (300,200))
img2 = cv2.resize(cv2.imread('images/road.jpg'), (300,200))
img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)



hor = np.hstack((img1, img2))

cv2.imshow("Images", hor)


cv2.imshow("Road", img2)

cv2.waitKey(0)
something = np.ones((3,3), np.uint8)
cap = cv2.VideoCapture(1)

while True:
    success, video = cap.read()
    cv2.imshow("Rustam", video)
    video = cv2.cvtColor(video, cv2.COLOR_RGB2GRAY)
    cv2.imshow("Rustam Gray color", video)
    video = cv2.Canny(video, 100, 200)
    imgDialation = cv2.dilate(video, kernel=something, iterations=1)
    
    
    cv2.imshow("Video Capture", video)
    cv2.imshow("Second window", imgDialation)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
