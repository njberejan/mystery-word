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

def reveal_letter(player_guess, mystery_word, blank_string):
#this code was implemented via stackoverflow. Will need some clarification why this works.
    blank_list = list(blank_string)
    for index, item in enumerate(mystery_word):
        if player_guess == item:
            blank_list[index] = player_guess

    return blank_list

def completely_guessed(blank_list):
    if '_' not in blank_list:
        return True

def game():
    guess_number = 8
    player_guesses = []
    unusable, easy, medium, hard = create_list()
    #generates lists to pull from
    mystery_word = computer_word(easy, medium, hard).lower().strip()
    #generates mystery_word from above lists
    print(mystery_word)
    #print debug
    print("the length of the str is: " , len(mystery_word))
    #print debug
    print("The mystery word is {} letters long.".format(len(mystery_word.strip())))
    blank_list = list(len(mystery_word) * '_')
    #generates initial blank list

    while True:
        player_guess = guess_letter()
        #player is prompted, enters letter
        blank_list = reveal_letter(player_guess, mystery_word, blank_list)
        #reveal letter function runs, returns string concatenated from blank list w/ added letter
        print(" ".join(blank_list))
        #prints the string with the added letter
        if completely_guessed(blank_list):
        #determines if game is over
            print("You guessed the word!")
            break
        elif guess_number < 1:
            print("You have failed to guess the word. You lose. The mystery word was: {}.".format(mystery_word))
            break
        elif player_guess in player_guesses:
            print("You have already guessed that number!")
            continue
        elif is_in_word(player_guess, mystery_word):
        #determines if letter guessed was in word, returns true and prints below.
            player_guesses.append(player_guess)
            print("You guessed a letter! Guesses remaining: {}".format(str(guess_number)))
            continue
        else:
        #guessed letter is not in word, is_in_word returns False.
            guess_number -= 1
            print("That letter is not in the mystery word! Guesses remaining: {}".format(str(guess_number)))
            continue

def main():
    game()
    while True:
        play_again = input("Would you like to play again? Y/n: ")
        if play_again.lower() == 'y':
            game()
        else:
            break

main()
