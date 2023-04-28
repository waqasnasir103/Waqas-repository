from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title('My Snake Game')
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, 'Up')
screen.onkey(snake.move_down, 'Down')
screen.onkey(snake.move_right, 'Right')
screen.onkey(snake.move_left, 'Left')
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.10)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_counter()
        snake.extend()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
        # scoreboard.game_over()
        # game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            # game_is_on = False




screen.exitonclick()
