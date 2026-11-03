print("welcome to roller coaster!")
height = int(input("what is your height in cm?"))
if height >= 120:
    print("you can ride the roller coaster!")
else:
    print("sorry, grow taller and come back next time!")


#Nested if statements & elif statements
print("welcome to roller coaster!")
height = int(input("what is your height in cm?"))
if height >= 120:
    print("you can ride the roller coaster!")
    age = int(input("what is your age?"))
    if age < 12:
        print("please pay $5")
    elif age <= 18:
        print("please pay $7")
    else:
        print("please pay $12")
else:
    print("sorry, grow taller and come back next time!")

    

#comparison operators
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# == equal to
# != not equal to


#Modulus operator
# % returns the remainder of a division
number = int(input("which number do you want to check?"))
if number % 2 == 0:
    print("this is an even number")
else:
    print("this is an odd number")