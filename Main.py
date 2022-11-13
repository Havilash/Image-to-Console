from PIL import Image
import io
import requests
from colors import COLORS

cmd_width = 256
cmd_height = 50
# os.system("mode " + str(cmd_width) + ", " + str(cmd_height))

# https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg

inp = input("Image: ")
if inp != "":
    try:
        image = Image.open(inp, "r")
    except:
        response = requests.get(inp)
        print(response.url, "\n")
        image_bytes = io.BytesIO(response.content)
        image = Image.open(image_bytes)
else:
    response = requests.get("https://picsum.photos/100/100")
    print(response.url, "\n")
    image_bytes = io.BytesIO(response.content)
    image = Image.open(image_bytes)

image = image.convert("LA")
pixel = list(image.getdata())

width, height = image.size

for i in range(height):
    for j in range(width):
        pixel_val = pixel[(i * width) + j][0]
        color = int(pixel_val / 255 * (len(COLORS) - 1))
        try:
            if pixel[(i * width) + j][1] != 0:
                print(COLORS[color], end="")
            else:
                print("  ", end="")
        except IndexError:
            print(COLORS[color], end="")
    print(end="\n")
