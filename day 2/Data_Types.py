#string
print("hello"[4])
print("123" + "3456")

#intger
print(123 + 456)
162_364_459

#float
3.14159

#boolean
True
False


#changing data types
num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("your name has " + new_num_char + " characters.")


a = float(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))

#program that adds two digit number together

#don't change the code below
two_digit_number = input("Type two digit number: ")
#don't change the code above
####################################
#write your code below this line

#check the data type of two_digit_number
print(type(two_digit_number))
#get the first_digit and second_digit using subscripting then convert str to int
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
#add the two digits together and print the result
result = int(first_digit) + int(second_digit)
print(result)
