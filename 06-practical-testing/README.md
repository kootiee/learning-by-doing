# Practical Testing

Wa-hey! You've written tests to prove a function works! Awesome! However, some of you have already been asking me, "how does this tie in with what we've done so far, with `main()` and import guards and all that?" Great question. Today we're starting to look at just that.

Some things are easy to test. The function we looked at last week was what we call a *pure function*. This means that it took its input parameter(s), and used it to return some new output. It didn't do any input or output. It didn't read from disk, it didn't prompt the user, it didn't print anything or send anything over a network. We gave it some stuff, and using *only* that stuff, it returned us a value.

These properties make pure functions easy to test. We can invent what arguments we want to pass in to the function, and directly check the returned values to check that they match what we expect. However, most of the programs and functions we've seen so far *aren't* pure. They print stuff, prompt the user, read and write to files. In fact, that's what makes them interesting; if your program can't interact with the outside world, it's not able to do anything useful.

One of the key parts of designing good software - and good software should be easy to test - is learning how to separate input/output from pure functions as much as is practical. That means your program can still do interesting things, but as much code as possible is easy to test. That's what we're looking at this week.

## Your Mission

Bury the house deeds in the yard and hide the jewelry, 'cause this week we're playing poker!

Well, not *playing* poker exactly, but we are going to be scoring poker. If you've never played, the objective of most varieties of poker is to end up with five cards in your hand. The value of the hand depends on the cards in the hand, and there are special names for each value of hand. Then there's a whole bunch of bluffing and betting, which we're not covering today. We're just going to look at poker hands.

Using our shorthand for cards last week, a poker hand of five cards might look like this: "4H QH 4D 2S 10C". That tells us the rank and suit of the five cards in the hand. Then we can use the following table to determine the value and name of the hand. These values are arranged in increasing order; High Card is the lowest, Royal Flush is the highest.

### High Card

Nothing special about this hand. There's no pattern to the cards at all. An example would be "AS 10S 5H 7C 6S".

### One Pair

Easy enough; this hand has one pair of rank cards. For instance: "AS 10S 5H 10C 6S". There are two tens in this hand, so we have one pair.

### Two Pair

You'll never believe this, but this is a hand with two pairs of ranked cards. E.g. "3H 8C 8H 9S 3D"

### Three Of A Kind

Three of one rank of card, such as "6S 6H 7C JD 6D". There are three sixes, so we have three of a kind.

### Straight

Bit different; this is where all five cards form a continuous sequence, like "2H 3C 4S 5H 6D", or "JD 8C 10S 9S 7D". In this scenario, an Ace can be low ("AS 2H 3C 4S 5D") or high ("10H JH QC KD AS") but not both at the same time.

### Flush

All the cards are of the same suit, regardless of the rank. e.g. "4H 8H 2H 9H 7H"

### Full House

A Three Of A Kind and One Pair in the same hand: "4H 4D 4C 8S 8D"

### Four Of A Kind

Four of any rank: "JC JD JS JC 5H"

### Straight Flush

It's a Straight and a Flush at the same time; five adjacent cards of the same suit. e.g. "AC 2C 3C 4C 5C"

### Royal Flush

A Straight Flush that goes from ten to ace; "10S JS QS KS AS". The highest ranking hand in the game.

## What Are We Doing Exactly?

As you may have guessed, your task is to write a program which prompts the user for a string representing a poker hand, and displays the name of the hand in response. The names of hands should be printed exactly as they are here. Any invalid input should result in the message "Sorry, that's invalid" and the program stopping. You *are* allowed to copy over your `card.py` module from the last exercise, so you can concentrate on the new stuff.

You will of course have to write tests for as much of your program as possible. The restrictions might seem very harsh, but they're there to push you in the right direction. You will have to run your program several times to check it works, but *most* of your development can and should be done through your tests. They're there to help, as am I.

# Restrictions
* Your program should be split up into at least two separate modules.
* Your module `poker.py` contains your import guard and your main function.
* Your module `pure_poker.py` contains *only* pure functions.
* `pure_poker.py` *cannot at any point during development* contain the following statements or functions:
  * print
  * input
  * open
* `poker.py` *cannot* contain the following:
  * indexing 
  * imports of any modules other than `pure_poker`
* You may have as many pure modules or test modules as you like.
* Each test may only have one assert.
* Gijs Compensation Measures are still in effect: no globals.
* As standard from now on, no raw code; everything must be in a function apart from import guards, constants, and decorators.
