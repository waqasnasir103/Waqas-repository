from turtle import Turtle


class Turtles(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.y_co = 20
        self.goto(0, -280)

    def move_up(self):
        new_y = self.ycor() + self.y_co
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - self.y_co
        self.goto(self.xcor(), new_y)

    def restart(self):
        self.goto(0, -280)
