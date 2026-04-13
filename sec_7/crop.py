from PIL import Image


image_path = "robot.jpg"
image = Image.open(image_path)


crop_box = (200, 200, 400, 400) 


cropped_image = image.crop(crop_box)

cropped_image.show()