from turtle import Turtle, Screen

snow = Turtle()



def move_forward():
    snow.forward(10)

screen = Screen()
screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()