from turtle import Turtle, Screen

snow = Turtle()

def move_forward():
    snow.forward(10)

def move_backward():
    snow.backward(10)

def turn_left():
    new_heading = snow.heading() + 10
    snow.setheading(new_heading)

def turn_right():
    new_heading = snow.heading() - 10
    snow.setheading(new_heading)

def clear_drawing():
    snow.clear()
    snow.penup()
    snow.home()
    snow.pendown()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()