import cv2
import numpy as np

img = cv2.imread('salt-and-pepper-robot.jpg', cv2.IMREAD_COLOR)

filtered_img = cv2.medianBlur(img, 3)  # kernel size 3x3

cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', filtered_img)

cv2.waitKey(0)
cv2.destroyAllWindows()