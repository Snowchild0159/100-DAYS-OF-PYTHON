from data import data
import random
from art import vs,logo
from clear import clear


account1 =  random.choice(data)
account2 =  random.choice(data)
    

def high_low(account1, account2):
    """Compare the follower count of two accounts"""
    if account1['follower_count'] > account2['follower_count']:
        return account1
    else:
        return account2

game_is_over = False
print(logo)
score = 0
while not game_is_over:
    print("Welcome to the Higher Lower Game!")
    print(f"Compare A: {account1['name']}, a {account1['description']}, from {account1['country']}.")
    print(vs)
    print(f"Against B: {account2['name']}, a {account2['description']}, from {account2['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    winner = high_low(account1, account2)
    if guess == 'a' and winner == account1:
        score += 1
        clear()
        print(logo)
        print(f"You are right! {account1['name']} has more followers than {account2['name']}.")
        print(f"Your current score is: {score}")
        account2 = random.choice(data)
    elif guess == 'b' and winner == account2:
        score += 1
        clear()
        print(logo)
        print(f"You are right! {account2['name']} has more followers than {account1['name']}.")
        print(f"Your current score is: {score}")
        account1 = account2
        account2 = random.choice(data)
    else:
        clear()
        print(logo)
        print(f"Sorry, that's wrong. {winner['name']} has more followers than the other.")
        print(f"Your final score is: {score}")
        game_is_over = True


