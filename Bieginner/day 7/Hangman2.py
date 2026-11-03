import random
#letter to guess.
#Testing code

#Step 2
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random. choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')


    


#3TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be
# [_", "_"] with 5 "_" representing each
display = []
for position in range(0 , len(chosen_word)):
        display.append("_")


    #2TODO-2: - Loop through each position in the chosen_word;
    #If the letter at tbat position matches 'guess' then
    # reveal thet Letter in the display at that positton.
    # #e.g. If the user guessed "p" and the chosen word was
    # "apple", then display should be ["_", "p", "p","_u, "_"|.

#4TODO-1: - Use a while loop to let the user
# guess again. The loop should only stop once
# the user has guessed all the letters in the
# chosen_word and 'display' has no more
# blanks ("_"). Then you can tell the user
# they've won.



while "_" in display :
    guess = input("Guess a letter: ").lower()
    for position in range(0 , len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess :
            display[position] = guess

    print(display)
    # #3TODO-3: - Print 'display' and you should see the guessed
    # letter in the correct position and every other letter
    # reptace with "_".
    # #Hint - Beh't worry aboot getting the user to guess the
    # next letter. We'll tackle that in step 3.

