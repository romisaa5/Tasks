import cv2

img = cv2.imread('robot.jpg')

# تدوير 90 درجة في اتجاه عقارب الساعة
rotated_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('Rotated Image', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()