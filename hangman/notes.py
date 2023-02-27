#   === === === HANGMAN === === ==== 

#   THE MISSION
# - The computer picks a word from a selection it knows, shows you the blanks, and asks you to guess. 
# - Every successful guess fills in those blanks.
# - Every failed guess draws a new piece of the hangman. 
# - You have six chances to win.

# count the same letters. if count is greater than 1 than, found the second index with index with the second parameter (location). 

#   === === === IMPORT GUARD === === ==== 

from words import word
from sys import exit

#   === === === CODE === === ==== 

def main():
    print(word)
    chances = -1
    blanks = '_' * len(word) 
    guessing(chances, blanks)

def guessing(chances, blanks):
    user_input = input('\nChoose a letter: ')
    checking_letter(user_input, chances, blanks)

def checking_letter(user_input, chances, check_blanks):
    if user_input in list(word):
        index = word.index(user_input) 
        blanks(user_input, index, check_blanks, chances)
    hangman(chances, check_blanks)

def blanks(user_input, index, blanks, chances):
    print('\nYou did it! You have successfully guessed a letter!', end=('\n'))
    target_slice = word
    while user_input in target_slice:
        blanks = blanking(word, index + (len(word)- len(target_slice)), blanks)
        target_slice = target_slice[index + 1:]
    winning(chances, blanks)

def blanking(blanks, index, user_input):
    new_blanks = blanks[:index] + word[index] + blanks[index + 1:]
    return new_blanks

def winning(chances, blanks):
    print(' '.join(blanks))
    if blanks == word:
        print('\nYou did it! You won this game :)\n')
        exit()
    guessing(chances, blanks)

def hangman(chances, blanks):
    hangman = ['''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    try_again(chances, hangman, blanks)

def try_again(chances, hangman, blanks):
    chances += 1
    print(hangman[chances], '\nThe entered letter does not exist in the word.\n')
    if chances == 5:
        print('Unfortunately, you lost. Don\'t worry, you can play again!')
        exit()
    guessing(chances, blanks)   
       
#   === === === IMPORT GUARD === === ==== 

if __name__ == '__main__':
    main()

