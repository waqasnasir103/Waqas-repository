from turtle import Turtle


def liner():
    line_list = []
    y = -270
    for i in range(10):
        line = Turtle()
        line.shape('square')
        line.color('white')
        line.shapesize(stretch_wid=2, stretch_len=.5)
        line.penup()
        line_list.append(line)
        line.goto(0, y)
        y += 80


class Scorer(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        liner()

    def update_score(self):
        self.clear()
        self.goto(-120, 200)
        self.write(self.l_score, False, align='center', font=('arial', 50, 'normal'))
        self.goto(120, 200)
        self.write(self.r_score, False, align='center', font=('arial', 50, 'normal'))

    def l_scores(self):
        self.l_score += 1
        self.update_score()

    def r_scores(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game    Over', False, align='center', font=('arial', 70, 'bold'))

