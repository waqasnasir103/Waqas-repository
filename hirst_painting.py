import random

import colorgram
from turtle import Turtle, Screen, colormode
# the file would be any file, but it should have a .jpg extension.
colors = colorgram.extract('download.jpg', 2 ** 32)
color_list = []
for count in range(len(colors)):
    r = colors[count].rgb.r
    g = colors[count].rgb.g
    b = colors[count].rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)

tom = Turtle()
tom.speed('fastest')
x = -600
y = 300
pos = (x, y)
colormode(255)

n = 0


def dot_printer():
    global n
    for i in range(13):
        tom.penup()
        global y
        tom.goto(x, y)
        for j in range(41):
            tom.pendown()
            # codes = fun(color_list)
            tom.color(random.choice(color_list))
            tom.dot(10)
            tom.penup()
            tom.forward(30)
            n += 1
        y -= 50


dot_printer()
# for i in range(10):
#     a = fun()
#     print(a.__next__())
print(len(color_list))
s = Screen()
s.screensize(canvwidth=400, canvheight=400)
s.exitonclick()
