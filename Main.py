from PIL import Image
import os

COLORS = ["--", "**", "OO", "00", r"%%", "##"]
cmd_width = 256
cmd_height = 50
os.system('mode ' + str(cmd_width) + ', '+ str(cmd_height))
os.system(r"C:\Users\havil\Documents\Projects\Python\ImageToConsole\myfile.png")
image_file = Image.open('Japan_small_icon.png', 'r')
pixel_rgb = list(image_file.getdata())

print(pixel_rgb)
width, height = image_file.size
# print(width, height)

for i in range(height):
    for j in range(width):
        pixel_val = (pixel_rgb[i*j][0]+pixel_rgb[i*j][1]+pixel_rgb[i*j][2])/3
        color = int(pixel_val/255*(len(COLORS)-1))
        # print(color)
        if pixel_rgb[i*j][3] != 0:
            print(COLORS[color], end="")
        else:
            print("  ", end="")
    print(end='\n')