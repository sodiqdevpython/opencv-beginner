#                GRAY ga o'tkazish
   

import cv2
from matplotlib import pyplot as plt


img = cv2.imread('images/loki.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


plt.imshow(img, cmap='gray')

plt.show()


#               BLUR ga o'tkazish

import cv2

img = cv2.resize(cv2.imread('images/loki.jpg'), (300,300))
blurImg = cv2.resize(cv2.GaussianBlur(img, (7,7), 0), (300,300))

cv2.imshow("Oddiy holatdagi", img)
cv2.imshow("Blur", blurImg)

cv2.waitKey(0)


#             Canny ga o'tkazish


import cv2

img = cv2.resize(cv2.imread('images/mountain.webp'), (500,300))

img = cv2.Canny(img, 100,200)

cv2.imshow("Loki", img)

cv2.waitKey(0)



import cv2
import numpy as np

nimadir = np.ones((3,3), np.uint8)

img = cv2.resize(cv2.imread('images/mountain.webp'), (400, 200))

imgBlur = cv2.GaussianBlur(img, (7,7), 0)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

imgGray2 = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)

imgCanny = cv2.Canny(imgBlur, 100, 200)

imgDialation = cv2.dilate(imgCanny, kernel=nimadir, iterations=1)

cv2.imshow("Mountain", img)
cv2.imshow("Mountain Blur", imgBlur)
cv2.imshow("Mountain Gray", imgGray)
cv2.imshow("Mountain Gray 2", imgGray2)
cv2.imshow("Mountain Canny", imgCanny)
cv2.imshow("Boshqacharoq", imgDialation)



cv2.waitKey(0)
