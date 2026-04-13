from PIL import Image
import numpy as np


image_path = "robot.jpg"
image1 = Image.open(image_path)
image = Image.open(image_path).convert("L")  


image_array = np.array(image)


inverted_image_array = 255 - image_array


inverted_image = Image.fromarray(inverted_image_array)
image1.show()
inverted_image.show()  