import cv2

img = cv2.imread('robot.jpg')

# Flip أفقي (فوق لتحت)
flipped_h = cv2.flip(img, 0)
cv2.imshow('Flip (Horizontal)', flipped_h)
cv2.waitKey(0)

# Flip رأسي (يمين لشمال)
flipped_v = cv2.flip(img, 1)
cv2.imshow('Flip (Vertical)', flipped_v)
cv2.waitKey(0)

# Flip في الاتجاهين
flipped_both = cv2.flip(img, -1)
cv2.imshow('Flip (Both)', flipped_both)
cv2.waitKey(0)

cv2.destroyAllWindows()