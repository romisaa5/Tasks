import cv2

img = cv2.imread("robot.jpg")

b, g, r = cv2.split(img)

cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

merged = cv2.merge((b, g, r))

cv2.imshow("Merged Image", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()