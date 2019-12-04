import sys
from PIL import Image

assert len(sys.argv) == 3, "Please specify an input path and output path"

input_path = sys.argv[1]
output_path = sys.argv[2]

img = Image.open(input_path)
width, height = img.size

# Create a new, all-white image that's the same size as the original
new_img = Image.new("RGB", (width, height), "white")

# TODO: Replace this with your own filter!
for i in range(width // 2, width):
    for j in range(1, height // 2):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (0, 0, b))

for i in range(1, width // 2):
    for j in range(1, height // 2):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (r, r, r))

for i in range(width // 2, width):
    for j in range(height // 2, height):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (r, 0, 0))

for i in range(1, width // 2):
    for j in range(height // 2, height):
        r, g, b = img.getpixel((i, j))
        new_img.putpixel((i, j), (0, g, 0))

new_img.save(output_path, "JPEG")
