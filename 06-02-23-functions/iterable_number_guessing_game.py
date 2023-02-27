#   === === === NUMBER GUESSING GAME === === ==== 

#   THE MISSION
# - The computer picks a number between 1 and 100, and asks you to guess.
# - It tells you if you were too high or too low, and gives you six chances to guess.

from random import randint

def main():
    user_input, target_number = numbers()
    guessing(user_input, target_number, count = 6)

def numbers():
    random_number = randint(0, 100)
    input_user = int(input('Let\'s play a game! Guess a number. You can choose between 0 and 100: '))
    return input_user, random_number

def winning(user_input, target_number, count):
    if user_input == target_number: 
        print('You did it! You won this game :) \nYou had', count, 'chances left. Well done!')

def guessing(user_input, target_number, count):
    while user_input != target_number:
        count = count - 1
        if count == 0:
            print('Unfortunately, you lost. No more guesses left. \nDon\'t worry, you can play again!')
            break
        else:
            user_input = higher_or_lower(user_input, target_number)
    winning(user_input, target_number, count)

def higher_or_lower(user_input, target_number):
    if user_input < target_number:
        user_input = int(input('\t\tGuess higher. You can do this! You can choose again: '))
    elif user_input > target_number:
        user_input = int(input('\t\tGuess lower. You can do this! You can choose again:  '))
    return user_input

#   IMPORT GUARD
if __name__ == '__main__':
    main()

# Commit this!
# You can do this without exit() - line 23 is easy mode -> line 30 is hard mode
# Line 21 and 26 does the same thing - they check if it is equal (or not)
# higher_or_lower() can return something to guessing() -> new user_input()
# recursion is a function that calls itself! So it's allowed to call another function ;)