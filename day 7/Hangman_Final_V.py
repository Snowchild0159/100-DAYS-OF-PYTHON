import random
from Hangman_words_list import word_list

logo = r'''

 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/


'''
# Hangman drawings
HANGMAN_PICS = [
    r'''
  +---+
      |
      |
      |
     ===''',

    r'''
  +---+
  O   |
      |
      |
     ===''',

    r'''
  +---+
  O   |
  |   |
      |
     ===''',

    r'''
  +---+
  O   |
 /|   |
      |
     ===''',

    r'''
  +---+
  O   |
 /|\  |
      |
     ===''',

    r'''
  +---+
  O   |
 /|\  |
 /    |
     ===''',

    r'''
  +---+
  O   |
 /|\  |
 / \  |
     ==='''
]

# ---------------------------------------
# LOGO
# ---------------------------------------

print(logo)


# ---------------------------------------
# Choose a random word
# ---------------------------------------


chosen_word = random.choice(word_list)

# print(f"Pssst, the solution is {chosen_word}.")


# ---------------------------------------
# Player lives
# ---------------------------------------

lives = 6


# ---------------------------------------
# Create the blank display
# ---------------------------------------

display = []

for position in range(len(chosen_word)):
    display.append("_")

print(display)


# ---------------------------------------
# Main game loop
# ---------------------------------------

while "_" in display and lives > 0:
     
    guess = input("\nGuess a letter: ").lower()
   
    if guess in  display:
     print(f"you've already choose this letter '{guess}'")
    # Check if the guessed letter is in the word
    for position in range(len(chosen_word)):

        letter = chosen_word[position]

        if letter == guess:
            display[position] = guess




    # If the guessed letter is wrong
    if guess not in chosen_word:

        lives -= 1

        print(f"\n'{guess}' is not in the word. \n  You lose a life.")
        print(HANGMAN_PICS[6 - lives])


    # Show current progress
    print(display)
    print(f"Lives remaining: {lives}")


# ---------------------------------------
# End of game
# ---------------------------------------

if lives == 0:
    print("\nYou lose :(")
    print(f"The word was: {chosen_word}")

else:
    print("\nYou win!!!")