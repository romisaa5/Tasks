import cv2
from matplotlib import pyplot as plt

gray_img = cv2.imread('robot.jpg', 0)

inv_img1 = 255 - gray_img
inv_img2 = cv2.bitwise_not(gray_img)

plt.subplot(1, 3, 1)
plt.imshow(gray_img, cmap='gray')
plt.title('gray img')

plt.subplot(1, 3, 2)
plt.imshow(inv_img1, cmap='gray')
plt.title('inv_img1')

plt.subplot(1, 3, 3)
plt.imshow(inv_img2, cmap='gray')
plt.title('inv_img2')

plt.show()
cv2.waitKey()
cv2.destroyAllWindows()