# Assessment 2 - Rummy

SURPRISE ASSESSMENT! I figured, since I'm not there to help you anyway, I may as well use the opportunity to see how well you're doing. Do the exercise this week, we'll discuss how you did next week, and we'll adjust the forthcoming lessons from there.

As usual, this is intended to be one step more involved than last time. It's not meant to be a vertical cliff face. If it feels that way, take a deep breath and come back to it later. If I've accidentally set an exercise that's way too hard, that's my fault not yours; it will not be held against you. It's all just practice and information.

## Your Mission

For this assessment, we'll be scoring card hands again, but this time for Rummy!
In Rummy, the objective is to build a hand of seven cards, containing any two of the following patterns:
* three of a kind: three of any rank.
* four of a kind: four of any rank.  
* straight three: a straight of three adjacent cards of the same suit.
* straight four: a straight of four adjacent cards of the same suit.

If we're aiming for a hand of seven cards, then we need one pattern of three, and one pattern of four. You can have two of the same sort of pattern; three Jacks and four sixes is a valid hand, for instance. In Rummy, aces are always low; AS 2S 3S is a valid straight, but QS KS AS is not.

There's no relative ranking of hands in Rummy like in poker; the first player to get a winning hand wins!

Some examples:

* AC AS 5C 8C 6C 7C AH:  *WIN* a straight four and three of a kind. Note that I haven't written the cards down in order, but it still counts.
* AH 2H 3H 4H 5H 6H 7H: *WIN* A straight four and a straight three. It doesn't matter which patter contains the 4H, it's valid either way. Notice that two straights are a winning hand; it doesn't have to ybe  3/4 of a kind and a straight. 
* 10H 9H 8H 7H 7C 7S 7D: *WIN* this is ambiguous, it could be a straight three and four of a kind, or it could be a straight four and three of a kind. Either way, this is a winning hand. 
* QC KC AC AS 2S 3S 4S: *LOSE* Aces are low, so A, 2, 3, 4 *is* a straight, but Q, K, A is *not*.
* 3C 3D 3H 3S 4S 5C 6S: *LOSE* Straights have to be all the same suit. This is just a four of a kind.
* AH 2H 3H 4H 5H 6H 7H 8H: *INVALID* Valid hands only have seven cards.
* AH 2H 3H 4B 5H 6H 7H: *INVALID* 'B' is not a valid suit.
* potatopotato: *INVALID* It may surprise you that a potato is not a real playing card.

## What Are We Doing Exactly?

As you may have guessed, your task is to write a program which prompts the user for a string representing a Rummy hand, and prints "WIN", "LOSE" or "INVALID" in response. You *are* allowed to copy over your `card.py` module from a previous exercise, should you choose.

You will of course have to write tests for as much of your program as possible.  As in recent weeks, the best way to do this is to separate input and output from the processing. Remember to check for invalid hands as well as winning and losing hands. 

This is an assessment, so you will be working individually. Once you're done, make sure your project is committed, and pushed to Github. Good luck. :)

# Restrictions
* Your program should be split up into at *least* two separate modules.
* Your module `rummy.py` contains your import guard and your main function.
* Your module `pure_rummy.py` contains *only* pure functions.
* `pure_rummy.py` *cannot at any point during development* contain the following statements or functions:
  * print
  * input
  * open
* `rummy.py` *cannot* contain the following:
  * indexing 
  * imports of any system modules (i.e. you can import it if you *you* wrote it)
* You may have as many pure modules or test modules as you like.
* Each test may only have one assert.
* Gijs Compensation Measures are still in effect: no globals.
* As standard from now on, no raw code; everything must be in a function apart from import guards, constants, and decorators.
