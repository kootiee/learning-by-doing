# Rummy - scoring card hands

# The objective is to build a hand of seven cards.

# The cards contains any two of the follwing patterns:
#   -   three of a kind: three of any rank.
#   -   four of a kind: four of any rank.
#   -   straight three: a straight of three adjancent cards of the same suit. 
#   -   straight four: a straight of four adjacent cards of the same suit. 

# Aiming for a hand of seven cards:
#   -   one pattern of three and one pattern of four.

# In Rummy aces are always low.
# In Rummy there is no relative ranking of hands like in poker; the first player to get a winning hand wins.

# Write a program wich prompts the user for a string representing a Rummy hand.
# In response the program prints 'WIN', 'LOSE' or 'INVALID'.

# The assessment allows to copy the card.py module.
# Write tests for as much as the program needs.
# The best way to do this is to seperate input and output from the processing.

# Restrictions:
#   -   program should be split up into at least two separate modules.
#   -   module rummy.py contains your import guard and main function.
#   -   module pure_rummy.py contains only pure functions.
#   -   pure_rummy.py can not at any point during development contain the following statements or functions:
#       > print, input and open.
#   -   rummy.py can not contain the following:
#       > indexing and imports of any systems modules (i.e. you can import it if you wrote it)
#   -   you may have as many pure modules or test modules.
#   -   each test may only have one assert.
#   -   no globals.
#   -   everything must be in a function apart from import guards, constants and decorators.


from pure_rummy import RANKS_DICT, SUITS_DICT, check_user_input, determine_hand_value
from typing import List, Dict, Set, Tuple
from sys import exit


def main():
    display_ranks_suits()
    chosen_cards = user_input()


def display_ranks_suits():
    print('\n', '=== SCORING RUMMY ===', '\n')
    print('- Rank:')
    for key, value in RANKS_DICT.items():
        print(f"    - {key}: {value}")
    print('\n', '- Suits:')
    for key, value in SUITS_DICT.items():
        print(f"    - {key}: {value}")
    print()


def user_input() -> List[str]:
    chosen_cards: str = input('Combine a rank (a single letter or number) and suit (a single letter) together. You can enter seven cards with spaces in between. For example: AC 5H KD 3H 8D 4H 9H. Please enter your cards: ').upper()
    list_chosen_cards: List[str] = chosen_cards.split()
    for card in list_chosen_cards:
        if not check_user_input(card):
            print("Invalid input. The program will close. Please try again.")
            exit()
    return list_chosen_cards


def value_of_hand(chosen_cards: List[str]):
    print('With the value of this hand you', determine_hand_value(chosen_cards))


# === import guard ===


if __name__ == '__main__':
    main()

