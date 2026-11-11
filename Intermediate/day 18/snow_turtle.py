from turtle import Turtle, Screen


snow = Turtle()
print(snow)
snow.shape("turtle")
snow.color("DarkRed", "DarkGreen")
# for _ in range(4):
#     snow.forward(100)
#     snow.right(90)

for _ in range(15):
    snow.forward(10)
    snow.penup()
    snow.forward(10)
    snow.pendown()


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()