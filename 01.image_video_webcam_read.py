def s(a):
    cv2.waitKey(a*1000)
    cv2.destroyAllWindows()

#!                     Image Read

import cv2

img = cv2.imread('images/loki.jpg')

img = cv2.resize(img, (500, 300))

cv2.imshow("Loki Image", img)

s(2)

# print('Destroyed')


#!                     Video Read

import cv2

video = cv2.VideoCapture('videos/musk.mp4')
w = 640
h = 360

while True:
    success, target = video.read()
    cv2.imshow("Elon Musk", target)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


import cv2

frameW = 640
frameH = 480

capture = cv2.VideoCapture('videos/musk.mp4')
capture.set(3, frameW)
capture.set(4, frameH)

while True:
    success, video = capture.read()
    video = cv2.resize(video, (frameW, frameH))
    cv2.imshow("Myself", video)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


capture.release()
cv2.destroyAllWindows()

#?  Homework 

# 1.Get image and resize it 
# 2.Simple video reader 
# 3.Capture read and resize it

# Task 1  --done

"""
import cv2

img = cv2.imread('images/mountain.webp', 0)

img = cv2.resize(img, (300,300))

cv2.imshow("winname", img)

cv2.waitKey(0)
"""


# Task 2 


import cv2

vid = cv2.VideoCapture('images/loki.jpg')
h = 200
w = 200

vid.set(3, w)
vid.set(4, h)

while True:
    success, video = vid.read()
    video = cv2.resize(video, (w,h))
    cv2.imshow("This is Elon Musk", video)
    print(success)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()

# Task 3


import cv2

cap = cv2.VideoCapture(0)

w = 200
h = 200

cap.set(3,w)
cap.set(4,h)

while True:
    success, video = cap.read()
    video = cv2.resize(video, (w,h))
    video = cv2.cvtColor(video, cv2.COLOR_RGB2GRAY)
    
    cv2.imshow("winname", video)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()