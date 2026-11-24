from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snow Snake Game")
screen.tracer(0)

snow_snake = Snake()
food = Food()
scoreboard = Scoreboard()
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

    #detect collision with food.
    if snow_snake.head.distance(food) < 15:
        food.refresh()
        snow_snake.extend()
        scoreboard.increase_score()
        
    #detect collision with the wall. 
    if snow_snake.head.xcor() > 280 or snow_snake.head.xcor() < -280 or snow_snake.head.ycor() > 280 or snow_snake.head.ycor() < -280: 
        scoreboard.reset()
        snow_snake.reset()


    for segment in snow_snake.snake[1:]:
        
        if snow_snake.head.distance(segment) < 10:
            scoreboard.reset()
            snow_snake.reset()


    









screen.exitonclick()
