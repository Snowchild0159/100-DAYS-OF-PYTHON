import turtle as t
import random


snow = t.Turtle()
print(snow)
snow.shape("arrow")
snow.color("DarkRed", "DarkGreen")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_circle():
    snow.speed(30)
    snow.color(random_color())
    snow.circle(100)


draw_circle()
current_heading = snow.heading()
for _ in range(36):
    snow.setheading(current_heading + 10)
    draw_circle()
    current_heading = snow.heading()








my_screen = t.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()