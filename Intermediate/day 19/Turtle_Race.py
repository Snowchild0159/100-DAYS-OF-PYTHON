from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Turtle Race, Make Your BET!",prompt= "Which turtle will win the race? ANNZ or SNOW: ")


snow = Turtle(shape="turtle")
annz = Turtle(shape="turtle")

snow.color("blue")
annz.color("red")
snow.penup()
annz.penup()
snow.goto(x=-230, y=20)
annz.goto(x=-230, y=-20)

if user_bet:
    is_race_on = True

while is_race_on:

    if snow.xcor() > 230:
        is_race_on = False
        if user_bet == "snow":
            print("you've won! SNOW is the winning turtle")
        else:
            print("you've lost! ANNZ is the winning turtle")
  
    elif annz.xcor() > 230:
        is_race_on = False
        if user_bet == "annz":
            print("you've won! ANNZ is the winning turtle")
        else:
            print("you've lost! SNOW is the winning turtle")







    snow.forward(random.randint(0, 10))
    annz.forward(random.randint(0, 10))
    
    
















screen.exitonclick()