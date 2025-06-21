import tkinter as tk
from PIL import Image, ImageTk
import base64
from turtle import Turtle, Screen


# question 6.1.3
def show_image_popup():
    popup = tk.Toplevel(root)
    popup.title("Image Popup")

    # Load JPG image using pil
    pil_image = Image.open("image.jpg")
    tk_image = ImageTk.PhotoImage(pil_image)

    label = tk.Label(popup, image=tk_image)
    label.image = tk_image
    label.pack()

    close_btn = tk.Button(popup, text="Close", command=popup.destroy)
    close_btn.pack()

root = tk.Tk()
root.title("Main Window")

button = tk.Button(root, text="Show Image", command=show_image_popup)
button.pack(pady=20)

#root.mainloop()

# question 6.1.4
secret = "CgkJICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAuLS0tW1tfX11dLS0tLS4KICAgICAgICAgICAgICA7LS0tLS0tLS0tLS0tLS" \
         "58ICAgICAgIF9fX18KICAgICAgICAgICAgICB8ICAgICAgICAgICAgIHx8ICAgLi0tW1tfX11dLS0tLgogICAgICAgICAgICAgIHwgICAg" \
         "ICAgICAgICAgfHwgIDstLS0tLS0tLS0tLS58CiAgICAgICAgICAgICAgfCAgICAgICAgICAgICB8fCAgfCAgICAgICAgICAgfHwKICAgIC" \
         "AgICAgICAgICB8X19fX19fX19fX19fX3wvICB8ICAgICAgICAgICB8fAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHxfX19fX" \
         "19fX19fX3wvCgo="


def decode_secret(msg: str) -> str:
    decoded_data = base64.b64decode(msg.encode()).decode("utf-8")
    return decoded_data

print(decode_secret(secret))


# question 6.3.3
from gtts import gTTS
import os

mytext = "first time i'm using a package in next.py course "
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file
myobj.save("welcome.mp3")

# Playing the converted file
os.system("start welcome.mp3")


# question 6.4
from turtle import Turtle


def draw_dots_art(first: tuple, second: tuple) -> None:

    turtles: list[Turtle] = [Turtle(), Turtle(), Turtle()]
    colors = ["red", "purple", "white"]

    list(map(lambda t: t.speed(100), turtles))


    turtles[0].screen.bgcolor("black")

    for tnum, turtle in enumerate(turtles):
        # Set the new coordinate system: (0, 0) is top-left, (600, 400) is bottom-right
        turtle.screen.setworldcoordinates(0, 400, 600, 0)
        turtle.pencolor(colors[tnum])

        turtle.penup()

        turtle.pensize(1)

        turtle.setx(first[0])
        turtle.sety(first[1])

        turtle.pendown()

        for i in range(2, len(first), 2):
            turtle.goto(first[i] + tnum * 4, first[i + 1] + tnum * 4)

        turtle.penup()
        turtle.setx(second[0])
        turtle.sety(second[1])
        turtle.pendown()

        for i in range(2, len(second), 2):
            turtle.goto(second[i] + tnum * 4, second[i + 1] + tnum * 4)

    # prevent instant closer
    input()



# list of dots, in the following format: [x, y, x, y, x, y,...]
first = (
    146, 399, 163, 403, 170, 393, 169, 391, 166, 386, 170, 381, 170, 371, 170,
    355, 169, 346, 167, 335, 170, 329, 170, 320, 170, 310, 171, 301, 173, 290,
    178, 289, 182, 287, 188, 286, 190, 286, 192, 291, 194, 296, 195, 305, 194,
    307, 191, 312, 190, 316, 190, 321, 192, 331, 193, 338, 196, 341, 197, 346,
    199, 352, 198, 360, 197, 366, 197, 373, 196, 380, 197, 383, 196, 387, 192,
    389, 191, 392, 190, 396, 189, 400, 194, 401, 201, 402, 208, 403, 213, 402,
    216, 401, 219, 397, 219, 393, 216, 390, 215, 385, 215, 379, 213, 373, 213,
    365, 212, 360, 210, 353, 210, 347, 212, 338, 213, 329, 214, 319, 215, 311,
    215, 306, 216, 296, 218, 290, 221, 283, 225, 282, 233, 284, 238, 287, 243,
    290, 250, 291, 255, 294, 261, 293, 265, 291, 271, 291, 273, 289, 278, 287,
    279, 285, 281, 280, 284, 278, 284, 276, 287, 277, 289, 283, 291, 286, 294,
    291, 296, 295, 299, 300, 301, 304, 304, 320, 305, 327, 306, 332, 307, 341,
    306, 349, 303, 354, 301, 364, 301, 371, 297, 375, 292, 384, 291, 386, 302,
    393, 324, 391, 333, 387, 328, 375, 329, 367, 329, 353, 330, 341, 331, 328,
    336, 319, 338, 310, 341, 304, 341, 285, 341, 278, 343, 269, 344, 262, 346,
    259, 346, 251, 349, 259, 349, 264, 349, 273, 349, 280, 349, 288, 349, 295,
    349, 298, 354, 293, 356, 286, 354, 279, 352, 268, 352, 257, 351, 249, 350,
    234, 351, 211, 352, 197, 354, 185, 353, 171, 351, 154, 348, 147, 342, 137,
    339, 132, 330, 122, 327, 120, 314, 116, 304, 117, 293, 118, 284, 118, 281,
    122, 275, 128, 265, 129, 257, 131, 244, 133, 239, 134, 228, 136, 221, 137,
    214, 138, 209, 135, 201, 132, 192, 130, 184, 131, 175, 129, 170, 131, 159,
    134, 157, 134, 160, 130, 170, 125, 176, 114, 176, 102, 173, 103, 172, 108,
    171, 111, 163, 115, 156, 116, 149, 117, 142, 116, 136, 115, 129, 115, 124,
    115, 120, 115, 115, 117, 113, 120, 109, 122, 102, 122, 100, 121, 95, 121,
    89, 115, 87, 110, 82, 109, 84, 118, 89, 123, 93, 129, 100, 130, 108,
    132, 110, 133, 110, 136, 107, 138, 105, 140, 95, 138, 86, 141, 79, 149,
    77, 155, 81, 162, 90, 165, 97, 167, 99, 171, 109, 171, 107, 161, 111,
    156, 113, 170, 115, 185, 118, 208, 117, 223, 121, 239, 128, 251, 133, 259,
    136, 266, 139, 276, 143, 290, 148, 310, 151, 332, 155, 348, 156, 353, 153,
    366, 149, 379, 147, 394, 146, 399
)
second = (
    156, 141, 165, 135, 169, 131, 176, 130, 187, 134, 191, 140, 191, 146, 186,
    150, 179, 155, 175, 157, 168, 157, 163, 157, 159, 157, 158, 164, 159, 175,
    159, 181, 157, 191, 154, 197, 153, 205, 153, 210, 152, 212, 147, 215, 146,
    218, 143, 220, 132, 220, 125, 217, 119, 209, 116, 196, 115, 185, 114, 172,
    114, 167, 112, 161, 109, 165, 107, 170, 99, 171, 97, 167, 89, 164, 81,
    162, 77, 155, 81, 148, 87, 140, 96, 138, 105, 141, 110, 136, 111, 126,
    113, 129, 118, 117, 128, 114, 137, 115, 146, 114, 155, 115, 158, 121, 157,
    128, 156, 134, 157, 136, 156, 136
)

draw_dots_art(first, second)