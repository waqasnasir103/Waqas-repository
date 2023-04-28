from turtle import Turtle
ALIGN = 'center'
FONT = ('arial', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 280)
        self.pendown()
        self.score = 0
        with open('snake_highscore.txt', 'r') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score}   High Score: {self.high_score}', False, ALIGN, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('snake_highscore.txt', mode= 'w') as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('Game Over', False, ALIGN, font=('arial', 30, 'normal'))

    def score_counter(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
