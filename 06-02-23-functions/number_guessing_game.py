#   === === === NUMBER GUESSING GAME === === ==== 

#   THE MISSION
# - The computer picks a number between 1 and 100, and asks you to guess.
# - It tells you if you were too high or too low, and gives you six chances to guess.

from random import randint
from sys import exit

def main():
    count = 6
    user_input, target_number = numbers()
    winning_or_not(user_input, target_number, count)

def numbers():
    random_number = randint(0, 100)
    input_user = int(input('Let\'s play a game! Guess a number. You can choose between 0 and 100: '))
    return input_user, random_number

def winning_or_not(user_input, target_number, count):
    if user_input == target_number:
        print('You did it! You won this game :) \nYou had', count, 'chances left. Well done!')
    else:
        chances(user_input, target_number, count)

def chances(user_input, target_number, count):        
    count = count - 1
    print('You have', count, 'chances left.', end=' ')
    loser(user_input, target_number, count)

def loser(user_input, target_number, count):
    if count == 0:
        print('Unfortunately, you lost. Don\'t worry, you can play again!')
        exit()
    higher_or_lower(user_input, target_number, count)
    
def higher(user_input, target_number, count):
    lower_number = int(input('Guess higher. You can do this! You can choose again: '))
    return winning_or_not(lower_number, target_number, count)
    
def lower(user_input, target_number, count):
    higher_number = int(input('Guess lower. You can do this! You can choose again: '))
    return winning_or_not(higher_number, target_number, count)

def higher_or_lower(user_input, target_number, count):
    if user_input < target_number:
        higher(user_input, target_number, count)
    elif user_input > target_number:
        lower(user_input, target_number, count)
        
#   IMPORT GUARD
if __name__ == '__main__':
    main()
