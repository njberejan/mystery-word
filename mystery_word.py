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
