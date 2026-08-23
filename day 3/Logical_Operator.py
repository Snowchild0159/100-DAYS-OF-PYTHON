#logical operators are used to combine conditional statements
#logical operators are "and", "or" and "not"
#and operator example:
#and operator is used to check if both conditions are true, if both are true then the result will be true, otherwise it will be false
#or operator example:
#or operator is used to check if at least one condition is true, if at least one condition is true then the result will be true, otherwise it will be false
#not operator example:
#not operator is used to reverse the result, if the result is true then it will return false, and vice versa


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
#logical operator example "and":
    elif age >= 45 and age <= 55:
        print("Everything will be OK!. you have a free ride ticket on us!")
    else:
        print("adult tickets are $12")
        bill = 12
    want_photo = input("do you want a photo taken? Y or N.")
    if want_photo == "Y":
        bill += 3
    print(f"your final bill is ${bill}")
else:
    print("sorry, grow taller and come back next time!")