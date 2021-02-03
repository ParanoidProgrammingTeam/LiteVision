import cv2
import numpy as np
import matplotlib as plt

img = cv2.imread('OpenCV/Photos/frc.png', cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_green = np.array([60, 180, 150])
upper_green = np.array([80, 255, 255])

mask = cv2.inRange(hsv, lower_green, upper_green)

contours, hieararchy = cv2.findContours(mask, cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.imshow('mask', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()