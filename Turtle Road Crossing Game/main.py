import time
from turtle import Screen
from turtles import Turtles
from cars import Cars
from levels import Level


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('Turtle Road Crossing Game')
screen.tracer(0)

turtle = Turtles()
cars = Cars()
levels = Level()

game_is_running = True

screen.listen()
screen.onkey(turtle.move_up, 'Up')
screen.onkey(turtle.move_down, 'Down')
sleep_timer = 0.1

while game_is_running:
    time.sleep(sleep_timer)
    screen.update()
    cars.create_cars()
    cars.cars_running()

    if turtle.ycor() > 280:
        levels.level_up()
        turtle.restart()
        sleep_timer -= 0.01

    # if turtle.distance(cars.position()) == 0:
    #     levels.game_over()
    #     game_is_running = False
    for car in cars.all_cars:
        if car.distance(turtle) < 30:
            levels.game_over()
            time.sleep(2)
            game_is_running = False

screen.exitonclick()
