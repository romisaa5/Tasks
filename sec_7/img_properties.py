from PIL import Image, ImageFilter, ImageEnhance


image = Image.open("robot.jpg")
print("Size:", image.size)
print("Mode:", image.mode)
print("Format:", image.format)
image.show()