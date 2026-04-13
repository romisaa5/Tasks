from PIL import Image


image = Image.open("robot.jpg").convert("RGB")


red_channel, green_channel, blue_channel = image.split()

red_channel.show()
green_channel.show()
blue_channel.show()


merged_image = Image.merge("RGB", (red_channel, green_channel, blue_channel))


merged_image.show()