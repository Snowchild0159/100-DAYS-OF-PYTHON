import random

name_string = input("Give me everybody's name, seperated by a comma. \n")
name = name_string.split(", ")

num_items = len(name)
random_choice = random.randint(0 , num_items - 1)


person_who_will_pay = name[random_choice]

#another simple way : 
#person_who_will_pay = random.choice(name)


print(f"{person_who_will_pay} will pay the bill")
