from PIL import Image

image = Image.open("lenna.jpg")
rgb_image = image.convert("RGB")

red, green, blue = rgb_image.split()

left_crop = 30
left_crop_half = left_crop/2
right_crop = 512 - left_crop_half

coordinates = (left_crop, 0, red.width, red.height)
r_crop_right = red.crop(coordinates)

coordinates = (left_crop_half, 0, right_crop, red.height)
r_crop_left = red.crop(coordinates)

r_blended = Image.blend(r_crop_right, r_crop_left, 0.4)

coordinates = (0, 0, 482, blue.height)
b_crop_right = blue.crop(coordinates)

coordinates = (left_crop_half, 0, right_crop, blue.height)
b_crop_left = blue.crop(coordinates)

b_blended = Image.blend(b_crop_right, b_crop_left, 0.4)

coordinates = (left_crop_half, 0, right_crop, green.height)
green_crop = green.crop(coordinates)

final_lenna = Image.merge("RGB", (r_blended, green_crop, b_blended))
final_lenna.save('final_lenna.jpg')
final_lenna.thumbnail((80, 80))
final_lenna.save('final_lenna_thmb.jpg')
