import random

Rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)


''')

Paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)



''')

Scissors = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)


''')

Game = [ Rock , Paper , Scissors]

choice = input("what do you choose? type 0 for Rock , 1 for Paper , 2 for Scissors \n")
int_choice = int(choice)
your_choice = Game[int_choice]
computer_choice = random.choice(Game)
print(f"your choice is \n {your_choice}")
print(f"computer choice is \n {computer_choice}")
if your_choice == computer_choice : 
    print("it is draw !!!")

#easier solution : 
else:
    if your_choice == Rock and computer_choice == Scissors or your_choice == Scissors and computer_choice == Paper or your_choice == Paper and computer_choice == Rock:
        print("you  win!!!")
    
    else:
        print("computer wins :(")


#another solution : 
 # if your_choice == Rock and computer_choice == Scissors :
    #     print("you  win!!!")
    # elif your_choice == Rock and computer_choice == Paper :
    #     print("computer wins :(")
    # elif your_choice == Scissors and computer_choice == Paper :
    #     print("you  win!!!")
    # elif your_choice == Paper and computer_choice == Scissors :
    #     print("computer wins :(")
    # elif your_choice == Paper and computer_choice == Rock :
    #     print("you  win!!!")
    # else:
    #     print("computer wins :(")



