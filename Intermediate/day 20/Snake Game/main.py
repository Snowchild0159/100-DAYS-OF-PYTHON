from turtle import Turtle , Screen
import time
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snow Snake Game")
screen.tracer(0)

snow_snake = Snake()

screen.listen()
screen.onkey(snow_snake.up, "Up")
screen.onkey(snow_snake.down, "Down")
screen.onkey(snow_snake.left, "Left")
screen.onkey(snow_snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)


    snow_snake.move()
    









screen.exitonclick()
