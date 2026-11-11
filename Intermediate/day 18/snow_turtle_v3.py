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
    random_color = (r, g, b)
    return random_color

direction = [0, 90, 180, 270]

def draw_line():
    snow.pensize(25)
    snow.speed(10)
    snow.forward(30)

for _ in range(200):
    snow.color(random_color())
    snow.setheading(random.choice(direction))
    draw_line()






my_screen = t.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()