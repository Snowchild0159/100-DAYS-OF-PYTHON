from turtle import Turtle, Screen
import random


snow = Turtle()
print(snow)
snow.shape("turtle")
snow.color("DarkRed", "DarkGreen")

colors = ["DarkRed", "DarkGreen", "DarkBlue", "DarkOrange", "DarkViolet", "DarkCyan", "DarkMagenta"]

def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        snow.forward(100)
        snow.right(angle)

for shape_side_n in range(3, 11):
    snow.color(random.choice(colors))
    draw_shape(shape_side_n)





my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()