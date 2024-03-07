# OOP I Did It Again

Why yes, I do think I'm funny; how could you tell?

The concept here is simple; you're going to do a variation of a previous exercise using the object-oriented techniques we've been looking at for the past few weeks. The idea being that the problem itself is something you're familiar with; you can concentrate on the OO parts of the exercise.

You're going to be building this using everything we've used so far; you'll not have any raw code, you'll test everything, etc, etc. However I'm going to add some restrictions to push you in an OO direction. I really want you to conentrate on the object-oriented aspect of this; if you make a working program without using any OO techniques, then that's not a win in my book.

Read the description carefully; it's there to help you. Rewatch previous lessons if you need to, especially the stuff about how to break down problems and instructions. Start by working out which parts are probably going to be classes. Remember, nouns tend to become classes, adjectives and information tend to be properties, and verbs become methods. When you think 'I need something in my program to do *this*', think carefully about where that thing should go.

Work individually on this one; you need to develop your design skills. But you can't improve them in a vacuum; ask me for help. It's not an assessment, it's a practice exercise, and you can't learn without making mistakes. This will probably take a few weeks to finish, and that's fine. :)

## Your Mission

Bury the house deeds in the yard and hide the jewelry, 'cause this week we're playing poker!

Again!

The full details about poker are reproduced here so you don't have to look them up. 

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

You need to write a program which allows the user to enter *two* shorthand strings. Those strings each represent a hand of cards. Each card has a rank and suit, and the normal restrictions apply there. Each hand should contain exactly five cards. The first string contains the cards for Player 1, and the second string contains the cards for Player 2.

Your program should print which player wins the round, and why. So, an example run of the program might look like this:

```
> Enter Player 1's cards: 10H 10C 4H 4S 10S
> Enter Player 2's cards: AH 3H 2H 5H 4H
> Player 2 wins!
> A Straight Flush beats A Full House!
```

If the hands are the same, then the highest relevant card wins. Note in the next example, that although Player 2 has the highest card, Player 1 still wins; their pair of 10s beats the pair of 3s. Player 2's king isn't part of the hand, so it doesn't affect the result.

```
> Enter Player 1's cards: 10H 10C 4H 5S 7S
> Enter Player 2's cards: 3S 3H 2H 5H KH
> Player 1 wins!
> One Pair (10) beats One Pair (3)!
```

You will of course have to write tests for as much of your program as possible. The restrictions might seem very harsh, but they're there to push you in the right direction. You will have to run your program several times to check it works, but *most* of your development can and should be done through your tests. They're there to help, as am I.

# Restrictions
* Your program should be split up into at least three separate modules.
* Your module `main.py` contains your import guard and your main function.
* Your other modules should contain one class definition each. Those modules may include each other.
* Your modules containing classes *cannot at any point during development* contain the following statements or functions:
  * print
  * input
  * open
* __Your modules containing classes *cannot at any point during development* contain the following statements or functions__:
  * print
  * input
  * open
  * I've seen some of you doing this, but I'm serious; you have tests and a debugger. Use those tools.
* Your classes *must not* directly alter properties of other classes. `my_object.increase_score()` is fine, but `my_object.score += 1` is not.
* `main.py` *should* be as simple as possible. Most of your program's logic should be in the classes.
* You should have one test module per class module.
* Each test may only have one assert.
* Gijs Compensation Measures are still in effect: no globals.
* As standard from now on, no raw code; everything must be in a function apart from import guards, constants, and decorators.
