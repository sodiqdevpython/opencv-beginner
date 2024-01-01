import cv2

cap = cv2.VideoCapture(0)

width = 400
height = 300

cap.set(3, width)
cap.set(4, height)

while True:
    success, video = cap.read()
    video = cv2.resize(video, (width, height))
    video = cv2.Canny(video, 100, 200)
    cv2.imshow("Winname", video)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()