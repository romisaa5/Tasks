import cv2

original_img = cv2.imread('robot.jpg')
cv2.imshow('My Img', original_img)


gray_img = cv2.imread('robot.jpg', 0)
cv2.imshow('gray img', gray_img)


half_img = cv2.resize(original_img, (0, 0), fx=0.5, fy=0.5)
cv2.imshow('half size', half_img)


scale_img = cv2.resize(original_img, (500, 600))
cv2.imshow('scale_img', scale_img)


stretch_img = cv2.resize(original_img, (500, 600), interpolation=cv2.INTER_NEAREST)
cv2.imshow('stretch_img', stretch_img)

cv2.waitKey()
cv2.destroyAllWindows()