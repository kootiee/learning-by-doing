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
    string_word = '_' * len(word) 
    guessing(chances, string_word)

def guessing(chances, string_word):
    user_input = input('\nChoose a letter: ')
    checking_letter(user_input, chances, string_word)

def checking_letter(user_input, chances, string_word):
    if user_input in list(word):
        index = word.index(user_input)
        blanks(user_input, index, string_word, chances)
    hangman(chances, string_word)

def blanks(user_input, index, string_word, chances):
    print('\nYou did it! You have successfully guessed a letter!', end=('\n'))
    string_word = string_word[:index] + user_input + string_word[index + 1:]
    winning(chances, string_word)

def winning(chances, string_word):
    print(' '.join(string_word))
    if string_word == word:
        print('\nYou did it! You won this game :)\n')
        exit()
    guessing(chances, string_word)

def hangman(chances, string_word):
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
    try_again(chances, hangman, string_word)

def try_again(chances, hangman, string_word):
    chances += 1
    print(hangman[chances], '\nThe entered letter does not exist in the word.\n')
    if chances == 5:
        print('Unfortunately, you lost. Don\'t worry, you can play again!')
        exit()
    guessing(chances, string_word)   
       
#   === === === IMPORT GUARD === === ==== 

if __name__ == '__main__':
    main()

