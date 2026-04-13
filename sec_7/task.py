from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


image_path = "assets/5.jpg"
image = Image.open(image_path).convert("RGB")
image_array = np.array(image)
inverted_array = 255 - image_array
inverted_image = Image.fromarray(inverted_array)


rotated_image = inverted_image.transpose(Image.ROTATE_90)


combined_width = image.width + rotated_image.width
combined_height = max(image.height, rotated_image.height)
combined = Image.new("RGB", (combined_width, combined_height))
combined.paste(image, (0, 0))
combined.paste(rotated_image, (image.width, 0))
combined.show()