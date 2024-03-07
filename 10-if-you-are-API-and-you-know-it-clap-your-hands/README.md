# If You're API And You Know It Clap Your Hands

Today we're moving on to another topic. You have the very basics of programming now, so let's look at some more interesting things that you can do with them. We're going to start looking at interacting with other systems, starting with something you're familiar with: websites! Specifically, web APIs. "web API" is a fancy way of saying "a website intended for a computer to use, as opposed to a human."

We're going to go through an example together, and then you're going to try to write your own programs to use some simple APIs. Everything you've learned so far - functions, classes, tests - it's all still important. We're just using it in more interesting ways.

## Your Mission

There's a lot to go through, no rush. Reading the documentation on the API websites is part of the exercise.

1. Read through and follow `demo.py`. Solve the exercise at the end.
2. Use the Evil Insult Generator (https://evilinsult.com/api/#generate-insult-get) to print five insults to the terminal.
3. Use the Coffee API (https://coffee.alexflipnote.dev/) to to get a random image of a coffee and display it. 
  * hint:
``` python
import subprocess
subrocess.run(['firefox', 'www.github.com'])
```
4. Write a program that acts as a menu driven interface to the Advice API (https://api.adviceslip.com/). The user should be able to get a random piece of advice, get advice by ID, or search by keyword and see a list of matching IDs.


