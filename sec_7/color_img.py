from PIL import Image
import numpy as np


image_path = "arobot.jpg"
image1 = Image.open(image_path)
image = Image.open(image_path).convert("RGB")  


image_array = np.array(image)


inverted_image_array = 255 - image_array


inverted_image = Image.fromarray(inverted_image_array)
image1.show()
inverted_image.show()  