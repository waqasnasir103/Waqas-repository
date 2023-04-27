from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=600, height=500)
is_game_over = False
user_input = screen.textinput('Enter Color', 'On which color you wanna bet').lower()
if user_input:
    is_game_over = True
color_list = ['red', 'blue', 'brown', 'grey', 'black', 'purple', 'green', 'orange']
xcor = [230, 160, 100, 30, -30, -100, -160, -230]
turtle_list = []
for i in range(8):
    turtle = Turtle(shape='turtle')
    turtle.color(color_list[i])
    turtle.penup()
    turtle.setposition(x=-280, y=xcor[i])
    turtle_list.append(turtle)

while is_game_over:
    for i in range(8):
        turtle_list[i].forward(random.randint(0, 10))
        if turtle_list[i].xcor() > 275.1:
            color = turtle_list[i].pencolor()
            is_game_over = False
            if user_input == color:
                print(f'You Won. {color.capitalize()} Turtle has finished first')
            else:
                print(f'You Lost. {color.capitalize()} Turtle has finished first Because your bet was on'
                      f' {user_input.capitalize()} Turtle')


screen.exitonclick()
