from PIL import Image
import matplotlib.pyplot as plt


image_path = "assets/5.jpg"
image = Image.open(image_path)


flipped_horizontal = image.transpose(Image.FLIP_LEFT_RIGHT)


flipped_vertical = image.transpose(Image.FLIP_TOP_BOTTOM)


plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image)
plt.axis('off')  


plt.subplot(1, 3, 2)
plt.title('flipped_horizontal')
plt.imshow(flipped_horizontal)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('flipped_vertical')
plt.imshow(flipped_vertical)
plt.axis('off')