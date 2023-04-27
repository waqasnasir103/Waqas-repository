from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-235, 245)
        self.write(f'Level: {self.level}', False, align='center', font=('arial', 15, 'normal'))

    def level_up(self):
        self.reset()
        self.level += 1
        self.hideturtle()
        self.penup()
        self.goto(-235, 245)
        self.write(f'Level: {self.level}', False, align='center', font=('arial', 15, 'normal'))

    def game_over(self):
        self.reset()
        self.goto(0, 0)
        self.write('Game  Over', False, align='center', font=('arial', 30, 'normal'))
