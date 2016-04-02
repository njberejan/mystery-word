# Requirements
# Write functions to select a subset of the complete word list. DONE
# Write a function to select a word at random from the word list. DONE
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
    #make try/except block instead?
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
            if len(line.strip()) <= 3:
                unusable_words.append(line)
            elif len(line.strip()) < 6:
                potential_words_easy.append(line)
            elif len(line.strip()) < 8:
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
    # - 1 is another lazy solution to blank space problem
    #instead of printing len(mystery_word) try mystery_word.replace('', '_ ')
    for i in range(0, len(mystery_word)):
        # if ord(mystery_word[i]) != 32:
        mystery_word = mystery_word.replace(mystery_word[i:], '_ ')
        continue
    return mystery_word

def is_in_word(player_guess, mystery_word):
    if player_guess in mystery_word:
        return player_guess

# def find_all(mystery_word, player_guess):
#     return [i for i, letter in enumerate(mystery_word) if letter == player_guess]

# def reveal_letter(player_guess, blanked_word, mystery_word):
#     if is_in_word(player_guess, mystery_word):
#         while True:
#             if player_guess in mystery_word:
#                 index = mystery_word.find(player_guess)
#                 mystery_word = mystery_word.replace(player_guess, "_")
#                 blanked_word = blanked_word[:index] + player_guess + blanked_word[index + 1:]
#                 print(blanked_word)
#                 return blanked_word
#                 continue
#             else:
#                 break
        # if player_guess in mystery_word:
        #     replaced_letter = mystery_word[mystery_word.index(player_guess)]
        #     blanked_word = blanked_word.replace(replaced_letter, player_guess)
        # print(replaced_letter)
        # print(blanked_word)
        # print(mystery_word)
#LEAVING OFF HERE FOR TIME BEING 2:11 FRIDAY

def reveal_letter(player_guess, mystery_word):
    mys_list = list(mystery_word)
    word_guessed = []
    for letter in mystery_word:
        word_guessed.append("_ ")


def print_output(x, output):
    print(''.join([str(x)+" " for x in output]))

# mystery_word_list = list(mystery_word)
# if player_guess in mystery_word_list:
#     mystery_word = blanked_word.replace()

def main():

    unusable, easy, medium, hard = create_list()
    mystery_word = computer_word(easy, medium, hard).lower().strip()
    print(mystery_word)
    print("the length of the str is: " , len(mystery_word))
    print("The mystery word is {} letters long.".format(len(mystery_word.strip())))
    print(display_word(mystery_word))
    # blanked_word = display_word(mystery_word)
    # print(mystery_word) PRINT DEBUG, ENSURES PROGRAM STORING ORIGINAL mystery_word
    # print(blanked_word) AS WELL AS NEWLY CREATED blanked_word
    while True:
        player_guess = guess_letter()
        reveal_letter(player_guess, mystery_word)
        print_output(output)
        # print_output(output)
        # if "_" not in blanked_word:
        #     print("You completed the word!")
        # elif is_in_word(player_guess, mystery_word):
        #     blanked_word = reveal_letter(player_guess, blanked_word, mystery_word)
        #     print("You guessed a letter!")
        #     continue
        # else:
        #     print("That letter is not in the mystery word!")
        #     continue


main()

#regular expression for string character replacement?

#loop for dictionary:
    # for word in words:
    #     if word in word_count:
    #         word_count[word] += 1
    #     else:
    #         word_count[word] = 1
#may need to put individual letters in string in a dictionary to determine frequency
#of letter in word?

#more explicitly:
# d={}
# with open('new_file.txt', 'r') as words:
#         for words in words:
#                 cleaned=word.strip().lower()
#                 if cleaned not in d:
#                         d[cleaned] = 1
#                     else:
#                         d[cleaned] += 1
