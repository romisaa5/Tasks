from PIL import Image, ImageFilter, ImageEnhance
import matplotlib.pyplot as plt


image_path = r"robot.jpg"
image = Image.open(image_path)


resized_image = image.resize((200, 200))

rotated_image = image.rotate(45)

grayscale_image = image.convert("L")

blurred_image = image.filter(ImageFilter.BLUR)

enhancer = ImageEnhance.Brightness(image)
bright_image = enhancer.enhance(1.5)  

bright_image.save("modified_image.jpg")


plt.subplot(2, 3, 1)
plt.title('Original Image')
plt.imshow(image)
plt.axis('off')  


plt.subplot(2, 3, 2)
plt.title('Resized Image')
plt.imshow(resized_image)
plt.axis('off')


plt.subplot(2, 3, 3)
plt.title('Rotated Image')
plt.imshow(rotated_image)
plt.axis('off')


plt.subplot(2, 3, 4)
plt.title('Grayscale Image')
plt.imshow(grayscale_image, cmap='gray') 
plt.axis('off')