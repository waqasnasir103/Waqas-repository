from turtle import Screen
from paddles import Paddles
from ball import Ball
from scorer import Scorer
import time


screen = Screen()

screen.setup(width=800, height=600)
screen.title('Pong Game')
screen.bgcolor('black')
screen.tracer(0)

game_is_on = True

l_paddle = Paddles((-370, 0))
r_paddle = Paddles((370, 0))

ball = Ball()

scorer = Scorer()


screen.listen()
screen.onkey(l_paddle.paddle_up, 'w')
screen.onkey(l_paddle.paddle_down, 's')
screen.onkey(r_paddle.paddle_up, 'Up')
screen.onkey(r_paddle.paddle_down, 'Down')

sleep_timer = 0.1

while game_is_on:

    screen.update()
    time.sleep(sleep_timer)
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_from_wall()

    if (ball.xcor() > 350 and ball.distance(r_paddle) < 50) or (ball.xcor() < -350 and ball.distance(l_paddle) < 50):
        ball.bounce_from_paddle()
        sleep_timer -= 0.001

    if ball.xcor() > 390:
        scorer.r_scores()
        ball.reset_position()
        sleep_timer = 0.1

    if ball.xcor() < -390:
        scorer.l_scores()
        ball.reset_position()
        sleep_timer = 0.1

    if scorer.l_score > 12 or scorer.r_score > 12:
        scorer.game_over()
        game_is_on = False


screen.exitonclick()
