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
while not game_is_over:
    print(logo)
    print("Welcome to the Higher Lower Game!")
    print(f"Compare A: {account1['name']}, a {account1['description']}, from {account1['country']}.")
    print(vs)
    print(f"Against B: {account2['name']}, a {account2['description']}, from {account2['country']}.")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    winner = high_low(account1, account2)
    if guess == 'a' and winner == account1:
        clear()
        print(f"You are right! {account1['name']} has more followers than {account2['name']}.")
        account2 = random.choice(data)
    elif guess == 'b' and winner == account2:
        clear()
        print(f"You are right! {account2['name']} has more followers than {account1['name']}.")
        account1 = account2
        account2 = random.choice(data)
    else:
        clear()
        print(f"Sorry, that's wrong. {winner['name']} has more followers than the other.")
        game_is_over = True


