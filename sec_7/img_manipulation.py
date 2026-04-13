from PIL import Image


img = Image.open('robot.jpg')

flipped_lr = img.transpose(Image.FLIP_LEFT_RIGHT)


flipped_tb = img.transpose(Image.FLIP_TOP_BOTTOM)


rotated_90 = img.transpose(Image.ROTATE_90)


rotated_180 = img.transpose(Image.ROTATE_180)


transposed = img.transpose(Image.TRANSPOSE)


transposed.save('output.jpg')


im = Image.open("robot.jpg")

rgb_im = im.convert('RGB')
rgb_im.save('robot_new.jpg')
print("Image saved successfully ...")


im = Image.open(r"robot.jpg")


width, height = im.size


left = 5
top = height / 4
right = 164
bottom = 3 * height / 4


im1 = im.crop((left, top, right, bottom))


im1.show()