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

def is_in_word(player_guess, mystery_word):
    if player_guess in mystery_word:
        return player_guess

def reveal_letter(player_guess, mystery_word, word_update, blank_list):
    mys_list = list(mystery_word)
    if str(player_guess) in mys_list:
        blank_list[mys_list.index(str(player_guess))] = str(player_guess)
        return blank_list

def main():

    unusable, easy, medium, hard = create_list()
    mystery_word = computer_word(easy, medium, hard).lower().strip()
    print(mystery_word)
    print("the length of the str is: " , len(mystery_word))
    print("The mystery word is {} letters long.".format(len(mystery_word.strip())))
    blank_list = list(len(mystery_word) * '_')
    word_update = (len(mystery_word) * '_')
    while True:
        player_guess = guess_letter()
        if reveal_letter(player_guess, mystery_word, word_update, blank_list):
            word_update = ''.join(blank_list)
        print(word_update)
        if '_' not in blank_list:
            print("You guessed the word!")
            break
        elif is_in_word(player_guess, mystery_word):
            print("You guessed a letter!", word_update)
            continue
        else:
            print("That letter is not in the mystery word!")
            continue


main()
