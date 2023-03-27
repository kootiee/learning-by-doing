# Assessment 1

FEAR! TERROR! PANIC! An assessment! mesapeeplegonnadie!!!!

Chill there, my hypothetical anxious friend. This is another exercise like any other. You won't be getting help from me to unblock you, but it's not intended to be difficult. Every concept in this exercise is something we've practiced before. You're all going to knock this out of the park!

## Assessment Rules

The differences between this and a regular week is just the amount of help you'll get from me. I will answer any questions regarding git, and getting hold of the assignment. If you suspect that the assignment is broken, ask me. I will also help you if you have questions about the assignment; if the instructions are not clear, please ask. Other than that, you'll have to solve it yourselves. Try to work on your own; if you're *really* stuck, ask each other, but please be very clear about this (i.e. a comment saying `# Portia helped me with this line`). Looking stuff up is perfectly fine.

But what exactly will you be knocking out of the park? What indeed...

## Your Mission

This exercise is all about quizzes! You'll be making a game where you ask the player some quiz questions, check their answers, score them, and keep a high score for the next game.

In this directory, you'll find a file called `questions.txt`. It contains a whole bunch of trivia questions. They're laid out in the following order:
1. The text of the actual question
2. A list of possible answers, separated by commas
3. The correct answer

You will need to:
* read this file, and parse it into a list of records, each one representing a question, with all its possible answers, and the correct solution
* select five questions at random
* display the high score, along with the name of the high scorer
* ask these questions to the player. 
    * You'll need to show the question, and all four possible answers
    * The answers must be in a random order; they can't always be displayed in the same order as they are in the text file.
    * The player should be able to enter something short to pick their answer. If the answer is "injuries whilst cheese rolling", the player doesn't want to type all that. Let them enter "2" to pick the second possible answer, and so on.
* After the player has answered five questions, display their score
* If their score is higher than or equal to the high score, they get to enter their name, and they're displayed as the high scorer at the start of the next run of the program.

## Restrictions
* The only things allowed in your program are:
    * imports
    * an import guard `if __name__ == "__main__": main()`
    * functions
    * constants
* No global variables, as per The Gijs Directive
* You are *not* allowed to edit `questions.txt`

Note that there is no restriction on function length; you're all using functions competently now, so there's no need to force you to do it.
