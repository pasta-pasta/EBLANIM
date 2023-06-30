import textwrap

import numpy as np
from PIL import Image, ImageDraw, ImageFont


task = input("Введите задание: ")

# Создаем базу с квадратом и номером
w, h = 1920, 1400
back = (255, 255, 255)
base_image = Image.new("RGB", (w, h), back)
draw = ImageDraw.Draw(base_image)
font = ImageFont.truetype("timesbd.ttf", 35)
text = str(task)
textw, texth = draw.textsize(text, font=font)

padding = 10
rect_x0, rect_y0 = 20, 25
rect_x1 = max(rect_x0 + textw + 2 * padding, 105)
rect_y1 = max(rect_y0 + texth + 2 * padding, 70)

for i in range(2):
    draw.rectangle((rect_x0 + i, rect_y0 + i, rect_x1 - i, rect_y1 - i), fill=back, outline="black")

x = rect_x0 + ((rect_x1 - rect_x0) - textw) / 2
y = rect_y0 + ((rect_y1 - rect_y0) - texth) / 2
draw.text((x, y), text, font=font, fill="black")



# Пишем текст
font = ImageFont.truetype("times.ttf", 30)
text = open("text.txt", encoding="UTF-8").read()
pad_left = rect_x1 + 20
pad_right = pad_left / 2
max_width = w - (pad_right + pad_left)

text_width = draw.textsize('A', font=font)[0]  # Ширина одной буквы
chars_per_line = int(max_width // text_width)  # Ширина строки в символах


currentstroka = ""
currenth, line_spacing = 40, 5
x = pad_left
for i in text:
    if draw.textsize(currentstroka, font=font)[0] >= max_width or i == "\n":
        if i == " " or i == "\n":
            currenth += 33 + line_spacing
            currentstroka = ""
            x = pad_left
            continue
        elif i == "," or i == ".":
            draw.text((x, y), i, font=font, fill="black")
            currenth += 33 + line_spacing
            currentstroka = ""
            x = pad_left - draw.textsize(i, font=font)[0]
            continue
        else:
            currenth += 33 + line_spacing
            currentstroka = ""
            draw.text((x, y), "-", font=font, fill="black")
            x = pad_left
    y = currenth
    draw.text((x, y), i, font=font, fill='black')
    currentstroka += i
    x+= draw.textsize(i, font=font)[0]

lasttext = "Ответ: _____________________________."

draw.text((pad_left, currenth+(h-currenth)/2), lasttext, font=font, fill="black")


base_image.save("output.png")