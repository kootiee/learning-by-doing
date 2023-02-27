# Working With Data

So far, the exercises we've done have dealt with very simple data; numbers and strings. However, nearly all programs in the real world deal with more complicated things than that. A word processor deals with a whole book's worth of text, as well as formatting information. Photoshop deals with rich graphical data. Spotify deals with music and pictures, as well as data about people; name, address, payment, etc. So, this week we'll be looking at ways to start dealing with this by combining several simple pieces of information into something more complex; a *record*.

We'll start by looking at records that are provided for you, and the exercise will be about sorting, searching, and altering those records. This is to get you more used to the concepts and thinking about data. In a future exercise, you'll be given raw data, and asked to structure the records yourself. During this exercise, make a note of what makes these records easy to work with, or what you find makes them difficult to work with; this will help you next time.

## Your Mission

This exercise is all about movies! You'll be making what is effectively "My First IMDB"!

In this directory, you will find a Python module called `movie_data.py`. It contains a function, `movie()`, which will build a record containing information that you specify, and a list, `movies`, which contains several records representing movies. You may wonder why these particular movies were chosen. They were selected by a complex computer science process called "what I could remember off the top of my head on a Sunday morning before the coffee had kicked in." If you think different movies should have been selected, sod off and write your own course. :)

You should write the following programs. These are arranged in what I hope is an increasing order of difficulty.
* **report.py :** This program will import the movie data, and print the following information to the screen:
```
Total number of movies: 231
Average rating of movies: 2.7
Best movie: "2 Fast 2 Furious"
Worst movie: "Citizen Kane"
```
Obviously, you should print the *real* answers rather than what's here. I will use a program to check that your reports are correct, so make sure your formatting and spelling is exactly the same.
* **report_hard.py :** This program will import the movie data, and print the following information to the screen:
```
Actor appearring in most movies: Julia Roberts
Actor with best average rating: Jean Claude Van Damme
Least popular genre in the 1980's: music videos
```
Same as above; print the answers exactly.
* **report_harder.py :** This program will import the movie data, and print the answer to the following question. The answer is one single movie title, with double quotes. The question is:
    * Matthew Broderick sucks. He makes every movie one point worse. Judd Nelson is *harsh*. He makes every movie one point better. Moreover, he's *so cool*, that his coolness is contagious and does not obey the laws of space-time. Anyone who has ever been in a movie with Judd Nelson, makes every other movie they're in one point better. With all that in mind: What's the best Ally Sheedy movie?
* **dojo_movie_database.py :** This program will import the movie data, and then provide a menu of options to the user. The user can select an option, the program will do it, and afterwards the program should return to the main menu. The options are:
    1. *List :* List the name and year of all movies, separated by a comma.
    2. *Actor Search :* Prompt for an actor's name, then list the name and year of all their movies.
    3. *Genre Search :* Prompt for a genre name, then list the name and year of every movie in that genre.
    4. *Add :* Prompts for a title, actors, year, genre, and a rating, then adds that movie to the database in memory. This new movie should show up in the other searches.
    5. *Quit :* Ends the program.
    
# Restrictions
* The only things allowed in your program are:
    * imports
    * an import guard `if __name__ == '__main__': main()`
    * functions
    * constants
* You are not allowed other code or variables at the top level of your module. Inside functions however, you can do whatever you like.
* No global variables. At all. We do not accept The Gijs Scenario. :)
* Try to have no more than eight lines of code per function.
* You have to calculate the answers in your program; you can't just work it out by hand and then `print("Godzilla")`.
* You are *not* allowed to edit `movie_data.py`

