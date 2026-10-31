
import random
from art import logo


numbers = list(range(1, 101))
lives = (input("do you want to play easy or hard mode? type 'easy' or 'hard': "))
if lives == "easy":
    lives = 10
elif lives == "hard":
    lives = 5

correct_number = random.choice(numbers)

def guess_number(lives):
    print(logo)
    game_over = False
    while not game_over:
        guess = int(input("Make a guess: "))
        print(f"You have {lives} attempts remaining to guess the number.")
        if guess == correct_number:
            print(f"you got it! the answer was {correct_number}")
            game_over = True
        elif guess > correct_number:
            print("Too high.")
            lives -= 1
            if lives == 0:
                print("you've run out of guesses, you lose.")
                game_over = True
            else:
                print("Guess again.")
        elif guess < correct_number:
            print("Too low.")
            lives -= 1
            if lives == 0:
                print("you've run out of guesses, you lose.")
                game_over = True
            else:
                print("Guess again.")

guess_number(lives)