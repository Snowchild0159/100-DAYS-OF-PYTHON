print("welcome to roller coaster!")
height = int(input("what is your height in cm?"))
bill = 0
if height >= 120:
    print("you can ride the roller coaster!")
    age = int(input("what is your age?"))
    if age < 12:
        print("child tickets are $5")
        bill = 5
    elif age <= 18:
        print("youth tickets are $7")
        bill = 7
    else:
        print("adult tickets are $12")
        bill = 12
    want_photo = input("do you want a photo taken? Y or N.")
    if want_photo == "Y":
        bill += 3
    print(f"your final bill is ${bill}")
else:
    print("sorry, grow taller and come back next time!")