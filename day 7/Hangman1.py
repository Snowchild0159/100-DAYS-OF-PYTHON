import random
#Step 1

word_list = ["ardvark", "baboon", "camel"]

# 3TODO-1 - Randomly choose a word from the word_list and
# # assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)
# 3TODO-2 - Ask the user to guess a letter and assign
# their answer to a variable called guess. Make guess
# lowercase.
guess = input("guess a letter : \n").lower()
# #TOD0-3 - Check if the letter the user guessed (guess)
# is one of the leters in the chosen_word.
for word in chosen_word :
    if guess == word :
        print(True)
    else:
        print(False)