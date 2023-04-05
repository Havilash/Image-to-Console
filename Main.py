import cv2
from PIL import Image
import io
import requests
from colors import COLORS
import os
import time

# CMD_WIDTH = 256
# CMD_HEIGHT = 50
# os.system("mode " + str(CMD_WIDTH) + ", " + str(CMD_HEIGHT))

# https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885__480.jpg


def image_to_console(image: Image.Image):
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


def main():
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

    image_to_console(image)


def cam():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    while True:
        os.system("cls")
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("test", img)
        img_pil = Image.fromarray(img)
        img_pil = img_pil.resize((300, 150))
        image_to_console(img_pil)

        k = cv2.waitKey(30)
        if k % 256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break

    cam.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    cam()
