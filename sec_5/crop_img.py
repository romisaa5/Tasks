
import cv2

img = cv2.imread('robot.jpg')
cropped = img[10:200, 100:500]

cv2.imshow('image', img)
cv2.imshow('cropped', cropped)
cv2.waitKey()
print(cropped.shape)
cv2.destroyAllWindows()