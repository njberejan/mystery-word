# Requirements
# Write functions to select a subset of the complete word list.
# Write a function to select a word at random from the word list.
# Write a function to display a word with blanks/letters filled in the appropriate spots.
# Write a function to check if a word has been completely guessed.
# Write other helper functions as necessary to help with the flow of the game.
# Run mystery_word_test.py and ensure you pass all the unit tests.

#computer must select random word from words.txt DONE
    #omit words less than 4 letters (see diff modes) DONE
#at start, user must select difficulty DONE
    #easy: word has 4-6 characters DONE
    #normal: word has 6-8 characters DONE
    #hard: word has 8+ characters DONE
#at start, must let user know how many letters in random word DONE
#prompt user to guess one letter in word DONE
    #not case sensitive (.lower() or .upper()) DONE
    #if user enters > 1 character, inform and redo DONE
#let user know if guess appears in random word
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

def guess_letter():
    while True:
        player_guess = input("Please guess a letter: ").lower()
        if player_guess.isnumeric():
            print("That is a number.")
            continue
        elif len(player_guess) == 1:
                return player_guess
        else:
            print("Please enter only one letter.")
            continue

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

def display_word(mystery_word):
    #another lazy solution to blank space problem
    print((len(mystery_word) - 1) * '_ ')

def is_in_word(player_guess, mystery_word):
    if player_guess in mystery_word:
        print("You guessed a letter!")

def reveal_letter(is_in_word()):
    #LEAVNG OFF HERE 10PM. CAN FUNCTION BE ARGUMENT FOR ANOTHER FUNCTION?


def main():

    unusable, easy, medium, hard = create_list()
    mystery_word = computer_word(easy, medium, hard).lower()
    print(mystery_word)
    #line below is lazy, technically fixes problem.
    #was returning .format consistenly one too long. must be blank space on line from text file.
    print("The mystery word is {} letters long.".format(len(mystery_word) - 1))
    blank_word = display_word(mystery_word)
    player_guess = guess_letter()
    is_in_word(player_guess, mystery_word)


main()
