import numpy as np
from PIL import Image
from collections import defaultdict
from tkinter import filedialog
import tkinter as tk

colours = ["white"] * 10
colour_displays = []


def get_image():
    image = Image.open(filedialog.askopenfilename(filetypes=[('Allowed Types', '*.jpeg *.jpg *.png')]))
    data = np.array(image)
    count_colors(data, number_of_colours=10)


def count_colors(img, number_of_colours):
    img = img.reshape(-1, img.shape[-1])
    color = defaultdict(int)

    for pixel in img:
        rgb = (pixel[0], pixel[1], pixel[2])
        color[rgb] += 1

    sorted_color = sorted(color.items(), key=lambda k_v: k_v[1], reverse=True)
    sorted_color = sorted_color[:number_of_colours]

    update_colours(sorted_color)


def show_colours():
    global colour_displays
    count = 0
    colour_displays = []
    for colour in colours:
        colour_displays.append(tk.Canvas(bg=colour, width=90, height=80))
        colour_displays[count].grid(row=2, column=count, padx=10)
        count += 1


def update_colours(colour_list):
    rgb_list = [value[0] for value in colour_list]
    count = 0
    for rgb in rgb_list:
        position_text = tk.Label(fg="white", text=f"{colour_list[count][1]} pixels")
        position_text.grid(row=1, column=count, padx=10)

        hex_colour = "#%02x%02x%02x" % rgb
        colour_displays[count].configure(bg=hex_colour)

        value_text = tk.Label(fg="white", text=hex_colour)
        value_text.grid(row=3, column=count, padx=10, pady=(0, 20))
        count += 1


window = tk.Tk()
window.title("Image Colour Finder")

button = tk.Button(text="Upload image", command=get_image, width=10, height=2, font=("Arial", 15, "bold"))
button.grid(row=0, column=4, columnspan=2, pady=10)

show_colours()

window.mainloop()
