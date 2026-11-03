# #########################scope.py#########################
# # This file is part of the Python Challenge.
# enemies = 1
# def increase_enemies():
#     enemies = 2
#     print(f"Enemies inside function: {enemies}")

# increase_enemies()
# print(f"Enemies outside function: {enemies}")

#global scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)  # This will raise an error because potion_strength is not defined in this scope

#local scope
# player_health = 10
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(potion_strength)
#     drink_potion()
#     print(player_health)  # This will work because player_health is defined in the global scope

# game()    

#THERE IS NO BLOCK SCOPE IN PYTHON, ONLY FUNCTION SCOPE

# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5: 
#         new_enemy = enemies[0]
#     print(new_enemy)
#modefying global scope

enemies = 2

def increase_enemies():
    print(f"Enemies inside function: {enemies}")
    return enemies +1

enemies = increase_enemies()
print(f"Enemies outside function: {enemies}")

# enemies = 2

# def increase_enemies():
#     global enemies  # This tells Python to use the global variable 'enemies'not recomanded 
#     enemies += 1
#     print(f"Enemies inside function: {enemies}")

# increase_enemies()
# print(f"Enemies outside function: {enemies}")

#global constants
# PI = 3.14
# URL = "https://www.google.com"
# TWITTER_HANDLE = "@pythonchallenge"

# def calc():
#     radius = 5
#     area =  PI * radius ** 2
#     print(f"Area of the circle: {area}")