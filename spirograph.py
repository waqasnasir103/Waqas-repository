from turtle import Turtle, Screen, colormode
import random


t = Turtle()
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


def rep_circle():
    t.speed('fastest')
    for i in range(90):
        t.color(random_color())
        t.circle(100)
        t.setheading(i * 4)
        # t.degrees(i)


rep_circle()

s = Screen()
s.exitonclick()