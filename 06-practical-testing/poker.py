# - Task:
#   - Scoring poker
#   - In poker, players form sets of five playing cards, called hands.
#   - A poker hand of five cards might look like this: "4H QH 4D 2S 10C". That tells us the rank and suit of the five cards in the hand. 


#   - Then we can use the following table to determine the value and name of the hand. These values are arranged in increasing order; High Card is the lowest, Royal Flush is the highest.
#   - High Card
#       - Nothing special about this hand. There's no pattern to the cards at all. An example would be "AS 10S 5H 7C 6S".
#   - One pair
#       - Easy enough; this hand has one pair of rank cards. For instance: "AS 10S 5H 10C 6S". There are two tens in this hand, so we have one pair.
#   - Two pair
#       - You'll never believe this, but this is a hand with two pairs of ranked cards. E.g. "3H 8C 8H 9S 3D"
#   - Three of a kind
#       - Three of one rank of card, such as "6S 6H 7C JD 6D". There are three sixes, so we have three of a kind.
#   - Straight
#       - Bit different; this is where all five cards form a continuous sequence, like "2H 3C 4S 5H 6D", or "JD 8C 10S 9S 7D". In this scenario, an Ace can be low ("AS 2H 3C 4S 5D") or high ("10H JH QC KD AS") but not both at the same time.ac
#   - Flush
#       - All the cards are of the same suit, regardless of the rank. e.g. "4H 8H 2H 9H 7H"
#   - Full house
#       - A Three Of A Kind and One Pair in the same hand: "4H 4D 4C 8S 8D"
#   - Four of a kind
#       - Four of any rank: "JC JD JS JC 5H"
#   - Straight flush
#       - It's a Straight and a Flush at the same time; five adjacent cards of the same suit. e.g. "AC 2C 3C 4C 5C"
#   - Royal flush
#       -A Straight Flush that goes from ten to ace; "10S JS QS KS AS". The highest ranking hand in the game.


#   - Testing with main() and import guards
#   - Write a program which prompts the user for a string representing a poker hand, and displays the name of the hand in response.
#   - The names of hands should be printed exactly as they are here.
#   - Any invalid input should result in the message "Sorry, that's invalid" and the program stopping.
#   - You are allowed to copy over your card.py module from the last exercise, so you can concentrate on the new stuff.


# - Restrictions:
#   - Your program should be split up into at least two separate modules.
#   - Your module poker.py contains your import guard and your main function.
#   - Your module pure_poker.py contains only pure functions
#   - pure_poker.py cannot at any point during development contain the following statements or functions:  print, input, open
#   - poker.py cannot contain the following: indexing, imports of any modules other than pure_poker
#   - You may have as many pure modules or test modules as you like.
#   - Each test may only have one assert.
#   - No globals
#   - As standard from now on, no raw code; everything must be in a function apart from import guards, constants, and decorators.


# - Notes:
#   - Pure functions: it took its input parameter(s), and used it to return some new output. It didn't do any input or output. It didn't read from disk, it didn't prompt the user, it didn't print anything or send anything over a network. We gave it some stuff, and using only that stuff, it returned us a value. These properties make pure functions easy to test. We can invent what arguments we want to pass in to the function, and directly check the returned values to check that they match what we expect.
#   - One of the key parts of designing good software - and good software should be easy to test - is learning how to separate input/output from pure functions as much as is practical.
#   - RANK_DICT = {1:['A','ace'], 2:['2','two'], 3:['3','three'], 4:['4','four'], 5:['5':'five'], 6:['6','six'], 7:['7':'seven'], 8:['8','eight'], 9:['9','nine'], 10:['10':'ten'], 11:['J':'jack'], 12:['Q','queen'], 13:['K':'king']}
#   - SUITS_DICT = {1:['C','clubs'], 2:['H', 'hearts'], 3:['S','spades'], 4:['D':'diamonds']}


# === code ===
from pure_poker import RANKS_DICT, SUITS_DICT, check_user_input, determine_hand_value
from typing import List, Dict
from sys import exit


def main():
    display_ranks_suits()
    chosen_cards = user_input()
    value_of_hand(chosen_cards)


def display_ranks_suits():
    print('\n', '=== SCORING POKER ===', '\n')
    print('- Rank:')
    for key, value in RANKS_DICT.items():
        print(f"    - {key}: {value}")
    print('\n', '- Suits:')
    for key, value in SUITS_DICT.items():
        print(f"    - {key}: {value}")
    print()


def user_input() -> List[str]:
    chosen_cards: str = input('Combine a rank (a single letter or number) and suit (a single letter) together. You can enter five cards with spaces in between. For example: AC 5H KD 3H 8D. Please enter your cards: ').upper()
    list_chosen_cards: List[str] = chosen_cards.split()
    for card in list_chosen_cards:
        if not check_user_input(card):
            print("Invalid input. The program will close. Please try again.")
            exit()
    return list_chosen_cards


def value_of_hand(chosen_cards: List[str]):
    print('The value of this hand is', determine_hand_value(chosen_cards))


# === import guard ===


if __name__ == '__main__':
    main()
