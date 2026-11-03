#PEMDAS
#(Parentheses))
#(Exponents))
#(Multiplication))
#(Division))
#(Addition))
#(Subtraction))

print(3*3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

#BMI calculator
#Don't change the code below
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
#Don't change the code above
#Write your code below this line
BMI = int(weight) / float(height) ** 2
print(float(BMI))


#round function
print(round(8/3))   
print(round(8/3, 2))

#floor
print(8 // 3)


result = 4 / 2
result /=2
print(result)

score = 0 
#user score a point
score += 1
print(score)

#f-string
points = 1
length = 180
is_winning = True 

print(f"you points is {points} , your length is{length} , you are winning {is_winning}")
