import cv2
from matplotlib import pyplot as plt

img = cv2.resize(cv2.imread('images/mountain.webp'), (500,300))
imgCroped = img[100:200, 100:400]

plt.imshow(img)
plt.show()



cv2.imshow("winname", img)
cv2.imshow("second", imgCroped)



cv2.waitKey(0)



#            Practice

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/road.jpg')
imgCroped = img[200:400, 250:300]
imgCroped = cv2.resize(imgCroped, (img.shape[1], img.shape[0]))

plt.subplot(1,2,1)
plt.imshow(img)

plt.subplot(1,2,2)
plt.imshow(imgCroped)

plt.show()

cv2.imshow("Normal image", img)
cv2.imshow("Croped image", imgCroped)

cv2.waitKey(0)
