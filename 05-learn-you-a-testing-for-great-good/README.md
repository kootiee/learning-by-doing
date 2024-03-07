# Learn You A Testing For Great Good

You have written some programs now, well done! As I'm sure you've noticed, when you're working on a slightly larger program, it can be difficult to notice when your changes break things. Not only that, some time can pass between *breaking* something, and *noticing that you've broken it*. Academic studies have shown that the sooner you notice a mistake, the easier and cheaper it is to fix it; you already have the context you need fresh in your mind. So, we're going to look at a way to spot errors as quickly as possible: automated testing.

This is my *favorite topic ever*, so we will go slowly, but in some depth. From here on in, you'll be writing tests for everything you build.

## Your Mission

Who fancies a game of cards?

Playing cards and card games have been a staple way of teaching computer science stuff for many years; it was a cliche when I was studying it in the 90s. However, the classics are classics for a reason, and we're going to be using playing cards to explore many concepts in the near future.

Your first playing card task is to write a function called `parse_card` which can take a short description of a playing card, and return a dictionary of data about that card. So, if the input to the function was the string `"5H"`, the function should return:
```python
{
    "rank": "5",
    "suit": "hearts",
    "description": "a five of hearts"
}
```

Another example; for `"AS"`, the return value should be:
```python
{
    "rank": "ace",
    "suit": "spades",
    "description": "an ace of spades"
}
```

The twist of course being that you'll need to write a full set of tests for this function. Moreover, you are *not* allowed to exercise the function any other way. No `print` function, no writing to file, no `main()`, nothing. Your tests will be your only way to understand your work.

# Restrictions
* The only things allowed in your modules are:
    * imports
    * functions
    * constants
    * decorators
* Note that an import guard is not on the list. You are not allowed to `python my_program.py`.
* You are not allowed to call `print`.
* No, really. Not at all.
* You *may* run your tests in the debugger, but this is not necessary.
* Your main module *must* be called `card.py`, and your test module `test_card.py`.
* Your function *must* be called `parse_card`.
* You can write as many other functions as you like, but `parse_card` should be the entry point to your module. If `parse_card` calls other things, that's cool, but not necessary.
* `parse_card` should take one parameter, the string containing the short description of the card.
* Valid ranks in the short description are A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
* Valid suits in the short description are C, D, H, S
* If the input string cannot be correctly parsed, or is invalid in some way, the `parse_card` should raise a `ValueError`.
* The description must correctly use 'a' or 'an' depending on whether the written name of the rank starts with a vowel.
* Each test function can only contain one `assert`.
* There is no set limit on how many tests you can write. Write as many or as few as you think are required to prove that your function works as you intend.
* This exercise is governed by the Gijs Directive; no global variables.
