
import cv2

img = cv2.imread('robot.jpg')

# x1,y1 = start point | x2,y2 = end point
cropped = img[10:200, 100:500]

cv2.imshow('image', img)
cv2.imshow('cropped', cropped)
cv2.waitKey()
print(cropped.shape)
cv2.destroyAllWindows()