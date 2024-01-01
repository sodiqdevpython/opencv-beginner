
def s(a):
    cv2.waitKey(a*1000)
    cv2.destroyAllWindows()

#                     Image Read

import cv2

img = cv2.imread('images/loki.jpg')

img = cv2.resize(img, (500, 300))

cv2.imshow("Loki Image", img)

s(2)

print('Destroyed')


#                    Video Read

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
