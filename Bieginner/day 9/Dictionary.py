programming_Dictionary = {
    "Bug" : "an error in program that prevents the program from running as expected", 
    "Function" : "a piece of code that you can easily call over and over again",
}

#retrieving items from dictionary
print(programming_Dictionary["Bug"])

#adding items to dictionary
programming_Dictionary["loop"] = "the action of doing something over and over again"

#empty Dictionary
empty_Dictionary = {}
# print(empty_Dictionary)


#wipe out an existing dictionary
# programming_Dictionary = {}
# print(programming_Dictionary)


#edit an item in a dictionary
programming_Dictionary["Bug"] = "a moth in your computer"
print(programming_Dictionary)


#loop through dictionary 
for key in programming_Dictionary : 
  print(key)
  print(programming_Dictionary[key])

