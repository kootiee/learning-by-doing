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
    guessing(blanks, chances)

def guessing(blanks, chances):
    user_input = input('\nChoose a letter: ')
    checking_letter(user_input, blanks, chances)

def checking_letter(user_input, blanks, chances):
    if user_input in list(word):
        blanky(user_input, blanks, chances)
    hangman(blanks, chances)

def blanky(user_input, blanks, chances):
    print('\nYou did it! You have successfully guessed a letter!', end=('\n'))
    target_slice = word
    while user_input in target_slice:
        index = target_slice.index(user_input) 
        blanks = blanking(word, index + (len(word)- len(target_slice)), blanks)
        target_slice = target_slice[index + 1:]
    winning(blanks, chances)

def blanking(word, index, blanks):
    new_blanks = blanks[:index] + word[index] + blanks[index + 1:]
    return new_blanks

def winning(blanks, chances):
    print(' '.join(blanks))
    if blanks == word:
        print('\nYou did it! You won this game :)\n')
        exit()
    guessing(blanks, chances)

def hangman(blanks, chances):
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
    try_again(hangman, blanks, chances)

def try_again(hangman, blanks, chances):
    chances += 1
    print(hangman[chances], '\nThe entered letter does not exist in the word.\n')
    if chances == 5:
        print('Unfortunately, you lost. Don\'t worry, you can play again!')
        exit()
    guessing(blanks, chances)   
       
#   === === === IMPORT GUARD === === ==== 

if __name__ == '__main__':
    main()

