import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# cap = cv2.imread("./1.jpg")
while (1):
    ret, image = cap.read()
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower = np.array([100, 60, 100])
    upper = np.array([120, 120, 180])

    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow('image', image)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    # cv2.waitKey(0)
    k = cv2.waitKey(5) & 0xff
    if k == 27:
        break
cv2.destroyAllWindows()
