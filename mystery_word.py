# Requirements
# Write functions to select a subset of the complete word list.
# Write a function to select a word at random from the word list.
# Write a function to display a word with blanks/letters filled in the appropriate spots.
# Write a function to check if a word has been completely guessed.
# Write other helper functions as necessary to help with the flow of the game.
# Run mystery_word_test.py and ensure you pass all the unit tests.

#computer must select random word from words.txt
    #omit words less than 4 letters (see diff modes)
#at start, user must select difficulty
    #easy: word has 4-6 characters
    #normal: word has 6-8 characters
    #hard: word has 8+ characters
#at start, must let user know how many letters in random word
#prompt user to guess one letter in word
    #not case sensitive (.lower() or .upper())
    #if user enters > 1 character, inform and redo
#let user know if guess appears in random words
#display partially guessed word as well as letters guessed.
    #ex: bombard display as B O _ B _ _ _ D
#user is limited to 8 guesses
    #remind user of how many guesses remain after each input
#user only loses a guess if incorrect, not for correct guess
#if user guesses same letter twice, inform user and have guess again
    #do not subtract a guess though!
#game ends when user completes word or runs out of guesses.
    #if runs out of guesses, word is revealed.
#after game ends, prompt player if wants to play again

import random

def player_input():
        while True:
            player_guess = input("Please guess a single letter: ")
            try:
                player_guess.isapha()
                return player_guess
            except:
                print("That is not a letter! Please try again.")

# def guess_letter():
#     if player_guess in mystery_word:

def create_list():
# Write functions to select a subset of the complete word list.
    unusable_words = []
    potential_words_easy = []
    potential_words_medium = []
    potential_words_hard = []
    with open('words.txt', 'r') as f:
        for line in f:
            if len(line) < 4:
                unusable_words.append(line)
            elif len(line) < 6:
                potential_words_easy.append(line)
            elif len(line) < 8:
                potential_words_medium.append(line)
            else:
                potential_words_hard.append(line)
        return unusable_words, potential_words_easy, potential_words_medium, potential_words_hard

def computer_word(easy, medium, hard):
# Write a function to select a word at random from the word list.
    while True:
        difficulty = input("Please select a difficulty: (e)asy, (m)edium, or (h)ard: ").upper()
        if difficulty == 'E':
            mystery_word = random.choice(easy)
            return mystery_word
        elif difficulty == 'M':
            mystery_word = random.choice(medium)
            return mystery_word
        elif difficulty == 'H':
            mystery_word = random.choice(hard)
            return mystery_word
        else:
            print ("Please select e, m, or h.")
            continue

# def display_word():
#     print(len(mystery_word)) * '_ '
#     if guess_letter() == True:


# def word_guessed():

def main():

    # lists = create_list()
    unusable, easy, medium, hard = create_list()
    mystery_word = computer_word(easy, medium, hard)
    print(mystery_word)

main()
