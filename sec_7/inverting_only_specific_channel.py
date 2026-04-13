from PIL import Image
import numpy as np


image_path = "robot.jpg"
image1 = Image.open(image_path)
image1.show()
image = Image.open(image_path).convert("RGB")  


image_array = np.array(image)


inverted_image_array = 255 - image_array
inverted_image_array[:, :, 1] = 255 - image_array[:, :, 1]  


inverted_image = Image.fromarray(inverted_image_array)
inverted_image.show()