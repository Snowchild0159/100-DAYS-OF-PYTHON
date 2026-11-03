# #describe the problem 
# def my_function():
# #    for i in range(1,20): this is a for loop that will iterate through the numbers 1 to 19
#     for i in range(1, 21):  # this is a for loop that will iterate through the numbers 1 to 20
#         if i == 20:
#             print("snow")
# my_function()



# #reproduce the bug
# from random import randint
# dice_imgs = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
# # dice_num = randint(1, 6)  # this will generate a random number between 1 and 6 including 6
# dice_num = randint(0, 5)  # this will generate a random number between 1 and 5
# print(dice_imgs[dice_num])  # this will print the image at the generated index


# # play computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994: 
#     print("You are a millenial.")
# # elif year > 1994: this will miss anyone born in 1994
# elif year >= 1994: #this will catch anyone born in 1994 or later aka fix the bug
#     print("You are a Gen Z.")

# #fix the errors
# # age = input("How old are you?") # this will take the input as a string which will cause an error when trying to compare it to an integer
# age = int(input("How old are you?"))
# if age > 18:
# # print("You can drive at age {age}.")#this is an entendation error, the print statement should be indented to be inside the if statement
#     print(f"You can drive at age {age}.")

# #print is your friend
# page = 0
# word_per_page = 0
# # page == int(input("Number of pages: "))
# # word_per_page == int(input("Number of words per page: "))
# # this will cause an error because the variables page and word_per_page are not being assigned the input values, they are being compared to the input values. The correct way to assign the input values to the variables is to use a single equal sign (=) instead of a double equal sign (==).
# page =int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = page * word_per_page
# print(total_words)

# #use a debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     # b_list.append(new_item) # this will cause an error because new_item is not defined outside of the for loop. The correct way to fix this is to define new_item before the for loop and then update it inside the for loop. 
#     print(b_list)

# mutate([1,2,3,5,8,13])